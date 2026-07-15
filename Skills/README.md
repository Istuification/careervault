# Skills

## Cel

Folder **Skills** zawiera kompetencje zidentyfikowane na podstawie doświadczenia, osiągnięć oraz projektów zgromadzonych w Career Vault.

Skills nie są listą deklarowanych umiejętności.

Każda kompetencja powinna być poparta konkretnymi dowodami w postaci Achievementów, Stories oraz innych elementów Career Vault.

Skills pełnią rolę warstwy kompetencyjnej całego systemu wiedzy.

Odpowiadają na pytanie:

> Co potrafię udowodnić poprzez swoje doświadczenia i osiągnięcia?

---

# Rola Skills w Career Vault

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

Skills stanowią warstwę interpretacyjną pomiędzy osiągnięciami a wyższymi poziomami modelu wiedzy.

To właśnie Skills pozwalają przekształcić pojedyncze osiągnięcia w spójny obraz kompetencji zawodowych.

---

# Czym jest Skill?

Skill opisuje kompetencję możliwą do zaobserwowania poprzez działania, decyzje oraz rezultaty.

Skill nie opisuje technologii.

Skill nie opisuje narzędzia.

Skill nie opisuje certyfikatu.

Skill opisuje zdolność do osiągania określonych rezultatów.

---

## Przykład

❌ BPMN 2.0

To metoda.

✅ Process Design

To kompetencja.

---

## Przykład

❌ Bitrix24

To narzędzie.

✅ Workflow Automation

To kompetencja.

---

## Przykład

❌ Excel

To narzędzie.

✅ Data Analysis

To kompetencja.

---

# Fakty ponad deklaracje

Najważniejsza zasada Career Vault:

> Fakty ponad deklaracje.

Każdy Skill powinien posiadać dowody potwierdzające jego praktyczne wykorzystanie.

Przykład:

```yaml
name: Process Design

evidence:
  achievements:
    - ACH-001
    - ACH-003
    - ACH-005
```

Jeżeli nie istnieją dowody potwierdzające daną kompetencję, prawdopodobnie nie powinna ona jeszcze znajdować się w Career Vault.

---

# Evidence-Based Skills

Career Vault wykorzystuje podejście Evidence-Based Skills.

Skill nie opisuje tego:

> czego się nauczyłem.

Skill opisuje:

> co wielokrotnie udowodniłem w praktyce.

Dlatego kompetencje powinny wynikać z doświadczeń, projektów oraz osiągniętych rezultatów.

Nie odwrotnie.

---

# Rodzaje kompetencji

## Kompetencje rdzeniowe

Najsilniej definiują profil zawodowy.

Przykłady:

* Systems Thinking
* Process Design
* Knowledge Management
* Operations Management

---

## Kompetencje wspierające

Regularnie wykorzystywane obszary wspierające kompetencje rdzeniowe.

Przykłady:

* Product Management
* Leadership
* Workflow Automation
* Technical Communication

---

## Kompetencje rozwijane

Obszary znajdujące się w trakcie aktywnego rozwoju.

Przykłady:

* Product Strategy
* AI Systems
* Commercial Discovery

---

# Schemat rekordu

Każdy Skill powinien być zapisany jako osobny plik YAML.

```yaml
id:

name:

category:

importance:

level:

summary:

capabilities:

methods:

tools:

evidence:

experience:
  first_used:
  years:

career_relevance:

keywords:

related_skills:
```

---

# Opis pól

## id

Unikalny identyfikator kompetencji.

Przykłady:

```text
SKILL-001
SKILL-010
SKILL-018
```

Identyfikator powinien pozostać niezmienny przez cały czas życia repozytorium.

---

## name

Nazwa kompetencji.

Przykłady:

```text
Process Design
Product Management
Leadership
Knowledge Management
```

---

## category

Główna kategoria kompetencji.

Przykłady:

```text
Operations
Product
Management
Knowledge
Systems
Analytics
Communication
```

---

## importance

Określa, jak bardzo dana kompetencja definiuje profil zawodowy.

Nie określa poziomu umiejętności.

### 10

Kompetencja rdzeniowa.

### 8–9

Bardzo ważna kompetencja wspierająca.

