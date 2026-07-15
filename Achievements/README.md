# Achievements

## Cel

Folder **Achievements** zawiera najważniejsze osiągnięcia zawodowe i prywatne zgromadzone w ramach Career Vault.

Achievement jest pojedynczym, możliwym do udokumentowania osiągnięciem, projektem, usprawnieniem, wdrożeniem, transformacją lub zmianą, która wywarła zauważalny wpływ na organizację, zespół, produkt, proces lub rozwój osobisty.

Achievements stanowią główne źródło dowodów w całym Career Vault.

Jeżeli Experience dostarcza kontekstu, a Skills opisują kompetencje, to Achievements odpowiadają na pytanie:

> Co faktycznie zostało osiągnięte?

---

# Rola Achievements w Career Vault

Career Vault przechowuje wiedzę na wielu poziomach abstrakcji.

```text
Experience
↓
Gdzie zdobywałem doświadczenie?

Achievements
↓
Co osiągnąłem?

Skills
↓
Jakie kompetencje potwierdzają te osiągnięcia?

Stories
↓
Jak opowiadać o tych doświadczeniach?

Development Areas
↓
Jakie wzorce rozwojowe obserwuję u siebie?

Identity
↓
Kim jestem jako profesjonalista?
```

Achievements są fundamentem całego systemu.

Wszystkie pozostałe moduły powinny opierać się na informacjach zapisanych w Achievementach.

---

# Czym jest Achievement?

Achievement opisuje konkretną sytuację, projekt, usprawnienie lub rezultat osiągnięty w określonym kontekście.

Dobry Achievement:

* opisuje rzeczywisty problem lub potrzebę,
* zawiera kontekst biznesowy,
* pokazuje podjęte działania,
* wskazuje zastosowane kompetencje,
* opisuje rezultat,
* dokumentuje wpływ,
* może zostać wykorzystany jako dowód doświadczenia.

Achievement nie opisuje obowiązków.

Achievement opisuje rezultat, zmianę lub wpływ wykraczający poza samo wykonywanie obowiązków.

---

# Fakty ponad deklaracje

Najważniejsza zasada Career Vault:

> Fakty ponad deklaracje.

Przykład:

❌ Jestem dobrym liderem.

✅ Przeprowadziłem restrukturyzację działu serwisu oraz ustabilizowałem jego funkcjonowanie.

Kompetencje powinny wynikać z osiągnięć.

Nie odwrotnie.

---

# Rodzaje Achievementów

## Zawodowe

Identyfikator:

```text
ACH-001
ACH-002
...
```

Dotyczą doświadczenia zawodowego, działalności biznesowej, projektów organizacyjnych, wdrożeń, produktów oraz inicjatyw realizowanych w pracy.

---

## Prywatne

Identyfikator:

```text
ACH-P001
ACH-P002
...
```

Dotyczą działań realizowanych poza pracą zawodową.

Mogą dokumentować kompetencje rozwijane poprzez:

* działalność społeczną,
* organizację wydarzeń,
* hobby,
* projekty prywatne,
* aktywność edukacyjną.

---

# Poziomy wpływu

Achievement może dotyczyć różnych poziomów oddziaływania.

## Indywidualny

Wpływ na własną pracę lub efektywność.

Przykład:

* stworzenie własnego narzędzia automatyzującego pracę.

---

## Zespołowy

Wpływ na sposób pracy zespołu.

Przykład:

* usprawnienie workflow działu.

---

## Działowy

Wpływ na funkcjonowanie całego działu.

Przykład:

* restrukturyzacja działu serwisu.

---

## Organizacyjny

Wpływ na funkcjonowanie całej organizacji.

Przykład:

* wdrożenie systemu wykorzystywanego przez wiele działów.

---

## Struktura rekordu

### Pola obowiązkowe

```yaml
id:
title:

period:
  start:
  end:

company:
roles:

situation:
actions:
impact:

skills:
themes:

importance:
```

### Pola opcjonalne

```yaml
category:
evidence:
metrics:
fin:
related_tools:
star_candidates:
notes:
```

---

## Opis pól

### id

Unikalny identyfikator rekordu.

Przykład:

```yaml
id: ACH-001
```

---

### title

Krótka nazwa osiągnięcia.

Powinna opisywać rezultat lub inicjatywę.

Przykład:

```yaml
title: Wdrożenie systemu KPI dla działu handlowego
```

---

### period

Okres, w którym osiągnięcie miało miejsce.

Przykład:

```yaml
period:
  start: 2022-01
  end: 2022-12
```

Jeżeli osiągnięcie trwało przez dłuższy okres, należy podać pełny zakres.

---

### company

Organizacja, w której osiągnięcie zostało zrealizowane.

Przykład:

```yaml
company: KIPI
```

---

### roles

Stanowiska lub role pełnione podczas realizacji osiągnięcia.

