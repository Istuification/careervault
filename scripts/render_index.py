#!/usr/bin/env python3
"""
render_index.py

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
    python scripts/render_index.py            # zapis do repo
    python scripts/render_index.py --check     # tylko walidacja, bez zapisu
    python scripts/render_index.py --stdout    # wypis na ekran

W GitHub Actions uruchamiany PRZED render_site.py, zeby swiezy indeks trafil
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
    W("> **Plik generowany automatycznie** przez `scripts/render_index.py`.")
    W("> Nie edytuj ręcznie — zmiany wprowadzaj w rekordach Vaulta i przegeneruj.")
    W(f"> Stan: {now} UTC · commit `{commit}`")
    W("")
    W("Przeznaczenie: **wyłączne źródło danych dla skilla `/generuj-cv`**.")
    W("Nie zastępuje README sekcji — te pozostają dokumentacją dla człowieka.")
    W("")
    W(f"Zakres: **{len(prof)}** achievementów zawodowych, **{len(priv)}** prywatnych, "
      f"**{len(model.skill)}** kompetencji, **{len(model.story)}** historii.")
    W("")
    W("---")
    W("")

    # -- instrukcja ------------------------------------------------------
    W("## Jak czytać ten plik")
    W("")
    W("**Tabela A** to jedyne miejsce, z którego dobiera się dowody. Jeden wiersz =")
    W("jeden achievement = jeden potencjalny bullet w CV. Kolumna `Skills` jest")
    W("**pełną i zamkniętą** listą kompetencji, do których ten achievement wolno")
    W("przypisać — para spoza tej listy jest błędem walidacji, nie kwestią oceny.")
    W("")
    W("**Tabela B** służy fazie dopasowania oferty i paskowi kompetencji w CV.")
    W("Kryterium głównym jest dopasowanie do oferty, nie waga ani liczba dowodów.")
    W("")
    W("**Sekcja C** zawiera gotowe bullety. Wybierz jeden albo złóż własny")
    W("**wyłącznie z faktów w danym bloku** — nie dopisuj niczego z pamięci.")
    W("**Sekcja D** to materiał dla achievementów bez historii.")
    W("")

    # -- role ------------------------------------------------------------
    W("**Kody ról** (do rozłożenia bulletów na stanowiska w CV):")
    W("")
    W("| Kod | Stanowisko | Okres | #ACH |")
    W("| --- | --- | --- | --- |")
    for code, label, period, achs in model.roles:
        W(f"| `{code}` | {label} | {period} | {len(achs)} |")
    W("")
    quota = " / ".join(f"{k} {v}" for k, v in ROLE_QUOTA.items())
    W(f"Docelowy rozkład bulletów: **{quota}**. Przypisanie ACH do roli pochodzi")
    W("z `Experience.md` (sekcje `### <Rola>`), nie z dat — achievementy ciągłe")
    W("należą do roli, w której powstały.")
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
    W("Dodatkowo: brak powtórzonych ACH, brak powtórzonych SKILL, rozkład")
    W(f"bulletów na role zgodny z kwotą ({quota}).")
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