### 6–7

Kompetencja specjalistyczna.

### 1–5

Kompetencja pomocnicza.

---

## level

Poziom kompetencji.

Dopuszczalne wartości:

```text
Expert
Advanced
Intermediate
Basic
```

### Expert

Kompetencja wykorzystywana regularnie przez wiele lat i potwierdzona licznymi dowodami.

### Advanced

Kompetencja wykorzystywana samodzielnie w praktyce i potwierdzona wieloma przykładami.

### Intermediate

Kompetencja wykorzystywana okazjonalnie lub w ograniczonym zakresie.

### Basic

Podstawowa znajomość obszaru.

---

## summary

Krótki opis kompetencji.

Powinien odpowiadać na pytanie:

> Na czym polega ta kompetencja?

---

## capabilities

Lista zdolności składających się na daną kompetencję.

Przykład:

```yaml
capabilities:
  - workflow-design
  - process-mapping
  - process-optimization
```

---

## methods

Metody wykorzystywane podczas pracy.

Przykład:

```yaml
methods:
  - BPMN 2.0
  - Root Cause Analysis
  - Continuous Improvement
```

---

## tools

Narzędzia wykorzystywane podczas pracy.

Przykład:

```yaml
tools:
  - Bitrix24
  - Excel
  - Wiki.js
```

---

## evidence

Najważniejsze pole całego rekordu.

Opisuje źródła potwierdzające kompetencję.

Przykład:

```yaml
evidence:
  achievements:
    - ACH-001
    - ACH-003

  stories:
    - STORY-001
    - STORY-005

  development_areas:
    - DEV-002
```

---

## experience

Opis historii wykorzystania kompetencji.

Przykład:

```yaml
experience:
  first_used: 2020
  years: 5
```

### first_used

Pierwszy znany moment praktycznego wykorzystania kompetencji.

### years

Przybliżona liczba lat praktycznego doświadczenia.

---

## career_relevance

Ocena przydatności kompetencji dla określonych ścieżek zawodowych.

Przykład:

```yaml
career_relevance:
  product_manager: 8
  operations_manager: 10
  process_manager: 10
```

Skala:

```text
1 = niska przydatność
10 = kluczowa kompetencja
```

---

## keywords

Słowa kluczowe wspierające wyszukiwanie.

Przykład:

```yaml
keywords:
  - process design
  - workflow
  - operations
```

---

## related_skills

Powiązane kompetencje.

Przykład:

```yaml
related_skills:
  - SKILL-002
  - SKILL-012
```

---

# Kompetencje, metody i narzędzia

## Skills

Opisują kompetencje.

Przykłady:

* Process Design
* Leadership
* Product Management
* Knowledge Management

---

## Methods

Opisują sposoby pracy.

Przykłady:

* BPMN 2.0
* Root Cause Analysis
* Continuous Improvement

---

## Tools

Opisują narzędzia.

Przykłady:

* Bitrix24
* Excel
* Wiki.js
* Power BI

---

# Relacje z pozostałymi modułami

## Experience

Dostarcza kontekstu zawodowego.

## Achievements

Stanowią główne źródło dowodów.

## Skills

Grupują osiągnięcia w kompetencje.

## Stories

Pokazują wykorzystanie kompetencji w praktyce.

## Development Areas

Pokazują wzorce rozwojowe wynikające z wykorzystania kompetencji.

## Identity

Stanowi syntezę wszystkich kompetencji oraz doświadczeń zgromadzonych w Career Vault.

---

# Zasady utrzymania

1. Każdy Skill powinien posiadać dowody potwierdzające jego wykorzystanie.
2. Nie twórz Skills dla pojedynczych narzędzi.
3. Nie twórz Skills dla pojedynczych technologii.
4. Preferuj kompetencje zamiast technologii.
5. Łącz Skills z Achievementami.
6. Łącz Skills ze Stories.
7. Łącz Skills z Development Areas.
8. Łącz Skills z innymi Skills.
9. Aktualizuj kompetencje wraz z rozwojem Career Vault.
10. Dodawaj nowe Skills dopiero wtedy, gdy istnieją dowody ich praktycznego wykorzystania.

---

# Najważniejsza zasada