Przykład:

```yaml
roles:
  - Product Manager
  - Operations Manager
```

---

### situation

Krótki opis sytuacji wyjściowej.

Odpowiada na pytanie:

> W jakim kontekście wystąpiło osiągnięcie?

Przykład:

```yaml
situation: >
  Firma nie posiadała spójnego systemu raportowania wyników sprzedaży.
```

---

### actions

Opis podjętych działań.

Odpowiada na pytanie:

> Co konkretnie zrobiłem?

Przykład:

```yaml
actions:
  - Zmapowałem proces sprzedaży.
  - Zdefiniowałem kluczowe wskaźniki.
  - Wdrożyłem cykliczne raportowanie.
```

---

### impact

Opis rezultatów i efektów działań.

Odpowiada na pytanie:

> Co zmieniło się dzięki tym działaniom?

Przykład:

```yaml
impact:
  - Zwiększono przejrzystość procesu sprzedaży.
  - Skrócono czas przygotowania raportów.
  - Ułatwiono identyfikację problemów operacyjnych.
```

---

### skills

Kompetencje potwierdzane przez achievement.

Wartości powinny odpowiadać identyfikatorom z modułu `Skills`.

Przykład:

```yaml
skills:
  - process-design
  - workflow-automation
  - data-analysis
```

---

### themes

Tematy lub obszary, których dotyczy achievement.

Themes opisują kontekst, a nie kompetencje.

Przykład:

```yaml
themes:
  - operations
  - reporting
  - sales
```

---

### importance

Ocena znaczenia achievementu.

Rekomendowana skala:

```yaml
importance: 10
```

Gdzie:

| Wartość | Znaczenie                |
| ------- | ------------------------ |
| 9–10    | Kluczowe osiągnięcie     |
| 7–8     | Bardzo ważne osiągnięcie |
| 5–6     | Istotne osiągnięcie      |
| 1–4     | Osiągnięcie pomocnicze   |

Pole służy do priorytetyzacji przy budowie CV, Stories i analizie AI.

---

### category

Opcjonalna kategoria nadrzędna.

Przykłady:

```yaml
category: operations
```

```yaml
category: leadership
```

```yaml
category: product
```

---

### evidence

Dowody potwierdzające achievement.

Mogą to być:

* raporty,
* dashboardy,
* procedury,
* prezentacje,
* dokumentacja,
* wyniki biznesowe,
* inne artefakty pracy.

Przykład:

```yaml
evidence:
  - KPI dashboard
  - Monthly sales report
  - Internal process documentation
```

---

### metrics

Mierzalne wyniki achievementu.

Przykład:

```yaml
metrics:
  reporting_time:
    before: 4h
    after: 20m

  conversion_rate:
    improvement: "+18%"
```

---

### fin

Lista analiz finansowych rekordu.

Zasada nadrzędna: blok `fin` występuje **wyłącznie w Achievementach**
(single source of truth). Stories i pozostałe moduły odsyłają do niego
identyfikatorem (np. "metodologia: ACH-001, blok fin / FIN-001A"),
nigdy nie duplikują wyceny.

Każda analiza zawiera:

* `id` — identyfikator w formacie FIN-XXX (litera przy wielu analizach
  jednego rekordu, np. FIN-001A, FIN-001B),
* `value_type` — typ wartości: Capacity Release / Cost Avoidance /
  Reduced Lead Time / Strategic Enablement,
* wycenę — `estimated_value`, `quantified` lub `unit_value_pln`,
* `calculation` — jawny wzór,
* `assumptions` — wszystkie przyjęte założenia,
* `confidence` — poziom pewności,
* `note` — obowiązkową notę: "Szacunek własny metodą X;
  nie są to dane księgowe firmy".

Zasady rzetelności: wartości w widełkach, zaokrąglanie konserwatywne
(w dół), zakaz sumowania nakładających się oszczędności, brakujące dane
wejściowe oznaczane jawnie zamiast zgadywane.

Przykład:

```yaml
fin:
  - id: FIN-001A
    value_type: Capacity Release
    estimated_value:
      annual_pln: 100000-160000
    calculation: >
      (11 h - 1,5 h) × 18-20 montaży/mies. × 50-70 PLN/h × 12 mies.
    assumptions:
      - czas przed wdrożeniem ok. 11 h, po wdrożeniu ok. 1,5 h
      - konserwatywny koszt organizacyjny pracy 50-70 PLN/h
    confidence: medium-high
    note: >
      Szacunek własny metodą Time Savings × Capacity Cost;
      nie są to dane księgowe firmy.
```

---

### related_tools

Narzędzia wykorzystane podczas realizacji.

Przykład:

```yaml
related_tools:
  - Excel
  - Power BI
  - ERP
```

---

### star_candidates

