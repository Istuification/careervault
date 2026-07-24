#!/usr/bin/env python3
"""
render_site.py

Buduje witryne GitHub Pages dla Career Vault.

Co powstaje w katalogu dist/:

  index.html
      Landing page dla ludzi (rekruterow) + wskazowka dla asystentow AI.
      Trzy warianty pliku tekstowego do pobrania/podgladu.

  vault-full.txt        cala tresc repozytorium
  vault-evidence.txt    warstwa dowodowa
  vault-assessments.txt warstwa interpretacyjna

Rozmiary w tokenach nie sa wpisane na sztywno -- build() mierzy kazdy
wariant i wstawia wynik do naglowka, na landing i do llms.txt.

  robots.txt, sitemap.xml, llms.txt

Indeks generatora CV (`Vaultshot index.md`) NIE jest publikowany. Zostaje
w repozytorium jako zrodlo dla skilla /generuj-cv. W blokach CORE plikow
zbiorczych zastapil go `dist/wiring-context.md` -- mapa relacji miedzy
rekordami wszystkich typow, generowana przez render_wiring.py, ktory MUSI
byc uruchomiony przed tym skryptem.

Kazdy plik .txt ma na poczatku:
  - naglowek ZAKRES (co jest w pliku, czego NIE MA, gdzie znalezc reszte),
  - protokol dla asystenta AI,
  - spis plikow z numerami linii.

Kolejnosc plikow w kazdym .txt jest ustalona wg priorytetu czytania:
dokumenty najbogatsze semantycznie (przewodnik, tozsamosc, model poznawczy,
README sekcji) ida pierwsze, zeby model zbudowal ramy interpretacyjne, zanim
dojdzie do surowych rekordow YAML.

Uruchamiane przez GitHub Actions przy kazdym commicie, mozna tez lokalnie:

    python scripts/render_site.py
"""

import os
import re
import html
import datetime
import subprocess

ROOT = os.getcwd()
OUTPUT_DIR = "dist"
REPO_URL = "https://github.com/Istuification/careervault"
SITE_URL = "https://istuification.github.io/careervault"

ROBOTS_DIRECTIVE = "index, follow"
GENERATE_SITEMAP = True
GOOGLE_SITE_VERIFICATION = "CGT3gQeHAQC3i1Br876eXIn_R690XbIp7YUSjt2Q5MY"

EXCLUDE_DIRS = {".git", ".github", "dist", "node_modules", ".vscode", "scripts"}
INCLUDE_EXTENSIONS = {".md", ".yaml", ".yml", ".txt"}

# Indeks generatora CV. Powstaje w render_index.py i zostaje w repozytorium
# (galaz main) -- NIE trafia juz ani do plikow zbiorczych, ani do dist/.
# Wykluczenie ponizej chroni przed wciagnieciem go przez automatyczne
# zbieranie plikow, bo jego odbiorca jest skill /generuj-cv, nie czytelnik
# strony.
INDEX_FILENAME = "Vaultshot index.md"

# Kontekst podpinania. Zastapil indeks w bloku CORE plikow zbiorczych.
# Powod: indeks jest jednokierunkowy (ACH -> SKILL/STORY) i sluzy produkcji
# CV, natomiast ten plik pokazuje relacje w obie strony i obejmuje takze
# warstwe interpretacyjna (BP, PRED). Dla czytelnika plikow zbiorczych --
# czlowieka albo modelu oceniajacego dopasowanie -- to wlasciwsza mapa.
#
# Sciezka wskazuje na dist/, wiec render_wiring.py MUSI zostac uruchomiony
# przed tym skryptem. build.py wymusza ta kolejnosc (krok 4 przed 5).
WIRING_FILENAME = os.path.join("dist", "wiring-context.md")

EXCLUDE_FILES = {INDEX_FILENAME.lower()}


# ---------------------------------------------------------------------------
# DEFINICJA WARIANTOW PLIKU TEKSTOWEGO
# ---------------------------------------------------------------------------
#
# CORE_ORDER -- dokumenty czytane najpierw. Sa najbardziej tresciwe semantycznie
# i zawieraja referencje do identyfikatorow, wiec model latwiej odnajduje sie
# potem w surowych rekordach.
#
# Kolejnosc jest swiadoma:
#   1. AI Interpretation Guide  -- jak czytac cala reszte
#   1a. Kontekst podpinania     -- mapa relacji SKILL/STORY/DEV/BP/PRED
#   2. About / Identity / Experience -- kim jest kandydat, w jakim kontekscie
#   3. Cognitive model          -- jak podejmuje decyzje
#   4. Context Entries          -- w jakich warunkach powstawaly dowody
#   5. README sekcji            -- legenda do rekordow ACH / SKILL / STORY
#   6. README glowny            -- nawigacja po repo (na koncu bloku core)
# ---------------------------------------------------------------------------

CORE_EVIDENCE = [
    "AI Interpretation Guide.md",
    WIRING_FILENAME,
    "About.md",
    "Identity.md",
    "Experience.md",
    "Assessments/Cognitive model.md",
    "Context Entries/README.md",
    "Context Entries/CTX-001.yaml",
    "Context Entries/CTX-002.yaml",
    "Context Entries/CTX-003.yaml",
    "Achievements/README.md",
    "Skills/README.md",
    "Stories/README.md",
    "README.md",
]

