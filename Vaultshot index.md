# VaultShot — Indeks Generatora CV

> **Plik generowany automatycznie** przez `scripts/build_index.py`.
> Nie edytuj ręcznie — zmiany wprowadzaj w rekordach Vaulta i przegeneruj.
> Stan: 2026-07-24 07:02 UTC · commit `f646726`

Przeznaczenie: **wyłączne źródło danych dla skilla `/generuj-cv`**.
Nie zastępuje README sekcji — te pozostają dokumentacją dla człowieka.

Zakres: **21** achievementów zawodowych, **6** prywatnych, **21** kompetencji, **11** historii.

---

## Jak czytać ten plik

**Tabela A** to jedyne miejsce, z którego dobiera się dowody. Jeden wiersz =
jeden achievement = jeden potencjalny bullet w CV. Kolumna `Skills` jest
**pełną i zamkniętą** listą kompetencji, do których ten achievement wolno
przypisać — para spoza tej listy jest błędem walidacji, nie kwestią oceny.

**Tabela B** służy fazie dopasowania oferty i paskowi kompetencji w CV.
Kryterium głównym jest dopasowanie do oferty, nie waga ani liczba dowodów.

**Sekcja C** zawiera gotowe bullety. Wybierz jeden albo złóż własny
**wyłącznie z faktów w danym bloku** — nie dopisuj niczego z pamięci.
**Sekcja D** to materiał dla achievementów bez historii.

**Kody ról** (do rozłożenia bulletów na stanowiska w CV):

| Kod | Stanowisko | Okres | #ACH |
| --- | --- | --- | --- |
| `KOOR` | Koordynator ds. Montaży | 2020-09 – 2023-09 | 8 |
| `KIER` | p.o. Kierownika Serwisu | 2023-09 – 2025-01 | 6 |
| `PM` | Product Manager / Business Analyst | 2025-01 – obecnie | 8 |

Docelowy rozkład bulletów: **PM 3 / KIER 2 / KOOR 1**. Przypisanie ACH do roli pochodzi
z `Experience.md` (sekcje `### <Rola>`), nie z dat — achievementy ciągłe
należą do roli, w której powstały.

---

## A. Achievementy — dowody, relacje, rola