Elementy szczególnie przydatne przy budowie Story.

Przykład:

```yaml
star_candidates:
  - problem: brak raportowania
  - action: wdrożenie KPI
  - result: szybsze decyzje
```

---

### notes

Dodatkowe informacje pomocnicze.

Pole nie powinno zawierać kluczowych danych, które powinny znaleźć się w polach głównych.

---

# Relacje z pozostałymi modułami

## Experience

Dostarcza kontekstu kariery.

## Achievements

Stanowią źródło dowodów.

## Skills

Opisują kompetencje potwierdzone Achievementami.

## Stories

Przekształcają Achievementy w narrację.

## Development Areas

Powstają na podstawie analizy wielu Achievementów i Stories.

## Identity

Stanowi syntezę wiedzy zgromadzonej w całym Career Vault.

---

# Zasady utrzymania

1. Jeden Achievement powinien opisywać jedno osiągnięcie.
2. Preferuj rezultaty zamiast obowiązków.
3. Preferuj fakty zamiast opinii.
4. Unikaj duplikowania informacji.
5. Dodawaj mierzalne rezultaty, gdy są dostępne.
6. Łącz Achievementy ze Skills.
7. Łącz Achievementy ze Stories.
8. Łącz Achievementy z Development Areas, jeśli stanowią ich źródło.
9. Aktualizuj rekordy, gdy pojawią się nowe informacje.
10. Preferuj jakość nad ilość.

---

# Najważniejsza zasada

Achievement nie opisuje tego, za co odpowiadałem.

Achievement opisuje to, co udało mi się osiągnąć.

Jeżeli czegoś nie można powiązać z konkretnym osiągnięciem, nie powinno stanowić podstawy do budowania kompetencji, narracji ani wniosków rozwojowych.

---

# Indeks rekordów

> **Sekcja generowana automatycznie** ze stanu Vaulta (commit `ac0d179`, 2026-07-11).
> Po dodaniu lub zmianie rekordu należy ją przegenerować — nie edytuj list ręcznie.

Łącznie: **27** rekordów — 21 zawodowych, 6 prywatnych.

## Zawodowe (21)

| ID | Tytuł | Firma | Okres | Waga |
| --- | --- | --- | --- | --- |
| `ACH-001` | Transformacja działu Instal/Solar | KIPI | 2020-09 → 2023-09 | 10 |
| `ACH-002` | Samodzielne opanowanie platformy Bitrix24 - od zera do projektanta automatyzacji | KIPI | 2020-09 → 2023-09 | 9 |
| `ACH-003` | Stworzenie bazy wiedzy serwisowej BPMN 2.0 | KIPI | 2023-09 → 2025-01 | 10 |
| `ACH-004` | Restrukturyzacja i stabilizacja działu serwisu | KIPI | 2023-09 → 2025-01 | 10 |
| `ACH-005` | Zaprojektowanie i wdrożenie systemu gwarancyjnego | KIPI | 2025-01 → current | 10 |
| `ACH-006` | Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów | KIPI | 2025-01 → 2025-12 | 9 |
| `ACH-007` | Samodzielne wdrożenie systemu VOIP i infolinii | KIPI | 2023-09 → 2025-01 | 8 |
| `ACH-008` | Koordynacja wdrożenia produktów PV Stand i PV-Box | KIPI | 2022 → 2023 | 7 |
| `ACH-009` | Reorganizacja infrastruktury magazynowej i danych magazynowych w ERP | KIPI | 2020 → 2023 | 7 |
| `ACH-010` | Projektowanie organizacji na podstawie analizy danych operacyjnych | KIPI | 2023-09 → 2025-01 | 8 |
| `ACH-011` | Stworzenie systemu kalkulacji komponentów dla działu handlowego | KIPI | 2020 → 2023 | 7 |
| `ACH-012` | Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych | KIPI | 2023-09 → 2025-01 | 9 |
| `ACH-013` | Rozwój i administracja ekosystemu systemów operacyjnych organizacji | KIPI | 2020-09 → current | 8 |
| `ACH-014` | Budowa standardów dokumentacyjnych wspierających rozwój organizacji | KIPI | 2020-09 → current | 8 |
| `ACH-015` | Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych | KIPI | 2025-04 → current | 9 |
| `ACH-016` | Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami | KIPI | 2025-12 → current | 9 |
| `ACH-017` | Stabilizacja kooperacji OEM i operacyjny business enablement | KIPI | 2025-03 → 2025-09 | 8 |
| `ACH-018` | Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego | KIPI | 2025-11 → 2026-06 | 7 |
| `ACH-019` | Architektura procesu życia produktu - projekt modelu operacyjnego firmy produktowej | KIPI | 2025-09 → 2026-02 | 7 |
| `ACH-020` | Zbudowanie i prowadzenie procesów rekrutacyjnych dla ról technicznych | KIPI | 2022-08 → current | 7 |
| `ACH-021` | Hybrydowy model współpracy z podwykonawcami montażowymi | KIPI | 2021-10 → 2023-09 | 6 |

