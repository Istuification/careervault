#!/usr/bin/env python3
"""
render_readmes.py

Generuje sekcje "Indeks rekordow" / "Encje powiazane" / "Luki w powiazaniach"
wewnatrz README poszczegolnych modulow.

Sekcja generowana zyje miedzy znacznikami:

    <!-- VAULT:GENERATED:START -->
    ...tresc nadpisywana przy kazdym buildzie...
    <!-- VAULT:GENERATED:END -->

Wszystko POZA tymi znacznikami jest tekstem pisanym recznie i nigdy nie
jest ruszane. Znaczniki sa komentarzami HTML, wiec nie widac ich w renderze
na GitHubie.

Obslugiwane moduly:
    Achievements/          ACH-*      indeks + relacje + luki
    Skills/                SKILL-*    indeks + relacje + luki
    Stories/               STORY-*    indeks + relacje + luki
    Development Areas/     DEV-*      indeks + zrodla
    Assessments/Predictors/            PRED-*  indeks
    Assessments/Behavioral Patterns/   BP-*    indeks

Kalibracje (CAL-*) celowo pominiete -- to wersjonowane dokumenty opisowe,
ktorych spis pozostaje w README pisany recznie.

Uruchamianie:
    python scripts/render_readmes.py            # zapis
    python scripts/render_readmes.py --check    # tylko sprawdz, czy aktualne
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vault_model import VaultModel  # noqa: E402

START = "<!-- VAULT:GENERATED:START -->"
END = "<!-- VAULT:GENERATED:END -->"

STAMP_NOTE = (
    "> **Sekcja generowana automatycznie** ze stanu Vaulta "
    "(`scripts/render_readmes.py`).\n"
    "> Nie edytuj recznie — zmiany wprowadzaj w rekordach i przegeneruj."
)


# ---------------------------------------------------------------------------
# NARZEDZIA
# ---------------------------------------------------------------------------

def esc(text):
    """Tresc bezpieczna w komorce tabeli markdown."""
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def trim(text, n):
    text = " ".join(str(text).split())
    return text if len(text) <= n else text[:n - 1].rstrip(" ,-") + "…"


def link(ids, titles=None, sep="<br>"):
    """Lista identyfikatorow jako `ID` — Tytul."""
    if not ids:
        return "—"
    if titles is None:
        return " ".join(f"`{i}`" for i in ids)
    out = []
    for i in ids:
        t = titles.get(i, "")
        out.append(f"`{i}` — {esc(trim(t, 70))}" if t else f"`{i}`")
    return sep.join(out)


# ---------------------------------------------------------------------------
# RENDERERY SEKCJI
# ---------------------------------------------------------------------------

def render_achievements(m):
    W = []
    a = W.append
    skill_t = {k: v["name"] for k, v in m.skill.items()}
    story_t = {k: v["title"] for k, v in m.story.items()}
    dev_t = {k: v["title"] for k, v in m.dev.items()}

    prof, priv = m.prof_ids(), m.priv_ids()

    a("# Indeks rekordów")
    a("")
    a(STAMP_NOTE)
    a("")
    a(f"Łącznie: **{len(m.ach)}** rekordów — {len(prof)} zawodowych, {len(priv)} prywatnych.")
    a("")
    a(f"## Zawodowe ({len(prof)})")
    a("")
    a("| ID | Tytuł | Firma | Okres | Waga |")
    a("| --- | --- | --- | --- | --- |")
    for i in prof:
        x = m.ach[i]
        a(f"| `{i}` | {esc(x['title'])} | {esc(x.get('company', ''))} | "
          f"{x['start']} → {x['end']} | {x.get('importance', '')} |")
    a("")
    a(f"## Prywatne ({len(priv)})")
    a("")
    a("| ID | Tytuł | Okres | Waga |")
    a("| --- | --- | --- | --- |")
    for i in priv:
        x = m.ach[i]
        a(f"| `{i}` | {esc(trim(x['title'], 110))} | {x['start']} → {x['end']} | "
          f"{x.get('importance', '')} |")
    a("")
    a("---")
    a("")

    a("# Encje powiązane")
    a("")
    a(STAMP_NOTE)
    a("")
    a("Źródła powiązań (single source of truth — powiązania nie są duplikowane "
      "w rekordach ACH):")
    a("")
    a("* **Skills** — pole `evidence` w rekordach `SKILL-*`,")
    a("* **Stories** — pole `evidence.achievement_ids` w rekordach `STORY-*`,")
    a("* **Development Areas** — pole `sources.achievements` w rekordach `DEV-*`.")
    a("")
    a("| ID | Tytuł | Skills | Stories | Development Areas |")
    a("| --- | --- | --- | --- | --- |")
    for i in prof + priv:
        a(f"| `{i}` | {esc(trim(m.ach[i]['title'], 90))} | "
          f"{link(m.a2s.get(i, []), skill_t)} | "
          f"{link(m.a2st.get(i, []), story_t)} | "
          f"{link(m.a2dev.get(i, []), dev_t)} |")
    a("")
    a("---")
    a("")

    a("# Luki w powiązaniach")
    a("")
    a(STAMP_NOTE)
    a("")
    a("## Achievementy bez Story")
    a("")
    a("Nie jest to błąd — Story powstaje tylko tam, gdzie istnieje łuk narracyjny. "
      "Lista jako materiał do przeglądu:")
    a("")
    gaps = [i for i in prof + priv if not m.a2st.get(i)]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(trim(m.ach[i]['title'], 110))}")
    else:
        a("_Brak — każdy Achievement ma powiązaną historię._")
    a("")
    a("## Achievementy bez powiązanego Skilla")
    a("")
    a("Achievement bez kompetencji nie jest wykorzystywany jako dowód w module Skills:")
    a("")
    gaps = [i for i in prof + priv if not m.a2s.get(i)]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(trim(m.ach[i]['title'], 110))}")
    else:
        a("_Brak — każdy Achievement jest dowodem co najmniej jednej kompetencji._")
    return "\n".join(W)


def render_skills(m):
    W = []
    a = W.append
    ach_t = {k: v["title"] for k, v in m.ach.items()}
    skill_t = {k: v["name"] for k, v in m.skill.items()}
    story_t = {k: v["title"] for k, v in m.story.items()}
    dev_t = {k: v["title"] for k, v in m.dev.items()}

    # SKILL -> DEV (z sources.skills)
    s2dev = {}
    for did, d in m.dev.items():
        for sk in d["skills"]:
            s2dev.setdefault(sk, []).append(did)

    ids = sorted(m.skill)

    a("# Indeks rekordów")
    a("")
    a(STAMP_NOTE)
    a("")
    a(f"Łącznie: **{len(ids)}** kompetencji.")
    a("")
    a("| ID | Nazwa | Kategoria | Poziom | Waga | Dowody (ACH) |")
    a("| --- | --- | --- | --- | --- | --- |")
    for i in ids:
        s = m.skill[i]
        a(f"| `{i}` | {esc(s['name'])} | {esc(s.get('category', ''))} | "
          f"{esc(s.get('level', ''))} | {s.get('importance', '')} | "
          f"{len(s['evidence'])} |")
    a("")
    a("---")
    a("")

    a("# Encje powiązane")
    a("")
    a(STAMP_NOTE)
    a("")
    a("Źródła powiązań:")
    a("")
    a("* **Achievements** — pole `evidence` rekordu `SKILL-*` (powiązanie bezpośrednie),")
    a("* **Related skills** — pole `related_skills` rekordu `SKILL-*`,")
    a("* **Development Areas** — pole `sources.skills` w rekordach `DEV-*`,")
    a("* **Stories** — powiązanie **wyliczone**: Story wskazujące Achievement, "
      "który jest dowodem tej kompetencji.")
    a("")
    a("| ID | Nazwa | Achievements (dowody) | Related skills | Development Areas |")
    a("| --- | --- | --- | --- | --- |")
    for i in ids:
        s = m.skill[i]
        rel = [r for r in s.get("related", []) if r != i]
        a(f"| `{i}` | {esc(s['name'])} | {link(s['evidence'], ach_t)} | "
          f"{link(rel, skill_t)} | {link(sorted(s2dev.get(i, [])), dev_t)} |")
    a("")
    a("## Rozwinięcie per rekord")
    a("")
    for i in ids:
        s = m.skill[i]
        rel = [r for r in s.get("related", []) if r != i]
        stories = sorted({st for aid in s["evidence"] for st in m.a2st.get(aid, [])})
        a(f"### `{i}` — {s['name']}")
        a("")
        a("* **Achievements (dowody):**")
        for x in s["evidence"] or ["_brak_"]:
            a(f"  - `{x}` — {esc(trim(ach_t.get(x, ''), 100))}" if x != "_brak_" else "  - _brak_")
        a("* **Related skills:**")
        for x in rel or ["_brak_"]:
            a(f"  - `{x}` — {skill_t.get(x, '')}" if x != "_brak_" else "  - _brak_")
        a("* **Stories (wyliczone przez ACH):**")
        for x in stories or ["_brak_"]:
            a(f"  - `{x}` — {esc(trim(story_t.get(x, ''), 100))}" if x != "_brak_" else "  - _brak_")
        a("* **Development Areas:**")
        for x in sorted(s2dev.get(i, [])) or ["_brak_"]:
            a(f"  - `{x}` — {dev_t.get(x, '')}" if x != "_brak_" else "  - _brak_")
        a("")
    a("---")
    a("")

    a("# Luki w powiązaniach")
    a("")
    a(STAMP_NOTE)
    a("")
    a("## Kompetencje bez dowodu")
    a("")
    gaps = [i for i in ids if not m.skill[i]["evidence"]]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(m.skill[i]['name'])}")
    else:
        a("_Brak — każda kompetencja wskazuje co najmniej jeden Achievement._")
    a("")
    a("## Kompetencje bez słów kluczowych")
    a("")
    a("Brak `keywords` oznacza, że dopasowanie do oferty opiera się wyłącznie na nazwie:")
    a("")
    gaps = [i for i in ids if not m.skill[i].get("keywords")]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(m.skill[i]['name'])}")
    else:
        a("_Brak — każda kompetencja ma słowa kluczowe._")
    a("")
    a("## Autoreferencje w `related_skills`")
    a("")
    a("Kompetencja wskazująca samą siebie — wpis bez znaczenia informacyjnego, "
      "pomijany w listach powyżej:")
    a("")
    self_ref = [i for i in ids if i in m.skill[i].get("related", [])]
    if self_ref:
        for i in self_ref:
            a(f"* `{i}` ({esc(m.skill[i]['name'])}) wskazuje `{i}`")
    else:
        a("_Brak._")
    return "\n".join(W)


def render_stories(m):
    W = []
    a = W.append
    ach_t = {k: v["title"] for k, v in m.ach.items()}
    skill_t = {k: v["name"] for k, v in m.skill.items()}
    dev_t = {k: v["title"] for k, v in m.dev.items()}
    ids = sorted(m.story)

    a("# Indeks rekordów")
    a("")
    a(STAMP_NOTE)
    a("")
    a(f"Łącznie: **{len(ids)}** historii.")
    a("")
    a("| ID | Tytuł | Achievementy źródłowe |")
    a("| --- | --- | --- |")
    for i in ids:
        s = m.story[i]
        a(f"| `{i}` | {esc(s['title'])} | "
          f"{', '.join(f'`{x}`' for x in s['ach']) or '—'} |")
    a("")
    a("---")
    a("")

    a("# Encje powiązane")
    a("")
    a(STAMP_NOTE)
    a("")
    a("Źródła powiązań:")
    a("")
    a("* **Achievements** — pole `evidence.achievement_ids` rekordu `STORY-*`,")
    a("* **Development Areas** — pole `sources.stories` w rekordach `DEV-*`,")
    a("* **Skills** — powiązanie **wyliczone**: kompetencje, których pole `evidence` "
      "wskazuje Achievement źródłowy tej historii.")
    a("  Nie należy mylić z polem `competencies` w rekordzie Story, które jest "
      "listą etykiet narracyjnych.")
    a("")
    a("| ID | Tytuł | Achievements | Skills (wyliczone) | Development Areas |")
    a("| --- | --- | --- | --- | --- |")
    for i in ids:
        s = m.story[i]
        skills = sorted({sk for aid in s["ach"] for sk in m.a2s.get(aid, [])})
        a(f"| `{i}` | {esc(trim(s['title'], 90))} | {link(s['ach'], ach_t)} | "
          f"{link(skills, skill_t)} | {link(sorted(m.st2dev.get(i, [])), dev_t)} |")
    a("")
    a("---")
    a("")

    a("# Luki w powiązaniach")
    a("")
    a(STAMP_NOTE)
    a("")
    a("## Historie bez `evidence.achievement_ids`")
    a("")
    a("Zasada utrzymania nr 1 mówi: każda Story opiera się na co najmniej jednym "
      "Achievemencie.")
    a("")
    gaps = [i for i in ids if not m.story[i]["ach"]]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(m.story[i]['title'])}")
    else:
        a("_Brak — każda historia wskazuje co najmniej jeden Achievement._")
    a("")
    a("## Historie bez `cv_bullets`")
    a("")
    gaps = [i for i in ids if not m.story[i]["bullets"]]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(m.story[i]['title'])}")
    else:
        a("_Brak — każda historia ma gotowe sformułowania do CV._")
    return "\n".join(W)


def render_dev(m):
    W = []
    a = W.append
    ach_t = {k: v["title"] for k, v in m.ach.items()}
    skill_t = {k: v["name"] for k, v in m.skill.items()}
    story_t = {k: v["title"] for k, v in m.story.items()}
    ids = sorted(m.dev)

    a("# Indeks rekordów")
    a("")
    a(STAMP_NOTE)
    a("")
    a(f"Łącznie: **{len(ids)}** obszarów rozwoju.")
    a("")
    a("| ID | Tytuł | Kategoria | Status |")
    a("| --- | --- | --- | --- |")
    for i in ids:
        d = m.dev[i]
        a(f"| `{i}` | {esc(d['title'])} | {esc(d['category'])} | {esc(d['status'])} |")
    a("")
    a("---")
    a("")

    a("# Encje powiązane")
    a("")
    a(STAMP_NOTE)
    a("")
    a("Źródłem powiązań jest pole `sources` rekordu `DEV-*`. "
      "Development Area bez źródeł nie powinien istnieć.")
    a("")
    a("| ID | Tytuł | Achievements | Stories | Skills |")
    a("| --- | --- | --- | --- | --- |")
    for i in ids:
        d = m.dev[i]
        a(f"| `{i}` | {esc(trim(d['title'], 60))} | {link(d['ach'], ach_t)} | "
          f"{link(d['stories'], story_t)} | {link(d['skills'], skill_t)} |")
    a("")
    a("---")
    a("")

    a("# Luki w powiązaniach")
    a("")
    a(STAMP_NOTE)
    a("")
    a("## Obszary bez źródeł dowodowych")
    a("")
    gaps = [i for i in ids if not (m.dev[i]["ach"] or m.dev[i]["stories"])]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(m.dev[i]['title'])}")
    else:
        a("_Brak — każdy obszar wskazuje Achievement lub Story._")
    return "\n".join(W)


def render_pred(m):
    W = []
    a = W.append
    ids = sorted(m.pred)

    a("# Indeks rekordów")
    a("")
    a(STAMP_NOTE)
    a("")
    a(f"Łącznie: **{len(ids)}** predyktorów.")
    a("")
    a("Kolumna `#STORY` podaje liczbę wspierających historii. `Konflikty` "
      "wskazuje historie sprzeczne z hipotezą — wartość niezerowa jest sygnałem "
      "do rewizji, nie błędem.")
    a("")
    a("| ID | Nazwa | Status | Pewność | #STORY | Konflikty | Wersja | Aktualizacja |")
    a("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for i in ids:
        p = m.pred[i]
        a(f"| `{i}` | {esc(p['name'])} | {esc(p['status'])} | {esc(p['confidence'])} | "
          f"{len(p['stories'])} | {len(p['conflicting'])} | {esc(p['version'])} | "
          f"{esc(p['updated'])} |")
    a("")
    a("---")
    a("")

    a("# Encje powiązane")
    a("")
    a(STAMP_NOTE)
    a("")
    a("Źródłem powiązań jest frontmatter rekordu `PRED-*`.")
    a("")
    a("| ID | Nazwa | Wspierające historie | Kalibracje | Narzędzia źródłowe |")
    a("| --- | --- | --- | --- | --- |")
    for i in ids:
        p = m.pred[i]
        a(f"| `{i}` | {esc(trim(p['name'], 50))} | {link(p['stories'])} | "
          f"{link(p['cal'])} | {esc(', '.join(p['created_from'])) or '—'} |")
    a("")
    a("---")
    a("")

    a("# Luki w powiązaniach")
    a("")
    a(STAMP_NOTE)
    a("")
    a("## Predyktory bez wspierającej historii")
    a("")
    a("Hipoteza bez zakotwiczenia w obserwowanej sytuacji pozostaje niezweryfikowana:")
    a("")
    gaps = [i for i in ids if not m.pred[i]["stories"]]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(m.pred[i]['name'])}")
    else:
        a("_Brak — każdy predyktor wskazuje co najmniej jedną historię._")
    a("")
    a("## Predyktory bez kalibracji")
    a("")
    gaps = [i for i in ids if not m.pred[i]["cal"]]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(m.pred[i]['name'])}")
    else:
        a("_Brak — każdy predyktor przeszedł co najmniej jedną kalibrację._")
    return "\n".join(W)


def render_bp(m):
    W = []
    a = W.append
    ids = sorted(m.bp)

    a("# Indeks rekordów")
    a("")
    a(STAMP_NOTE)
    a("")
    a(f"Łącznie: **{len(ids)}** wzorców zachowań.")
    a("")
    a("| ID | Nazwa | Status | Pewność | #STORY | #ACH |")
    a("| --- | --- | --- | --- | --- | --- |")
    for i in ids:
        b = m.bp[i]
        a(f"| `{i}` | {esc(b['name'])} | {esc(b['status'])} | {esc(b['confidence'])} | "
          f"{len(b['stories'])} | {len(b['ach'])} |")
    a("")
    a("---")
    a("")

    a("# Encje powiązane")
    a("")
    a(STAMP_NOTE)
    a("")
    a("Źródłem powiązań jest pole `derived_from` rekordu `BP-*`. Wzorzec opisuje "
      "zachowanie obserwowane w wielu niezależnych sytuacjach — liczba źródeł jest "
      "miarą jego powtarzalności.")
    a("")
    a("| ID | Nazwa | Stories | Achievements |")
    a("| --- | --- | --- | --- |")
    for i in ids:
        b = m.bp[i]
        a(f"| `{i}` | {esc(trim(b['name'], 50))} | {link(b['stories'])} | "
          f"{link(b['ach'])} |")
    a("")
    a("---")
    a("")

    a("# Luki w powiązaniach")
    a("")
    a(STAMP_NOTE)
    a("")
    a("## Wzorce bez źródeł")
    a("")
    gaps = [i for i in ids if not (m.bp[i]["stories"] or m.bp[i]["ach"])]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(m.bp[i]['name'])}")
    else:
        a("_Brak — każdy wzorzec wskazuje źródła w `derived_from`._")
    a("")
    a("## Wzorce oparte na pojedynczym źródle")
    a("")
    a("Jedno źródło nie wystarcza, by mówić o wzorcu powtarzalnym:")
    a("")
    gaps = [i for i in ids if len(m.bp[i]["stories"]) + len(m.bp[i]["ach"]) == 1]
    if gaps:
        for i in gaps:
            a(f"* `{i}` — {esc(m.bp[i]['name'])}")
    else:
        a("_Brak — każdy wzorzec opiera się na wielu źródłach._")
    return "\n".join(W)


TARGETS = [
    ("Achievements/README.md", render_achievements),
    ("Skills/README.md", render_skills),
    ("Stories/README.md", render_stories),
    ("Development Areas/README.md", render_dev),
    ("Assessments/Predictors/README.md", render_pred),
    ("Assessments/Behavioral Patterns/README.md", render_bp),
]


# ---------------------------------------------------------------------------
# PODMIANA SEKCJI
# ---------------------------------------------------------------------------

def splice(path, body):
    """Podmienia tresc miedzy znacznikami. Zwraca (nowy_tekst, zmienione)."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()

    if START not in text or END not in text:
        raise SystemExit(
            f"BLAD: {path} nie zawiera znacznikow {START} / {END}.\n"
            f"       Dodaj je recznie w miejscu, gdzie ma trafic sekcja generowana."
        )
    if text.index(END) < text.index(START):
        raise SystemExit(f"BLAD: {path} — znacznik END wystepuje przed START.")

    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END), re.S
    )
    new = pattern.sub(lambda _: START + "\n" + body.rstrip() + "\n" + END, text, count=1)
    return new, (new != text)


