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
    W("**Kody ról** (metadana informacyjna na bullecie, nie kwota doboru —")
    W("rozkład bulletów na role wynika z dopasowania do oferty, każda rola tyle")
    W("ile realnie pasuje):")
    W("")
    W("| Kod | Stanowisko | Okres | #ACH |")
    W("| --- | --- | --- | --- |")
    for code, label, period, achs in model.roles:
        W(f"| `{code}` | {label} | {period} | {len(achs)} |")
    W("")