## Prywatne (6)

| ID | Tytuł | Okres | Waga |
| --- | --- | --- | --- |
| `ACH-P001` | Regularne prowadzenie wystąpień publicznych i koordynacja społeczności | 2019 → current | 8 |
| `ACH-P002` | Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych | 2019 → current | 8 |
| `ACH-P003` | Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia | 2023-05 → 2024-05 | 6 |
| `ACH-P004` | Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych | 2019 → current | 10 |
| `ACH-P005` | Wieloletni wolontariat kaznodziejski — komunikacja perswazyjna w terenie i rezyliencja psychologiczna | 2013 → current | 8 |
| `ACH-P006` | VaultShot CV — zaprojektowanie i wdrożenie systemu generowania aplikacji dopasowanych pod ofertę (redukcja czasu ~94% przy pełnej dowodowości), będącego jednocześnie strategiczną odpowiedzią na mechanikę rynku rekrutacyjnego i meta-dowodem własnych kompetencji analityczno-systemowych | 2026-06 → current | 9 |

---

# Encje powiązane

> **Sekcja generowana automatycznie** ze stanu Vaulta (commit `ac0d179`, 2026-07-11).
> Po dodaniu lub zmianie rekordu należy ją przegenerować — nie edytuj list ręcznie.

Źródła powiązań (single source of truth — powiązania nie są duplikowane w rekordach ACH):

* **Skills** — pole `evidence` w rekordach `SKILL-*`,
* **Stories** — pole `evidence.achievement_ids` w rekordach `STORY-*`,
* **Development Areas** — pole `sources.achievements` w rekordach `DEV-*`.

## Tabela zbiorcza

