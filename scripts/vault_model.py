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
        start = m.end()
        lines = []
        for line in text[start:].split("\n")[1:]:
            if line.strip() == "":
                if lines:
                    break
                continue
            if not line.startswith((" ", "\t")):
                break
            lines.append(line.strip())
        return " ".join(lines)
    return val


def _clean(value):
    """Czysci pojedyncza wartosc listy YAML.

    Usuwa komentarz inline (` # ...`) oraz otaczajace cudzyslowy.

    Kolejnosc ma znaczenie. Wersja wczesniejsza sprawdzala tylko, czy
    wartosc zaczyna sie i konczy cudzyslowem -- przez co `"tekst" # opis`
    (cudzyslow zamkniety, po nim komentarz) wracal razem z cudzyslowami.
    Teraz szukamy domkniecia cudzyslowu i sprawdzamy, co po nim zostaje:
    tylko pusty ogon albo komentarz oznacza prawidlowy skalar cytowany.

    Ucinanie tresci po ` #` jest zgodne ze specyfikacja YAML (PyYAML robi
    dokladnie to samo), wiec zostaje bez zmian. Sygnalizowaniem takich
    przypadkow zajmuje sie walidacja, nie parser.
    """
    v = value.strip()

    if v[:1] in ("'", '"'):
        q = v[0]
        end = v.find(q, 1)
        if end != -1:
            rest = v[end + 1:].strip()
            if rest == "" or rest.startswith("#"):
                return v[1:end].strip()
        # Cudzyslow niedomkniety albo tresc za nim -- to nie jest skalar
        # cytowany, tylko zwykly tekst zaczynajacy sie od cudzyslowu.

    v = re.split(r"\s+#", v, maxsplit=1)[0]
    return v.strip()


def _items(lines, start):
    """Pozycje listy YAML (`- x`) zaczynajac od indeksu `start`.

    Puste linie i linie komentarza wewnatrz bloku sa pomijane -- YAML je
    dopuszcza, a wersja regexowa konczyla na nich zbieranie i cicho
    zwracala pusta liste. Zatrzymujemy sie na pierwszej linii, ktora nie
    jest ani pozycja listy, ani pusta, ani komentarzem (czyli na kolejnym
    kluczu).
    """
    out = []
    for line in lines[start:]:
        s = line.strip()
        if s == "" or s.startswith("#"):
            continue
        m = re.match(r"^[ \t]*-[ \t]+(.*)$", line)
        if not m:
            break
        v = _clean(m.group(1))
        if v:
            out.append(v)
    return out


def _count_items(scope, key, item_prefix=None):
    """Liczba linii `- x` widocznych pod kluczem `key`.

    Skan niezalezny od `_items` -- sluzy wylacznie walidacji. Sens ma to,
    ze jest napisany inaczej niz parser: gdy parser przestanie sobie
    radzic z jakims formatowaniem, ten licznik nadal poda liczbe z pliku
    i roznica ujawni strate.
    """
    lines = scope.split("\n")
    for i, line in enumerate(lines):
        m = re.match(rf"^[ \t]*{re.escape(key)}:[ \t]*(.*)$", line)
        if not m:
            continue
        if m.group(1).strip():      # `key: []` albo `key: wartosc`
            return 0
        n = 0
        for nxt in lines[i + 1:]:
            s = nxt.strip()
            if s == "" or s.startswith("#"):
                continue
            if s.startswith("- "):
                if item_prefix is None or _clean(s[2:]).startswith(item_prefix):
                    n += 1
                continue
            break                   # kolejny klucz konczy liste
        return n
    return 0


def _block(text, key):
    """Blok podrzedny klucza najwyzszego poziomu.

    Zwraca linie nalezace do `key:` -- wciete albo puste -- i konczy na
    pierwszej linii bez wciecia. Dzieki temu wyszukiwanie podkluczy nie
    wychodzi poza rodzica.
    """
    m = re.search(rf"^{re.escape(key)}:[ \t]*$", text, re.M)
    if not m:
        return ""
    out = []
    for line in text[m.end():].split("\n")[1:]:
        if line.strip() == "":
            out.append(line)
            continue
        if not line.startswith((" ", "\t")):
            break
        out.append(line)
    return "\n".join(out)


