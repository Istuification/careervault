#!/usr/bin/env python3
"""
test_parser.py

Test regresyjny prymitywow parsera z vault_model.py.

Powstal po audycie, ktory pokazal, ze parser regexowy nie zawodzi glosno --
przy nieznanym formatowaniu po cichu zwraca pusta liste, a rekord znika
z indeksu bez zadnego sladu w logu. Kazdy przypadek ponizej odpowiada
jednemu takiemu cichemu zgubieniu.

Czesc A dziala na czystej bibliotece standardowej i musi przechodzic
zawsze. Czesc B porownuje parser z PyYAML na prawdziwych rekordach --
jesli PyYAML nie jest zainstalowany, jest pomijana (build w GitHub
Actions nie instaluje zadnych zaleznosci).

Uruchamianie:
    python scripts/test_parser.py

Kody wyjscia:
    0  wszystkie testy przeszly
    1  co najmniej jeden test nie przeszedl
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from vault_model import (  # noqa: E402
    VaultModel, _list, _nested_list, _clean, _period, _count_items,
)

FAILED = []


def check(name, got, want):
    if got == want:
        print(f"  ok    {name}")
    else:
        print(f"  BLAD  {name}\n          otrzymano: {got!r}\n          oczekiwano: {want!r}")
        FAILED.append(name)


# ---------------------------------------------------------------------------
# A. PRZYPADKI BRZEGOWE PARSERA
# ---------------------------------------------------------------------------

def test_primitives():
    print("\n— prymitywy —")

    # `_nested_list` nie moze wyjsc poza blok rodzica. Gdy `sources:` nie ma
    # `skills:`, poprzednia wersja brala pierwszy `skills:` napotkany
    # gdziekolwiek dalej w pliku.
    leak = (
        "id: DEV-999\n"
        "sources:\n"
        "  achievements:\n"
        "    - ACH-001\n"
        "review:\n"
        "  skills:\n"
        "    - SKILL-999\n"
    )
    check("nested_list nie wycieka poza rodzica",
          _nested_list(leak, "sources", "skills"), [])
    check("nested_list czyta wlasny podklucz",
          _nested_list(leak, "sources", "achievements"), ["ACH-001"])

    # Pusta linia i komentarz miedzy kluczem a lista sa poprawnym YAML-em.
    check("lista po pustej linii",
          _list("keywords:\n\n  - BPMN\n  - UML\n", "keywords"), ["BPMN", "UML"])
    check("lista po komentarzu",
          _list("keywords:\n  # komentarz\n  - BPMN\n", "keywords"), ["BPMN"])
    check("pusta linia wewnatrz listy",
          _list("keywords:\n  - BPMN\n\n  - UML\n", "keywords"), ["BPMN", "UML"])

    # Lista konczy sie na kolejnym kluczu -- nie wolno przeskoczyc dalej.
    check("lista konczy sie na kolejnym kluczu",
          _list("keywords:\nroles:\n  - PM\n", "keywords"), [])
    check("nie lapie listy zagniezdzonej",
          _list("evidence:\n  achievement_ids:\n    - ACH-001\n", "evidence"), [])

    # Cudzyslowy i komentarze.
    check("komentarz po skalarze cytowanym", _clean('"tekst" # opis'), "tekst")
    check("hash wewnatrz cudzyslowu", _clean('"tekst # z hashem"'), "tekst # z hashem")
    check("dwukropek w cudzyslowie", _clean("'wartosc z: dwukropkiem'"), "wartosc z: dwukropkiem")
    check("komentarz po wartosci prostej", _clean("SKILL-004   # Product Management"), "SKILL-004")
    check("hash bez spacji to tresc", _clean("wartosc#bez-spacji"), "wartosc#bez-spacji")
    # Cudzyslow otwarty, ale nie domkniety wokol calej wartosci -- to zwykly
    # tekst, nie skalar cytowany (tak jest w STORY-011).
    check("cudzyslow tylko na poczatku", _clean('"dziala" to nie to samo co "ulozone"'),
          '"dziala" to nie to samo co "ulozone"')

    # `period` niezalezny od kolejnosci kluczy.
    check("period w kolejnosci start-end",
          _period("period:\n  start: 2023-01\n  end: 2024-01\n"), ("2023-01", "2024-01"))
    check("period w kolejnosci end-start",
          _period("period:\n  end: 2024-01\n  start: 2023-01\n"), ("2023-01", "2024-01"))
    check("period z dodatkowym kluczem",
          _period("period:\n  start: 2023-01\n  note: x\n  end: 2024-01\n"),
          ("2023-01", "2024-01"))

    # Licznik walidacyjny: pole jawnie puste to nie strata.
    check("licznik ignoruje jawnie puste",
          _count_items("conflicting_stories: []\n", "conflicting_stories"), 0)
    check("licznik liczy pozycje",
          _count_items("stories:\n  - STORY-001\n  - STORY-002\n", "stories"), 2)
    check("licznik z filtrem prefiksu",
          _count_items("evidence:\n  - ACH-015\n  - opis tekstowy\n", "evidence", "ACH-"), 1)


# ---------------------------------------------------------------------------
# B. PARSER vs PyYAML NA PRAWDZIWYCH REKORDACH
# ---------------------------------------------------------------------------

def test_against_pyyaml(root):
    print("\n— zgodnosc z PyYAML —")
    try:
        import yaml
    except ImportError:
        print("  pominieto (brak PyYAML — to nie jest blad)")
        return

    m = VaultModel(root)
    checked = skipped = 0

    def norm(v):
        # Parser zwraca "" dla klucza nieobecnego, PyYAML zwraca None.
        # Dla porownania to ten sam stan: brak wartosci.
        if v is None:
            return []
        items = v if isinstance(v, list) else [v]
        return [str(x).strip() for x in items if str(x).strip() != ""]

    plan = [
        ("Achievements", "ACH-", m.ach, [
            ("title", lambda y: y.get("title")),
            ("company", lambda y: y.get("company")),
            ("importance", lambda y: y.get("importance")),
            ("start", lambda y: (y.get("period") or {}).get("start")),
            ("end", lambda y: (y.get("period") or {}).get("end")),
        ]),
        ("Skills", "SKILL-", m.skill, [
            ("name", lambda y: y.get("name")),
            ("keywords", lambda y: y.get("keywords")),
            ("related", lambda y: y.get("related_skills")),
            ("evidence", lambda y: [x for x in (y.get("evidence") or [])
                                    if str(x).startswith("ACH-")]),
        ]),
        ("Stories", "STORY-", m.story, [
            ("title", lambda y: y.get("title")),
            ("ach", lambda y: (y.get("evidence") or {}).get("achievement_ids")),
            ("bullets", lambda y: y.get("cv_bullets")),
        ]),
        ("Development Areas", "DEV-", m.dev, [
            ("title", lambda y: y.get("title")),
            ("ach", lambda y: (y.get("sources") or {}).get("achievements")),
            ("stories", lambda y: (y.get("sources") or {}).get("stories")),
            ("skills", lambda y: (y.get("sources") or {}).get("skills")),
        ]),
    ]

    for folder, prefix, records, fields in plan:
        d = os.path.join(root, folder)
        for fname in sorted(os.listdir(d)):
            if not (fname.startswith(prefix) and fname.lower().endswith((".yaml", ".yml"))):
                continue
            raw = open(os.path.join(d, fname), encoding="utf-8").read()
            try:
                y = yaml.safe_load(raw)
            except Exception:
                # Rekord nie jest poprawnym YAML-em. Parser regexowy sobie
                # z nim radzi, wiec to nie jest blad tego testu -- ale nie
                # ma z czym porownac.
                skipped += 1
                continue
            if not isinstance(y, dict):
                skipped += 1
                continue
            rec = records.get(str(y.get("id", "")).strip())
            if rec is None:
                FAILED.append(f"{fname}: rekord nie trafil do modelu")
                print(f"  BLAD  {fname}: rekord nie trafil do modelu")
                continue
            for field, getter in fields:
                if norm(rec.get(field)) != norm(getter(y)):
                    FAILED.append(f"{fname}.{field}")
                    print(f"  BLAD  {fname}.{field}\n"
                          f"          parser: {norm(rec.get(field))!r}\n"
                          f"          yaml  : {norm(getter(y))!r}")
                checked += 1

    print(f"  ok    porownano {checked} pol"
          + (f", pominieto {skipped} rekordow bez poprawnego YAML-a" if skipped else ""))


def main():
    root = os.getcwd()
    test_primitives()
    test_against_pyyaml(root)

    print()
    if FAILED:
        print(f"NIEPOWODZENIE — {len(FAILED)} testow nie przeszlo:")
        for f in FAILED:
            print(f"  ! {f}")
        return 1
    print("Wszystkie testy przeszly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