| ID | Tytuł | Skills | Stories | Development Areas |
| --- | --- | --- | --- | --- |
| `ACH-001` | Transformacja działu Instal/Solar | `SKILL-001` — Process Design<br>`SKILL-002` — Operations Management<br>`SKILL-003` — Knowledge Management<br>`SKILL-005` — Leadership<br>`SKILL-006` — Technical Documentation<br>`SKILL-008` — Business Systems<br>`SKILL-009` — Workflow Automation<br>`SKILL-011` — Stakeholder Management<br>`SKILL-012` — Change Management<br>`SKILL-014` — Project Management<br>`SKILL-015` — Organizational Design<br>`SKILL-017` — Cross-Functional Facilitation | `STORY-001` — Transformacja organizacji pracy działu Instal/Solar | `DEV-005` — Assertiveness and Difficult Conversations<br>`DEV-006` — Boundary Management |
| `ACH-002` | Samodzielne opanowanie platformy Bitrix24 - od zera do projektanta automatyzacji | `SKILL-008` — Business Systems<br>`SKILL-009` — Workflow Automation | — | — |
| `ACH-003` | Stworzenie bazy wiedzy serwisowej BPMN 2.0 | `SKILL-001` — Process Design<br>`SKILL-003` — Knowledge Management<br>`SKILL-006` — Technical Documentation<br>`SKILL-007` — Training & Enablement<br>`SKILL-010` — Service Operations<br>`SKILL-012` — Change Management<br>`SKILL-015` — Organizational Design | `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej | — |
| `ACH-004` | Restrukturyzacja i stabilizacja działu serwisu | `SKILL-001` — Process Design<br>`SKILL-002` — Operations Management<br>`SKILL-005` — Leadership<br>`SKILL-007` — Training & Enablement<br>`SKILL-008` — Business Systems<br>`SKILL-009` — Workflow Automation<br>`SKILL-010` — Service Operations<br>`SKILL-011` — Stakeholder Management<br>`SKILL-012` — Change Management<br>`SKILL-014` — Project Management<br>`SKILL-015` — Organizational Design<br>`SKILL-016` — Operational Analysis<br>`SKILL-017` — Cross-Functional Facilitation | `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu<br>`STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych<br>`STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej | `DEV-005` — Assertiveness and Difficult Conversations<br>`DEV-006` — Boundary Management |
| `ACH-005` | Zaprojektowanie i wdrożenie systemu gwarancyjnego | `SKILL-001` — Process Design<br>`SKILL-003` — Knowledge Management<br>`SKILL-004` — Product Management<br>`SKILL-006` — Technical Documentation<br>`SKILL-007` — Training & Enablement<br>`SKILL-008` — Business Systems<br>`SKILL-009` — Workflow Automation<br>`SKILL-011` — Stakeholder Management<br>`SKILL-012` — Change Management<br>`SKILL-014` — Project Management<br>`SKILL-016` — Operational Analysis<br>`SKILL-017` — Cross-Functional Facilitation<br>`SKILL-019` — Business Analysis & Requirements Engineering | `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu | — |
| `ACH-006` | Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów | `SKILL-003` — Knowledge Management<br>`SKILL-004` — Product Management<br>`SKILL-005` — Leadership<br>`SKILL-007` — Training & Enablement<br>`SKILL-011` — Stakeholder Management<br>`SKILL-013` — Public Speaking<br>`SKILL-017` — Cross-Functional Facilitation | `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu | `DEV-005` — Assertiveness and Difficult Conversations<br>`DEV-006` — Boundary Management |
| `ACH-007` | Samodzielne wdrożenie systemu VOIP i infolinii | `SKILL-008` — Business Systems<br>`SKILL-009` — Workflow Automation<br>`SKILL-010` — Service Operations | — | — |
| `ACH-008` | Koordynacja wdrożenia produktów PV Stand i PV-Box | `SKILL-002` — Operations Management<br>`SKILL-004` — Product Management<br>`SKILL-006` — Technical Documentation<br>`SKILL-011` — Stakeholder Management<br>`SKILL-012` — Change Management<br>`SKILL-014` — Project Management<br>`SKILL-015` — Organizational Design<br>`SKILL-017` — Cross-Functional Facilitation | — | `DEV-004` — Commercial Discovery<br>`DEV-005` — Assertiveness and Difficult Conversations<br>`DEV-006` — Boundary Management |
| `ACH-009` | Reorganizacja infrastruktury magazynowej i danych magazynowych w ERP | `SKILL-002` — Operations Management<br>`SKILL-008` — Business Systems | `STORY-006` — Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewności | — |
| `ACH-010` | Projektowanie organizacji na podstawie analizy danych operacyjnych | `SKILL-002` — Operations Management<br>`SKILL-004` — Product Management<br>`SKILL-005` — Leadership<br>`SKILL-010` — Service Operations<br>`SKILL-015` — Organizational Design<br>`SKILL-016` — Operational Analysis<br>`SKILL-017` — Cross-Functional Facilitation | `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych | `DEV-005` — Assertiveness and Difficult Conversations<br>`DEV-006` — Boundary Management |
| `ACH-011` | Stworzenie systemu kalkulacji komponentów dla działu handlowego | `SKILL-001` — Process Design<br>`SKILL-016` — Operational Analysis<br>`SKILL-019` — Business Analysis & Requirements Engineering | `STORY-007` — Standaryzacja ofertowania i kalkulacji rentowności instalacji PV | `DEV-004` — Commercial Discovery |
| `ACH-012` | Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych | `SKILL-002` — Operations Management<br>`SKILL-005` — Leadership<br>`SKILL-007` — Training & Enablement<br>`SKILL-010` — Service Operations<br>`SKILL-011` — Stakeholder Management<br>`SKILL-012` — Change Management<br>`SKILL-015` — Organizational Design<br>`SKILL-016` — Operational Analysis<br>`SKILL-017` — Cross-Functional Facilitation | `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV<br>`STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym | `DEV-001` — Leadership Through Accountability<br>`DEV-002` — Personal Capacity Management |
| `ACH-013` | Rozwój i administracja ekosystemu systemów operacyjnych organizacji | `SKILL-001` — Process Design<br>`SKILL-002` — Operations Management<br>`SKILL-004` — Product Management<br>`SKILL-008` — Business Systems<br>`SKILL-009` — Workflow Automation<br>`SKILL-017` — Cross-Functional Facilitation | `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu | `DEV-004` — Commercial Discovery<br>`DEV-005` — Assertiveness and Difficult Conversations<br>`DEV-006` — Boundary Management |
| `ACH-014` | Budowa standardów dokumentacyjnych wspierających rozwój organizacji | `SKILL-001` — Process Design<br>`SKILL-003` — Knowledge Management<br>`SKILL-004` — Product Management<br>`SKILL-006` — Technical Documentation<br>`SKILL-017` — Cross-Functional Facilitation | `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu | `DEV-004` — Commercial Discovery<br>`DEV-006` — Boundary Management |
| `ACH-015` | Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych | `SKILL-001` — Process Design<br>`SKILL-004` — Product Management<br>`SKILL-009` — Workflow Automation<br>`SKILL-016` — Operational Analysis<br>`SKILL-019` — Business Analysis & Requirements Engineering<br>`SKILL-020` — AI Tooling & Automation | — | `DEV-007` — Asymmetric Self-Valuation |
| `ACH-016` | Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami | `SKILL-004` — Product Management<br>`SKILL-011` — Stakeholder Management<br>`SKILL-019` — Business Analysis & Requirements Engineering | — | `DEV-007` — Asymmetric Self-Valuation |
| `ACH-017` | Stabilizacja kooperacji OEM i operacyjny business enablement | `SKILL-001` — Process Design<br>`SKILL-004` — Product Management<br>`SKILL-011` — Stakeholder Management<br>`SKILL-012` — Change Management | — | — |
| `ACH-018` | Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego | `SKILL-001` — Process Design<br>`SKILL-004` — Product Management<br>`SKILL-007` — Training & Enablement<br>`SKILL-009` — Workflow Automation<br>`SKILL-012` — Change Management | — | — |
| `ACH-019` | Architektura procesu życia produktu - projekt modelu operacyjnego firmy produktowej | `SKILL-001` — Process Design<br>`SKILL-019` — Business Analysis & Requirements Engineering | — | `DEV-007` — Asymmetric Self-Valuation |
| `ACH-020` | Zbudowanie i prowadzenie procesów rekrutacyjnych dla ról technicznych | `SKILL-005` — Leadership<br>`SKILL-007` — Training & Enablement | — | — |
| `ACH-021` | Hybrydowy model współpracy z podwykonawcami montażowymi | `SKILL-001` — Process Design<br>`SKILL-011` — Stakeholder Management | — | — |
| `ACH-P001` | Regularne prowadzenie wystąpień publicznych i koordynacja społeczności | `SKILL-005` — Leadership<br>`SKILL-007` — Training & Enablement<br>`SKILL-013` — Public Speaking<br>`SKILL-017` — Cross-Functional Facilitation | — | — |
| `ACH-P002` | Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych | `SKILL-005` — Leadership<br>`SKILL-011` — Stakeholder Management<br>`SKILL-013` — Public Speaking<br>`SKILL-014` — Project Management | — | — |
| `ACH-P003` | Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia | `SKILL-005` — Leadership<br>`SKILL-013` — Public Speaking<br>`SKILL-014` — Project Management | — | — |
| `ACH-P004` | Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych | `SKILL-003` — Knowledge Management<br>`SKILL-006` — Technical Documentation<br>`SKILL-015` — Organizational Design<br>`SKILL-016` — Operational Analysis<br>`SKILL-017` — Cross-Functional Facilitation | — | — |
| `ACH-P005` | Wieloletni wolontariat kaznodziejski — komunikacja perswazyjna w terenie i rezyliencja psychologiczna | `SKILL-007` — Training & Enablement<br>`SKILL-018` — Persuasive Communication | — | — |
| `ACH-P006` | VaultShot CV — zaprojektowanie i wdrożenie systemu generowania aplikacji dopasowanych pod ofertę (redukcja czasu ~94% przy pełnej dowodowości), będącego jednocześnie strategiczną odpowiedzią na mechanikę rynku rekrutacyjnego i meta-dowodem własnych kompetencji analityczno-systemowych | — | — | — |

## Rozwinięcie per rekord

### `ACH-001` — Transformacja działu Instal/Solar

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-002` — Operations Management
  - `SKILL-003` — Knowledge Management
  - `SKILL-005` — Leadership
  - `SKILL-006` — Technical Documentation
  - `SKILL-008` — Business Systems
  - `SKILL-009` — Workflow Automation
  - `SKILL-011` — Stakeholder Management
  - `SKILL-012` — Change Management
  - `SKILL-014` — Project Management
  - `SKILL-015` — Organizational Design
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories:**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
* **Development Areas:**
  - `DEV-005` — Assertiveness and Difficult Conversations
  - `DEV-006` — Boundary Management