| ACH | Tytuł | Rola | Okres | W | Skills (zamknięta lista) | Stories |
| --- | --- | --- | --- | --- | --- | --- |
| `ACH-001` | Transformacja działu Instal/Solar | KOOR | 2020-09→2023-09 | 10 | SKILL-001 SKILL-002 SKILL-003 SKILL-005 SKILL-006 SKILL-008 SKILL-009 SKILL-011 SKILL-012 SKILL-014 SKILL-015 SKILL-017 | STORY-001 |
| `ACH-002` | Samodzielne opanowanie platformy Bitrix24 - od zera do projektanta… | KOOR | 2020-09→2023-09 | 9 | SKILL-008 SKILL-009 SKILL-021 | — |
| `ACH-003` | Stworzenie bazy wiedzy serwisowej BPMN 2.0 | KIER | 2023-09→2025-01 | 10 | SKILL-001 SKILL-003 SKILL-006 SKILL-007 SKILL-010 SKILL-012 SKILL-015 SKILL-021 | STORY-005 |
| `ACH-004` | Restrukturyzacja i stabilizacja działu serwisu | KIER | 2023-09→2025-01 | 10 | SKILL-001 SKILL-002 SKILL-005 SKILL-007 SKILL-008 SKILL-009 SKILL-010 SKILL-011 SKILL-012 SKILL-014 SKILL-015 SKILL-016 SKILL-017 | STORY-002 STORY-004 STORY-005 |
| `ACH-005` | Zaprojektowanie i wdrożenie systemu gwarancyjnego | PM | 2025-01→teraz | 10 | SKILL-001 SKILL-003 SKILL-004 SKILL-006 SKILL-007 SKILL-008 SKILL-009 SKILL-011 SKILL-012 SKILL-014 SKILL-016 SKILL-017 SKILL-019 | STORY-003 |
| `ACH-006` | Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klien… | PM | 2025-01→2025-12 | 9 | SKILL-003 SKILL-004 SKILL-005 SKILL-007 SKILL-011 SKILL-013 SKILL-017 | STORY-003 |
| `ACH-007` | Samodzielne wdrożenie systemu VOIP i infolinii | KIER | 2023-09→2025-01 | 8 | SKILL-008 SKILL-009 SKILL-010 | — |
| `ACH-008` | Koordynacja wdrożenia produktów PV Stand i PV-Box | KOOR | 2022→2023 | 7 | SKILL-002 SKILL-004 SKILL-006 SKILL-011 SKILL-012 SKILL-014 SKILL-015 SKILL-017 | — |
| `ACH-009` | Reorganizacja infrastruktury magazynowej i danych magazynowych w ERP | KOOR | 2020→2023 | 7 | SKILL-002 SKILL-008 | STORY-006 |
| `ACH-010` | Projektowanie organizacji na podstawie analizy danych operacyjnych | KIER | 2023-09→2025-01 | 8 | SKILL-002 SKILL-004 SKILL-005 SKILL-010 SKILL-015 SKILL-016 SKILL-017 SKILL-021 | STORY-004 |
| `ACH-011` | Stworzenie systemu kalkulacji komponentów dla działu handlowego | KOOR | 2020→2023 | 7 | SKILL-001 SKILL-016 SKILL-019 | STORY-007 |
| `ACH-012` | Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych… | KIER | 2023-09→2025-01 | 9 | SKILL-002 SKILL-005 SKILL-007 SKILL-010 SKILL-011 SKILL-012 SKILL-015 SKILL-016 SKILL-017 | STORY-008 STORY-009 |
| `ACH-013` | Rozwój i administracja ekosystemu systemów operacyjnych organizacji | KOOR | 2020-09→teraz | 8 | SKILL-001 SKILL-002 SKILL-004 SKILL-008 SKILL-009 SKILL-017 | STORY-003 |
| `ACH-014` | Budowa standardów dokumentacyjnych wspierających rozwój organizacji | PM | 2020-09→teraz | 8 | SKILL-001 SKILL-003 SKILL-004 SKILL-006 SKILL-017 | STORY-003 |
| `ACH-015` | Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów se… | PM | 2025-04→teraz | 9 | SKILL-001 SKILL-004 SKILL-009 SKILL-016 SKILL-019 SKILL-020 | STORY-010 |
| `ACH-016` | Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymag… | PM | 2025-12→teraz | 9 | SKILL-004 SKILL-011 SKILL-019 SKILL-021 | — |
| `ACH-017` | Stabilizacja kooperacji OEM i operacyjny business enablement | PM | 2025-03→2025-09 | 8 | SKILL-001 SKILL-004 SKILL-011 SKILL-012 | STORY-011 |
| `ACH-018` | Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego | PM | 2025-11→2026-06 | 7 | SKILL-001 SKILL-004 SKILL-007 SKILL-009 SKILL-012 | — |
| `ACH-019` | Architektura procesu życia produktu - projekt modelu operacyjnego f… | PM | 2025-09→2026-02 | 7 | SKILL-001 SKILL-019 | — |
| `ACH-020` | Zbudowanie i prowadzenie procesów rekrutacyjnych dla ról techniczny… | KOOR | 2022-08→teraz | 7 | SKILL-005 SKILL-007 | — |
| `ACH-021` | Hybrydowy model współpracy z podwykonawcami montażowymi | KOOR | 2021-10→2023-09 | 6 | SKILL-001 SKILL-011 | — |

### Prywatne — użycie wyjątkowe, tylko gdy oferta wprost tego dotyczy