Skill nie opisuje tego, czego się nauczyłem.

Skill opisuje to, co potrafię udowodnić poprzez doświadczenie, osiągnięcia oraz powtarzalne rezultaty.

Jeżeli kompetencja nie posiada dowodów, nie powinna stanowić części Career Vault.

---

# Indeks rekordów

> **Sekcja generowana automatycznie** ze stanu Vaulta (commit `ac0d179`, 2026-07-11).
> Po dodaniu lub zmianie rekordu należy ją przegenerować — nie edytuj list ręcznie.

Łącznie: **20** kompetencji.

| ID | Nazwa | Kategoria | Poziom | Waga | Dowody (ACH) |
| --- | --- | --- | --- | --- | --- |
| `SKILL-001` | Process Design | Operations | Expert | 10 | 12 |
| `SKILL-002` | Operations Management | Operations | Advanced | 10 | 7 |
| `SKILL-003` | Knowledge Management | Knowledge | Expert | 10 | 6 |
| `SKILL-004` | Product Management | Product | Advanced | 10 | 10 |
| `SKILL-005` | Leadership | Management | Advanced | 8 | 9 |
| `SKILL-006` | Technical Documentation | Knowledge | Expert | 9 | 6 |
| `SKILL-007` | Training & Enablement | Knowledge | Advanced | 9 | 9 |
| `SKILL-008` | Business Systems | Systems | Advanced | 9 | 7 |
| `SKILL-009` | Workflow Automation | Systems | Advanced | 9 | 8 |
| `SKILL-010` | Service Operations | Operations | Advanced | 9 | 5 |
| `SKILL-011` | Stakeholder Management | Management | Advanced | 9 | 10 |
| `SKILL-012` | Change Management | Management | Advanced | 10 | 8 |
| `SKILL-013` | Public Speaking | Communication | Advanced | 8 | 4 |
| `SKILL-014` | Project Management | Management | Advanced | 8 | 6 |
| `SKILL-015` | Organizational Design | Operations | Advanced | 9 | 7 |
| `SKILL-016` | Operational Analysis | Analytics | Advanced | 8 | 7 |
| `SKILL-017` | Cross-Functional Facilitation | Communication | Advanced | 8 | 11 |
| `SKILL-018` | Persuasive Communication | Communication | Advanced | 8 | 1 |
| `SKILL-019` | Business Analysis & Requirements Engineering | Product & Business | Advanced | 8 | 5 |
| `SKILL-020` | AI Tooling & Automation | Systems | Advanced | 8 | 1 |

---

# Encje powiązane

> **Sekcja generowana automatycznie** ze stanu Vaulta (commit `ac0d179`, 2026-07-11).
> Po dodaniu lub zmianie rekordu należy ją przegenerować — nie edytuj list ręcznie.

Źródła powiązań:

* **Achievements** — pole `evidence` rekordu `SKILL-*` (powiązanie bezpośrednie),
* **Related skills** — pole `related_skills` rekordu `SKILL-*` (powiązanie bezpośrednie),
* **Development Areas** — pole `sources.skills` w rekordach `DEV-*` (dopasowanie po ID lub po nazwie kompetencji),
* **Stories** — powiązanie **wyliczone**: Story wskazujące Achievement, który jest dowodem tej kompetencji.

## Tabela zbiorcza

