# Skills

## Cel

Folder **Skills** zawiera kompetencje zidentyfikowane na podstawie doświadczenia, osiągnięć i projektów opisanych w Career Vault.

Skills nie są listą deklarowanych umiejętności.

Każda kompetencja powinna być poparta konkretnymi dowodami znajdującymi się w Achievementach.

---

# Rola Skills w Career Vault

Career Vault składa się z pięciu warstw:

```text
Identity
↓
Kim jestem?

Experience
↓
Gdzie zdobyłem doświadczenie?

Achievements
↓
Co osiągnąłem?

Skills
↓
Co potrafię?

Stories
↓
Jak o tym opowiadać?
```

Skills stanowią warstwę pośrednią pomiędzy osiągnięciami a dokumentami końcowymi takimi jak CV, profile zawodowe czy przygotowanie do rozmów kwalifikacyjnych.

---

# Czym jest Skill?

Skill opisuje kompetencję możliwą do zaobserwowania poprzez działania i rezultaty.

Przykład:

❌ „Znam BPMN”

To wiedza o narzędziu.

✅ „Projektowanie procesów”

To kompetencja.

---

Przykład:

❌ „Umiem Bitrix24”

To znajomość systemu.

✅ „Workflow Automation”

To kompetencja.

---

# Fakty ponad deklaracje

Każdy skill powinien posiadać powiązane achievementy potwierdzające jego istnienie.

Przykład:

```yaml
name: Process Design

evidence:
  - ACH-001
  - ACH-003
  - ACH-005
```

Jeżeli nie istnieją achievementy potwierdzające daną kompetencję, prawdopodobnie nie powinna ona jeszcze znajdować się w Career Vault.

---

# Struktura pliku

Każdy skill powinien być zapisany jako osobny plik YAML.

Przykład:

```yaml
id: SKILL-001

name: Process Design

category: Operations

importance: 10

level: Expert

summary: >
  Krótki opis kompetencji.

capabilities:
  - capability-1
  - capability-2

methods:
  - method-1
  - method-2

tools:
  - tool-1
  - tool-2

evidence:
  - ACH-001
  - ACH-003

experience:
  first_used: 2020
  years: 5

career_relevance:
  product_manager: 8
  operations_manager: 10

keywords:
  - process design

related_skills:
  - SKILL-002
```

---

# Poziomy kompetencji

## Expert

Kompetencja regularnie wykorzystywana w praktyce, potwierdzona wieloma achievementami i wieloletnim doświadczeniem.

---

## Advanced

Kompetencja wykorzystywana samodzielnie w złożonych sytuacjach i potwierdzona kilkoma achievementami.

---

## Intermediate

Kompetencja wykorzystywana okazjonalnie lub w ograniczonym zakresie.

---

## Basic

Podstawowa znajomość obszaru bez istotnych dowodów doświadczenia.

---

# Importance

Pole `importance` określa, jak bardzo dana kompetencja definiuje profil zawodowy.

Nie określa poziomu umiejętności.

Przykład:

Można posiadać kompetencję na poziomie Expert, która nie jest kluczowa dla kariery zawodowej.

---

## 10

Kompetencja rdzeniowa.

Definiuje profil zawodowy.

---

## 8–9

Bardzo ważna kompetencja wspierająca.

Regularnie wykorzystywana w pracy.

---

## 6–7

Kompetencja specjalistyczna lub sytuacyjna.

---

## 1–5

Kompetencja pomocnicza.

---

# Rodzaje informacji

## Skills

Opisują kompetencje.

Przykłady:

* Process Design
* Product Management
* Leadership
* Knowledge Management

---

## Methods

Opisują metody pracy.

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

## Achievements

Stanowią dowody wykorzystania kompetencji.

---

# Relacja do pozostałych elementów Career Vault

## Identity

Opisuje profil zawodowy.

## Experience

Opisuje historię zawodową.

## Achievements

Dostarczają dowodów.

## Skills

Grupują dowody w kompetencje.

## Stories

Pokazują wykorzystanie kompetencji w praktyce.

---

# Zasady utrzymania

1. Każdy skill powinien posiadać achievementy potwierdzające jego istnienie.
2. Nie twórz skilli dla pojedynczych narzędzi.
3. Nie twórz skilli dla pojedynczych technologii.
4. Preferuj kompetencje zamiast technologii.
5. Łącz skille z achievementami.
6. Łącz skille z innymi skillami.
7. Aktualizuj kompetencje wraz z rozwojem Career Vault.

---

# Najważniejsza zasada

Skill nie opisuje tego, czego się nauczyłem.

Skill opisuje to, co potrafię udowodnić.