### `ACH-002` — Samodzielne opanowanie platformy Bitrix24 - od zera do projektanta automatyzacji

* **Skills:**
  - `SKILL-008` — Business Systems
  - `SKILL-009` — Workflow Automation
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-003` — Knowledge Management
  - `SKILL-006` — Technical Documentation
  - `SKILL-007` — Training & Enablement
  - `SKILL-010` — Service Operations
  - `SKILL-012` — Change Management
  - `SKILL-015` — Organizational Design
* **Stories:**
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
* **Development Areas:**
  - _brak_

### `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-002` — Operations Management
  - `SKILL-005` — Leadership
  - `SKILL-007` — Training & Enablement
  - `SKILL-008` — Business Systems
  - `SKILL-009` — Workflow Automation
  - `SKILL-010` — Service Operations
  - `SKILL-011` — Stakeholder Management
  - `SKILL-012` — Change Management
  - `SKILL-014` — Project Management
  - `SKILL-015` — Organizational Design
  - `SKILL-016` — Operational Analysis
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories:**
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
* **Development Areas:**
  - `DEV-005` — Assertiveness and Difficult Conversations
  - `DEV-006` — Boundary Management

### `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-003` — Knowledge Management
  - `SKILL-004` — Product Management
  - `SKILL-006` — Technical Documentation
  - `SKILL-007` — Training & Enablement
  - `SKILL-008` — Business Systems
  - `SKILL-009` — Workflow Automation
  - `SKILL-011` — Stakeholder Management
  - `SKILL-012` — Change Management
  - `SKILL-014` — Project Management
  - `SKILL-016` — Operational Analysis
  - `SKILL-017` — Cross-Functional Facilitation
  - `SKILL-019` — Business Analysis & Requirements Engineering
* **Stories:**
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
* **Development Areas:**
  - _brak_

### `ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów

