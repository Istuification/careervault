#!/usr/bin/env python3
"""
build_index.py

Generuje `Vaultshot index.md` — jedyne zrodlo danych dla skilla /generuj-cv.

Po co ten plik istnieje:
    README sekcji (Achievements, Skills, Stories) zawieraja te same relacje
    zapisane trzy razy w trzech formatach — tabela zbiorcza, rozwiniecie per
    rekord, lista luk. Lacznie ~3000 linii, z czego generator CV potrzebuje
    okolo 240. README zostaja bez zmian (sa dla czlowieka); ten plik jest
    ich skondensowanym odpowiednikiem dla maszyny.

Struktura wyniku:
    A — achievementy: rola, okres, waga, ZAMKNIETA lista SKILL, powiazane STORY
    B — kompetencje: poziom, waga, liczba dowodow, slowa kluczowe
    C — gotowe bullety z rekordow STORY (z policzona dlugoscia)
    D — surowe `impact` dla ACH bez STORY
    E — testy walidacyjne do wykonania przed oddaniem YAML

Uruchamianie:
    python scripts/build_index.py            # zapis do repo
    python scripts/build_index.py --check     # tylko walidacja, bez zapisu
    python scripts/build_index.py --stdout    # wypis na ekran

W GitHub Actions uruchamiany PRZED build_vault.py, zeby swiezy indeks trafil
do plikow zbiorczych.
"""

import os
import sys
import datetime
import subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vault_model import VaultModel, ROLE_MAP  # noqa: E402

ROOT = os.getcwd()
INDEX_FILENAME = "Vaultshot index.md"

# Limit znakow bulletu w szablonie Typst (main.typ, funkcja vault-bullet).
# Trzy plakietki ID zjadaja ~32 znaki ekwiwalentu na koncu ostatniej linii,
# wiec 130 to gorna granica przy ktorej bullet nadal miesci sie w 2 liniach.
BULLET_LIMIT = 130

# Docelowy rozklad bulletow na stanowiska w CV (suma = liczba bulletow).
ROLE_QUOTA = {"PM": 3, "KIER": 2, "KOOR": 1}


def trim(text, n):
    text = " ".join(text.split())
    return text if len(text) <= n else text[:n - 1].rstrip(" ,-") + "…"