| ID | Nazwa | Achievements (dowody) | Related skills | Development Areas |
| --- | --- | --- | --- | --- |
| `SKILL-001` | Process Design | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-011` — Stworzenie systemu kalkulacji komponentów dla działu handlowego<br>`ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji<br>`ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji<br>`ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych<br>`ACH-017` — Stabilizacja kooperacji OEM i operacyjny business enablement<br>`ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego<br>`ACH-019` — Architektura procesu życia produktu - projekt modelu operacyjnego firmy produktowej<br>`ACH-021` — Hybrydowy model współpracy z podwykonawcami montażowymi | `SKILL-002` — Operations Management<br>`SKILL-003` — Knowledge Management<br>`SKILL-005` — Leadership | `DEV-003` — Delegation and Leverage<br>`DEV-004` — Commercial Discovery<br>`DEV-007` — Asymmetric Self-Valuation |
| `SKILL-002` | Operations Management | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-009` — Reorganizacja infrastruktury magazynowej i danych magazynowych w ERP<br>`ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych<br>`ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych<br>`ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji | `SKILL-001` — Process Design<br>`SKILL-005` — Leadership<br>`SKILL-011` — Stakeholder Management | `DEV-002` — Personal Capacity Management<br>`DEV-004` — Commercial Discovery |
| `SKILL-003` | Knowledge Management | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów<br>`ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji<br>`ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych | `SKILL-001` — Process Design<br>`SKILL-006` — Technical Documentation<br>`SKILL-007` — Training & Enablement | `DEV-003` — Delegation and Leverage<br>`DEV-005` — Assertiveness and Difficult Conversations<br>`DEV-006` — Boundary Management |
| `SKILL-004` | Product Management | `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów<br>`ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych<br>`ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji<br>`ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji<br>`ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych<br>`ACH-016` — Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami<br>`ACH-017` — Stabilizacja kooperacji OEM i operacyjny business enablement<br>`ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego | `SKILL-001` — Process Design<br>`SKILL-006` — Technical Documentation<br>`SKILL-011` — Stakeholder Management | `DEV-004` — Commercial Discovery<br>`DEV-007` — Asymmetric Self-Valuation |
| `SKILL-005` | Leadership | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów<br>`ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych<br>`ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych<br>`ACH-020` — Zbudowanie i prowadzenie procesów rekrutacyjnych dla ról technicznych<br>`ACH-P001` — Regularne prowadzenie wystąpień publicznych i koordynacja społeczności<br>`ACH-P002` — Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych<br>`ACH-P003` — Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia | — | `DEV-001` — Leadership Through Accountability<br>`DEV-006` — Boundary Management |
| `SKILL-006` | Technical Documentation | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji<br>`ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych | `SKILL-003` — Knowledge Management<br>`SKILL-004` — Product Management<br>`SKILL-007` — Training & Enablement | — |
| `SKILL-007` | Training & Enablement | `ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów<br>`ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych<br>`ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego<br>`ACH-020` — Zbudowanie i prowadzenie procesów rekrutacyjnych dla ról technicznych<br>`ACH-P001` — Regularne prowadzenie wystąpień publicznych i koordynacja społeczności<br>`ACH-P005` — Wieloletni wolontariat kaznodziejski — komunikacja perswazyjna w terenie i rezyliencja psychologiczna | `SKILL-003` — Knowledge Management<br>`SKILL-006` — Technical Documentation<br>`SKILL-013` — Public Speaking | — |
| `SKILL-008` | Business Systems | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-002` — Samodzielne opanowanie platformy Bitrix24 - od zera do projektanta automatyzacji<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-007` — Samodzielne wdrożenie systemu VOIP i infolinii<br>`ACH-009` — Reorganizacja infrastruktury magazynowej i danych magazynowych w ERP<br>`ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji | `SKILL-001` — Process Design<br>`SKILL-009` — Workflow Automation<br>`SKILL-010` — Service Operations | — |
| `SKILL-009` | Workflow Automation | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-002` — Samodzielne opanowanie platformy Bitrix24 - od zera do projektanta automatyzacji<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-007` — Samodzielne wdrożenie systemu VOIP i infolinii<br>`ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji<br>`ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych<br>`ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego | `SKILL-001` — Process Design<br>`SKILL-002` — Operations Management<br>`SKILL-008` — Business Systems | — |
| `SKILL-010` | Service Operations | `ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-007` — Samodzielne wdrożenie systemu VOIP i infolinii<br>`ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych<br>`ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych | `SKILL-001` — Process Design<br>`SKILL-002` — Operations Management<br>`SKILL-012` — Change Management | — |
| `SKILL-011` | Stakeholder Management | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów<br>`ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych<br>`ACH-016` — Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami<br>`ACH-017` — Stabilizacja kooperacji OEM i operacyjny business enablement<br>`ACH-021` — Hybrydowy model współpracy z podwykonawcami montażowymi<br>`ACH-P002` — Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych | `SKILL-004` — Product Management<br>`SKILL-005` — Leadership<br>`SKILL-007` — Training & Enablement | `DEV-001` — Leadership Through Accountability<br>`DEV-004` — Commercial Discovery<br>`DEV-005` — Assertiveness and Difficult Conversations<br>`DEV-006` — Boundary Management |
| `SKILL-012` | Change Management | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych<br>`ACH-017` — Stabilizacja kooperacji OEM i operacyjny business enablement<br>`ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego | `SKILL-001` — Process Design<br>`SKILL-002` — Operations Management<br>`SKILL-005` — Leadership<br>`SKILL-015` — Organizational Design | — |
| `SKILL-013` | Public Speaking | `ACH-P001` — Regularne prowadzenie wystąpień publicznych i koordynacja społeczności<br>`ACH-P002` — Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych<br>`ACH-P003` — Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia<br>`ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów | `SKILL-007` — Training & Enablement<br>`SKILL-011` — Stakeholder Management | — |
| `SKILL-014` | Project Management | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-P002` — Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych<br>`ACH-P003` — Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia | `SKILL-005` — Leadership<br>`SKILL-011` — Stakeholder Management<br>`SKILL-012` — Change Management | — |
| `SKILL-015` | Organizational Design | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych<br>`ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych<br>`ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych | `SKILL-002` — Operations Management<br>`SKILL-005` — Leadership<br>`SKILL-012` — Change Management | — |
| `SKILL-016` | Operational Analysis | `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych<br>`ACH-011` — Stworzenie systemu kalkulacji komponentów dla działu handlowego<br>`ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych<br>`ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych<br>`ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych | `SKILL-001` — Process Design<br>`SKILL-002` — Operations Management<br>`SKILL-015` — Organizational Design | — |
| `SKILL-017` | Cross-Functional Facilitation | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów<br>`ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych<br>`ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych<br>`ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji<br>`ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji<br>`ACH-P001` — Regularne prowadzenie wystąpień publicznych i koordynacja społeczności<br>`ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych | `SKILL-003` — Knowledge Management<br>`SKILL-005` — Leadership<br>`SKILL-007` — Training & Enablement<br>`SKILL-011` — Stakeholder Management<br>`SKILL-015` — Organizational Design | `DEV-005` — Assertiveness and Difficult Conversations<br>`DEV-006` — Boundary Management |
| `SKILL-018` | Persuasive Communication | `ACH-P005` — Wieloletni wolontariat kaznodziejski — komunikacja perswazyjna w terenie i rezyliencja psychologiczna | `SKILL-013` — Public Speaking<br>`SKILL-011` — Stakeholder Management<br>`SKILL-017` — Cross-Functional Facilitation | — |
| `SKILL-019` | Business Analysis & Requirements Engineering | `ACH-016` — Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami<br>`ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego<br>`ACH-011` — Stworzenie systemu kalkulacji komponentów dla działu handlowego<br>`ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych<br>`ACH-019` — Architektura procesu życia produktu - projekt modelu operacyjnego firmy produktowej | — | `DEV-007` — Asymmetric Self-Valuation |
| `SKILL-020` | AI Tooling & Automation | `ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych | — | — |

## Rozwinięcie per rekord

### `SKILL-001` — Process Design

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-011` — Stworzenie systemu kalkulacji komponentów dla działu handlowego
  - `ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji
  - `ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji
  - `ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych
  - `ACH-017` — Stabilizacja kooperacji OEM i operacyjny business enablement
  - `ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego
  - `ACH-019` — Architektura procesu życia produktu - projekt modelu operacyjnego firmy produktowej
  - `ACH-021` — Hybrydowy model współpracy z podwykonawcami montażowymi
