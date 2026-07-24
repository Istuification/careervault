# Development Areas

## Cel

Folder **Development Areas** zawiera uporządkowane obszary rozwoju zawodowego wynikające z rzeczywistych doświadczeń, obserwacji i powtarzalnych wzorców zachowań.

Development Areas nie są listą wad ani cech osobistych.
Nie są też ogólnymi deklaracjami typu „muszę lepiej zarządzać czasem” bez dowodów w danych.

Ich zadaniem jest pokazanie:

* jakie wzorce pojawiają się powtarzalnie,
* jakie ryzyka lub ograniczenia z nich wynikają,
* jakie mocne strony temu towarzyszą,
* nad czym świadomie pracuję dalej.

---

## Rola w Career Vault

Career Vault składa się z kilku warstw:

```text
Identity
↓
Kim jestem zawodowo?

Experience
↓
Gdzie zdobyłem doświadczenie?

Achievements
↓
Co osiągnąłem?

Skills
↓
Jakie kompetencje pokazują te osiągnięcia?

Stories
↓
Jak o tym opowiadać?

Development Areas
↓
Nad czym świadomie pracuję?
```

Development Areas są warstwą refleksyjną i rozwojową.

Uzupełniają Identity, ale nie są jej częścią.

---

## Zasada tworzenia

Każdy Development Area powinien:

* wynikać z rzeczywistych Story, Achievements lub innych dowodów,
* opisywać powtarzalny wzorzec, a nie pojedynczy incydent,
* zawierać zarówno mocne strony, jak i ryzyka,
* wskazywać wnioski i aktualny kierunek rozwoju,
* być na tyle konkretny, aby można go było wykorzystać w rozmowie rekrutacyjnej lub rozwojowej.

Development Area powinien odpowiadać na pytanie:

> Jakie wzorce obserwuję u siebie i nad czym świadomie pracuję?

---

## Kiedy tworzyć Development Area

Twórz Development Area wtedy, gdy:

* ten sam wzorzec pojawia się w wielu sytuacjach,
* wpływa na sposób pracy lub wyniki,
* prowadzi do powtarzalnych konsekwencji,
* został rozpoznany i nazwany świadomie,
* ma znaczenie dla dalszego rozwoju zawodowego.

Nie twórz Development Area dla:

* pojedynczego błędu,
* chwilowej trudności,
* cechy niemającej znaczenia zawodowego,
* ogólnej samooceny bez dowodów.

---

## Struktura rekordu

Każdy Development Area powinien być zapisany jako osobny plik YAML.

```yaml
id:
title:
summary:

category:
status:

sources:
  stories:
    -
  achievements:
    -
  skills:
    -

observed_pattern:
  -

strengths:
  -

risks:
  -

evidence:
  -

root_cause_analysis:
  assumption:
  reality:

key_realizations:
  -

current_approach:
  -

development_goal:
  >

interview_usage:
  strengths_questions:
    -
  weakness_questions:
    -
  growth_questions:
    -
```

---

## Opis pól

### `id`

Unikalny identyfikator Development Area.

Przykład:

```yaml
id: DEV-001
```

Powinien być stabilny i niezmienny.

---

### `title`

Krótka nazwa obszaru rozwoju.

Powinna być konkretna i opisywać wzorzec, np.:

* Leadership Through Accountability
* Personal Capacity Management
* Delegation and Leverage
* Commercial Discovery

---

### `summary`

Zwięzły opis obszaru rozwoju.

Powinien odpowiadać na pytanie:

> Jaki wzorzec obserwuję i dlaczego jest to istotne?

---

### `category`

Główna kategoria obszaru rozwoju.

Przykłady:

* Leadership
* Self Management
* Product & Business
* Communication
* Operations

---

### `status`

Status rozwoju.

Przykłady:

* Active Development
* Emerging Development Area
* Stable
* Needs More Evidence

---

### `sources`

Źródła, na których opiera się Development Area.

Powinny obejmować:

* Stories
* Achievements
* Skills

