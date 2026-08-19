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