| ACH | Tytuł | Okres | W | Skills | Stories |
| --- | --- | --- | --- | --- | --- |
| `ACH-P001` | Regularne prowadzenie wystąpień publicznych i koordynacja społeczno… | 2019→teraz | 8 | SKILL-005 SKILL-007 SKILL-013 SKILL-017 | — |
| `ACH-P002` | Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji t… | 2019→teraz | 8 | SKILL-005 SKILL-011 SKILL-013 SKILL-014 | — |
| `ACH-P003` | Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia | 2023-05→2024-05 | 6 | SKILL-005 SKILL-013 SKILL-014 | — |
| `ACH-P004` | Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi infor… | 2019→teraz | 10 | SKILL-003 SKILL-006 SKILL-015 SKILL-016 SKILL-017 SKILL-021 | — |
| `ACH-P005` | Wieloletni wolontariat kaznodziejski — komunikacja perswazyjna w te… | 2013→teraz | 8 | SKILL-007 SKILL-018 | — |
| `ACH-P006` | VaultShot CV — zaprojektowanie i wdrożenie systemu generowania apli… | 2026-06→teraz | 9 | SKILL-003 SKILL-009 SKILL-020 SKILL-021 | — |

---

## B. Kompetencje — dopasowanie do oferty

`#ACH` = liczba dowodów. Skille bez słów kluczowych dopasowuj po nazwie
i po kolumnie `Nazwa` — brak keywords nie oznacza słabszej kompetencji.

| SKILL | Nazwa | Kategoria | Poziom | W | #ACH | Słowa kluczowe |
| --- | --- | --- | --- | --- | --- | --- |
| `SKILL-001` | Process Design | Operations | Expert | 10 | 12 | process design, workflow design, process optimization, business process management, bpm… |
| `SKILL-002` | Operations Management | Operations | Advanced | 10 | 7 | operations, service operations, organizational scaling, logistics, operational excellence |
| `SKILL-003` | Knowledge Management | Knowledge | Expert | 10 | 7 | knowledge management, documentation, onboarding, knowledge base, information architecture… |
| `SKILL-004` | Product Management | Product | Advanced | 10 | 10 | product management, product development, product launch, warranty systems, technical prod… |
| `SKILL-005` | Leadership | Management | Advanced | 8 | 9 | _(brak)_ |
| `SKILL-006` | Technical Documentation | Knowledge | Expert | 9 | 6 | technical documentation, technical writing, procedures, instructions, documentation manag… |
| `SKILL-007` | Training & Enablement | Knowledge | Advanced | 9 | 9 | training, onboarding, enablement, knowledge transfer, technical training, partner educati… |
| `SKILL-008` | Business Systems | Systems | Advanced | 9 | 7 | business systems, crm, systems integration, digital transformation, operations systems, p… |
| `SKILL-009` | Workflow Automation | Systems | Advanced | 9 | 9 | workflow automation, process automation, workflow, automation, process optimization, oper… |
| `SKILL-010` | Service Operations | Operations | Advanced | 9 | 5 | service operations, service management, technical service, workflow management, service p… |
| `SKILL-011` | Stakeholder Management | Management | Advanced | 9 | 10 | stakeholder management, communication, partner management, cross-functional collaboration… |
| `SKILL-012` | Change Management | Management | Advanced | 10 | 8 | change management, transformation, organizational change, process transformation, organiz… |
| `SKILL-013` | Public Speaking | Communication | Advanced | 8 | 4 | public speaking, presentations, communication, facilitation, training, audience engagement |
| `SKILL-014` | Project Management | Management | Advanced | 8 | 6 | project management, planning, execution, coordination, scheduling, risk management |
| `SKILL-015` | Organizational Design | Operations | Advanced | 9 | 7 | organizational design, organizational development, workforce planning, organizational str… |
| `SKILL-016` | Operational Analysis | Analytics | Advanced | 8 | 7 | data analysis, analytics, reporting, kpi, root cause analysis, decision making |
| `SKILL-017` | Cross-Functional Facilitation | Communication | Advanced | 8 | 11 | cross-functional facilitation, context translation, internal advisory, problem framing, o… |
| `SKILL-018` | Persuasive Communication | Communication | Advanced | 8 | 1 | persuasive communication, objection handling, cold outreach, rapport building, rejection… |
| `SKILL-019` | Business Analysis & Requirements Engineering | Product & Business | Advanced | 8 | 5 | _(brak)_ |
| `SKILL-020` | AI Tooling & Automation | Systems | Advanced | 8 | 2 | _(brak)_ |
| `SKILL-021` | Systems Thinking | Systems | Expert | 10 | 6 | systems thinking, systems architecture, root cause analysis, dependency analysis, informa… |

---