# Wariant "assessments": bez README sekcji dowodowych (ACH/SKILL/STORY),
# bez Context Entries; za to z README warstwy interpretacyjnej.
CORE_ASSESSMENTS = [
    "AI Interpretation Guide.md",
    WIRING_FILENAME,
    "About.md",
    "Identity.md",
    "Experience.md",
    "Assessments/Cognitive model.md",
    "Assessments/README.md",
    "README.md",
]

# Prefiksy katalogow przypisane do warstw.
EVIDENCE_DIRS = ["Achievements/", "Skills/", "Stories/", "Development Areas/", "Context Entries/"]
ASSESSMENT_DIRS = ["Assessments/"]

VARIANTS = {
    "full": {
        "filename": "vault-full.txt",
        "label": "Pełny Vault",
        "tokens": "",  # wyliczane w build() — patrz fmt_tokens()
        "core": CORE_EVIDENCE,
        "includes": "wszystko",
        "scope_yes": [
            "Achievements (ACH-*) — udokumentowane osiągnięcia",
            "Skills (SKILL-*) — kompetencje z dowodami",
            "Stories (STORY-*) — narracyjne opisy sytuacji zawodowych",
            "Development Areas (DEV-*) — obszary rozwojowe i luki",
            "Context Entries (CTX-*) — kontekst organizacyjny",
            "Assessment Data — surowe wyniki testów",
            "Behavioral Patterns (BP-*), Calibrations (CAL-*), Predictors (PRED-*)",
            "Cognitive model, About, Identity, Experience, AI Interpretation Guide",
            "Kontekst podpinania — mapa relacji miedzy rekordami wszystkich typow",
        ],
        "scope_no": [],
        "elsewhere": [],
    },
    "evidence": {
        "filename": "vault-evidence.txt",
        "label": "Warstwa dowodowa",
        "tokens": "",  # wyliczane w build() — patrz fmt_tokens()
        "core": CORE_EVIDENCE,
        "includes": "evidence",
        "scope_yes": [
            "Achievements (ACH-*) — udokumentowane osiągnięcia",
            "Skills (SKILL-*) — kompetencje z dowodami",
            "Stories (STORY-*) — narracyjne opisy sytuacji zawodowych",
            "Development Areas (DEV-*) — obszary rozwojowe i luki",
            "Context Entries (CTX-*) — kontekst organizacyjny",
            "Cognitive model, About, Identity, Experience, AI Interpretation Guide",
            "Kontekst podpinania — mapa relacji miedzy rekordami wszystkich typow",
        ],
        "scope_no": [
            "Assessment Data — surowe wyniki testów psychometrycznych",
            "Behavioral Patterns (BP-*) — wzorce zachowań wyprowadzone z testów",
            "Calibrations (CAL-*) — kalibracje samooceny",
            "Predictors (PRED-*) — predyktory dopasowania do ról",
        ],
        "elsewhere": ["vault-assessments.txt", "vault-full.txt"],
    },
    "assessments": {
        "filename": "vault-assessments.txt",
        "label": "Warstwa interpretacyjna",
        "tokens": "",  # wyliczane w build() — patrz fmt_tokens()
        "core": CORE_ASSESSMENTS,
        "includes": "assessments",
        "scope_yes": [
            "Assessment Data — surowe wyniki testów psychometrycznych",
            "Behavioral Patterns (BP-*) — wzorce zachowań wyprowadzone z testów",
            "Calibrations (CAL-*) — kalibracje samooceny",
            "Predictors (PRED-*) — predyktory dopasowania do ról",
            "Cognitive model, About, Identity, Experience, AI Interpretation Guide",
            "Kontekst podpinania — mapa relacji miedzy rekordami wszystkich typow",
        ],
        "scope_no": [
            "Achievements (ACH-*) — udokumentowane osiągnięcia",
            "Skills (SKILL-*) — kompetencje z dowodami",
            "Stories (STORY-*) — narracyjne opisy sytuacji zawodowych",
            "Development Areas (DEV-*) — obszary rozwojowe i luki",
            "Context Entries (CTX-*) — kontekst organizacyjny",
        ],
        "elsewhere": ["vault-evidence.txt", "vault-full.txt"],
    },
}

# Kolejnosc wariantow na landingu i w komunikatach.
VARIANT_ORDER = ["evidence", "assessments", "full"]

# Domyslny plik wskazywany botom w llms.txt i w metadanych.
DEFAULT_VARIANT = "evidence"


# ---------------------------------------------------------------------------
# NARZEDZIA
# ---------------------------------------------------------------------------

