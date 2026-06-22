# Behavioral Patterns

## Cel dokumentu

Behavioral Patterns są drugą warstwą interpretacyjną Cognitive Model.

Ich zadaniem jest identyfikacja powtarzalnych wzorców zachowań występujących w rzeczywistych sytuacjach.

Behavioral Pattern nie opisuje pojedynczego mechanizmu.

Behavioral Pattern nie jest również teorią wyjaśniającą działanie badanego.

Stanowi uporządkowany opis zachowania, które wielokrotnie pojawia się w niezależnych Stories.

Behavioral Patterns stanowią pomost pomiędzy Predictorami a Cognitive Model.

---

## Miejsce w architekturze Vault

```text
Assessment Data      Stories
        ↓               ↓
          Calibration
                ↓
           Predictors
                ↓
      Behavioral Patterns
                ↓
         Cognitive Model
```

Assessment Data dostarczają danych pomiarowych.

Stories dostarczają obserwacji zachowań.

Calibration integruje oba źródła.

Predictors opisują pojedyncze mechanizmy.

Behavioral Patterns opisują powtarzalne zachowania obserwowane w rzeczywistości.

Cognitive Model wyjaśnia, dlaczego te wzorce występują.

---

## Czym jest Behavioral Pattern?

Behavioral Pattern jest powtarzalnym wzorcem działania zaobserwowanym w wielu niezależnych Stories.

Behavioral Pattern powinien odpowiadać na pytanie:

> Co badany regularnie robi?

Przykłady:

* Operational Transformation Under Ambiguity
* Knowledge Externalization as Scaling Mechanism
* Influence Without Formal Authority
* Cross-Functional Facilitation and Alignment
* Evidence-Based Organizational Diagnosis

Behavioral Pattern powinien opisywać zachowanie.

Nie powinien opisywać cechy osobowości.

Nie powinien opisywać pojedynczego mechanizmu poznawczego.

---

## Źródła Behavioral Patterns

Behavioral Patterns są budowane na podstawie:

* Predictorów,
* powtarzalnych wzorców występujących w Stories,
* wcześniejszych kalibracji.

Behavioral Pattern nie powinien być tworzony wyłącznie na podstawie Assessment Data.

Behavioral Pattern nie powinien być tworzony na podstawie pojedynczej Story.

Do utworzenia Behavioral Pattern wymagane są wielokrotne obserwacje podobnego zachowania.

---

## Rola Behavioral Patterns

Behavioral Patterns odpowiadają na pytanie:

> Jak mechanizmy opisane przez Predictors manifestują się w rzeczywistości?

Przykład:

```text
Predictors

- Model-Centric Decision Making
- Systemic Problem Structuring
- Evidence-Driven Belief Updating

↓

Behavioral Pattern

Evidence-Based Organizational Diagnosis
```

Predictors opisują potencjalne mechanizmy.

Behavioral Pattern opisuje rzeczywiste zachowanie obserwowane w wielu sytuacjach.

---

## Status Behavioral Patterns

### Candidate

Wzorzec został zidentyfikowany, ale posiada ograniczoną liczbę obserwacji.

### Validated

Wzorzec został zaobserwowany wielokrotnie w niezależnych Stories i jest wspierany przez Predictors.

### Deprecated

Wzorzec utracił wartość wyjaśniającą lub został zastąpiony dokładniejszym modelem.

---

## Relacja pomiędzy Predictorami i Behavioral Patterns

Predictor opisuje pojedynczy mechanizm.

Behavioral Pattern opisuje zachowanie wynikające ze współdziałania wielu Predictorów.

Pojedynczy Predictor może wspierać wiele Behavioral Patterns.

Pojedynczy Behavioral Pattern zwykle wykorzystuje od 2 do 4 Predictorów.

Behavioral Pattern powinien być wsparty zarówno przez Predictors, jak i przez rzeczywiste obserwacje zawarte w Stories.

---

## Relacja pomiędzy Behavioral Patterns i Cognitive Model

Behavioral Patterns nie wyjaśniają zachowania.

