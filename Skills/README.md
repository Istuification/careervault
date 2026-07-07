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