* **Related skills:**
  - `SKILL-002` — Operations Management
  - `SKILL-003` — Knowledge Management
  - `SKILL-005` — Leadership
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-007` — Standaryzacja ofertowania i kalkulacji rentowności instalacji PV
* **Development Areas:**
  - `DEV-003` — Delegation and Leverage
  - `DEV-004` — Commercial Discovery
  - `DEV-007` — Asymmetric Self-Valuation

### `SKILL-002` — Operations Management

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box
  - `ACH-009` — Reorganizacja infrastruktury magazynowej i danych magazynowych w ERP
  - `ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych
  - `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych
  - `ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji
* **Related skills:**
  - `SKILL-001` — Process Design
  - `SKILL-005` — Leadership
  - `SKILL-011` — Stakeholder Management
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-006` — Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewności
  - `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV
  - `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym
* **Development Areas:**
  - `DEV-002` — Personal Capacity Management
  - `DEV-004` — Commercial Discovery

### `SKILL-003` — Knowledge Management

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów
  - `ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji
  - `ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych
* **Related skills:**
  - `SKILL-001` — Process Design
  - `SKILL-006` — Technical Documentation
  - `SKILL-007` — Training & Enablement
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
* **Development Areas:**
  - `DEV-003` — Delegation and Leverage
  - `DEV-005` — Assertiveness and Difficult Conversations
  - `DEV-006` — Boundary Management

### `SKILL-004` — Product Management

* **Achievements (dowody):**
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów
  - `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box
  - `ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych
  - `ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji
  - `ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji
  - `ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych
  - `ACH-016` — Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami
  - `ACH-017` — Stabilizacja kooperacji OEM i operacyjny business enablement
  - `ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego
* **Related skills:**
  - `SKILL-001` — Process Design
  - `SKILL-006` — Technical Documentation
  - `SKILL-011` — Stakeholder Management
* **Stories (wyliczone przez ACH):**
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
* **Development Areas:**
  - `DEV-004` — Commercial Discovery
  - `DEV-007` — Asymmetric Self-Valuation

### `SKILL-005` — Leadership

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów
  - `ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych
  - `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych
  - `ACH-020` — Zbudowanie i prowadzenie procesów rekrutacyjnych dla ról technicznych
  - `ACH-P001` — Regularne prowadzenie wystąpień publicznych i koordynacja społeczności
  - `ACH-P002` — Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych
  - `ACH-P003` — Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia
* **Related skills:**
  - _brak_
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV
  - `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym
