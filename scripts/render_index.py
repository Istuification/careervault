    W("Przypisanie ACH do roli pochodzi z `Experience.md` (sekcje `### <Rola>`),")
    W("nie z dat — achievementy ciągłe należą do roli, w której powstały.")
    W("")
    W("---")
    W("")

    # -- A ----------------------------------------------------------------
    W("## A. Achievementy — dowody, relacje, rola")
    W("")
    W("| ACH | Tytuł | Rola | Okres | W | Skills (zamknięta lista) | Stories |")
    W("| --- | --- | --- | --- | --- | --- | --- |")
    for a in prof:
        x = model.ach[a]
        per = f"{x['start']}→{x['end']}".replace("current", "teraz")
        sk = " ".join(model.a2s.get(a, [])) or "—"
        st = " ".join(model.a2st.get(a, [])) or "—"
        W(f"| `{a}` | {trim(x['title'], 68)} | {model.role_of(a)} | {per} | "
          f"{x['importance']} | {sk} | {st} |")
    W("")

    if priv:
        W("### Prywatne — użycie wyjątkowe, tylko gdy oferta wprost tego dotyczy")
        W("")
        W("| ACH | Tytuł | Okres | W | Skills | Stories |")
        W("| --- | --- | --- | --- | --- | --- |")
        for a in priv:
            x = model.ach[a]
            per = f"{x['start']}→{x['end']}".replace("current", "teraz")
            W(f"| `{a}` | {trim(x['title'], 68)} | {per} | {x['importance']} | "
              f"{' '.join(model.a2s.get(a, [])) or '—'} | "
              f"{' '.join(model.a2st.get(a, [])) or '—'} |")
        W("")

    W("---")
    W("")

    # -- B ----------------------------------------------------------------
    W("## B. Kompetencje — dopasowanie do oferty")
    W("")
    W("`#ACH` = liczba dowodów. Skille bez słów kluczowych dopasowuj po nazwie")
    W("i po kolumnie `Nazwa` — brak keywords nie oznacza słabszej kompetencji.")
    W("")
    W("| SKILL | Nazwa | Kategoria | Poziom | W | #ACH | Słowa kluczowe |")
    W("| --- | --- | --- | --- | --- | --- | --- |")
    for sid in sorted(model.skill):
        s = model.skill[sid]
        kw = ", ".join(s["keywords"]) if s["keywords"] else "_(brak)_"
        W(f"| `{sid}` | {s['name']} | {s['category']} | {s['level']} | "
          f"{s['importance']} | {len(s['evidence'])} | {trim(kw, 90)} |")
    W("")
    W("---")
    W("")

    # -- C ----------------------------------------------------------------
    W("## C. Bullety CV — gotowe sformułowania")
    W("")
    W(f"Liczba w nawiasie to długość. Limit szablonu: **{BULLET_LIMIT} znaków** —")
    W("dłuższe skracaj zachowując liczby, nie dopisuj nowych faktów.")
    W("")
    for stid in sorted(model.story):
        s = model.story[stid]
        W(f"### `{stid}` → {' '.join(s['ach']) or '—'}")
        W(f"_{trim(s['title'], 90)}_")
        W("")
        if not s["bullets"]:
            W("_(brak `cv_bullets` w rekordzie — użyj sekcji D dla powiązanych ACH)_")
            W("")
            continue
        for b in s["bullets"]:
            flag = "" if len(b) <= BULLET_LIMIT else " **⚠ skróć**"
            W(f"- `[{len(b)}]` {b}{flag}")
        W("")

    W("---")
    W("")

    # -- D ----------------------------------------------------------------
    W("## D. Achievementy bez Story — materiał na bullet")
    W("")
    W("Brak gotowych sformułowań. Poniższe fakty (pole `impact`) są **jedynym**")
    W("dopuszczalnym materiałem — przenoś liczby dosłownie.")
    W("")
    orphan = [a for a in prof if a not in model.a2st]
    if not orphan:
        W("_Brak — każdy achievement zawodowy ma powiązaną historię._")
        W("")
    for a in orphan:
        W(f"### `{a}` · {trim(model.ach[a]['title'], 75)}")
        W(f"Rola: `{model.role_of(a)}` · waga {model.ach[a]['importance']}")
        W("")
        for im in model.ach[a]["impact"][:3]:
            W(f"- {im}")
        if not model.ach[a]["impact"]:
            W("_(rekord nie ma pola `impact`)_")
        W("")

    W("---")
    W("")

    # -- E ----------------------------------------------------------------
    W("## E. Walidacja przed oddaniem YAML")
    W("")
    W("Testy binarne, wszystkie sprawdzalne w tym pliku bez sięgania do Vaulta:")
    W("")
    W("1. **Para SKILL–ACH** — czy `SKILL-XXX` figuruje w kolumnie Skills wiersza")
    W("   `ACH-YYY` w tabeli A? Jeśli nie, para jest błędna.")
    W("2. **Para ACH–STORY** — czy `STORY-ZZZ` figuruje w kolumnie Stories wiersza")
    W("   `ACH-YYY` w tabeli A?")
    W(f"3. **Długość bulletu** — czy treść mieści się w {BULLET_LIMIT} znakach?")
    W("")
    W("Dodatkowo: brak powtórzonych ACH, brak powtórzonych SKILL.")
    W("")
    W("---")
    W("")
    W(f"_Wygenerowano {now} UTC z commita `{commit}`._")

    return "\n".join(out) + "\n"


def report(model):
    """Wypis walidacji na stdout. Zwraca liczbe bledow."""
    errs, warns, infos = model.errors(), model.warnings(), model.infos()
    print(f"Vault: {model.summary()}")
    for m in errs:
        print(f"  BLAD  {m}")
    for m in warns:
        print(f"  UWAGA {m}")
    for m in infos:
        print(f"  info  {m}")
    if not (errs or warns or infos):
        print("  brak zastrzezen")
    return len(errs)


def main():
    args = set(sys.argv[1:])
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        commit = "unknown"

    model = VaultModel(ROOT)
    n_err = report(model)

    if "--check" in args:
        return 1 if n_err else 0

    content = build_index_md(model, now, commit)

    if "--stdout" in args:
        print()
        print(content)
        return 0

    path = os.path.join(ROOT, INDEX_FILENAME)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"Zapisano {INDEX_FILENAME} ({len(content.splitlines())} linii, "
          f"{len(content)} znakow, ~{len(content) // 3.5:.0f} tokenow)")

    # Bledy nie przerywaja builda — strona ma sie zaktualizowac mimo wszystko.
    # Widac je w logu Actions.
    return 0


if __name__ == "__main__":
    sys.exit(main())
