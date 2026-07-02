#!/usr/bin/env python3
"""
build_vault.py

1. Skanuje repozytorium Career Vault i sklejaja wszystkie pliki tekstowe
   (.md, .yaml, .yml, .txt) w jeden duzy plik `dist/vault-full.txt`,
   przeznaczony do odczytu przez modele jezykowe (LLM).
2. Generuje `dist/index.html` -- landing page dla ludzi (np. rekruterow),
   z linkiem do repo na GitHubie oraz widocznym, kopiowalnym linkiem
   do wersji tekstowej dla AI.

Uruchamiane automatycznie przez GitHub Actions (patrz .github/workflows/build-vault.yml),
ale mozna tez odpalic lokalnie z poziomu glownego katalogu repo:

    python scripts/build_vault.py
"""

import os
import datetime
import subprocess

ROOT = os.getcwd()
OUTPUT_DIR = "dist"
OUTPUT_TXT = os.path.join(OUTPUT_DIR, "vault-full.txt")
OUTPUT_HTML = os.path.join(OUTPUT_DIR, "index.html")

REPO_URL = "https://github.com/Istuification/careervault"
VAULT_TXT_NAME = "vault-full.txt"

# Foldery pomijane przy skanowaniu (workflow, git, wynik builda itp.)
EXCLUDE_DIRS = {".git", ".github", "dist", "node_modules", ".vscode", "scripts"}

# Rozszerzenia plikow wliczanych do zbiorczego pliku
INCLUDE_EXTENSIONS = {".md", ".yaml", ".yml", ".txt"}

# Kolejnosc zgodna z sekcja "Rekomendowany sposob wykorzystania przez AI" w README:
PRIORITY_ORDER = [
    "AI Interpretation Guide.md",
    "Identity.md",
    "Assessments",
    "Achievements",
    "Stories",
    "Skills",
    "Experience.md",
    "Development Areas",
    "Context Entries",
    "About.md",
    "README.md",
]


def collect_files(root):
    collected = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")
        ]
        for fname in filenames:
            ext = os.path.splitext(fname)[1].lower()
            if ext in INCLUDE_EXTENSIONS:
                full_path = os.path.join(dirpath, fname)
                rel_path = os.path.relpath(full_path, root)
                collected.append(rel_path)
    return collected


def sort_key(rel_path):
    top = rel_path.split(os.sep)[0]
    prio = PRIORITY_ORDER.index(top) if top in PRIORITY_ORDER else len(PRIORITY_ORDER)
    return (prio, rel_path.lower())


def build_vault_txt(files, now, commit):
    lines = []
    lines.append("CAREER VAULT -- PELNA TRESC (wygenerowano automatycznie)")
    lines.append(f"Wygenerowano: {now} | Commit: {commit}")
    lines.append("=" * 70)
    lines.append("")
    lines.append("SPIS PLIKOW:")
    for f in files:
        lines.append(f" - {f}")
    lines.append("")
    lines.append("=" * 70)
    lines.append("")

    for f in files:
        full_path = os.path.join(ROOT, f)
        lines.append(f"### PLIK: {f}")
        lines.append("-" * 70)
        try:
            with open(full_path, "r", encoding="utf-8", errors="replace") as fh:
                content = fh.read()
        except Exception as e:
            content = f"[BLAD ODCZYTU PLIKU: {e}]"
        lines.append(content.rstrip())
        lines.append("")
        lines.append("=" * 70)
        lines.append("")

    return "\n".join(lines)


