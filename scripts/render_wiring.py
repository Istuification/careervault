#!/usr/bin/env python3
"""
render_wiring.py

Generuje `dist/wiring-context.md` -- kompaktowy zrzut Vaulta przeznaczony
do jednego konkretnego zadania: podjecia decyzji, pod ktore istniejace
rekordy podpiac NOWY ACH (albo STORY / PRED).

DLACZEGO OSOBNY PLIK, A NIE `Vaultshot index.md`

Indeks odpowiada na pytanie "co jest w Vaulcie" -- jest zorganizowany
wokol ACH, bo tak sie go czyta przy pisaniu CV. Podpinanie wymaga
odwrotnej perspektywy: "ktora kompetencja szuka dowodu", "ktora historia
ma luke", "ktory wzorzec opiera sie na jednym zrodle". To inny przekroj
tych samych danych i inna kolejnosc sortowania.

Roznica jest praktyczna. Model czytajacy indeks widzi ACH-y i musi
zgadnac, gdzie pasuja. Model czytajacy ten plik widzi kompetencje wraz
z ich slowami kluczowymi i aktualnym nasyceniem dowodami -- czyli
dokladnie to, na podstawie czego podejmuje sie decyzje.

CO JEST W SRODKU

  1. Sekcja SKILL   -- nazwa, poziom, keywords, capabilities, licznik dowodow
  2. Sekcja STORY   -- tytul, podpiete ACH, powiazane DEV
  3. Sekcja DEV     -- tytul, status, zrodla
  4. Sekcja BP      -- nazwa, pewnosc, zrodla
  5. Sekcja PRED    -- nazwa, pewnosc, wspierajace i sprzeczne historie
  6. Role           -- kody z Experience.md (do pola `experience` w patchu)
  7. Sygnaly        -- rekordy niedowiazane i przeciazone

CZEGO NIE MA I DLACZEGO

Brak tresci opisowych (`situation`, `actions`, `impact`, `observed_pattern`).
Kusi, zeby je dolozyc "dla kontekstu", ale to wlasnie one robia z Vaulta
215k tokenow. Do decyzji "czy ten ACH dowodzi tej kompetencji" wystarcza
nazwa kompetencji i jej slowa kluczowe -- tresc ACH model i tak ma przed
soba, bo wlasnie go napisal.

UZYCIE

    python scripts/render_wiring.py            # zapis do dist/
    python scripts/render_wiring.py --stdout   # na ekran
"""

import os
import sys
import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from vault_model import VaultModel  # noqa: E402


OUT_DIR = "dist"
OUT_FILENAME = "wiring-context.md"

# Progi sygnalow. Nie sa to bledy -- to punkty, w ktorych warto spojrzec
# rekordowi na rece. Dobrane z rozkladu obecnego Vaulta (mediana dowodow
# na kompetencje: 7, mediana kompetencji na ACH: 4).
SKILL_THIN = 2          # kompetencja o tylu dowodach lub mniej szuka wsparcia
SKILL_BLOATED = 15      # powyzej tego kompetencja jest prawdopodobnie za szeroka
ACH_OVERWIRED = 6       # ACH podpiety pod tyle kompetencji budzi watpliwosc


def _fmt(items, limit=None, sep=", "):
    """Lista jako tekst, opcjonalnie przycieta z licznikiem reszty."""
    if not items:
        return "—"
    if limit and len(items) > limit:
        return sep.join(items[:limit]) + f" (+{len(items) - limit})"
    return sep.join(items)


def _saturation(n):
    """Znacznik nasycenia dowodami -- czytelny dla czlowieka i dla modelu."""
    if n <= SKILL_THIN:
        return "SZUKA DOWODOW"
    if n >= SKILL_BLOATED:
        return "PRZECIAZONA"
    return ""