## C. Bullety CV — gotowe sformułowania

Liczba w nawiasie to długość. Limit szablonu: **130 znaków** —
dłuższe skracaj zachowując liczby, nie dopisuj nowych faktów.

### `STORY-001` → ACH-001
_Transformacja organizacji pracy działu Instal/Solar_

- `[122]` Przekształciłem dział montażowy z modelu opartego na komunikacji ad-hoc w uporządkowany workflow wspierany przez Bitrix24.
- `[122]` Skróciłem czas organizacji montaży z 1–2 dni do około 2–3 godzin oraz ograniczyłem liczbę błędów operacyjnych o około 70%.
- `[116]` Zaprojektowałem procesy i standardy informacyjne umożliwiające skalowanie działu do około 30 realizacji miesięcznie.

### `STORY-002` → ACH-004
_Restrukturyzacja i stabilizacja działu serwisu_

- `[94]` Przejąłem odpowiedzialność za dział serwisu i przeprowadziłem jego stabilizację organizacyjną.
- `[81]` Zaprojektowałem workflow oraz model pracy wspierający codzienną obsługę klientów.
- `[62]` Koordynowałem zespół serwisowy i wdrażałem nowych pracowników.
- `[89]` Zbudowałem kulturę współodpowiedzialności i rozwiązywania problemów bez szukania winnych.
- `[127]` Przygotowałem dział do przekazania i przez cztery miesiące wdrożyłem nowego kierownika, który prowadzi go samodzielnie do dziś.

### `STORY-003` → ACH-005 ACH-006 ACH-014 ACH-013
_Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatoró…_

- `[123]` Współtworzyłem kompleksowy system gwarancyjny obejmujący producentów, instalatorów, dystrybutorów i użytkowników końcowych.
- `[120]` Skróciłem czas uzyskania gwarancji z 7–8 dni do około 3 dni oraz czas rozpatrywania reklamacji z 4–5 dni do około 2 dni.
- `[122]` Zaprojektowałem procesy, workflowy i system identyfikacji urządzeń oparty na numerach seryjnych, zwiększając skalowalność.
- `[130]` Przeprowadziłem wieloetapowy proces zbierania wymagań i uzgadniania rozwiązań między interesariuszami o sprzecznych oczekiwaniach.

### `STORY-004` → ACH-004 ACH-010
_Projektowanie modelu działania serwisu przy braku danych historycznych_

- `[114]` Stworzyłem system analizy operacyjnej serwisu umożliwiający podejmowanie decyzji przy braku danych historycznych..
- `[119]` Obaliłem założenia i wskazałem rzeczywiste przyczyny przeciążenia działu obsługującego kilkadziesiąt tysięcy urządzeń..
- `[114]` Zaprojektowałem model działania serwisu wspierający wzrost skali działalności bez utraty kompetencji technicznych.
- `[89]` Wdrożyłem metryki i model zarządzania wykorzystywane przez kolejnych kierowników serwisu.

### `STORY-005` → ACH-003 ACH-004
_Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej_

- `[122]` Zaprojektowałem i wdrożyłem system knowledge management oparty na BPMN i Wiki.js obejmujący 120 schematów diagnostycznych.
- `[104]` Skróciłem czas osiągnięcia samodzielności operacyjnej nowych serwisantów z 8–9 miesięcy do 2–3 miesięcy.
- `[88]` Przechwyciłem i ustrukturyzowałem wiedzę ekspercką krytyczną dla funkcjonowania serwisu.
- `[100]` Stworzyłem standard dokumentowania wiedzy technicznej wykorzystywany do dziś w procesie onboardingu.

### `STORY-006` → ACH-009
_Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewności_

- `[119]` Poprowadziłem wdrożenie nowego produktu fotowoltaicznego od koncepcji do gotowości rynkowej, koordynując wiele działów.
- `[105]` Stworzyłem dokumentację produkcyjną, jakościową i użytkową bez wcześniejszego doświadczenia w FMEA i DTR.
- `[115]` Zaprojektowałem proces jakościowy oraz instrukcję montażową wysoko ocenioną przez produkcję i kierownictwo zakładu.
- `[113]` Dostarczyłem gotowy do produkcji produkt w krótkim oknie rynkowym wynikającym ze zmian regulacyjnych na rynku PV.

