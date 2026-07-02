#!/usr/bin/env python3
"""
build_vault.py

Skanuje repozytorium Career Vault i sklejaja wszystkie pliki tekstowe
(.md, .yaml, .yml, .txt) w jeden duzy plik `dist/vault-full.txt`
oraz prosty wrapper `dist/index.html`, gotowe do publikacji na GitHub Pages.

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

# Foldery pomijane przy skanowaniu (workflow, git, wynik builda itp.)
EXCLUDE_DIRS = {".git", ".github", "dist", "node_modules", ".vscode", "scripts"}

# Rozszerzenia plikow wliczanych do zbiorczego pliku
INCLUDE_EXTENSIONS = {".md", ".yaml", ".yml", ".txt"}

# Kolejnosc zgodna z sekcja "Rekomendowany sposob wykorzystania przez AI" w README:
# AI Interpretation Guide -> Identity -> Assessment -> Achievements/Stories/Skills/Experience -> Development Areas
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


def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    files = collect_files(ROOT)
    files.sort(key=sort_key)

    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"]
        ).decode().strip()
    except Exception:
        commit = "unknown"

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

    full_text = "\n".join(lines)

    with open(OUTPUT_TXT, "w", encoding="utf-8") as out:
        out.write(full_text)

    html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Career Vault -- pelna tresc</title>
<meta name="robots" content="noindex">
</head>
<body style="font-family: system-ui, sans-serif; max-width: 900px; margin: 2rem auto; padding: 0 1rem;">
<h1>Career Vault</h1>
<p>Ostatnia aktualizacja: {now} (commit {commit})</p>
<p>Pelna tresc repozytorium w jednym pliku tekstowym, przeznaczona do odczytu przez modele jezykowe (LLM):</p>
<p><a href="vault-full.txt">vault-full.txt</a> (link do wklejenia w rozmowie z LLM)</p>
<hr>
<pre style="white-space:pre-wrap; word-wrap:break-word;">{escape_html(full_text)}</pre>
</body>
</html>
"""
    with open(OUTPUT_HTML, "w", encoding="utf-8") as out:
        out.write(html)

    print(f"Zbudowano {OUTPUT_TXT}: {len(files)} plikow, {len(full_text)} znakow.")


if __name__ == "__main__":
    build()