def _list(text, key):
    """Lista wartosci klucza najwyzszego poziomu (`key:` + linie `- x`).

    Wciecie przed myslnikiem jest opcjonalne -- czesc rekordow zapisuje
    listy bez wciecia (dopuszczalne w YAML).
    """
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}:[ \t]*$", line):
            return _items(lines, i + 1)
    return []


def _nested_list(text, parent, child):
    """Lista zagniezdzona: `parent:` -> `  child:` -> `    - x`.

    Szukamy `child` wylacznie wewnatrz bloku `parent`. Poprzednia wersja
    uzywala wzorca `(?:.*\\n)*?`, ktory nie konczyl sie na bloku rodzica --
    gdy `sources:` nie mial `skills:`, parser bral pierwszy `skills:`
    napotkany gdziekolwiek dalej w pliku i cicho podstawial cudze dane.
    """
    block = _block(text, parent)
    if not block:
        return []
    lines = block.split("\n")
    for i, line in enumerate(lines):
        if re.match(rf"^[ \t]+{re.escape(child)}:[ \t]*$", line):
            return _items(lines, i + 1)
    return []


def _frontmatter(text):
    """Zwraca blok frontmattera jako tekst YAML (bez ograniczników).

    Obsluguje dwa warianty spotykane w Assessments:
      1. `---` na samej gorze pliku, zamkniete `---`,
      2. frontmatter owiniety w blok ```yaml (tak jest w CAL-001).

    Gdy nie znajdzie zadnego, zwraca pusty string -- wolajacy dostanie
    puste pola zamiast wyjatku.
    """
    stripped = text.lstrip()
    if stripped.startswith("---"):
        m = re.match(r"^---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)", stripped, re.S)
        if m:
            return m.group(1)
    m = re.search(r"```yaml[ \t]*\n(.*?)```", text, re.S)
    if m:
        return re.sub(r"^---[ \t]*$", "", m.group(1), flags=re.M)
    return ""


def _period(text):
    """Para (start, end) z bloku `period:`.

    Kazdy klucz czytany osobno. Wersja wczesniejsza wymagala `start`
    bezposrednio przed `end` -- odwrotna kolejnosc albo dodatkowy klucz
    miedzy nimi dawal cicho ("", "") i pusta kolumne okresu w tabeli.
    """
    block = _block(text, "period")
    if not block:
        return ("", "")

    def field(name):
        m = re.search(rf"^[ \t]+{name}:[ \t]*(\S+)", block, re.M)
        return m.group(1).strip() if m else ""

    return (field("start"), field("end"))


# ---------------------------------------------------------------------------
# MODEL
# ---------------------------------------------------------------------------

