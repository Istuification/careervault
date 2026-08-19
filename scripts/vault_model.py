#!/usr/bin/env python3
"""
vault_model.py

Parser rekordow Career Vault + budowa relacji miedzy nimi.

Modul nie generuje zadnych plikow. Dostarcza jeden obiekt `VaultModel`,
z ktorego korzystaja:
  - render_index.py   (render Vaultshot index.md)
  - render_site.py   (wstawienie indeksu do plikow zbiorczych)

CELOWO BEZ ZALEZNOSCI ZEWNETRZNYCH.
Rekordy Vaulta maja plaska, przewidywalna strukture YAML (klucz na poziomie
zerowym, listy jako "  - wartosc"), wiec parser regexowy wystarcza. Brak
PyYAML oznacza brak `pip install` w GitHub Actions i brak ryzyka, ze build
padnie po aktualizacji biblioteki. Jesli format kiedys sie skomplikuje,
podmienia sie wylacznie ten plik.

ZRODLA PRAWDY (single source of truth):
  - SKILL-*.evidence          -> ktore ACH dowodza kompetencji
  - STORY-*.evidence.achievement_ids -> ktore ACH opisuje historia
  - Experience.md, sekcje "### <Rola>" -> ktore ACH powstaly na ktorym stanowisku

Relacje NIE sa duplikowane w rekordach ACH. Mapy odwrotne (ACH -> SKILL,
ACH -> STORY) buduje ten modul.
"""

import os
import re


# ---------------------------------------------------------------------------
# KONFIGURACJA MAPOWANIA ROL
# ---------------------------------------------------------------------------
#
# Klucz  = naglowek "### <nazwa>" w Experience.md (dopasowanie po fragmencie)
# Wartosc = (kod do tabeli indeksu, etykieta w CV)
#
# Kolejnosc ma znaczenie: uzywana do sortowania chronologicznego w indeksie.
# ---------------------------------------------------------------------------

ROLE_MAP = [
    ("Installation Coordinator", "KOOR", "Koordynator ds. Montaży"),
    ("Acting Service Manager", "KIER", "p.o. Kierownika Serwisu"),
    ("Product Manager", "PM", "Product Manager / Business Analyst"),
]

ROLE_FALLBACK = "—"


# ---------------------------------------------------------------------------
# POLA PILNOWANE PRZED CICHYM ZGUBIENIEM
# ---------------------------------------------------------------------------
#
# (pole w rekordzie, klucz w YAML, blok nadrzedny albo None,
#  prefiks pozycji liczonych albo None)
#
# Parser regexowy nie rzuca wyjatkow -- gdy czegos nie rozpozna, zwraca
# pusta liste. Ta tabela pozwala walidacji porownac "klucz jest w pliku"
# z "pole wyszlo puste" i zamienic ciche zgubienie w ostrzezenie.
# ---------------------------------------------------------------------------

WATCHED = {
    "ACH-": [("impact", "impact", None, None),
             ("roles", "roles", None, None)],
    # `evidence` w SKILL-* celowo dopuszcza wpisy opisowe, ktore parser
    # odrzuca -- liczymy wiec wylacznie pozycje `ACH-*`.
    "SKILL-": [("keywords", "keywords", None, None),
               ("capabilities", "capabilities", None, None),
               ("related", "related_skills", None, None),
               ("evidence", "evidence", None, "ACH-")],
    "STORY-": [("ach", "achievement_ids", "evidence", None),
               ("bullets", "cv_bullets", None, None)],
    "DEV-": [("ach", "achievements", "sources", None),
             ("stories", "stories", "sources", None),
             ("skills", "skills", "sources", None)],
    "PRED-": [("created_from", "created_from", None, None),
              ("stories", "supporting_stories", None, None),
              ("conflicting", "conflicting_stories", None, None),
              ("cal", "related_calibrations", None, None)],
    "BP-": [("stories", "stories", "derived_from", None),
            ("ach", "achievements", "derived_from", None)],
}


# ---------------------------------------------------------------------------
# PRYMITYWY PARSERA
# ---------------------------------------------------------------------------

def _scalar(text, key):
    """Wartosc skalarna klucza najwyzszego poziomu.

    Obsluguje `key: wartosc` oraz `key: >` z blokiem wcietym ponizej.
    """
    m = re.search(rf"^{re.escape(key)}:[ \t]*(.*)$", text, re.M)
    if not m:
        return ""
    val = m.group(1).strip()
    if val in (">", "|", ">-", "|-"):
        # blok wielolinijkowy: zbierz wciete linie az do pustej + niewcietej
