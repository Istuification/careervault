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
            "visibility": "private" if aid in set(model.priv_ids()) else "professional",
            # Relacje wychodzace -- powielone z map na dole celowo:
            # konsument doboru pracuje na jednym rekordzie naraz.
            "skills": sorted(model.a2s.get(aid, [])),
            "stories": sorted(model.a2st.get(aid, [])),
            "development_areas": sorted(model.a2dev.get(aid, [])),
        }
        for aid, a in sorted(model.ach.items())
    }

    skills = {
        sid: {
            "id": sid,
            "name": s["name"],
            "category": s["category"],
            "level": s["level"],
            "importance": s["importance"],
            "keywords": s["keywords"],
            "capabilities": s["capabilities"],
            "related_skills": s["related"],
            # PELNA lista. To jest ten rekord, ktory w wiring-context.md
            # konczyl sie na "(+1)".
            "evidence": sorted(s["evidence"]),
            "evidence_count": len(s["evidence"]),
            "evidence_other": s["evidence_other"],
        }
        for sid, s in sorted(model.skill.items())
    }

    stories = {
        stid: {
            "id": stid,
            "title": st["title"],
            "achievements": sorted(st["ach"]),
            "cv_bullets": st["bullets"],
            "development_areas": sorted(model.st2dev.get(stid, [])),
        }
        for stid, st in sorted(model.story.items())
    }

    development_areas = {
        did: {
            "id": did,
            "title": d["title"],
            "category": d["category"],
            "status": d["status"],
            "achievements": sorted(d["ach"]),
            "stories": sorted(d["stories"]),
            "skills": sorted(d["skills"]),
        }
        for did, d in sorted(model.dev.items())
    }

    predictors = {
        pid: {
            "id": pid,
            "name": p["name"],
            "status": p["status"],
            "confidence": p["confidence"],
            "version": p["version"],
            "last_updated": p["updated"],
            "created_from": p["created_from"],
            "supporting_stories": p["stories"],
            "conflicting_stories": p["conflicting"],
            "related_calibrations": p["cal"],
            "related_behavioral_patterns": p["bp"],
        }
        for pid, p in sorted(model.pred.items())
    }

    behavioral_patterns = {
        bid: {
            "id": bid,
            "name": b["name"],
            "status": b["status"],
            "confidence": b["confidence"],
            "stories": sorted(b["stories"]),
            "achievements": sorted(b["ach"]),
        }
        for bid, b in sorted(model.bp.items())
    }

    roles = [
        {"code": code, "label": label, "period": period, "achievements": sorted(achs)}
        for code, label, period, achs in model.roles
    ]

    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": now,
        "commit": commit,
        # Deklaracja zakresu -- analogicznie do naglowkow pozostalych
        # artefaktow, zeby czytajacy model nie wyciagnal falszywego
        # wniosku "brak dowodu" z pominietego pola opisowego.
        "scope": {
            "complete": "Wszystkie identyfikatory i relacje. Zadna lista nie jest skracana.",
            "omitted": "Tresci opisowe rekordow (situation, actions, impact, "
                       "observed_pattern). Ich brak tutaj nie oznacza braku w Vaulcie.",
        },
        "counts": {
            "achievements": len(achievements),
            "skills": len(skills),
            "stories": len(stories),
            "development_areas": len(development_areas),
            "predictors": len(predictors),
            "behavioral_patterns": len(behavioral_patterns),
            "roles": len(roles),
        },
        "achievements": achievements,
        "skills": skills,
        "stories": stories,
        "development_areas": development_areas,
        "predictors": predictors,
        "behavioral_patterns": behavioral_patterns,
        "roles": roles,
        "relations": {
            "ach_to_skills": _sorted_map(model.a2s),
            "ach_to_stories": _sorted_map(model.a2st),
            "ach_to_development": _sorted_map(model.a2dev),
            "story_to_development": _sorted_map(model.st2dev),
            "ach_to_role": dict(sorted(model.ach_role.items())),
        },
    }


def run(root, model, now, commit, to_stdout=False):
    data = build(model, now, commit)
    # sort_keys=False -- kolejnosc pol jest ustalona wyzej i czytelna;
    # sortowanie alfabetyczne wymieszaloby metadane z trescia.
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"

    if to_stdout:
        sys.stdout.write(text)
        return

    out_dir = os.path.join(root, OUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUT_FILENAME), "w", encoding="utf-8") as fh:
        fh.write(text)


def _git_commit(root):
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=root, stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()
    except Exception:
        return "unknown"


def main():
    from vault_model import VaultModel

    root = os.getcwd()
    model = VaultModel(root)
    for msg in model.errors():
        print(f"BLAD  {msg}", file=sys.stderr)
    if model.errors():
        return 1

    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")
    to_stdout = "--stdout" in sys.argv
    run(root, model, now, _git_commit(root), to_stdout=to_stdout)
    if not to_stdout:
        print(f"Zapisano {OUT_DIR}/{OUT_FILENAME}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