def read_file(rel_path):
    full = os.path.join(ROOT, rel_path)
    try:
        with open(full, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except Exception as e:
        return f"[BLAD ODCZYTU PLIKU {rel_path}: {e}]"


def collect_all_files():
    collected = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")]
        for fname in filenames:
            if fname.lower() in EXCLUDE_FILES:
                continue
            if os.path.splitext(fname)[1].lower() in INCLUDE_EXTENSIONS:
                collected.append(os.path.relpath(os.path.join(dirpath, fname), ROOT))
    return collected


def norm(p):
    return p.replace("\\", "/")


def fmt_tokens(n_chars):
    """Rozmiar pliku jako przyblizona liczba tokenow.

    Dzielnik 3.5 znaku na token to konserwatywne przyblizenie dla polskiego
    tekstu z duza iloscia identyfikatorow. Zaokraglenie w gore do pelnego
    tysiaca, zeby liczba nie zmieniala sie przy kazdej drobnej edycji.
    """
    tys = round(n_chars / 3.5 / 1000)
    return f"~{tys} tys. tokenów"


def in_dirs(rel, prefixes):
    low = norm(rel).lower()
    return any(low.startswith(p.lower()) for p in prefixes)


def select_files(all_files, variant_key):
    """Zwraca liste plikow dla danego wariantu, w docelowej kolejnosci:
    najpierw blok CORE (dokladnie w zadanej kolejnosci), potem reszta
    posortowana wg vault_sort_key."""
    v = VARIANTS[variant_key]
    core = [f for f in v["core"] if os.path.isfile(os.path.join(ROOT, f))]
    core_set = {norm(f).lower() for f in core}

    rest = []
    for f in all_files:
        if norm(f).lower() in core_set:
            continue
        mode = v["includes"]
        if mode == "wszystko":
            rest.append(f)
        elif mode == "evidence":
            if in_dirs(f, EVIDENCE_DIRS):
                rest.append(f)
        elif mode == "assessments":
            if in_dirs(f, ASSESSMENT_DIRS):
                rest.append(f)

    return core + sorted(rest, key=vault_sort_key)


def vault_sort_key(f):
    """Sortowanie plikow SPOZA bloku core -- twarde dowody przed psychometria."""
    low = norm(f).lower()
    if low.startswith("context entries/"):
        group = 0
    elif low.startswith("achievements/"):
        group = 1
    elif low.startswith("skills/"):
        group = 2
    elif low.startswith("stories/"):
        group = 3
    elif low.startswith("development areas/"):
        group = 4
    elif low.startswith("assessments/assessment data"):
        group = 5
    elif low.startswith("assessments/behavioral patterns/"):
        group = 6
    elif low.startswith("assessments/calibrations/"):
        group = 7
    elif low.startswith("assessments/predictors/"):
        group = 8
    else:
        group = 9
    return (group, low)


# ---------------------------------------------------------------------------
# PLIKI ZBIORCZE .txt
# ---------------------------------------------------------------------------

def build_scope_header(variant_key):
    """Naglowek ZAKRES: co jest, czego nie ma, gdzie szukac reszty."""
    v = VARIANTS[variant_key]
    out = []
    out.append("ZAKRES TEGO PLIKU")
    out.append("-" * 70)
    out.append(f"Wariant: {v['label']} ({v['filename']}, {v['tokens']})")
    out.append("")
    out.append("TEN PLIK ZAWIERA:")
    for line in v["scope_yes"]:
        out.append(f"  + {line}")
    out.append("")

    if v["scope_no"]:
        out.append("TEGO PLIKU NIE MA W SRODKU — NIE WNIOSKUJ Z BRAKU:")
        for line in v["scope_no"]:
            out.append(f"  - {line}")
        out.append("")
        out.append("Powyzsze sekcje ISTNIEJA w Vaulcie, ale zostaly swiadomie pominiete")
        out.append("w tym wariancie, zeby zmiescic sie w oknie kontekstowym. Jesli")
        out.append("potrzebujesz ich do oceny, poinformuj o tym osobe, z ktora rozmawiasz,")
        out.append("i popros o jeden z plikow:")
        for other in v["elsewhere"]:
            out.append(f"  {SITE_URL}/{other}")
        out.append("")
        out.append("NIE pisz, ze 'brak dowodow na X', jesli X nalezy do sekcji wymienionej")
        out.append("powyzej jako pominieta. To brak w TYM PLIKU, nie brak w Vaulcie.")
    else:
        out.append("Ten wariant zawiera CALA tresc repozytorium — nic nie zostalo pominiete.")
    out.append("")
    return out


def build_protocol(variant_key):
    v = VARIANTS[variant_key]
    out = []
    out.append("PROTOKOL DLA ASYSTENTA AI:")
    out.append(f"- Ten plik ma {v['tokens']}. Agenci przegladajacy strony czesto NIE")
    out.append("  pobieraja duzych plikow w calosci — ucinaja je w polowie.")
    out.append("- Jesli nie masz PEWNOSCI, ze wczytales caly plik (sprawdz spis linii")
    out.append("  ponizej i dojdz do ostatniej pozycji), NIE oceniaj tresci. Zamiast")
    out.append("  tego popros osobe, z ktora rozmawiasz, o pobranie pliku i wklejenie")
    out.append("  go do rozmowy jako zalacznik.")
    out.append("- Opieraj sie wylacznie na tresci z Vaultu. Nie uzupelniaj brakujacych")
    out.append("  faktow z pamieci. Rekordy sa self-report: potwierdzaja spojnosc i")
    out.append("  istnienie, nie sa zewnetrzna weryfikacja pracodawcy.")
    out.append("- Kolejnosc plikow nie jest przypadkowa. Poczatek pliku (przewodnik,")
    out.append("  About, Identity, Experience, model poznawczy, README sekcji) buduje")
    out.append("  ramy interpretacyjne i zawiera referencje do identyfikatorow.")
    out.append("  Przeczytaj go, zanim zaczniesz oceniac surowe rekordy YAML.")
    out.append("- Priorytet dowodowy: najpierw Achievements (ACH-*) i Stories (STORY-*),")
    out.append("  potem testy, na koncu model poznawczy.")
    out.append("- Sekcja 'Kontekst podpinania' zaraz na poczatku pliku pokazuje, ktory")
    out.append("  rekord jest powiazany z ktorym i w ktora strone. Uzyj jej, zeby")
    out.append("  sprawdzic, czy dana kompetencja ma pokrycie w konkretnych")
    out.append("  osiagnieciach, zamiast opierac sie na samej deklaracji.")
    out.append("")
    return out


def build_vault_txt(files, variant_key, now, commit):
    # --- Przebieg 1: bloki tresci + offsety linii ---
    body_lines = []
    file_start_offset = {}

    def emit(text):
        for sub in text.split("\n"):
            body_lines.append(sub)

    for f in files:
        file_start_offset[f] = len(body_lines)
        emit(f"### PLIK: {f}")
        emit("-" * 70)
        emit(read_file(f).rstrip())
        emit("")
        emit("=" * 70)
        emit("")

    # --- Przebieg 2: naglowek ---
    v = VARIANTS[variant_key]
    header = []
    header.append(f"CAREER VAULT — {v['label'].upper()} (wygenerowano automatycznie)")
    header.append(f"Wygenerowano: {now} UTC | Commit: {commit}")
    header.append("=" * 70)
    header.append("")
    header += build_scope_header(variant_key)
    header.append("=" * 70)
    header.append("")
    header += build_protocol(variant_key)
    header.append("=" * 70)
    header.append("")
    header.append("SPIS PLIKOW (z numerami linii w tym pliku):")

    closing = ["", "=" * 70, ""]
    header_line_count = len(header) + len(files) + len(closing)

    for f in files:
        abs_line = header_line_count + file_start_offset[f] + 1
        header.append(f" - linia {abs_line:>6} : {f}")
    header += closing

    return "\n".join(header + body_lines)


# ---------------------------------------------------------------------------
# HTML: wspolny blok meta
# ---------------------------------------------------------------------------

def head_meta(path, title, description):
    path = path.strip("/")
    canonical = SITE_URL + "/" + (path + "/" if path else "")
    title_esc = html.escape(title, quote=True)
    desc_esc = html.escape(description, quote=True)
    parts = [
        f'<link rel="canonical" href="{canonical}">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:url" content="{canonical}">',
        f'<meta property="og:title" content="{title_esc}">',
        f'<meta property="og:description" content="{desc_esc}">',
        '<meta property="og:locale" content="pl_PL">',
        '<meta name="twitter:card" content="summary">',
        f'<meta name="twitter:title" content="{title_esc}">',
        f'<meta name="twitter:description" content="{desc_esc}">',
    ]
    if GOOGLE_SITE_VERIFICATION.strip():
        parts.insert(0, f'<meta name="google-site-verification" '
                        f'content="{html.escape(GOOGLE_SITE_VERIFICATION.strip(), quote=True)}">')
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# HTML: strona glowna
# ---------------------------------------------------------------------------

LANDING_TEMPLATE = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Career Vault — evidence-based career record</title>
<meta name="description" content="Ustrukturyzowana, oparta na dowodach baza wiedzy zawodowej. Przeglądaj repozytorium albo pobierz jeden z trzech plików przygotowanych dla asystentów AI.">
<meta name="robots" content="__ROBOTS__">
__HEAD_META__
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{
    --paper: #EEF1EC; --card: #E4E9E1; --ink: #16221D; --ink-soft: #4B5A54;
    --line: #C7D0C6; --teal: #24594B; --teal-ink: #F3F6F1;
    --indigo: #33396B; --indigo-ink: #F1F2F8; --radius: 10px;
  }
  *{ box-sizing: border-box; }
  html{ scroll-behavior: smooth; }
  body{ margin:0; background:var(--paper); color:var(--ink);
        font-family:"IBM Plex Sans", system-ui, sans-serif; line-height:1.55;
        -webkit-font-smoothing: antialiased; }
  .wrap{ max-width:1100px; margin:0 auto; padding:4.5rem 2rem 3rem; }
  .eyebrow{ font-family:"JetBrains Mono", monospace; font-size:0.78rem;
            letter-spacing:0.14em; text-transform:uppercase; color:var(--ink-soft);
            margin:0 0 1.1rem; }
  .eyebrow::before{ content:""; display:inline-block; width:0.5em; height:0.5em;
                    background:var(--teal); margin-right:0.6em; border-radius:1px;
                    vertical-align:middle; }
  h1{ font-family:"Fraunces", Georgia, serif; font-optical-sizing:auto; font-weight:500;
      font-size:clamp(2rem, 5vw, 3rem); line-height:1.12; letter-spacing:-0.01em; margin:0 0 1.1rem; }
  .lede{ font-size:1.05rem; color:var(--ink-soft); margin:0 0 2.75rem; }
  .lede strong{ color:var(--ink); font-weight:600; }
  .section-label{ font-family:"JetBrains Mono", monospace; font-size:0.78rem;
                  letter-spacing:0.1em; text-transform:uppercase; color:var(--ink-soft);
                  margin:0 0 1rem; }
  .paths{ display:grid; grid-template-columns:repeat(3, 1fr); gap:1.25rem; margin-bottom:2rem; }
  @media (max-width:900px){ .paths{ grid-template-columns:1fr; } }
  .card{ border:1px solid var(--line); border-radius:var(--radius); background:var(--card);
         display:flex; flex-direction:column; overflow:hidden; }
  .card.recommended{ border-color:var(--indigo); box-shadow:0 0 0 1px var(--indigo); }
  .card-tab{ display:flex; align-items:center; gap:0.55rem; padding:0.7rem 1.1rem;
             font-family:"JetBrains Mono", monospace; font-size:0.72rem; letter-spacing:0.1em;
             text-transform:uppercase; color:var(--indigo-ink); background:var(--indigo); }
  .card.human .card-tab{ background:var(--teal); color:var(--teal-ink); }
  .card-tab svg{ width:15px; height:15px; flex-shrink:0; }
  .card-tab .badge{ margin-left:auto; font-size:0.62rem; opacity:0.85; letter-spacing:0.08em; }
  .card-body{ padding:1.3rem 1.1rem 1.4rem; display:flex; flex-direction:column; gap:0.8rem; flex-grow:1; }
  .card-body h2{ font-family:"Fraunces", Georgia, serif; font-weight:500; font-size:1.25rem; margin:0; }
  .card-body p{ margin:0; color:var(--ink-soft); font-size:0.92rem; }
  .card-body p.grow{ flex-grow:1; }
  .size{ font-family:"JetBrains Mono", monospace; font-size:0.74rem; color:var(--indigo);
         letter-spacing:0.04em; }
  .btn{ display:inline-flex; align-items:center; justify-content:center; gap:0.4em;
        font-family:"JetBrains Mono", monospace; font-size:0.82rem; text-decoration:none;
        color:var(--indigo-ink); background:var(--indigo); border:none; border-radius:6px;
        padding:0.65rem 0.9rem; cursor:pointer; transition:transform 0.12s ease, opacity 0.12s ease; }
  .card.human .btn{ background:var(--teal); color:var(--teal-ink); }
  .btn.secondary{ background:transparent; color:var(--indigo); border:1px solid var(--line); }
  .btn:hover{ transform:translateY(-1px); opacity:0.92; }
  .btn:focus-visible{ outline:2px solid var(--ink); outline-offset:2px; }
  .human-row{ margin-bottom:2.75rem; }
  .human-row .card{ max-width:100%; }
  .ai-hint{ border:1px solid var(--line); border-left:3px solid var(--indigo);
            background:var(--card); border-radius:8px; padding:1rem 1.2rem; margin-bottom:2.75rem;
            font-size:0.95rem; color:var(--ink-soft); }
  .ai-hint strong{ color:var(--ink); }
  .ai-hint a{ color:var(--indigo); font-weight:600; }
  .ai-steps{ margin:0.6rem 0 0; padding-left:1.2rem; }
  .ai-steps li{ margin:0.35rem 0; }
  .about{ border-top:1px solid var(--line); padding-top:2rem; margin-bottom:2.5rem; }
  .about h3{ font-family:"JetBrains Mono", monospace; font-size:0.78rem; letter-spacing:0.1em;
             text-transform:uppercase; color:var(--ink-soft); margin:0 0 0.9rem; }
  .about p{ margin:0 0 0.9rem; color:var(--ink-soft); }
  .about p:last-child{ margin-bottom:0; }
  .about.prompts{ border-top:none; padding-top:0; margin-top:-1.6rem; }
  .prompt-list{ margin:0; padding:0; list-style:none; display:flex; flex-direction:column; gap:0.6rem; }
  .prompt-list li{ font-family:"JetBrains Mono", monospace; font-size:0.82rem; color:var(--ink);
                   background:var(--card); border:1px solid var(--line); border-radius:6px;
                   padding:0.6rem 0.8rem; line-height:1.5; }
  footer{ font-family:"JetBrains Mono", monospace; font-size:0.74rem; color:var(--ink-soft);
          border-top:1px solid var(--line); padding-top:1.3rem; display:flex; flex-wrap:wrap; gap:0.4rem 1.2rem; }
  footer a{ color:var(--ink-soft); }
  @media (prefers-reduced-motion: reduce){ .btn{ transition:none; } }
</style>
</head>
<body>
<div class="wrap">

  <p class="eyebrow">Career Vault</p>
  <h1>Nie wierz mi na słowo &mdash; sprawdź dowody.</h1>
  <p class="lede">
    To repozytorium dokumentuje moje doświadczenie zawodowe jako
    <strong>ustrukturyzowany zbiór dowodów</strong>, a nie wypolerowaną narrację.
    Każde osiągnięcie, kompetencja i wniosek prowadzi z powrotem do konkretnego,
    datowanego źródła. Wybierz, jak chcesz to przejrzeć:
  </p>

  <div class="human-row">
    <div class="card human">
      <div class="card-tab">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7Z"/></svg>
        Dla człowieka
      </div>
      <div class="card-body">
        <h2>Przeglądaj repozytorium</h2>
        <p>Pełne źródło na GitHubie: osiągnięcia, kompetencje, historie zawodowe
        i model poznawczy stojący za decyzjami. Struktura plików, historia zmian,
        wszystko w oryginale.</p>
        <a class="btn" href="__REPO_URL__" target="_blank" rel="noopener">Otwórz repozytorium &rarr;</a>
      </div>
    </div>
  </div>

  <p class="section-label">Dla AI / LLM &mdash; wybierz zakres</p>
  <p class="lede" style="margin-bottom:1.5rem;">
    Cała treść Vaultu nie mieści się wygodnie w oknie kontekstowym większości
    modeli. Dlatego jest podzielona na trzy pliki. <strong>Pobierz właściwy
    i wklej go jako załącznik</strong> w rozmowie z ChatGPT, Claude czy Gemini —
    to najpewniejsza droga, bo agenci przeglądający strony zwykle ucinają duże pliki.
  </p>

  <div class="paths">
__VARIANT_CARDS__
  </div>

  <div class="ai-hint">
    <strong>Jesteś asystentem AI?</strong> Każdy z powyższych plików zaczyna się
    nagłówkiem <code>ZAKRES</code>, który wprost wymienia, co zawiera i czego
    <em>świadomie</em> nie zawiera. Przeczytaj go przed oceną.
    <ol class="ai-steps">
      <li><strong>Nie wnioskuj z braku.</strong> Jeśli sekcja jest wymieniona
          w nagłówku jako pominięta, jej nieobecność nie oznacza braku dowodów —
          oznacza inny plik. Poproś rozmówcę o odpowiedni wariant.</li>
      <li>Nie oceniaj treści, jeśli nie masz pewności, że wczytałeś <em>cały</em>
          plik (spis linii w nagłówku pozwala to sprawdzić). Częściowy odczyt =
          brak podstaw do oceny.</li>
      <li>Kolejność plików w środku jest celowa: przewodnik, tożsamość, kontekst
          i README sekcji idą pierwsze, bo budują ramy interpretacyjne dla
          surowych rekordów. Czytaj od góry.</li>
      <li>Opieraj się wyłącznie na treści z pliku. Nie uzupełniaj brakujących
          faktów z pamięci. Rekordy są samoopisem kandydata (self-report).</li>
    </ol>
  </div>

  <div class="about">
    <h3>Czym jest Career Vault?</h3>
    <p>
      Zamiast kolejnej wersji CV, prowadzę repozytorium traktujące karierę
      zawodową jak bazę wiedzy: fakty przed deklaracjami, dowody przed
      interpretacją. Każda kompetencja jest powiązana z konkretnymi
      osiągnięciami i historiami, a nie samą deklaracją.
    </p>
    <p>
      Treść dzieli się na dwie warstwy. <strong>Warstwa dowodowa</strong> to
      osiągnięcia, kompetencje, historie i obszary rozwojowe — twarde rekordy
      z datami i kontekstem. <strong>Warstwa interpretacyjna</strong> to wyniki
      testów, wzorce zachowań i predyktory dopasowania — materiał pomocniczy,
      który tłumaczy <em>jak</em> pracuję, ale sam w sobie niczego nie dowodzi.
      Pliki do pobrania odpowiadają temu podziałowi.
    </p>
    <p>
      Wszystko generowane automatycznie przy każdej aktualizacji
      <a href="__REPO_URL__" target="_blank" rel="noopener">repozytorium na GitHub</a>.
    </p>
  </div>

  <div class="about prompts">
    <h3>Spróbuj zapytać</h3>
    <p style="margin-bottom: 1rem;">
      Po przekazaniu Vaultu asystentowi AI (najlepiej wklejając pobrany plik), dobry
      punkt startowy to jedno z tych pytań:
    </p>
    <ul class="prompt-list">
      <li>Na podstawie tego dokumentu przygotuj krótkie podsumowanie kandydata pod kątem roli [stanowisko].</li>
      <li>Jakie dowody wspierają twierdzenie, że ta osoba potrafi [konkretna kompetencja]?</li>
      <li>Porównaj udokumentowane kompetencje z wymaganiami tego ogłoszenia: [wklej ogłoszenie].</li>
      <li>Jakie pytania rekrutacyjne warto zadać tej osobie na podstawie sekcji Development Areas?</li>
    </ul>
  </div>

  <footer>
    <span>Ostatnia aktualizacja: __NOW__ UTC</span>
    <span>&middot;</span>
    <span>Commit: __COMMIT__</span>
    <span>&middot;</span>
    <span>__FILE_COUNT__ plików źródłowych</span>
    <span>&middot;</span>
    <a href="__REPO_URL__" target="_blank" rel="noopener">github.com/Istuification/careervault</a>
  </footer>

</div>
</body>
</html>
"""

VARIANT_CARD_TMPL = """    <div class="card{extra_class}">
      <div class="card-tab">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M8 10h.01M16 10h.01M8 15h8"/></svg>
        {tab}{badge}
      </div>
      <div class="card-body">
        <h2>{heading}</h2>
        <p class="grow">{desc}</p>
        <p class="size">{filename} &middot; {tokens}</p>
        <a class="btn" href="{filename}" download>Pobierz &darr;</a>
        <a class="btn secondary" href="{filename}" target="_blank" rel="noopener">Wyświetl</a>
      </div>
    </div>"""

VARIANT_COPY = {
    "evidence": {
        "tab": "Dowody",
        "badge": '<span class="badge">Zacznij tutaj</span>',
        "extra_class": " recommended",
        "heading": "Osiągnięcia i kompetencje",
        "desc": "Warstwa dowodowa: osiągnięcia, kompetencje, historie zawodowe, "
                "obszary rozwojowe i kontekst organizacyjny. To wystarczy, żeby "
                "ocenić dopasowanie do konkretnego ogłoszenia. Bez psychometrii.",
    },
    "assessments": {
        "tab": "Profil",
        "badge": "",
        "extra_class": "",
        "heading": "Profil psychometryczny",
        "desc": "Warstwa interpretacyjna: wyniki testów, wzorce zachowań, "
                "kalibracje samooceny i predyktory dopasowania do ról. Przydatne, "
                "gdy pytasz o styl pracy i współpracy, nie o dorobek.",
    },
    "full": {
        "tab": "Komplet",
        "badge": "",
        "extra_class": "",
        "heading": "Wszystko naraz",
        "desc": "Obie warstwy w jednym pliku — kompletna zawartość repozytorium. "
                "Duży: część modeli go nie udźwignie albo utnie w połowie. "
                "Wybierz, jeśli świadomie chcesz całość.",
    },
}


def build_variant_cards():
    cards = []
    for key in VARIANT_ORDER:
        v = VARIANTS[key]
        c = VARIANT_COPY[key]
        cards.append(VARIANT_CARD_TMPL.format(
            extra_class=c["extra_class"],
            tab=c["tab"],
            badge=c["badge"],
            heading=c["heading"],
            desc=c["desc"],
            filename=v["filename"],
            tokens=v["tokens"],
        ))
    return "\n".join(cards)


def build_landing_html(now, commit, file_count):
    html_out = LANDING_TEMPLATE
    meta = head_meta(
        "",
        "Career Vault — evidence-based career record",
        "Ustrukturyzowana, oparta na dowodach baza wiedzy zawodowej. Repozytorium "
        "oraz trzy pliki tekstowe przygotowane dla asystentów AI.",
    )
    html_out = html_out.replace("__HEAD_META__", meta)
    html_out = html_out.replace("__ROBOTS__", ROBOTS_DIRECTIVE)
    html_out = html_out.replace("__REPO_URL__", REPO_URL)
    html_out = html_out.replace("__VARIANT_CARDS__", build_variant_cards())
    html_out = html_out.replace("__NOW__", now)
    html_out = html_out.replace("__COMMIT__", commit)
    html_out = html_out.replace("__FILE_COUNT__", str(file_count))
    return html_out


# ---------------------------------------------------------------------------
# llms.txt / robots.txt / sitemap.xml
# ---------------------------------------------------------------------------

def build_llms_txt():
    base = SITE_URL + "/"
    lines = [
        "# Career Vault",
        "",
        "> Profil zawodowy oparty na dowodach — ustrukturyzowany zbior osiagniec, "
        "kompetencji, ocen i historii zawodowej. Tresc jest dostepna w trzech "
        "wariantach pliku tekstowego, roznacych sie zakresem.",
        "",
        "## Ktory plik wybrac (dla asystenta AI)",
        "",
    ]
    for key in VARIANT_ORDER:
        v = VARIANTS[key]
        c = VARIANT_COPY[key]
        lines.append(f"- [{v['filename']}]({base}{v['filename']}) — {c['heading']}. "
                     f"{v['tokens']}. {c['desc']}")
    lines += [
        "",
        f"Domyslnie zacznij od [{VARIANTS[DEFAULT_VARIANT]['filename']}]"
        f"({base}{VARIANTS[DEFAULT_VARIANT]['filename']}) — zawiera warstwe dowodowa,",
        "czyli material potrzebny do oceny dopasowania do stanowiska.",
        "",
        "## Zasady czytania",
        "",
        "- Kazdy plik zaczyna sie naglowkiem ZAKRES: wprost wymienia, co zawiera",
        "  i czego swiadomie nie zawiera. Przeczytaj go przed ocena.",
        "- NIE WNIOSKUJ Z BRAKU. Jesli sekcja jest wymieniona jako pominieta,",
        "  jej nieobecnosc nie oznacza braku dowodow — oznacza inny plik.",
        "- Pliki sa duze i agenci przegladajacy strony czesto ucinaja je w polowie.",
        "  Jesli nie masz pewnosci, ze wczytales calosc (patrz spis linii w naglowku),",
        "  NIE oceniaj tresci — popros czlowieka o pobranie i wklejenie pliku.",
        "- Kolejnosc plikow w srodku jest celowa: przewodnik interpretacyjny,",
        "  About, Identity, Experience, model poznawczy i README sekcji ida pierwsze,",
        "  bo buduja ramy dla surowych rekordow. Czytaj od gory.",
        "- Nie uzupelniaj brakujacych faktow z pamieci. Rekordy sa self-report.",
        "",
    ]
    return "\n".join(lines)


def build_sitemap():
    today = datetime.date.today().isoformat()
    urls = [SITE_URL + "/"]
    for key in VARIANT_ORDER:
        urls.append(f"{SITE_URL}/{VARIANTS[key]['filename']}")

    url_entries = []
    for loc in urls:
        url_entries.append(
            f'  <url>\n    <loc>{html.escape(loc, quote=True)}</loc>\n'
            f'    <lastmod>{today}</lastmod>\n  </url>'
        )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(url_entries) + '\n'
        '</urlset>\n'
    )


def build_robots():
    lines = ["User-agent: *", "Allow: /"]
    if GENERATE_SITEMAP:
        lines += ["", f"Sitemap: {SITE_URL}/sitemap.xml"]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# BUILD
# ---------------------------------------------------------------------------

def write(path, content):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def build():
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")
    try:
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
    except Exception:
        commit = "unknown"

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_files = collect_all_files()

    # 0) Pomiar. Naglowek kazdego wariantu podaje jego rozmiar w tokenach,
    # wiec liczbe trzeba znac ZANIM zlozy sie plik finalny. Skladamy wiec
    # kazdy wariant dwa razy: raz na sucho (zeby zmierzyc), raz na czysto
    # (juz z prawdziwa liczba w naglowku). Roznica miedzy przebiegami to
    # kilka znakow samej liczby, wiec pomiar jest stabilny.
    for key in VARIANT_ORDER:
        draft = build_vault_txt(select_files(all_files, key), key, now, commit)
        VARIANTS[key]["tokens"] = fmt_tokens(len(draft))

    # Kontrola zaleznosci. Blok CORE kazdego wariantu odwoluje sie do pliku
    # kontekstu podpinania, ktory powstaje w render_wiring.py. Gdyby go
    # zabraklo, select_files() po cichu go pominie (filtruje po os.path.isfile),
    # a pliki zbiorcze wyjda bez mapy relacji -- bez zadnego sladu w logu.
    if not os.path.isfile(os.path.join(ROOT, WIRING_FILENAME)):
        print(f"UWAGA — brak {WIRING_FILENAME}. Pliki zbiorcze powstana bez mapy "
              f"relacji.\n"
              f"        Uruchom `python scripts/render_wiring.py` przed tym "
              f"skryptem\n"
              f"        albo uzyj `python scripts/build.py`, ktory wymusza "
              f"kolejnosc.")

    # 1) Trzy warianty pliku tekstowego
    stats = []
    covered = set()
    for key in VARIANT_ORDER:
        files = select_files(all_files, key)
        text = build_vault_txt(files, key, now, commit)
        write(os.path.join(OUTPUT_DIR, VARIANTS[key]["filename"]), text)
        stats.append((key, len(files), len(text)))
        covered.update(norm(f).lower() for f in files)

    # Kontrola spojnosci: czy jakis plik repo nie trafil do zadnego wariantu.
    orphans = [f for f in all_files if norm(f).lower() not in covered]
    if orphans:
        print("UWAGA — pliki poza wszystkimi wariantami:")
        for f in sorted(orphans):
            print(f"  ! {f}")

    # 2) Strona glowna
    write(os.path.join(OUTPUT_DIR, "index.html"),
          build_landing_html(now, commit, len(all_files)))

    # 3) robots.txt / sitemap.xml
    if GENERATE_SITEMAP:
        write(os.path.join(OUTPUT_DIR, "sitemap.xml"), build_sitemap())
    write(os.path.join(OUTPUT_DIR, "robots.txt"), build_robots())

    # 4) llms.txt
    write(os.path.join(OUTPUT_DIR, "llms.txt"), build_llms_txt())

    # Indeks generatora CV NIE jest publikowany. Zostaje w repozytorium
    # (galaz main) jako zrodlo dla skilla /generuj-cv, ktory pobiera go
    # bezposrednio stamtad. Na strone nie trafia, bo jego odbiorca nie jest
    # czytelnik Vaultu, tylko narzedzie do skladania aplikacji.

    print(f"Zbudowano ({len(all_files)} plikow zrodlowych):")
    for key, nfiles, nchars in stats:
        print(f"  {VARIANTS[key]['filename']:24} {nfiles:3} plikow, "
              f"{nchars:7} znakow (~{nchars // 3.5:.0f} tokenow)")
    print("  index.html, robots.txt, sitemap.xml, llms.txt")


if __name__ == "__main__":
    build()