### `STORY-007` → ACH-011
_Standaryzacja ofertowania i kalkulacji rentowności instalacji PV_

- `[128]` Zaprojektowałem system wyceny, rentowności i list materiałowych PV, skracając przygotowanie oferty z 2–6 godzin do ok. 10 minut.
- `[125]` Przekształciłem wiedzę ekspercką z PV, elektryki i kosztorysowania w system używany przez sprzedaż, technikę i administrację.
- `[114]` Stworzyłem rozwiązanie, które przez ok. 4 lata było podstawą ofertowania i przygotowania realizacji instalacji PV.
- `[107]` Umożliwiłem skalowanie procesu sprzedaży bez proporcjonalnego zwiększania liczby specjalistów technicznych.

### `STORY-008` → ACH-012
_Zatrzymanie niekontrolowanego skalowania operacji PV_

- `[125]` Zidentyfikowałem ograniczenia operacyjne przy gwałtownym wzroście rynku PV i doprowadziłem do zmiany podejścia do skalowania.
- `[125]` Zarządzałem realizacją kilkudziesięciu instalacji w krótkim okresie, koordynując logistykę, planowanie i wsparcie techniczne.
- `[123]` Eskalowałem ryzyka jakościowe i bezpieczeństwa z przeciążenia organizacji, inicjując zwiększenie zasobów administracyjnych.
- `[120]` Współtworzyłem przejście z modelu opartego na wysiłku pojedynczych osób do modelu wspieranego przez procesy i narzędzia.

### `STORY-009` → ACH-012
_Budowa zespołu serwisowego po kryzysie kadrowym_

- `[127]` Przejąłem dział serwisu po odejściu kierownika i części zespołu, stabilizując funkcjonowanie i utrzymując kluczowych ekspertów.
- `[119]` Wdrożyłem model współpracy Tier 1 / Tier 2 wspierający transfer wiedzy i efektywne wykorzystanie kompetencji ekspertów.
- `[92]` Zbudowałem kulturę współpracy opartą na odpowiedzialności, wsparciu i orientacji na klienta.
- `[126]` Podjąłem trudne decyzje personalne i wypracowałem dojrzalsze podejście do równoważenia zaufania, odpowiedzialności i kontroli.

### `STORY-010` → ACH-015
_Paszportyzacja produktów - od chaosu numerów seryjnych do fundamentu danych dla serwisu i…_

- `[121]` Zaprojektowałem standard identyfikacji produktów i bazę ok. 60 000 kart w CRM, dając serwisowi wgląd w historię urządzeń.
- `[101]` Porządkując dane historyczne, ujawniłem ukryty waste produkcyjny (ok. 20% zestawów przepakowywanych).
- `[96]` Stworzony fundament danych umożliwił uruchomienie promocji sprzedażowej "Pierwsze uruchomienie".

### `STORY-011` → ACH-017
_Stabilizacja kooperacji OEM i granica między ugaszeniem pożaru a ułożeniem procesu_

- `[123]` Ustabilizowałem współpracę z podwykonawcami OEM (dwie nowe umowy, obieg dokumentów, plomby), umożliwiając wzrost produkcji.
- `[68]` Po trzech miesiącach przekazałem uporządkowany obszar nowemu PM-owi.
- `[119]` Wyprowadziłem z degradacji modelu po rotacji kryterium domknięcia wdrożenia: proces musi przeżyć odejście każdej osoby.

---

## D. Achievementy bez Story — materiał na bullet

Brak gotowych sformułowań. Poniższe fakty (pole `impact`) są **jedynym**
dopuszczalnym materiałem — przenoś liczby dosłownie.

### `ACH-002` · Samodzielne opanowanie platformy Bitrix24 - od zera do projektanta automat…
Rola: `KOOR` · waga 9

- w pełni samodzielne dojście od zera do projektowania automatyzacji klasy enterprise - bez szkoleń, wdrożeniowca i zaplecza IT
- kompetencja stała się fundamentem transformacji działu (ACH-001), a docelowo administracji ekosystemu systemów całej organizacji (ACH-013)
- wzorzec samodzielnego opanowywania systemów powtórzony później przy kolejnych technologiach (BPMN, VOIP, ERP, narzędzia AI)