* **Skills:**
  - `SKILL-003` — Knowledge Management
  - `SKILL-004` — Product Management
  - `SKILL-005` — Leadership
  - `SKILL-007` — Training & Enablement
  - `SKILL-011` — Stakeholder Management
  - `SKILL-013` — Public Speaking
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories:**
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
* **Development Areas:**
  - `DEV-005` — Assertiveness and Difficult Conversations
  - `DEV-006` — Boundary Management

### `ACH-007` — Samodzielne wdrożenie systemu VOIP i infolinii

* **Skills:**
  - `SKILL-008` — Business Systems
  - `SKILL-009` — Workflow Automation
  - `SKILL-010` — Service Operations
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box

* **Skills:**
  - `SKILL-002` — Operations Management
  - `SKILL-004` — Product Management
  - `SKILL-006` — Technical Documentation
  - `SKILL-011` — Stakeholder Management
  - `SKILL-012` — Change Management
  - `SKILL-014` — Project Management
  - `SKILL-015` — Organizational Design
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories:**
  - _brak_
* **Development Areas:**
  - `DEV-004` — Commercial Discovery
  - `DEV-005` — Assertiveness and Difficult Conversations
  - `DEV-006` — Boundary Management

### `ACH-009` — Reorganizacja infrastruktury magazynowej i danych magazynowych w ERP

* **Skills:**
  - `SKILL-002` — Operations Management
  - `SKILL-008` — Business Systems
* **Stories:**
  - `STORY-006` — Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewności
* **Development Areas:**
  - _brak_

### `ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych

* **Skills:**
  - `SKILL-002` — Operations Management
  - `SKILL-004` — Product Management
  - `SKILL-005` — Leadership
  - `SKILL-010` — Service Operations
  - `SKILL-015` — Organizational Design
  - `SKILL-016` — Operational Analysis
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories:**
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
* **Development Areas:**
  - `DEV-005` — Assertiveness and Difficult Conversations
  - `DEV-006` — Boundary Management

### `ACH-011` — Stworzenie systemu kalkulacji komponentów dla działu handlowego

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-016` — Operational Analysis
  - `SKILL-019` — Business Analysis & Requirements Engineering
* **Stories:**
  - `STORY-007` — Standaryzacja ofertowania i kalkulacji rentowności instalacji PV
* **Development Areas:**
  - `DEV-004` — Commercial Discovery

### `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych

* **Skills:**
  - `SKILL-002` — Operations Management
  - `SKILL-005` — Leadership
  - `SKILL-007` — Training & Enablement
  - `SKILL-010` — Service Operations
  - `SKILL-011` — Stakeholder Management
  - `SKILL-012` — Change Management
  - `SKILL-015` — Organizational Design
  - `SKILL-016` — Operational Analysis
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories:**
  - `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV
  - `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym
* **Development Areas:**
  - `DEV-001` — Leadership Through Accountability
  - `DEV-002` — Personal Capacity Management

### `ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-002` — Operations Management
  - `SKILL-004` — Product Management
  - `SKILL-008` — Business Systems
  - `SKILL-009` — Workflow Automation
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories:**
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
* **Development Areas:**
  - `DEV-004` — Commercial Discovery
  - `DEV-005` — Assertiveness and Difficult Conversations
  - `DEV-006` — Boundary Management

### `ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-003` — Knowledge Management
  - `SKILL-004` — Product Management
  - `SKILL-006` — Technical Documentation
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories:**
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
* **Development Areas:**
  - `DEV-004` — Commercial Discovery
  - `DEV-006` — Boundary Management

### `ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-004` — Product Management
  - `SKILL-009` — Workflow Automation
  - `SKILL-016` — Operational Analysis
  - `SKILL-019` — Business Analysis & Requirements Engineering
  - `SKILL-020` — AI Tooling & Automation
* **Stories:**
  - _brak_
* **Development Areas:**
  - `DEV-007` — Asymmetric Self-Valuation

### `ACH-016` — Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami

* **Skills:**
  - `SKILL-004` — Product Management
  - `SKILL-011` — Stakeholder Management
  - `SKILL-019` — Business Analysis & Requirements Engineering
* **Stories:**
  - _brak_
* **Development Areas:**
  - `DEV-007` — Asymmetric Self-Valuation