class VaultModel:
    """Wczytany Vault: rekordy + relacje + wynik walidacji."""

    def __init__(self, root):
        self.root = root
        self.ach = {}      # ACH-xxx -> dict
        self.skill = {}    # SKILL-xxx -> dict
        self.story = {}    # STORY-xxx -> dict
        self.dev = {}      # DEV-xxx -> dict
        self.pred = {}     # PRED-xxx -> dict
        self.bp = {}       # BP-xxx -> dict
        self.roles = []    # [(kod, etykieta, okres, [ACH...])] chronologicznie
        self.ach_role = {} # ACH-xxx -> kod roli
        self.a2s = {}      # ACH-xxx -> [SKILL-xxx]
        self.a2st = {}     # ACH-xxx -> [STORY-xxx]
        self.a2dev = {}    # ACH-xxx -> [DEV-xxx]
        self.st2dev = {}   # STORY-xxx -> [DEV-xxx]
        self.problems = [] # [(poziom, komunikat)]

        self._load_records()
        self._load_assessments()
        self._load_experience()
        self._build_relations()
        self._validate()

    # -- wczytywanie ------------------------------------------------------

    def _read(self, path):
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read()

    def _check_lost_items(self, label, text, prefix, rec):
        """Porownuje liczbe pozycji w zrodle z liczba pozycji po parsowaniu.

        Parser regexowy nie rzuca wyjatkow -- gdy formatowania nie rozpozna,
        po cichu zwraca krotsza (czesto pusta) liste, a rekord znika z
        indeksu bez sladu. To jedyne miejsce, w ktorym taka strata jest
        wykrywalna: liczymy linie `- x` bezposrednio pod kluczem prostym,
        niezaleznym skanem i porownujemy z wynikiem.

        Pole jawnie puste (`key: []`) daje zero po obu stronach, wiec nie
        generuje halasu.
        """
        for field, key, parent, item_prefix in WATCHED.get(prefix, []):
            scope = _block(text, parent) if parent else text
            if not scope:
                continue
            raw = _count_items(scope, key, item_prefix)
            got = len(rec.get(field) or [])
            if raw > got:
                where = f"{parent}.{key}" if parent else key
                self.problems.append(
                    ("WARN", f"{label}: `{where}` — w pliku {raw} pozycji, "
                             f"sparsowano {got}; sprawdz formatowanie listy")
                )

    def _load_records(self):
        for folder, prefix, target, parser in (
            ("Achievements", "ACH-", self.ach, self._parse_ach),
            ("Skills", "SKILL-", self.skill, self._parse_skill),
            ("Stories", "STORY-", self.story, self._parse_story),
            ("Development Areas", "DEV-", self.dev, self._parse_dev),
        ):
            d = os.path.join(self.root, folder)
            if not os.path.isdir(d):
                self.problems.append(("ERROR", f"Brak katalogu {folder}/"))
                continue
            for fname in sorted(os.listdir(d)):
                if not fname.lower().endswith((".yaml", ".yml")):
                    continue
                if not fname.startswith(prefix):
                    continue
                text = self._read(os.path.join(d, fname))
                rid = _scalar(text, "id")
                if not rid:
                    self.problems.append(("ERROR", f"{folder}/{fname}: brak pola `id`"))
                    continue
                expected = os.path.splitext(fname)[0]
                if rid != expected:
                    self.problems.append(
                        ("WARN", f"{folder}/{fname}: `id: {rid}` != nazwa pliku")
                    )
                target[rid] = parser(text)
                self._check_lost_items(f"{folder}/{fname}", text, prefix, target[rid])

    def _parse_ach(self, t):
        start, end = _period(t)
        return {
            "title": _scalar(t, "title"),
            "company": _scalar(t, "company"),
            "start": start,
            "end": end,
            "importance": _scalar(t, "importance"),
            "impact": _list(t, "impact"),
            "roles": _list(t, "roles"),
        }

    def _parse_skill(self, t):
        return {
            "name": _scalar(t, "name"),
            "category": _scalar(t, "category"),
            "level": _scalar(t, "level"),
            "importance": _scalar(t, "importance"),
            "keywords": _list(t, "keywords"),
            "capabilities": _list(t, "capabilities"),
            "related": _list(t, "related_skills"),
            "evidence": [x for x in _list(t, "evidence") if x.startswith("ACH-")],
            # Wpisy opisowe zamiast identyfikatorow -- nie trafiaja do
            # indeksu, ale warto o nich wiedziec.
            "evidence_other": [x for x in _list(t, "evidence")
                               if not x.startswith("ACH-")],
        }

    def _parse_story(self, t):
        return {
            "title": _scalar(t, "title"),
            "ach": _nested_list(t, "evidence", "achievement_ids"),
            "bullets": _list(t, "cv_bullets"),
        }

    def _parse_dev(self, t):
        return {
            "title": _scalar(t, "title"),
            "category": _scalar(t, "category"),
            "status": _scalar(t, "status"),
            "ach": _nested_list(t, "sources", "achievements"),
            "stories": _nested_list(t, "sources", "stories"),
            "skills": _nested_list(t, "sources", "skills"),
        }

    def _load_assessments(self):
        """Wczytuje PRED-* i BP-* z frontmattera YAML na gorze pliku .md.

        CAL-* celowo pominiete: kalibracje to wersjonowane dokumenty opisowe,
        ktorych indeks pozostaje w README pisany recznie.
        """
        for folder, prefix, target, parser in (
            (os.path.join("Assessments", "Predictors"), "PRED-", self.pred, self._parse_pred),
            (os.path.join("Assessments", "Behavioral Patterns"), "BP-", self.bp, self._parse_bp),
        ):
            d = os.path.join(self.root, folder)
            if not os.path.isdir(d):
                self.problems.append(("ERROR", f"Brak katalogu {folder}/"))
                continue
            for fname in sorted(os.listdir(d)):
                if not fname.lower().endswith(".md"):
                    continue
                if not fname.startswith(prefix):
                    continue
                fm = _frontmatter(self._read(os.path.join(d, fname)))
                rid = _scalar(fm, "id")
                if not rid:
                    self.problems.append(
                        ("ERROR", f"{folder}/{fname}: brak pola `id` we frontmatterze")
                    )
                    continue
                expected = os.path.splitext(fname)[0]
                if rid != expected:
                    self.problems.append(
                        ("WARN", f"{folder}/{fname}: `id: {rid}` != nazwa pliku")
                    )
                target[rid] = parser(fm)
                self._check_lost_items(f"{folder}/{fname}", fm, prefix, target[rid])

    def _parse_pred(self, fm):
        return {
            "name": _scalar(fm, "name"),
            "status": _scalar(fm, "status"),
            "confidence": _scalar(fm, "confidence"),
            "version": _scalar(fm, "version"),
            "updated": _scalar(fm, "last_updated"),
            "created_from": _list(fm, "created_from"),
            "stories": _list(fm, "supporting_stories"),
            "conflicting": _list(fm, "conflicting_stories"),
            "cal": _list(fm, "related_calibrations"),
            # Rekordy uzywaja dwoch nazw tego samego pola -- starsze
            # `related_behavioral_patterns`, nowsze `related_hypotheses`.
            "bp": _list(fm, "related_behavioral_patterns") or _list(fm, "related_hypotheses"),
        }

    def _parse_bp(self, fm):
        return {
            "name": _scalar(fm, "name"),
            "status": _scalar(fm, "status"),
            "confidence": _scalar(fm, "confidence"),
            "stories": _nested_list(fm, "derived_from", "stories"),
            "ach": _nested_list(fm, "derived_from", "achievements"),
        }

    def _load_experience(self):
        """Mapowanie ACH -> rola z Experience.md.

        Zrodlem sa sekcje `### <Rola>` zawierajace liste identyfikatorow ACH.
        Uzywamy tego zamiast dat, bo achievementy ciagle (`end: current`)
        naleza do roli, w ktorej powstaly, a nie do biezacej.
        """
        path = os.path.join(self.root, "Experience.md")
        if not os.path.isfile(path):
            self.problems.append(("ERROR", "Brak Experience.md — mapowanie rol niedostepne"))
            return

        text = self._read(path)
        sections = dict()
        for m in re.finditer(r"^### (.+?)\n(.*?)(?=^### |\Z)", text, re.M | re.S):
            sections[m.group(1).strip()] = m.group(2)

        for needle, code, label in ROLE_MAP:
            body = None
            for name, content in sections.items():
                if needle.lower() in name.lower():
                    body = content
                    break
            if body is None:
                self.problems.append(
                    ("WARN", f"Experience.md: nie znaleziono sekcji dla roli '{needle}'")
                )
                continue

            per = re.search(r"\*\*Okres:\*\*\s*\n(.+)", body)
            period = per.group(1).strip() if per else ""
            achs = sorted(set(re.findall(r"ACH-[\w\d]+", body)))
            self.roles.append((code, label, period, achs))
            for a in achs:
                if a in self.ach_role and self.ach_role[a] != code:
                    self.problems.append(
                        ("WARN", f"{a} przypisany do wielu rol "
                                 f"({self.ach_role[a]} i {code}) — zostaje pierwsza")
                    )
                    continue
                self.ach_role[a] = code

    # -- relacje ----------------------------------------------------------

    def _build_relations(self):
        for sid, s in self.skill.items():
            for a in s["evidence"]:
                self.a2s.setdefault(a, []).append(sid)
        for stid, s in self.story.items():
            for a in s["ach"]:
                self.a2st.setdefault(a, []).append(stid)
        for did, d in self.dev.items():
            for a in d["ach"]:
                self.a2dev.setdefault(a, []).append(did)
            for st in d["stories"]:
                self.st2dev.setdefault(st, []).append(did)
        for d in (self.a2s, self.a2st, self.a2dev, self.st2dev):
            for k in d:
                d[k] = sorted(set(d[k]))

    # -- walidacja --------------------------------------------------------

    def _validate(self):
        P = self.problems.append

        for sid, s in self.skill.items():
            for a in s["evidence"]:
                if a not in self.ach:
                    P(("ERROR", f"{sid}.evidence wskazuje na nieistniejacy {a}"))
            if not s["evidence"]:
                P(("WARN", f"{sid} nie ma zadnego dowodu (`evidence` puste)"))
            for x in s["evidence_other"]:
                P(("WARN", f"{sid}.evidence: '{x}' nie jest identyfikatorem ACH "
                           f"— pozycja pomijana w indeksie"))
            if not s["keywords"]:
                P(("WARN", f"{sid} ({s['name']}) nie ma `keywords` — "
                           f"dopasowanie oferty oprze sie na samej nazwie"))

        for stid, s in self.story.items():
            for a in s["ach"]:
                if a not in self.ach:
                    P(("ERROR", f"{stid}.evidence.achievement_ids wskazuje na nieistniejacy {a}"))
            if not s["ach"]:
                P(("WARN", f"{stid} nie wskazuje zadnego ACH"))
            if not s["bullets"]:
                P(("WARN", f"{stid} nie ma `cv_bullets`"))
            for b in s["bullets"]:
                if len(b) > 130:
                    P(("INFO", f"{stid}: bullet {len(b)} zn (>130) — wymaga skrocenia w CV"))

        for aid in self.ach:
            if aid not in self.a2s:
                P(("WARN", f"{aid} nie jest dowodem zadnej kompetencji"))
            if aid.startswith("ACH-P"):
                continue
            if aid not in self.ach_role:
                P(("WARN", f"{aid} nie jest przypisany do zadnej roli w Experience.md"))

        for did, d in self.dev.items():
            for a in d["ach"]:
                if a not in self.ach:
                    P(("ERROR", f"{did}.sources.achievements wskazuje na nieistniejacy {a}"))
            for st in d["stories"]:
                if st not in self.story:
                    P(("ERROR", f"{did}.sources.stories wskazuje na nieistniejacy {st}"))
            for sk in d["skills"]:
                if sk.startswith("SKILL-") and sk not in self.skill:
                    P(("ERROR", f"{did}.sources.skills wskazuje na nieistniejacy {sk}"))
                elif not sk.startswith("SKILL-"):
                    P(("WARN", f"{did}.sources.skills: '{sk}' nie jest identyfikatorem "
                               f"— do ujednolicenia na SKILL-XXX"))
            if not (d["ach"] or d["stories"]):
                P(("WARN", f"{did} nie wskazuje zadnego ACH ani STORY"))

        for pid, p in self.pred.items():
            for st in p["stories"] + p["conflicting"]:
                if st not in self.story:
                    P(("ERROR", f"{pid} wskazuje na nieistniejacy {st}"))
            for b in p["bp"]:
                if b not in self.bp:
                    P(("ERROR", f"{pid}.related_behavioral_patterns wskazuje na nieistniejacy {b}"))
            if not p["stories"]:
                P(("WARN", f"{pid} nie ma zadnej wspierajacej historii"))

        for bid, b in self.bp.items():
            for st in b["stories"]:
                if st not in self.story:
                    P(("ERROR", f"{bid}.derived_from.stories wskazuje na nieistniejacy {st}"))
            for a in b["ach"]:
                if a not in self.ach:
                    P(("ERROR", f"{bid}.derived_from.achievements wskazuje na nieistniejacy {a}"))
            if not (b["stories"] or b["ach"]):
                P(("WARN", f"{bid} nie ma zadnego zrodla w `derived_from`"))

    # -- API --------------------------------------------------------------

    def prof_ids(self):
        """ACH zawodowe, posortowane numerycznie."""
        return sorted([a for a in self.ach if not a.startswith("ACH-P")],
                      key=lambda x: int(re.sub(r"\D", "", x)))

    def priv_ids(self):
        return sorted([a for a in self.ach if a.startswith("ACH-P")])

    def role_of(self, aid):
        return self.ach_role.get(aid, ROLE_FALLBACK)

    def errors(self):
        return [m for lvl, m in self.problems if lvl == "ERROR"]

    def warnings(self):
        return [m for lvl, m in self.problems if lvl == "WARN"]

    def infos(self):
        return [m for lvl, m in self.problems if lvl == "INFO"]

    def summary(self):
        return (f"{len(self.ach)} ACH ({len(self.prof_ids())} zawodowych), "
                f"{len(self.skill)} SKILL, {len(self.story)} STORY, "
                f"{len(self.dev)} DEV, {len(self.pred)} PRED, {len(self.bp)} BP, "
                f"{len(self.roles)} rol")