def run(root, check_only=False, model=None):
    """Generuje sekcje we wszystkich README. Zwraca liste zmienionych plikow."""
    m = model or VaultModel(root)
    changed = []
    for rel, renderer in TARGETS:
        path = os.path.join(root, rel)
        if not os.path.isfile(path):
            # Blad, nie pominiecie. TARGETS to zamknieta lista modulow --
            # brak pliku oznacza zmiane nazwy albo skasowanie, a nie
            # sytuacje dopuszczalna. Wczesniej build przechodzil na zielono
            # z cala sekcja indeksu wypadnieta z README.
            raise SystemExit(
                f"BLAD: brak pliku {rel}.\n"
                f"       Modul jest na liscie TARGETS, wiec jego README musi "
                f"istniec.\n"
                f"       Przywroc plik albo usun wpis z TARGETS "
                f"w scripts/render_readmes.py."
            )
        new, diff = splice(path, renderer(m))
        if diff:
            changed.append(rel)
            if not check_only:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
    return changed


def main():
    root = os.getcwd()
    check = "--check" in sys.argv
    changed = run(root, check_only=check)
    if check:
        if changed:
            print("README nieaktualne:")
            for c in changed:
                print(f"  ! {c}")
            sys.exit(1)
        print("README aktualne.")
    else:
        if changed:
            print(f"Zaktualizowano {len(changed)} README:")
            for c in changed:
                print(f"  {c}")
        else:
            print("README bez zmian.")


if __name__ == "__main__":
    main()