### `ACH-017` — Stabilizacja kooperacji OEM i operacyjny business enablement

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-004` — Product Management
  - `SKILL-011` — Stakeholder Management
  - `SKILL-012` — Change Management
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-004` — Product Management
  - `SKILL-007` — Training & Enablement
  - `SKILL-009` — Workflow Automation
  - `SKILL-012` — Change Management
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-019` — Architektura procesu życia produktu - projekt modelu operacyjnego firmy produktowej

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-019` — Business Analysis & Requirements Engineering
* **Stories:**
  - _brak_
* **Development Areas:**
  - `DEV-007` — Asymmetric Self-Valuation

### `ACH-020` — Zbudowanie i prowadzenie procesów rekrutacyjnych dla ról technicznych

* **Skills:**
  - `SKILL-005` — Leadership
  - `SKILL-007` — Training & Enablement
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-021` — Hybrydowy model współpracy z podwykonawcami montażowymi

* **Skills:**
  - `SKILL-001` — Process Design
  - `SKILL-011` — Stakeholder Management
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-P001` — Regularne prowadzenie wystąpień publicznych i koordynacja społeczności

* **Skills:**
  - `SKILL-005` — Leadership
  - `SKILL-007` — Training & Enablement
  - `SKILL-013` — Public Speaking
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-P002` — Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych

* **Skills:**
  - `SKILL-005` — Leadership
  - `SKILL-011` — Stakeholder Management
  - `SKILL-013` — Public Speaking
  - `SKILL-014` — Project Management
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-P003` — Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia

* **Skills:**
  - `SKILL-005` — Leadership
  - `SKILL-013` — Public Speaking
  - `SKILL-014` — Project Management
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych

* **Skills:**
  - `SKILL-003` — Knowledge Management
  - `SKILL-006` — Technical Documentation
  - `SKILL-015` — Organizational Design
  - `SKILL-016` — Operational Analysis
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-P005` — Wieloletni wolontariat kaznodziejski — komunikacja perswazyjna w terenie i rezyliencja psychologiczna

* **Skills:**
  - `SKILL-007` — Training & Enablement
  - `SKILL-018` — Persuasive Communication
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

### `ACH-P006` — VaultShot CV — zaprojektowanie i wdrożenie systemu generowania aplikacji dopasowanych pod ofertę (redukcja czasu ~94% przy pełnej dowodowości), będącego jednocześnie strategiczną odpowiedzią na mechanikę rynku rekrutacyjnego i meta-dowodem własnych kompetencji analityczno-systemowych

* **Skills:**
  - _brak_
* **Stories:**
  - _brak_
* **Development Areas:**
  - _brak_

---

# Luki w powiązaniach

> **Sekcja generowana automatycznie** ze stanu Vaulta (commit `ac0d179`, 2026-07-11).
> Po dodaniu lub zmianie rekordu należy ją przegenerować — nie edytuj list ręcznie.

## Achievementy bez Story

Nie jest to błąd — Story powstaje tylko tam, gdzie istnieje łuk narracyjny. Lista jako materiał do przeglądu:

* `ACH-002` — Samodzielne opanowanie platformy Bitrix24 - od zera do projektanta automatyzacji
* `ACH-007` — Samodzielne wdrożenie systemu VOIP i infolinii
* `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box
* `ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych
* `ACH-016` — Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami
* `ACH-017` — Stabilizacja kooperacji OEM i operacyjny business enablement
* `ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego
* `ACH-019` — Architektura procesu życia produktu - projekt modelu operacyjnego firmy produktowej
* `ACH-020` — Zbudowanie i prowadzenie procesów rekrutacyjnych dla ról technicznych
* `ACH-021` — Hybrydowy model współpracy z podwykonawcami montażowymi
* `ACH-P001` — Regularne prowadzenie wystąpień publicznych i koordynacja społeczności
* `ACH-P002` — Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych
* `ACH-P003` — Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia
* `ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych
* `ACH-P005` — Wieloletni wolontariat kaznodziejski — komunikacja perswazyjna w terenie i rezyliencja psychologiczna
* `ACH-P006` — VaultShot CV — zaprojektowanie i wdrożenie systemu generowania aplikacji dopasowanych pod ofertę (redukcja czasu ~94% przy pełnej dowodowości), będącego jednocześnie strategiczną odpowiedzią na mechanikę rynku rekrutacyjnego i meta-dowodem własnych kompetencji analityczno-systemowych

## Achievementy bez powiązanego Skilla

Achievement bez kompetencji nie jest wykorzystywany jako dowód w module Skills:

* `ACH-P006` — VaultShot CV — zaprojektowanie i wdrożenie systemu generowania aplikacji dopasowanych pod ofertę (redukcja czasu ~94% przy pełnej dowodowości), będącego jednocześnie strategiczną odpowiedzią na mechanikę rynku rekrutacyjnego i meta-dowodem własnych kompetencji analityczno-systemowych
