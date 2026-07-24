#!/usr/bin/env python3
"""
build.py

Orkiestrator calego builda Career Vault. Jedyny skrypt wolany przez
GitHub Actions -- reszta to biblioteki, ktore mozna tez uruchomic osobno
podczas pracy lokalnej.

Kolejnosc ma znaczenie:

    1. VaultModel        wczytanie i walidacja rekordow   (raz, wspolne)
    2. render_readmes    sekcje w README modulow
    3. render_index      Vaultshot index.md
    4. render_site       dist/ (pliki zbiorcze + strona)

Krok 3 musi poprzedzac 4, bo render_site wciaga gotowy indeks do plikow
zbiorczych i kopiuje go do dist/. Kroki 2 i 3 sa niezalezne.

Model jest budowany RAZ i przekazywany do wszystkich rendererow. Wczesniej
kazdy skrypt parsowal Vault od nowa -- przy trzech rendererach oznaczaloby
to trzy przebiegi po tych samych plikach i trzy niezalezne listy bledow.

Uruchamianie:
    python scripts/build.py              # pelny build
    python scripts/build.py --check      # nic nie zapisuje, zwraca kod bledu
    python scripts/build.py --skip-site  # bez dist/ (szybkie przy edycji rekordow)

Kody wyjscia:
    0  wszystko OK (ostrzezenia dopuszczalne)
    1  bledy walidacji Vaulta albo nieaktualne artefakty w trybie --check
"""

import os
import sys
import datetime
import subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from vault_model import VaultModel  # noqa: E402
import render_readmes               # noqa: E402
import render_index                 # noqa: E402


def git_commit(root):
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=root, stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()
    except Exception:
        return "unknown"


def hr(title):
    print(f"\n— {title} " + "—" * max(0, 60 - len(title)))


def main():
    root = os.getcwd()
    check = "--check" in sys.argv
    skip_site = "--skip-site" in sys.argv

    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M")
    commit = git_commit(root)

    # -- 1. Model --------------------------------------------------------
    hr("Vault")
    model = VaultModel(root)
    print(f"  {model.summary()}")

    for msg in model.errors():
        print(f"  BLAD    {msg}")
    for msg in model.warnings():
        print(f"  UWAGA   {msg}")
    for msg in model.infos():
        print(f"  INFO    {msg}")

    if model.errors():
        print("\nBuild przerwany — napraw bledy walidacji przed generowaniem.")
        return 1

    stale = []

    # -- 2. README modulow -----------------------------------------------
    hr("README modulow")
    changed = render_readmes.run(root, check_only=check, model=model)
    if changed:
        stale.extend(changed)
        verb = "nieaktualne" if check else "zaktualizowano"
        print(f"  {verb}: {len(changed)}")
        for c in changed:
            print(f"    {c}")
    else:
        print("  bez zmian")

    # -- 3. Indeks generatora CV -----------------------------------------
    hr("Vaultshot index")
    content = render_index.build_index_md(model, now, commit)
    idx_path = os.path.join(root, render_index.INDEX_FILENAME)
    old = ""
    if os.path.isfile(idx_path):
        with open(idx_path, encoding="utf-8") as fh:
            old = fh.read()

    # Stopka zawiera date i commit, wiec rozni sie przy kazdym uruchomieniu.
    # Do porownania "czy cos sie realnie zmienilo" bierzemy tresc bez niej.
    def body(t):
        return "\n".join(
            l for l in t.split("\n")
            if not l.startswith("> Stan:") and not l.startswith("_Wygenerowano")
        )

    if body(old) != body(content):
        stale.append(render_index.INDEX_FILENAME)
        print("  nieaktualny" if check else "  zaktualizowano")
    else:
        print("  bez zmian")

    if not check:
        with open(idx_path, "w", encoding="utf-8") as fh:
            fh.write(content)

    # -- 4. Kontekst podpinania ------------------------------------------
    # Niezalezny od dist/ (krok 5), wiec generowany takze przy --skip-site:
    # to wlasnie przy edycji rekordow jest najczesciej potrzebny.
    hr("Kontekst podpinania")
    import render_wiring  # noqa: E402
    if check:
        print("  pominieto (--check)")
    else:
        render_wiring.run(root, model, now, commit)
        print(f"  {render_wiring.OUT_DIR}/{render_wiring.OUT_FILENAME}")

    # -- 5. Strona -------------------------------------------------------
    if skip_site:
        hr("dist/")
        print("  pominieto (--skip-site)")
    elif check:
        hr("dist/")
        print("  pominieto (--check)")
    else:
        hr("dist/")
        import render_site  # noqa: E402  (import tutaj — czyta pliki z dysku)
        render_site.build()

    # -- podsumowanie ----------------------------------------------------
    hr("Wynik")
    if check and stale:
        print("  Artefakty nieaktualne wzgledem rekordow:")
        for s in stale:
            print(f"    ! {s}")
        print("\n  Uruchom `python scripts/build.py` i zacommituj wynik.")
        return 1

    warn = len(model.warnings())
    print(f"  OK — {model.summary()}"
          + (f", {warn} ostrzezen" if warn else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