Development Area nie powinien istnieć bez źródeł.

---

### `observed_pattern`

Opis powtarzalnego wzorca zachowania lub decyzji.

To najważniejsza część Development Area.

---

### `strengths`

Mocne strony związane z tym wzorcem.

Development Area nie ma opisywać wyłącznie słabości.

Powinien pokazywać również to, co działa dobrze.

---

### `risks`

Ryzyka, ograniczenia lub koszty uboczne wynikające z danego wzorca.

---

### `evidence`

Konkrety potwierdzające, że ten wzorzec rzeczywiście występuje.

Mogą to być:

* wydarzenia,
* decyzje,
* skutki,
* obserwacje,
* powiązane Stories.

---

### `root_cause_analysis`

Krótka analiza przyczyny wzorca.

Powinna pokazywać:

* jakie było pierwotne założenie,
* jak wyglądała rzeczywistość,
* skąd wzięła się zmiana w myśleniu.

---

### `key_realizations`

Najważniejsze wnioski wynikające z doświadczenia.

---

### `current_approach`

Jak obecnie pracuję z tym wzorcem.

To pole pokazuje, że Development Area nie jest tylko diagnozą, ale także świadomym kierunkiem działania.

---

### `development_goal`

Kierunek dalszego rozwoju.

Powinien być konkretny i praktyczny.

---

### `interview_usage`

Zakres pytań rekrutacyjnych, do których Development Area może być użyty.

Pomaga AI dopasować go do pytań o:

* słabe strony,
* styl pracy,
* rozwój,
* błędy,
* samoświadomość.

---

## Zasady jakości

1. Jeden Development Area = jeden spójny wzorzec.
2. Development Area musi mieć źródła.
3. Development Area musi opisywać coś powtarzalnego.
4. Nie wpisuj tu ogólnych haseł bez dowodów.
5. Nie myl Development Areas z Identity.
6. Nie myl Development Areas z pojedynczymi Stories.
7. Zapisuj zarówno mocne strony, jak i ryzyka.
8. Preferuj jakość nad liczbę.

Lista Development Areas może być rozwijana, ale tylko wtedy, gdy pojawi się nowy, powtarzalny wzorzec potwierdzony w Career Vault.

---

<!-- VAULT:GENERATED:START -->
# Indeks rekordów

> **Sekcja generowana automatycznie** ze stanu Vaulta (`scripts/render_readmes.py`).
> Nie edytuj recznie — zmiany wprowadzaj w rekordach i przegeneruj.

Łącznie: **7** obszarów rozwoju.

| ID | Tytuł | Kategoria | Status |
| --- | --- | --- | --- |
| `DEV-001` | Leadership Through Accountability | Leadership | Active Development |
| `DEV-002` | Personal Capacity Management | Self Management | Active Development |
| `DEV-003` | Delegation and Leverage | Leadership | Active Development |
| `DEV-004` | Commercial Discovery | Product & Business | Emerging Development Area |
| `DEV-005` | Assertiveness and Difficult Conversations | Communication | Active Development |
| `DEV-006` | Boundary Management | Self Management | Active Development |
| `DEV-007` | Asymmetric Self-Valuation | Self Management | Active Development (Fresh Awareness) |

---

# Encje powiązane

> **Sekcja generowana automatycznie** ze stanu Vaulta (`scripts/render_readmes.py`).
> Nie edytuj recznie — zmiany wprowadzaj w rekordach i przegeneruj.

Źródłem powiązań jest pole `sources` rekordu `DEV-*`. Development Area bez źródeł nie powinien istnieć.