LANDING_TEMPLATE = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Career Vault -- evidence-based career record</title>
<meta name="description" content="Ustrukturyzowana, oparta na dowodach baza wiedzy zawodowej. Przegladaj repozytorium lub przekaz jej tresc modelowi AI jednym linkiem.">
<meta name="robots" content="index, follow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{
    --paper: #EEF1EC;
    --card: #E4E9E1;
    --ink: #16221D;
    --ink-soft: #4B5A54;
    --line: #C7D0C6;
    --teal: #24594B;
    --teal-ink: #F3F6F1;
    --indigo: #33396B;
    --indigo-ink: #F1F2F8;
    --radius: 10px;
  }
  *{ box-sizing: border-box; }
  html{ scroll-behavior: smooth; }
  body{
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: "IBM Plex Sans", system-ui, sans-serif;
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }
  .wrap{
    max-width: 880px;
    margin: 0 auto;
    padding: 4.5rem 1.5rem 3rem;
  }
  .eyebrow{
    font-family: "JetBrains Mono", monospace;
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--ink-soft);
    margin: 0 0 1.1rem;
  }
  .eyebrow::before{
    content: "";
    display: inline-block;
    width: 0.5em;
    height: 0.5em;
    background: var(--teal);
    margin-right: 0.6em;
    border-radius: 1px;
    vertical-align: middle;
  }
  h1{
    font-family: "Fraunces", Georgia, serif;
    font-optical-sizing: auto;
    font-weight: 500;
    font-size: clamp(2rem, 5vw, 3rem);
    line-height: 1.12;
    letter-spacing: -0.01em;
    margin: 0 0 1.1rem;
  }
  .lede{
    font-size: 1.05rem;
    color: var(--ink-soft);
    max-width: 60ch;
    margin: 0 0 2.75rem;
  }
  .lede strong{ color: var(--ink); font-weight: 600; }

  .paths{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.1rem;
    margin-bottom: 2.75rem;
  }
  @media (max-width: 680px){
    .paths{ grid-template-columns: 1fr; }
  }
  .card{
    border: 1px solid var(--line);
    border-radius: var(--radius);
    background: var(--card);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .card-tab{
    display: flex;
    align-items: center;
    gap: 0.55rem;
    padding: 0.7rem 1.1rem;
    font-family: "JetBrains Mono", monospace;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--teal-ink);
    background: var(--teal);
  }
  .card.ai .card-tab{ background: var(--indigo); color: var(--indigo-ink); }
  .card-tab svg{ width: 15px; height: 15px; flex-shrink: 0; }
  .card-body{ padding: 1.3rem 1.1rem 1.4rem; display: flex; flex-direction: column; gap: 0.9rem; flex-grow: 1; }
  .card-body h2{
    font-family: "Fraunces", Georgia, serif;
    font-weight: 500;
    font-size: 1.3rem;
    margin: 0;
  }
  .card-body p{
    margin: 0;
    color: var(--ink-soft);
    font-size: 0.94rem;
    flex-grow: 1;
  }
  .btn{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.4em;
    font-family: "JetBrains Mono", monospace;
    font-size: 0.82rem;
    text-decoration: none;
    color: var(--teal-ink);
    background: var(--teal);
    border: none;
    border-radius: 6px;
    padding: 0.65rem 0.9rem;
    cursor: pointer;
    transition: transform 0.12s ease, opacity 0.12s ease;
  }
  .card.ai .btn{ background: var(--indigo); color: var(--indigo-ink); }
  .btn:hover{ transform: translateY(-1px); opacity: 0.92; }
  .btn:focus-visible{ outline: 2px solid var(--ink); outline-offset: 2px; }

  .copybox{
    display: flex;
    align-items: stretch;
    border: 1px solid var(--line);
    border-radius: 6px;
    overflow: hidden;
    background: var(--paper);
  }
  .copybox code{
    font-family: "JetBrains Mono", monospace;
    font-size: 0.76rem;
    padding: 0.6rem 0.7rem;
    flex-grow: 1;
    overflow-x: auto;
    white-space: nowrap;
    color: var(--ink);
  }
  .copybox button{
    font-family: "JetBrains Mono", monospace;
    font-size: 0.72rem;
    letter-spacing: 0.04em;
    border: none;
    border-left: 1px solid var(--line);
    background: var(--card);
    color: var(--ink);
    padding: 0 0.9rem;
    cursor: pointer;
    white-space: nowrap;
  }
  .copybox button:hover{ background: var(--indigo); color: var(--indigo-ink); }
  .copybox button:focus-visible{ outline: 2px solid var(--ink); outline-offset: -2px; }

  .about{
    border-top: 1px solid var(--line);
    padding-top: 2rem;
    margin-bottom: 2.5rem;
  }
  .about h3{
    font-family: "JetBrains Mono", monospace;
    font-size: 0.78rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--ink-soft);
    margin: 0 0 0.9rem;
  }
  .about p{ margin: 0 0 0.9rem; color: var(--ink-soft); max-width: 65ch; }
  .about p:last-child{ margin-bottom: 0; }
  .about.prompts{ border-top: none; padding-top: 0; margin-top: -1.6rem; }
  .prompt-list{
    margin: 0;
    padding: 0;
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
  }
  .prompt-list li{
    font-family: "JetBrains Mono", monospace;
    font-size: 0.82rem;
    color: var(--ink);
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 6px;
    padding: 0.6rem 0.8rem;
    line-height: 1.5;
  }

  footer{
    font-family: "JetBrains Mono", monospace;
    font-size: 0.74rem;
    color: var(--ink-soft);
    border-top: 1px solid var(--line);
    padding-top: 1.3rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem 1.2rem;
  }
  footer a{ color: var(--ink-soft); }

  @media (prefers-reduced-motion: reduce){
    .btn{ transition: none; }
  }
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

  <div class="paths">

    <div class="card human">
      <div class="card-tab">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7Z"/></svg>
        Dla człowieka
      </div>
      <div class="card-body">
        <h2>Przeglądaj repozytorium</h2>
        <p>Pełne źródło na GitHubie: osiągnięcia, kompetencje, historie zawodowe
        i model poznawczy stojący za decyzjami.</p>
        <a class="btn" href="__REPO_URL__" target="_blank" rel="noopener">Otwórz repozytorium &rarr;</a>
      </div>
    </div>

    <div class="card ai">
      <div class="card-tab">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M8 10h.01M16 10h.01M8 15h8"/></svg>
        Dla AI / LLM
      </div>
      <div class="card-body">
        <h2>Podaj to modelowi AI</h2>
        <p>Jeden plik tekstowy zawierający cały Vault. Wklej poniższy link
        w rozmowie z ChatGPT, Claude, Gemini lub innym asystentem AI.</p>
        <div class="copybox">
          <code id="vault-url">__VAULT_URL_PLACEHOLDER__</code>
          <button id="copy-btn" type="button">Kopiuj</button>
        </div>
        <a class="btn" href="__VAULT_TXT_NAME__" target="_blank" rel="noopener">Otwórz plik &rarr;</a>
      </div>
    </div>

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
      Ten plik dla AI (<code>__VAULT_TXT_NAME__</code>) jest generowany automatycznie
      przy każdej aktualizacji repozytorium, więc zawsze odzwierciedla
      aktualny stan wiedzy &mdash; bez ręcznego eksportowania czy kopiowania.
    </p>
  </div>

  <div class="about prompts">
    <h3>Spróbuj zapytać</h3>
    <p style="margin-bottom: 1rem;">
      Po wklejeniu linku do <code>__VAULT_TXT_NAME__</code> w rozmowie z AI, dobry punkt
      startowy to jedno z tych pytań:
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
<script>
  (function(){
    var codeEl = document.getElementById('vault-url');
    var absoluteUrl = window.location.origin
      + window.location.pathname.replace(/index\\.html$/, '')
      + '__VAULT_TXT_NAME__';
    codeEl.textContent = absoluteUrl;

    var btn = document.getElementById('copy-btn');
    btn.addEventListener('click', function(){
      navigator.clipboard.writeText(absoluteUrl).then(function(){
        var original = btn.textContent;
        btn.textContent = 'Skopiowano!';
        setTimeout(function(){ btn.textContent = original; }, 1600);
      }).catch(function(){
        var range = document.createRange();
        range.selectNode(codeEl);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
      });
    });
  })();
</script>
</body>
</html>
"""


def build_landing_html(now, commit, file_count):
    html = LANDING_TEMPLATE
    html = html.replace("__REPO_URL__", REPO_URL)
    html = html.replace("__VAULT_TXT_NAME__", VAULT_TXT_NAME)
    html = html.replace("__VAULT_URL_PLACEHOLDER__", VAULT_TXT_NAME)
    html = html.replace("__NOW__", now)
    html = html.replace("__COMMIT__", commit)
    html = html.replace("__FILE_COUNT__", str(file_count))
    return html


def build():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    files = collect_files(ROOT)
    files.sort(key=sort_key)

    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"]
        ).decode().strip()
    except Exception:
        commit = "unknown"

    vault_text = build_vault_txt(files, now, commit)
    with open(OUTPUT_TXT, "w", encoding="utf-8") as out:
        out.write(vault_text)

    landing_html = build_landing_html(now, commit, len(files))
    with open(OUTPUT_HTML, "w", encoding="utf-8") as out:
        out.write(landing_html)

    print(f"Zbudowano {OUTPUT_TXT} ({len(files)} plikow, {len(vault_text)} znakow).")
    print(f"Zbudowano {OUTPUT_HTML} (landing page).")


if __name__ == "__main__":
    build()
