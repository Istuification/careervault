#!/usr/bin/env python3
"""
render_json.py

Generuje `dist/vault.json` -- maszynowe wejscie do doboru rekordow.

DLACZEGO OSOBNY ARTEFAKT, A NIE PARSOWANIE `wiring-context.md`

`wiring-context.md` jest pisany dla LLM-a i swiadomie skraca dlugie listy
przez `_fmt(..., limit=N)`: zamiast wszystkich pozycji wypisuje pierwsze N
i dokleja `(+K)`. Dla czytelnika to bez znaczenia -- widzi skale, a szczegol
i tak sprawdzi w rekordzie. Dla parsera to katastrofa cicha: `obecne:` przy
SKILL-017 to zamknieta lista par ACH<->SKILL, wiec walidacja binarna oparta
na przycietej liscie odrzuci poprawna pare, ktorej po prostu w niej nie ma.
Nie poleci wyjatek, nie bedzie bledu w logu -- kandydat nigdy sie nie pojawi.
Diagnoza po fakcie jest droga, bo wszystko wyglada na dzialajace.

Do tego sam `wiring-context.md` deklaruje w naglowku, ze nie sluzy do
pisania CV ani wnioskowania o kompetencjach, i ze brak dowodu w nim nie
oznacza braku w Vaulcie. Ta deklaracja jest trafna i nie ma sensu z nia
walczyc parserem.

Ten plik jest odwrotnoscia tamtego w kazdym z tych wymiarow:

  * zero obcinania -- kazda lista w calosci,
  * stabilny kontrakt (`schema_version`), a nie formatowanie markdownu,
  * stempel `commit` i `generated_at`, wiec wiadomo z czego powstal,
  * relacje w obie strony (`a2s` i `evidence` w SKILL), zeby dobor
    nie musial odwracac mapy w locie i myslec o sortowaniu.

CO JEST W SRODKU

Pelny model: ACH, SKILL, STORY, DEV, PRED, BP, role oraz mapy relacji.
Bez tresci opisowych (`situation`, `actions`, `impact`) -- z tego samego
powodu, dla ktorego nie ma ich w `wiring-context.md`: to one robia
z Vaulta 215k tokenow, a do doboru wystarczaja identyfikatory, nazwy
i slowa kluczowe. Roznica polega na tym, ze tutaj *zadna lista
identyfikatorow nie jest skracana*.

UZYCIE
    python scripts/render_json.py            # zapis do dist/vault.json
    python scripts/render_json.py --stdout   # podglad
"""

import os
import sys
import json
import datetime
import subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

OUT_DIR = "dist"
OUT_FILENAME = "vault.json"

# Podnosic przy zmianie ksztaltu danych (usuniecie/zmiana znaczenia pola).
# Dodanie nowego pola nie wymaga podniesienia -- konsument ma je ignorowac.
SCHEMA_VERSION = 1


def _sorted_map(d):
    """Mapa relacji z posortowanymi kluczami i wartosciami.

    Sortowanie jest czescia kontraktu: bez niego kolejnosc zalezy od
    kolejnosci wczytania plikow, a diff `vault.json` szumi przy kazdym
    buildzie i przestaje niesc informacje.
    """
    return {k: sorted(v) for k, v in sorted(d.items())}


def build(model, now, commit):
    """Serializuje caly model. Zadna lista nie jest skracana."""

    priv_set = set(model.priv_ids())
    achievements = {
        aid: {
            "id": aid,
            "title": a["title"],
            "company": a["company"],
            "start": a["start"],
            "end": a["end"],
            "importance": a["importance"],
            "impact": a["impact"],
            "roles": a["roles"],
            "role_code": model.ach_role.get(aid),
            # Pole `visibility` w rekordzie wygrywa, gdy jest ustawione --
            # tak MK dopuszcza pojedynczy ACH-P do CV bez zmiany jego ID
            # (np. prywatny projekt VaultShot na oferty zwiazane z AI/tools).
            # Brak pola: domyslne zachowanie z prefiksu ACH-P, bez zmian.
            "visibility": a["visibility"] or ("private" if aid in priv_set else "professional"),
            # Relacje wychodzace -- powielone z map na dole celowo:
            # konsument doboru pracuje na jednym rekordzie naraz.
            "skills": sorted(model.a2s.get(aid, [])),
            "stories": sorted(model.a2st.get(aid, [])),
            "development_areas": sorted(model.a2dev.get(aid, [])),
        }
        for aid, a in sorted(model.ach.items())
    }

    skills = {