| ID | Tytuł | Achievements | Stories | Skills |
| --- | --- | --- | --- | --- |
| `DEV-001` | Leadership Through Accountability | `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zm… | `STORY-009` — Budowa zespołu serwisowego po kryzysie kadrowym | `SKILL-005` — Leadership<br>`SKILL-011` — Stakeholder Management |
| `DEV-002` | Personal Capacity Management | `ACH-012` — Utrzymanie kluczowych ekspertów i jakości obsługi w okresie dużych zm… | `STORY-001` — Transformacja organizacji pracy działu Instal/Solar<br>`STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych<br>`STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej<br>`STORY-007` — Standaryzacja ofertowania i kalkulacji rentowności instalacji PV<br>`STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV | `SKILL-002` — Operations Management |
| `DEV-003` | Delegation and Leverage | — | `STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych<br>`STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej<br>`STORY-006` — Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewn…<br>`STORY-007` — Standaryzacja ofertowania i kalkulacji rentowności instalacji PV<br>`STORY-008` — Zatrzymanie niekontrolowanego skalowania operacji PV | `SKILL-001` — Process Design<br>`SKILL-003` — Knowledge Management<br>`SKILL-021` — Systems Thinking |
| `DEV-004` | Commercial Discovery | `ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-011` — Stworzenie systemu kalkulacji komponentów dla działu handlowego<br>`ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji<br>`ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji | `STORY-006` — Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewn… | `SKILL-004` — Product Management<br>`SKILL-011` — Stakeholder Management<br>`SKILL-002` — Operations Management<br>`SKILL-001` — Process Design |
| `DEV-005` | Assertiveness and Difficult Conversations | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów<br>`ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych<br>`ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji | `STORY-001` — Transformacja organizacji pracy działu Instal/Solar<br>`STORY-002` — Restrukturyzacja i stabilizacja działu serwisu<br>`STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych<br>`STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej<br>`STORY-006` — Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewn… | `SKILL-017` — Cross-Functional Facilitation<br>`SKILL-011` — Stakeholder Management<br>`SKILL-003` — Knowledge Management |
| `DEV-006` | Boundary Management | `ACH-001` — Transformacja działu Instal/Solar<br>`ACH-004` — Restrukturyzacja i stabilizacja działu serwisu<br>`ACH-006` — Stworzenie i przeprowadzenie programu szkoleń dla partnerów i klientów<br>`ACH-008` — Koordynacja wdrożenia produktów PV Stand i PV-Box<br>`ACH-010` — Projektowanie organizacji na podstawie analizy danych operacyjnych<br>`ACH-013` — Rozwój i administracja ekosystemu systemów operacyjnych organizacji<br>`ACH-014` — Budowa standardów dokumentacyjnych wspierających rozwój organizacji | `STORY-001` — Transformacja organizacji pracy działu Instal/Solar<br>`STORY-002` — Restrukturyzacja i stabilizacja działu serwisu<br>`STORY-004` — Projektowanie modelu działania serwisu przy braku danych historycznych<br>`STORY-005` — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej<br>`STORY-006` — Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewn… | `SKILL-017` — Cross-Functional Facilitation<br>`SKILL-003` — Knowledge Management<br>`SKILL-005` — Leadership<br>`SKILL-011` — Stakeholder Management |
| `DEV-007` | Asymmetric Self-Valuation | `ACH-015` — Wdrożenie systemu paszportyzacji produktów i kodyfikacji numerów sery…<br>`ACH-016` — Zunifikowanie architektury ekosystemu aplikacji i zarządzanie wymagan…<br>`ACH-019` — Architektura procesu życia produktu - projekt modelu operacyjnego fir… | `STORY-010` — Paszportyzacja produktów - od chaosu numerów seryjnych do fundamentu…<br>`STORY-011` — Stabilizacja kooperacji OEM i granica między ugaszeniem pożaru a ułoż… | `SKILL-001` — Process Design<br>`SKILL-019` — Business Analysis & Requirements Engineering<br>`SKILL-004` — Product Management |

---

# Luki w powiązaniach

> **Sekcja generowana automatycznie** ze stanu Vaulta (`scripts/render_readmes.py`).
> Nie edytuj recznie — zmiany wprowadzaj w rekordach i przegeneruj.

## Obszary bez źródeł dowodowych

_Brak — każdy obszar wskazuje Achievement lub Story._
<!-- VAULT:GENERATED:END -->