* **Development Areas:**
  - `DEV-001` — Leadership Through Accountability
  - `DEV-006` — Boundary Management

### `SKILL-006` — Technical Documentation

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box
  - `ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji
  - `ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych
* **Related skills:**
  - `SKILL-003` — Knowledge Management
  - `SKILL-004` — Product Management
  - `SKILL-007` — Training & Enablement
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
* **Development Areas:**
  - _brak_

### `SKILL-007` — Training & Enablement

* **Achievements (dowody):**
  - `ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów
  - `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych
  - `ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego
  - `ACH-020` — Zbudowanie i prowadzenie procesów rekrutacyjnych dla ról technicznych
  - `ACH-P001` — Regularne prowadzenie wystąpień publicznych i koordynacja społeczności
  - `ACH-P005` — Wieloletni wolontariat kaznodziejski — komunikacja perswazyjna w terenie i rezyliencja psychologiczna
* **Related skills:**
  - `SKILL-003` — Knowledge Management
  - `SKILL-006` — Technical Documentation
  - `SKILL-013` — Public Speaking
* **Stories (wyliczone przez ACH):**
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV
  - `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym
* **Development Areas:**
  - _brak_

### `SKILL-008` — Business Systems

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-002` — Samodzielne opanowanie platformy Bitrix24 - od zera do projektanta automatyzacji
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-007` — Samodzielne wdrożenie systemu VOIP i infolinii
  - `ACH-009` — Reorganizacja infrastruktury magazynowej i danych magazynowych w ERP
  - `ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji
* **Related skills:**
  - `SKILL-001` — Process Design
  - `SKILL-009` — Workflow Automation
  - `SKILL-010` — Service Operations
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-006` — Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewności
* **Development Areas:**
  - _brak_

### `SKILL-009` — Workflow Automation

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-002` — Samodzielne opanowanie platformy Bitrix24 - od zera do projektanta automatyzacji
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-007` — Samodzielne wdrożenie systemu VOIP i infolinii
  - `ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji
  - `ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych
  - `ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego
* **Related skills:**
  - `SKILL-001` — Process Design
  - `SKILL-002` — Operations Management
  - `SKILL-008` — Business Systems
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
* **Development Areas:**
  - _brak_

### `SKILL-010` — Service Operations

* **Achievements (dowody):**
  - `ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-007` — Samodzielne wdrożenie systemu VOIP i infolinii
  - `ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych
  - `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych
* **Related skills:**
  - `SKILL-001` — Process Design
  - `SKILL-002` — Operations Management
  - `SKILL-012` — Change Management
* **Stories (wyliczone przez ACH):**
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV
  - `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym
* **Development Areas:**
  - _brak_

### `SKILL-011` — Stakeholder Management

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów
  - `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box
  - `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych
  - `ACH-016` — Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami
  - `ACH-017` — Stabilizacja kooperacji OEM i operacyjny business enablement
  - `ACH-021` — Hybrydowy model współpracy z podwykonawcami montażowymi
  - `ACH-P002` — Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych
* **Related skills:**
  - `SKILL-004` — Product Management
  - `SKILL-005` — Leadership
  - `SKILL-007` — Training & Enablement
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV
  - `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym
* **Development Areas:**
  - `DEV-001` — Leadership Through Accountability
  - `DEV-004` — Commercial Discovery
  - `DEV-005` — Assertiveness and Difficult Conversations
  - `DEV-006` — Boundary Management

### `SKILL-012` — Change Management

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box
  - `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych
  - `ACH-017` — Stabilizacja kooperacji OEM i operacyjny business enablement
  - `ACH-018` — Wdrożenie lejków sprzedażowych z e-podpisem dla działu handlowego
* **Related skills:**
  - `SKILL-001` — Process Design
  - `SKILL-002` — Operations Management
  - `SKILL-005` — Leadership
  - `SKILL-015` — Organizational Design
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV
  - `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym
* **Development Areas:**
  - _brak_

### `SKILL-013` — Public Speaking

* **Achievements (dowody):**
  - `ACH-P001` — Regularne prowadzenie wystąpień publicznych i koordynacja społeczności
  - `ACH-P002` — Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych
  - `ACH-P003` — Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia
  - `ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów
* **Related skills:**
  - `SKILL-007` — Training & Enablement
  - `SKILL-011` — Stakeholder Management
* **Stories (wyliczone przez ACH):**
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
* **Development Areas:**
  - _brak_

### `SKILL-014` — Project Management

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box
  - `ACH-P002` — Organizacja wielodniowych wydarzeń społecznościowych i ekspedycji terenowych
  - `ACH-P003` — Kompleksowa organizacja zaręczyn, wesela i oprawy wydarzenia
* **Related skills:**
  - `SKILL-005` — Leadership
  - `SKILL-011` — Stakeholder Management
  - `SKILL-012` — Change Management
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
* **Development Areas:**
  - _brak_

### `SKILL-015` — Organizational Design

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-003` — Stworzenie bazy wiedzy serwisowej BPMN 2.0
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box
  - `ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych
  - `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych
  - `ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych
* **Related skills:**
  - `SKILL-002` — Operations Management
  - `SKILL-005` — Leadership
  - `SKILL-012` — Change Management
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV
  - `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym
* **Development Areas:**
  - _brak_

### `SKILL-016` — Operational Analysis

* **Achievements (dowody):**
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych
  - `ACH-011` — Stworzenie systemu kalkulacji komponentów dla działu handlowego
  - `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych
  - `ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych
  - `ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych
* **Related skills:**
  - `SKILL-001` — Process Design
  - `SKILL-002` — Operations Management
  - `SKILL-015` — Organizational Design
* **Stories (wyliczone przez ACH):**
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-007` — Standaryzacja ofertowania i kalkulacji rentowności instalacji PV
  - `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV
  - `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym
* **Development Areas:**
  - _brak_

### `SKILL-017` — Cross-Functional Facilitation

* **Achievements (dowody):**
  - `ACH-001` — Transformacja działu Instal/Solar
  - `ACH-004` — Restrukturyzacja i stabilizacja działu serwisu
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów
  - `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box
  - `ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych
  - `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zmian organizacyjnych
  - `ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji
  - `ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji
  - `ACH-P001` — Regularne prowadzenie wystąpień publicznych i koordynacja społeczności
  - `ACH-P004` — Projektowanie systemów organizacyjnych, baz wiedzy i narzędzi informacyjnych