def build_wiring_md(model, now, commit):
    W = []
    a = W.append

    a("# Kontekst podpinania rekordow")
    a("")
    a("Plik generowany automatycznie przez `scripts/render_wiring.py`.")
    a("Nie edytowac recznie — zmiany zostana nadpisane przy kolejnym buildzie.")
    a("")
    a("## Do czego sluzy ten plik")
    a("")
    a("Zawiera **wylacznie szkielet relacyjny** Vaulta: identyfikatory, nazwy,")
    a("slowa kluczowe i aktualne powiazania. Nie zawiera tresci rekordow")
    a("(`situation`, `actions`, `impact`, `observed_pattern` i podobnych).")
    a("")
    a("Sluzy do jednej decyzji: **pod ktore istniejace rekordy podpiac nowy**")
    a("ACH, STORY albo PRED. Nie sluzy do oceny Vaulta, pisania CV ani")
    a("wnioskowania o kompetencjach — brak dowodu w tym pliku nie oznacza")
    a("braku dowodu w Vaulcie, bo tresc zostala tu celowo pominieta.")
    a("")
    a(f"Stan: {model.summary()}.")
    a("")

    # -- SKILL -----------------------------------------------------------
    a("---")
    a("")
    a("## Kompetencje (SKILL)")
    a("")
    a("Kolumna `dowody` to liczba ACH juz podpietych pod kompetencje.")
    a(f"Znacznik `SZUKA DOWODOW` przy <= {SKILL_THIN}, `PRZECIAZONA` przy >= {SKILL_BLOATED}.")
    a("")
    a("Podpiecie nowego ACH oznacza dopisanie go do `evidence:` w pliku kompetencji.")
    a("")

    by_cat = {}
    for sid, s in model.skill.items():
        by_cat.setdefault(s["category"] or "—", []).append(sid)

    for cat in sorted(by_cat):
        a(f"### {cat}")
        a("")
        for sid in sorted(by_cat[cat]):
            s = model.skill[sid]
            n = len(s["evidence"])
            flag = _saturation(n)
            head = f"**{sid}** — {s['name']}"
            if s["level"]:
                head += f" ({s['level']})"
            head += f" · dowody: {n}"
            if flag:
                head += f" · **{flag}**"
            a(head)
            if s["keywords"]:
                a(f"  - slowa kluczowe: {_fmt(s['keywords'], limit=8)}")
            if s["capabilities"]:
                a(f"  - zakres: {_fmt(s['capabilities'], limit=8)}")
            a(f"  - obecne: {_fmt(s['evidence'], limit=10)}")
            a("")

    # -- STORY -----------------------------------------------------------
    a("---")
    a("")
    a("## Historie (STORY)")
    a("")
    a("Podpiecie nowego ACH oznacza dopisanie go do `evidence.achievement_ids:`.")
    a("Historia opisuje zwykle jedno spojne wydarzenie — nowy ACH pasuje tylko")
    a("wtedy, gdy stanowi jej czesc, a nie gdy dotyczy podobnego tematu.")
    a("")
    for stid in sorted(model.story):
        s = model.story[stid]
        a(f"**{stid}** — {s['title']}")
        a(f"  - ACH: {_fmt(s['ach'])}")
        dev = model.st2dev.get(stid, [])
        if dev:
            a(f"  - zasila DEV: {_fmt(dev)}")
        bp = sorted([b for b, v in model.bp.items() if stid in v["stories"]])
        if bp:
            a(f"  - zasila BP: {_fmt(bp)}")
        pred = sorted([p for p, v in model.pred.items() if stid in v["stories"]])
        if pred:
            a(f"  - zasila PRED: {_fmt(pred)}")
        a("")

    # -- DEV -------------------------------------------------------------
    a("---")
    a("")
    a("## Obszary rozwoju (DEV)")
    a("")
    a("Podpiecie oznacza dopisanie do `sources.achievements:` albo `sources.stories:`.")
    a("DEV opisuje slabosc lub obszar do poprawy — podpina sie tu ACH pokazujacy")
    a("prace nad tym obszarem, nie kazdy ACH z tej samej dziedziny.")
    a("")
    for did in sorted(model.dev):
        d = model.dev[did]
        head = f"**{did}** — {d['title']}"
        if d["status"]:
            head += f" · {d['status']}"
        a(head)
        a(f"  - ACH: {_fmt(d['ach'])} · STORY: {_fmt(d['stories'])} · SKILL: {_fmt(d['skills'])}")
        a("")

    # -- BP --------------------------------------------------------------
    a("---")
    a("")
    a("## Wzorce behawioralne (BP)")
    a("")
    a("Podpiecie oznacza dopisanie do `derived_from.achievements:` albo")
    a("`derived_from.stories:` we frontmatterze pliku `.md`.")
    a("")
    for bid in sorted(model.bp):
        b = model.bp[bid]
        head = f"**{bid}** — {b['name']}"
        meta = " · ".join(x for x in (b["status"], b["confidence"]) if x)
        if meta:
            head += f" · {meta}"
        a(head)
        a(f"  - zrodla: STORY {_fmt(b['stories'])} · ACH {_fmt(b['ach'])}")
        a("")

    # -- PRED ------------------------------------------------------------
    a("---")
    a("")
    a("## Predyktory (PRED)")
    a("")
    a("Podpiecie oznacza dopisanie STORY do `supporting_stories:` albo")
    a("`conflicting_stories:`. Historia sprzeczna jest tak samo wartosciowa")
    a("jak wspierajaca — predyktor bez zadnej sprzecznej jest slabo skalibrowany.")
    a("")
    for pid in sorted(model.pred):
        p = model.pred[pid]
        head = f"**{pid}** — {p['name']}"
        meta = " · ".join(x for x in (p["status"], p["confidence"]) if x)
        if meta:
            head += f" · {meta}"
        a(head)
        a(f"  - wspierajace: {_fmt(p['stories'])}")
        a(f"  - sprzeczne: {_fmt(p['conflicting'])}")
        if p["bp"]:
            a(f"  - BP: {_fmt(p['bp'])}")
        a("")

    # -- Role ------------------------------------------------------------
    a("---")
    a("")
    a("## Role (Experience.md)")
    a("")
    a("Nowy ACH zawodowy musi trafic do sekcji `### <Rola>` w `Experience.md`,")
    a("inaczej walidacja zglosi go jako nieprzypisanego. ACH prywatne (`ACH-P*`)")
    a("sa z tego wymogu zwolnione.")
    a("")
    for code, label, period, achs in model.roles:
        a(f"**{code}** — {label} · {period or '—'} · {len(achs)} ACH")
    a("")

    # -- Sygnaly ---------------------------------------------------------
    a("---")
    a("")
    a("## Sygnaly")
    a("")
    a("Nie sa to bledy walidacji — to miejsca, w ktorych struktura Vaulta")
    a("moze wymagac uwagi przy najblizszym podpinaniu.")
    a("")

    sig = []

    thin = sorted([(len(s["evidence"]), sid, s["name"])
                   for sid, s in model.skill.items()
                   if len(s["evidence"]) <= SKILL_THIN])
    if thin:
        sig.append("**Kompetencje o slabym pokryciu** — kandydaci przy najblizszym ACH:")
        for n, sid, name in thin:
            sig.append(f"  - {sid} ({name}): {n} dowodow")
        sig.append("")

    bloated = sorted([(len(s["evidence"]), sid, s["name"])
                      for sid, s in model.skill.items()
                      if len(s["evidence"]) >= SKILL_BLOATED], reverse=True)
    if bloated:
        sig.append("**Kompetencje przeciazone** — rozwazyc rozbicie na wezsze:")
        for n, sid, name in bloated:
            sig.append(f"  - {sid} ({name}): {n} dowodow")
        sig.append("")

    over = sorted([(len(v), k) for k, v in model.a2s.items()
                   if len(v) > ACH_OVERWIRED], reverse=True)
    if over:
        sig.append(f"**ACH podpiete pod > {ACH_OVERWIRED} kompetencji** — "
                   f"sprawdzic, czy kazde podpiecie ma pokrycie w tresci:")
        for n, aid in over:
            sig.append(f"  - {aid}: {n} kompetencji ({_fmt(model.a2s[aid], limit=6)})")
        sig.append("")

    orphan = sorted([a for a in model.ach
                     if a not in model.a2st and a not in model.a2dev])
    if orphan:
        sig.append("**ACH bez STORY i bez DEV** — istnieja jako fakt, ale nie maja")
        sig.append("narracji, ktora mozna opowiedziec na rozmowie:")
        sig.append(f"  - {_fmt(orphan, limit=20)}")
        sig.append("")

    lonely_bp = sorted([b for b, v in model.bp.items()
                        if len(v["stories"]) + len(v["ach"]) <= 1])
    if lonely_bp:
        sig.append("**BP opierajace sie na jednym zrodle** — wzorzec z jednego")
        sig.append("przypadku jest hipoteza, nie wzorcem:")
        sig.append(f"  - {_fmt(lonely_bp, limit=20)}")
        sig.append("")

    uncal = sorted([p for p, v in model.pred.items() if not v["conflicting"]])
    if uncal:
        sig.append("**PRED bez historii sprzecznej** — brak kontrprzykladu oznacza,")
        sig.append("ze predyktor nie byl testowany na granicy:")
        sig.append(f"  - {_fmt(uncal, limit=20)}")
        sig.append("")

    cats = {}
    for s in model.skill.values():
        c = (s["category"] or "").strip()
        if c:
            cats.setdefault(c.lower().replace("&", "and").replace(" ", ""), set()).add(c)
    dupes = [sorted(v) for v in cats.values() if len(v) > 1]
    if dupes:
        sig.append("**Kategorie SKILL zapisane niejednolicie** — utrudnia grupowanie:")
        for group in dupes:
            sig.append(f"  - {' / '.join(group)}")
        sig.append("")

    if sig:
        W.extend(sig)
    else:
        a("Brak sygnalow.")
        a("")

    a("---")
    a("")
    a(f"_Wygenerowano {now} · commit {commit}_")

    return "\n".join(W) + "\n"


def run(root, model, now, commit, to_stdout=False):
    content = build_wiring_md(model, now, commit)
    if to_stdout:
        print(content)
        return content
    out_dir = os.path.join(root, OUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUT_FILENAME), "w", encoding="utf-8") as fh:
        fh.write(content)
    return content


def main():
    root = os.getcwd()
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")
    try:
        import subprocess
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=root,
            stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        commit = "unknown"

    model = VaultModel(root)
    if model.errors():
        print("Vault ma bledy walidacji — napraw je przed generowaniem kontekstu:")
        for e in model.errors():
            print(f"  {e}")
        return 1

    run(root, model, now, commit, to_stdout="--stdout" in sys.argv)
    if "--stdout" not in sys.argv:
        print(f"Zapisano {OUT_DIR}/{OUT_FILENAME}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
