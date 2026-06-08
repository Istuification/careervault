# Skills

## Cel

Folder **Skills** zawiera kompetencje zidentyfikowane na podstawie doświadczenia, osiągnięć oraz projektów zgromadzonych w Career Vault.

Skills nie są listą deklarowanych umiejętności.

Każda kompetencja powinna być poparta konkretnymi achievementami, które stanowią dowód jej praktycznego wykorzystania.

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

Skills stanowią warstwę pośrednią pomiędzy osiągnięciami a dokumentami końcowymi takimi jak CV, profile zawodowe, analizy kompetencji czy przygotowanie do rozmów kwalifikacyjnych.

---

# Czym jest Skill?

Skill opisuje kompetencję możliwą do zaobserwowania poprzez działania i rezultaty.

Przykład:

❌ „Znam BPMN”

To znajomość metody.

✅ „Process Design”

To kompetencja.

---

Przykład:

❌ „Umiem Bitrix24”

To znajomość narzędzia.

✅ „Workflow Automation”

To kompetencja.

---

Przykład:

❌ „Znam Excel”

To znajomość narzędzia.

✅ „Data Analysis”

To kompetencja.

---

# Fakty ponad deklaracje

Każdy Skill powinien posiadać powiązane achievementy potwierdzające jego wykorzystanie.

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

Definiuje profil zawodowy.

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

Kompetencja wykorzystywana regularnie przez wiele lat i potwierdzona licznymi achievementami.

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

Lista umiejętności składających się na daną kompetencję.

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

Achievementy potwierdzające kompetencję.

Przykład:

```yaml
evidence:
  - ACH-001
  - ACH-003
  - ACH-005
```

To najważniejsze pole całego rekordu.

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

# Rodzaje informacji

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

Grupują osiągnięcia w kompetencje.

## Stories

Pokazują wykorzystanie kompetencji w praktyce.

---

# Zasady utrzymania

1. Każdy Skill powinien posiadać achievementy potwierdzające jego wykorzystanie.
2. Nie twórz Skilli dla pojedynczych narzędzi.
3. Nie twórz Skilli dla pojedynczych technologii.
4. Preferuj kompetencje zamiast technologii.
5. Łącz Skills z Achievementami.
6. Łącz Skills z innymi Skills.
7. Aktualizuj kompetencje wraz z rozwojem Career Vault.
8. Dodawaj nowe Skills dopiero wtedy, gdy istnieją dowody ich praktycznego wykorzystania.

---

# Najważniejsza zasada

Skill nie opisuje tego, czego się nauczyłem.

Skill opisuje to, co potrafię udowodnić poprzez osiągnięcia.