### `ACH-007` · Samodzielne wdrożenie systemu VOIP i infolinii
Rola: `KIER` · waga 8

- uporządkowanie obsługi połączeń przychodzących
- usprawnienie kierowania zgłoszeń do właściwych osób
- integracja komunikacji telefonicznej z procesami operacyjnymi

### `ACH-008` · Koordynacja wdrożenia produktów PV Stand i PV-Box
Rola: `KOOR` · waga 7

- przygotowanie organizacji do wdrożenia nowych produktów
- zapewnienie kompletnej dokumentacji wdrożeniowej - od produkcji po gwarancje
- realizacja serii 0 z weryfikacją jakościową przed wejściem na rynek

### `ACH-016` · Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami
Rola: `PM` · waga 9

- projekt powierzony mi przez właścicieli firmy jako strategiczny
- zabezpieczenie organizacji przed długiem technologicznym trzech niekompatybilnych rozwiązań
- konsolidacja budżetu wokół jednego, rozszerzalnego ekosystemu (moduły dokładane etapami zamiast osobnych aplikacji)

### `ACH-018` · Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego
Rola: `PM` · waga 7

- dwa powtarzalne procesy (harmonogram, umowy bonusowe) w codziennym użyciu handlowców
- eliminacja dojazdów do klientów w celu podpisywania umów - podpis elektroniczny z poziomu CRM
- adopcja narzędzia przez dział, który wcześniej nie pracował procesowo w CRM

### `ACH-019` · Architektura procesu życia produktu - projekt modelu operacyjnego firmy pr…
Rola: `PM` · waga 7

- kompletny pakiet projektowy modelu operacyjnego (proces, dokumenty, dane, odpowiedzialności) gotowy do wdrożenia
- warstwa danych architektury zrealizowana produkcyjnie poprzez system paszportyzacji i numerów seryjnych (ACH-015)
- proces ECR/ECO działa jako rejestr zmian produktowych, wykorzystany m.in. przy wdrażaniu nowego PM-a

### `ACH-020` · Zbudowanie i prowadzenie procesów rekrutacyjnych dla ról technicznych
Rola: `KOOR` · waga 7

- 8-9 osób zatrudnionych w osobiście prowadzonych procesach (monterzy, serwisanci PV, serwisanci KIPI)
- model selekcji pod potencjał rozwoju umożliwił zatrudnianie osób spoza branży do ról technicznych
- jedna z osób wyselekcjonowanych pod potencjał rozwoju pełni dziś funkcję koordynatora działu szkoleń (rozwój to zasługa jej i jej przełożonego - selekcja okazała się trafna)

### `ACH-021` · Hybrydowy model współpracy z podwykonawcami montażowymi
Rola: `KOOR` · waga 6

- skalowanie do ~30 montaży miesięcznie bez proporcjonalnej rozbudowy zespołu etatowego
- żadna współpraca nie zakończyła się z powodu jakości - wymagania umowne plus kontrola odbiorowa działały prewencyjnie
- ograniczenie ryzyka BHP zespołu własnego przy zachowaniu pełnej kontroli nad krytyczną (elektryczną) częścią montażu

---

## E. Walidacja przed oddaniem YAML

Testy binarne, wszystkie sprawdzalne w tym pliku bez sięgania do Vaulta:

1. **Para SKILL–ACH** — czy `SKILL-XXX` figuruje w kolumnie Skills wiersza
   `ACH-YYY` w tabeli A? Jeśli nie, para jest błędna.
2. **Para ACH–STORY** — czy `STORY-ZZZ` figuruje w kolumnie Stories wiersza
   `ACH-YYY` w tabeli A?
3. **Długość bulletu** — czy treść mieści się w 130 znakach?

Dodatkowo: brak powtórzonych ACH, brak powtórzonych SKILL, rozkład
bulletów na role zgodny z kwotą (PM 3 / KIER 2 / KOOR 1).

---

_Wygenerowano 2026-07-24 07:02 UTC z commita `f646726`._