* **Related skills:**
  - `SKILL-003` — Knowledge Management
  - `SKILL-005` — Leadership
  - `SKILL-007` — Training & Enablement
  - `SKILL-011` — Stakeholder Management
  - `SKILL-015` — Organizational Design
* **Stories (wyliczone przez ACH):**
  - `STORY-001` — Transformacja organizacji pracy działu Instal/Solar
  - `STORY-002` — Restrukturyzacja i stabilizacja działu serwisu
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych
  - `STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - `STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV
  - `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym
* **Development Areas:**
  - `DEV-005` — Assertiveness and Difficult Conversations
  - `DEV-006` — Boundary Management

### `SKILL-018` — Persuasive Communication

* **Achievements (dowody):**
  - `ACH-P005` — Wieloletni wolontariat kaznodziejski — komunikacja perswazyjna w terenie i rezyliencja psychologiczna
* **Related skills:**
  - `SKILL-013` — Public Speaking
  - `SKILL-011` — Stakeholder Management
  - `SKILL-017` — Cross-Functional Facilitation
* **Stories (wyliczone przez ACH):**
  - _brak_
* **Development Areas:**
  - _brak_

### `SKILL-019` — Business Analysis & Requirements Engineering

* **Achievements (dowody):**
  - `ACH-016` — Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymaganiami
  - `ACH-005` — Zaprojektowanie i wdrożenie systemu gwarancyjnego
  - `ACH-011` — Stworzenie systemu kalkulacji komponentów dla działu handlowego
  - `ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych
  - `ACH-019` — Architektura procesu życia produktu - projekt modelu operacyjnego firmy produktowej
* **Related skills:**
  - _brak_
* **Stories (wyliczone przez ACH):**
  - `STORY-003` — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - `STORY-007` — Standaryzacja ofertowania i kalkulacji rentowności instalacji PV
* **Development Areas:**
  - `DEV-007` — Asymmetric Self-Valuation

### `SKILL-020` — AI Tooling & Automation

* **Achievements (dowody):**
  - `ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów seryjnych
* **Pozostałe dowody (spoza modułu Achievements):**
  - certyfikat Umiejętności Jutra AI 3.0
  - Career Vault (repozytorium w którym jest ten plik)
* **Related skills:**
  - _brak_
* **Stories (wyliczone przez ACH):**
  - _brak_
* **Development Areas:**
  - _brak_

---

# Luki w powiązaniach

> **Sekcja generowana automatycznie** ze stanu Vaulta (commit `ac0d179`, 2026-07-11).
> Po dodaniu lub zmianie rekordu należy ją przegenerować — nie edytuj list ręcznie.

## Dowody spoza modułu Achievements

Pole `evidence` powinno wskazywać identyfikatory `ACH-*`. Wpisy opisowe nie są policzalne jako dowód:

* `SKILL-020` (AI Tooling & Automation) — "certyfikat Umiejętności Jutra AI 3.0"
* `SKILL-020` (AI Tooling & Automation) — "Career Vault (repozytorium w którym jest ten plik)"

## Etykiety w `DEV-*.sources.skills` bez rekordu SKILL

Nazwy użyte w Development Areas, którym nie odpowiada żadna kompetencja w tym module — do ujednolicenia (mapowanie na istniejące `SKILL-*` albo utworzenie rekordu):

* "Team Management" — użyte w `DEV-001`
* "Conflict Resolution" — użyte w `DEV-001`
* "Ownership" — użyte w `DEV-002`
* "Problem Solving" — użyte w `DEV-002`
* "Organizational Analysis" — użyte w `DEV-002`
* "Systems Thinking" — użyte w `DEV-003`
* "Operational Leadership" — użyte w `DEV-003`

## Niespójność formatu referencji

Rekordy `DEV-001` – `DEV-004` wskazują kompetencje nazwami (np. "Leadership", "product-management"),
a `DEV-005` – `DEV-007` identyfikatorami (`SKILL-017`). Powiązania powyżej dopasowano po obu formach —
docelowo warto ujednolicić do identyfikatorów.