Behavioral Patterns opisują zachowanie.

Cognitive Model odpowiada za wyjaśnienie, dlaczego dane wzorce występują.

Behavioral Patterns stanowią główne źródło dowodów wykorzystywanych podczas budowy Cognitive Model.

---

## Zasada stabilności Behavioral Pattern

Kalibracja może:

* zwiększać lub zmniejszać confidence,
* dodawać nowe Stories,
* dodawać nowe dowody,
* doprecyzowywać opis wzorca,
* rozszerzać zakres zachowań objętych wzorcem.

Kalibracja nie powinna zmieniać podstawowego znaczenia wzorca.

Jeżeli nowy materiał wskazuje na inny wzorzec zachowania, należy utworzyć nowy Behavioral Pattern.

---

## Struktura Behavioral Pattern

Każdy Behavioral Pattern powinien być zapisany jako osobny plik Markdown zawierający metadane YAML oraz sekcje opisowe.

### Metadane

```yaml
---
id: BP-001

name: Operational Transformation Under Ambiguity

status: candidate
confidence: medium

based_on_predictors:
  - PRED-001
  - PRED-006
  - PRED-014

emerged_from_stories:
  - STORY-001
  - STORY-004
  - STORY-008

related_calibrations: []

last_updated: 2026-06-22
version: 1.0
---
```

---

## Elementy Behavioral Pattern

### Opis

Opis obserwowanego wzorca zachowania.

Odpowiada na pytanie:

> Co regularnie robi badany?

---

### Wzorzec zachowania

Opis przebiegu zachowania.

Przykład:

```text
Chaos lub niejasność
↓
Analiza sytuacji
↓
Strukturyzacja problemu
↓
Projekt rozwiązania
↓
Wdrożenie lub facylitacja zmiany
```

---

### Wspierające Predictors

Opis Predictorów wspierających wzorzec oraz ich roli.

---

### Zachowania przewidywane

Jakie zachowania powinny pojawiać się, jeśli wzorzec jest poprawny?

---

### Zachowania przeczące

Jakie zachowania osłabiają lub podważają wzorzec?

---

### Pytania walidacyjne

Pytania wykorzystywane podczas analizy Stories.

Przykład:

* Czy wystąpił problem systemowy?
* Czy badany próbował zrozumieć przyczynę źródłową?
* Czy stworzył strukturę lub proces?
* Czy rozwiązanie miało charakter skalowalny?

---

### Dowody potwierdzające

Historie, obserwacje oraz kalibracje wspierające wzorzec.

---

### Dowody przeczące

Historie, obserwacje oraz kalibracje pozostające w konflikcie ze wzorcem.

---

### Historia kalibracji

Lista Calibration Records wpływających na Behavioral Pattern.

---

### Ocena

Aktualna ocena jakości wzorca.

Powinna zawierać:

* confidence,
* liczbę wspierających Predictorów,
* liczbę wspierających Stories,
* liczbę Stories przeczących,
* poziom walidacji.

---

### Notatki

Ograniczenia interpretacyjne, potencjalne kierunki dalszej kalibracji oraz powiązania z innymi Behavioral Patterns.

---

## Weryfikacja jakości

Dobry Behavioral Pattern:

* opisuje rzeczywiste zachowanie,
* występuje w wielu niezależnych Stories,
* jest wspierany przez Predictors,
* generuje przewidywania,
* może zostać sfalsyfikowany.

Słaby Behavioral Pattern:

* jest jedynie parafrazą Predictorów,
* nie posiada wsparcia w Stories,
* opisuje cechę osobowości zamiast zachowania,
* nie generuje przewidywań,
* nie może zostać obalony.

---

## Cel długoterminowy

Celem Behavioral Patterns nie jest wyjaśnianie działania badanego.

Ich rolą jest identyfikacja i dokumentowanie powtarzalnych zachowań występujących w rzeczywistych sytuacjach.

Behavioral Patterns stanowią warstwę dowodową pomiędzy Predictorami a Cognitive Model i pozwalają budować model oparty na obserwacjach, a nie wyłącznie na deklaracjach.