def build_index_md(model, now, commit):
    W = [].append
    out = []
    W = out.append

    prof = model.prof_ids()
    priv = model.priv_ids()

    W("# VaultShot — Indeks Generatora CV")
    W("")
    W("> **Plik generowany automatycznie** przez `scripts/build_index.py`.")
    W("> Nie edytuj recznie — zmiany wprowadzaj w rekordach Vaulta i przegeneruj.")
    W(f"> Stan: {now} UTC · commit `{commit}`")
    W("")
    W("Przeznaczenie: **wylaczne zrodlo danych dla skilla `/generuj-cv`**.")
    W("Nie zastepuje README sekcji — te pozostaja dokumentacja dla czlowieka.")
    W("")
    W(f"Zakres: **{len(prof)}** achievementow zawodowych, **{len(priv)}** prywatnych, "
      f"**{len(model.skill)}** kompetencji, **{len(model.story)}** historii.")
    W("")
    W("---")
    W("")

    # -- instrukcja ------------------------------------------------------
    W("## Jak czytac ten plik")
    W("")
    W("**Tabela A** to jedyne miejsce, z ktorego dobiera sie dowody. Jeden wiersz =")
    W("jeden achievement = jeden potencjalny bullet w CV. Kolumna `Skills` jest")
    W("**pelna i zamknieta** lista kompetencji, do ktorych ten achievement wolno")
    W("przypisac — para spoza tej listy jest bledem walidacji, nie kwestia oceny.")
    W("")
    W("**Tabela B** sluzy fazie dopasowania oferty i paskowi kompetencji w CV.")
    W("Kryterium glownym jest dopasowanie do oferty, nie waga ani liczba dowodow.")
    W("")
    W("**Sekcja C** zawiera gotowe bullety. Wybierz jeden albo zloz wlasny")
    W("**wylacznie z faktow w danym bloku** — nie dopisuj niczego z pamieci.")
    W("**Sekcja D** to material dla achievementow bez historii.")
    W("")

    # -- role ------------------------------------------------------------
    W("**Kody rol** (do rozlozenia bulletow na stanowiska w CV):")
    W("")
    W("| Kod | Stanowisko | Okres | #ACH |")
    W("| --- | --- | --- | --- |")
    for code, label, period, achs in model.roles:
        W(f"| `{code}` | {label} | {period} | {len(achs)} |")
    W("")
    quota = " / ".join(f"{k} {v}" for k, v in ROLE_QUOTA.items())
    W(f"Docelowy rozklad bulletow: **{quota}**. Przypisanie ACH do roli pochodzi")
    W("z `Experience.md` (sekcje `### <Rola>`), nie z dat — achievementy ciagle")
    W("naleza do roli, w ktorej powstaly.")
    W("")
    W("---")
    W("")

    # -- A ----------------------------------------------------------------
    W("## A. Achievementy — dowody, relacje, rola")
    W("")
    W("| ACH | Tytul | Rola | Okres | W | Skills (zamknieta lista) | Stories |")
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
        W("### Prywatne — uzycie wyjatkowe, tylko gdy oferta wprost tego dotyczy")
        W("")
        W("| ACH | Tytul | Okres | W | Skills | Stories |")
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
    W("`#ACH` = liczba dowodow. Skille bez slow kluczowych dopasowuj po nazwie")
    W("i po kolumnie `Nazwa` — brak keywords nie oznacza slabszej kompetencji.")
    W("")
    W("| SKILL | Nazwa | Kategoria | Poziom | W | #ACH | Slowa kluczowe |")
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
    W("## C. Bullety CV — gotowe sformulowania")
    W("")
    W(f"Liczba w nawiasie to dlugosc. Limit szablonu: **{BULLET_LIMIT} znakow** —")
    W("dluzsze skracaj zachowujac liczby, nie dopisuj nowych faktow.")
    W("")
    for stid in sorted(model.story):
        s = model.story[stid]
        W(f"### `{stid}` → {' '.join(s['ach']) or '—'}")
        W(f"_{trim(s['title'], 90)}_")
        W("")
        if not s["bullets"]:
            W("_(brak `cv_bullets` w rekordzie — uzyj sekcji D dla powiazanych ACH)_")
            W("")
            continue
        for b in s["bullets"]:
            flag = "" if len(b) <= BULLET_LIMIT else " **⚠ skroc**"
            W(f"- `[{len(b)}]` {b}{flag}")
        W("")

    W("---")
    W("")

    # -- D ----------------------------------------------------------------
    W("## D. Achievementy bez Story — material na bullet")
    W("")
    W("Brak gotowych sformulowan. Ponizsze fakty (pole `impact`) sa **jedynym**")
    W("dopuszczalnym materialem — przenos liczby doslownie.")
    W("")
    orphan = [a for a in prof if a not in model.a2st]
    if not orphan:
        W("_Brak — kazdy achievement zawodowy ma powiazana historie._")
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
    W("Testy binarne, wszystkie sprawdzalne w tym pliku bez siegania do Vaulta:")
    W("")
    W("1. **Para SKILL–ACH** — czy `SKILL-XXX` figuruje w kolumnie Skills wiersza")
    W("   `ACH-YYY` w tabeli A? Jesli nie, para jest bledna.")
    W("2. **Para ACH–STORY** — czy `STORY-ZZZ` figuruje w kolumnie Stories wiersza")
    W("   `ACH-YYY` w tabeli A?")
    W(f"3. **Dlugosc bulletu** — czy tresc miesci sie w {BULLET_LIMIT} znakach?")
    W("")
    W("Dodatkowo: brak powtorzonych ACH, brak powtorzonych SKILL, rozklad")
    W(f"bulletow na role zgodny z kwota ({quota}).")
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
