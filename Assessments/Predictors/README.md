# Predictors

## Cel dokumentu

Predictors są pierwszą warstwą interpretacyjną Cognitive Model.

Ich zadaniem jest identyfikacja mechanizmów poznawczych, decyzyjnych, motywacyjnych oraz behawioralnych, które mogą wyjaśniać obserwowane działania badanego.

Predictors nie opisują całej osoby.

Predictors nie są również traktowane jako prawda.

Stanowią robocze hipotezy wyjaśniające rzeczywistość i służą jako budulec dla Behavioral Patterns oraz Cognitive Model.

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

Predictors opisują pojedyncze mechanizmy wspierane przez niezależne źródła.

Behavioral Patterns opisują powtarzalne wzorce działania wynikające ze współwystępowania wielu Predictorów.

Cognitive Model integruje całość w spójny model funkcjonowania badanego.

---

## Czym jest Predictor?

Predictor opisuje pojedynczy mechanizm mogący wyjaśniać określone zachowania, decyzje lub sposoby myślenia.

Predictor powinien odpowiadać na pytanie:

> Jaki mechanizm prawdopodobnie działa?

Przykłady:

* Model-Centric Decision Making
* Evidence-Driven Belief Updating
* Learning-Oriented Exploration
* Fairness-Oriented Evaluation
* Stakes-Adjusted Evidence Threshold

Predictor powinien opisywać jeden mechanizm.

Jeżeli Predictor zaczyna opisywać kilka niezależnych mechanizmów jednocześnie, powinien zostać rozdzielony lub zastąpiony dokładniejszym modelem.

---

## Źródła Predictorów

Predictors nie są tworzone bezpośrednio przez Assessment Data ani Stories.

Predictors powstają wyłącznie w wyniku procesu Calibration.

Calibration analizuje:

* Assessment Data,
* Stories,
* istniejące Predictors,
* wcześniejsze Calibration Records.

Predictor powinien być wspierany przez więcej niż jedno źródło danych.

---

## Status Predictorów

### Candidate

Mechanizm został zidentyfikowany, ale posiada ograniczoną ilość dowodów wspierających.

### Validated

Mechanizm został potwierdzony przez wiele niezależnych źródeł danych oraz obserwacji behawioralnych.

### Deprecated

Mechanizm utracił wartość wyjaśniającą lub został zastąpiony dokładniejszym modelem.

---

## Relacja pomiędzy Assessment Data, Stories i Predictorami

Assessment Data opisują potencjalne tendencje.

Stories opisują rzeczywiste zachowania.

Predictors stanowią aktualną interpretację najlepiej wyjaśniającą oba źródła jednocześnie.

Żadne pojedyncze źródło nie powinno samodzielnie tworzyć Predictorów.

---

## Relacja pomiędzy Predictorami i Behavioral Patterns

Predictor opisuje pojedynczy mechanizm.

Behavioral Pattern opisuje powtarzalny wzorzec działania obserwowany w rzeczywistości.

Pojedynczy Predictor może wspierać wiele Behavioral Patterns.

Pojedynczy Behavioral Pattern zwykle opiera się na współwystępowaniu 2–4 Predictorów oraz wielokrotnym występowaniu podobnego wzorca w Stories.

Przykład:

```text
Predictors

- Model-Centric Decision Making
- Systemic Problem Structuring
- Evidence-Driven Belief Updating

↓

Behavioral Pattern

Operational Transformation Under Ambiguity
```

---

## Zasada stabilności Predictora

Calibration może:

* zwiększać lub zmniejszać confidence,
* dodawać nowe źródła,
* dodawać nowe przewidywania,
* dodawać nowe dowody wspierające,
* dodawać nowe dowody przeczące,
* doprecyzowywać opis.

Calibration nie powinna zmieniać podstawowego znaczenia Predictora.

Jeżeli nowy materiał wskazuje na inny mechanizm niż pierwotnie zakładano, należy utworzyć nowy Predictor lub przeprowadzić formalną migrację modelu.

---

## Struktura Predictora

Każdy Predictor powinien być zapisany jako osobny plik Markdown zawierający metadane YAML oraz sekcje opisowe.

### Metadane

```yaml
---
id: PRED-001

name: Model-Centric Decision Making

status: validated
confidence: high

created_by:
  - CAL-001

related_patterns: []

supporting_calibrations: []

conflicting_calibrations: []

last_updated: 2026-06-22
version: 1.0
---
```

---

## Elementy Predictora

### Opis

Opis mechanizmu.

Odpowiada na pytanie:

> Jaki mechanizm opisuje ten Predictor?

---

### Źródła

Źródła wykorzystane podczas kalibracji.

Powinny wskazywać:

* Assessment Data,
* Stories,
* wcześniejsze Calibration Records.

---

### Zachowania Przewidywane

Jakie zachowania powinny pojawiać się, jeśli Predictor jest poprawny?

---

### Zachowania Przeczące

Jakie zachowania osłabiają lub podważają Predictor?

---

### Dowody Potwierdzające

Historie, obserwacje oraz kalibracje wspierające Predictor.

---

### Dowody Przeczące

Historie, obserwacje oraz kalibracje pozostające w konflikcie z Predictorem.

---

### Historia Kalibracji

Lista Calibration Records wpływających na Predictor.

---

### Ocena

Aktualna ocena jakości Predictora.

Powinna zawierać:

* confidence,
* siłę wsparcia z Assessment Data,
* siłę wsparcia ze Stories,
* poziom walidacji.

---

### Notatki

Ograniczenia interpretacyjne, potencjalne kierunki dalszej kalibracji oraz powiązania z innymi Predictorami.

---

## Weryfikacja jakości

Dobry Predictor:

* opisuje pojedynczy mechanizm,
* posiada wiele źródeł,
* generuje przewidywania,
* może zostać sfalsyfikowany,
* wspiera budowę Behavioral Patterns.

Słaby Predictor:

* opisuje wiele mechanizmów jednocześnie,
* jest wyłącznie parafrazą wyników testów,
* nie posiada dowodów behawioralnych,
* nie generuje przewidywań,
* nie może zostać obalony.

---

## Cel długoterminowy

Celem Predictorów nie jest opisanie osobowości badanego.

Ich rolą jest identyfikacja mechanizmów, które najlepiej wyjaśniają sposób myślenia, podejmowania decyzji, uczenia się oraz działania badanego.

Predictors stanowią fundament dla Behavioral Patterns oraz Cognitive Model i podlegają ciągłej kalibracji wraz z pojawianiem się nowych danych, historii oraz obserwacji.

---

<!-- VAULT:GENERATED:START -->
# Indeks rekordów

> **Sekcja generowana automatycznie** ze stanu Vaulta (`scripts/render_readmes.py`).
> Nie edytuj recznie — zmiany wprowadzaj w rekordach i przegeneruj.

Łącznie: **14** predyktorów.

Kolumna `#STORY` podaje liczbę wspierających historii. `Konflikty` wskazuje historie sprzeczne z hipotezą — wartość niezerowa jest sygnałem do rewizji, nie błędem.

| ID | Nazwa | Status | Pewność | #STORY | Konflikty | Wersja | Aktualizacja |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PRED-001` | Model-Centric Decision Making | validated | very high | 9 | 0 | 1.2 | 2026-06-23 |
| `PRED-002` | Evidence-Driven Belief Updating | validated | very high | 9 | 0 | 1.1 | 2026-06-23 |
| `PRED-003` | Fairness-Oriented Evaluation | validated | high | 9 | 0 | 1.2 | 2026-07-07 |
| `PRED-004` | Principle-Based Decision Making | validated | very high | 9 | 0 | 1.1 | 2026-06-23 |
| `PRED-005` | Learning-Oriented Exploration | candidate | high | 9 | 0 | 1.2 | 2026-06-25 |
| `PRED-006` | Systemic Problem Structuring | validated | very high | 9 | 0 | 1.3 | 2026-06-25 |
| `PRED-007` | Low Status Motivation | validated | high | 4 | 0 | 1.2 | 2026-07-07 |
| `PRED-008` | Selective Cognitive Reopening | candidate | medium | 3 | 0 | 1.2 | 2026-07-07 |
| `PRED-009` | Expert-over-Manager Preference | validated | very high | 9 | 0 | 1.2 | 2026-06-25 |
| `PRED-010` | Proven-System Optimization | validated | high | 10 | 0 | 1.4 | 2026-07-07 |
| `PRED-011` | Stakes-Adjusted Evidence Threshold | validated | high | 9 | 0 | 1.2 | 2026-06-25 |
| `PRED-012` | Tolerance for People vs Cognitive Errors | validated | very high | 9 | 0 | 1.1 | 2026-06-23 |
| `PRED-013` | Context-Adaptive Self-Presentation | validated | high | 2 | 0 | 1.2 | 2026-07-07 |
| `PRED-014` | Supportive Facilitation Orientation | validated | very high | 10 | 0 | 1.4 | 2026-07-07 |

---

# Encje powiązane

> **Sekcja generowana automatycznie** ze stanu Vaulta (`scripts/render_readmes.py`).
> Nie edytuj recznie — zmiany wprowadzaj w rekordach i przegeneruj.

Źródłem powiązań jest frontmatter rekordu `PRED-*`.

| ID | Nazwa | Wspierające historie | Kalibracje | Narzędzia źródłowe |
| --- | --- | --- | --- | --- |
| `PRED-001` | Model-Centric Decision Making | `STORY-001` `STORY-002` `STORY-004` `STORY-006` `STORY-008` `STORY-003` `STORY-005` `STORY-007` `STORY-009` | `CAL-001` | HEXACO, VIA, NFC, AOT, CIHS, Gallup |
| `PRED-002` | Evidence-Driven Belief Updating | `STORY-004` `STORY-006` `STORY-008` `STORY-003` `STORY-005` `STORY-007` `STORY-009` `STORY-001` `STORY-002` | `CAL-001` | AOT, CIHS, NFC, VIA |
| `PRED-003` | Fairness-Oriented Evaluation | `STORY-002` `STORY-003` `STORY-004` `STORY-005` `STORY-008` `STORY-009` `STORY-001` `STORY-006` `STORY-007` | `CAL-001` `CAL-004` | HEXACO, Schwartz, Moral Foundations Theory, VIA |
| `PRED-004` | Principle-Based Decision Making | `STORY-003` `STORY-008` `STORY-009` `STORY-001` `STORY-002` `STORY-004` `STORY-007` `STORY-005` `STORY-006` | `CAL-001` | HEXACO, Schwartz, Moral Foundations Theory, VIA, Gallup |
| `PRED-005` | Learning-Oriented Exploration | `STORY-004` `STORY-005` `STORY-006` `STORY-007` `STORY-008` `STORY-001` `STORY-002` `STORY-003` `STORY-009` | `CAL-001` `CAL-003` | Gallup, HEXACO, VIA, NFC |
| `PRED-006` | Systemic Problem Structuring | `STORY-001` `STORY-002` `STORY-003` `STORY-004` `STORY-005` `STORY-006` `STORY-007` `STORY-008` `STORY-009` | `CAL-001` `CAL-002` `CAL-003` | Gallup, HEXACO, NFC, AOT |
| `PRED-007` | Low Status Motivation | `STORY-011` `STORY-002` `STORY-005` `STORY-009` | `CAL-001` `CAL-004` | Schwartz, HEXACO, VIA, Gallup |
| `PRED-008` | Selective Cognitive Reopening | `STORY-004` `STORY-008` `STORY-009` | `CAL-001` `CAL-004` | AOT, CIHS, NFCS, Wywiad jakościowy |
| `PRED-009` | Expert-over-Manager Preference | `STORY-001` `STORY-002` `STORY-003` `STORY-004` `STORY-005` `STORY-006` `STORY-007` `STORY-008` `STORY-009` | `CAL-001` `CAL-003` | Gallup, VIA, Schwartz, Wywiad jakościowy |
| `PRED-010` | Proven-System Optimization | `STORY-001` `STORY-002` `STORY-003` `STORY-005` `STORY-007` `STORY-008` `STORY-004` `STORY-006` `STORY-009` `STORY-010` | `CAL-001` `CAL-002` `CAL-003` `CAL-004` | Schwartz, AOT, CIHS, Wywiad jakościowy |
| `PRED-011` | Stakes-Adjusted Evidence Threshold | `STORY-004` `STORY-006` `STORY-008` `STORY-001` `STORY-002` `STORY-003` `STORY-007` `STORY-005` `STORY-009` | `CAL-001` `CAL-003` | AOT, CIHS, NFCS, Wywiad jakościowy |
| `PRED-012` | Tolerance for People vs Cognitive Errors | `STORY-001` `STORY-002` `STORY-003` `STORY-005` `STORY-009` `STORY-004` `STORY-006` `STORY-008` `STORY-007` | `CAL-001` | HEXACO, Big Five, VIA, Schwartz, MFQ, AOT, Wywiad jakościowy |
| `PRED-013` | Context-Adaptive Self-Presentation | `STORY-010` `STORY-011` | `CAL-001` `CAL-004` | Wywiad jakościowy, Obserwacje behawioralne (CAL-004) |
| `PRED-014` | Supportive Facilitation Orientation | `STORY-001` `STORY-002` `STORY-005` `STORY-009` `STORY-003` `STORY-004` `STORY-006` `STORY-008` `STORY-007` `STORY-011` | `CAL-001` `CAL-002` `CAL-003` `CAL-004` | Gallup, Schwartz, VIA, Wywiad jakościowy |

---

# Luki w powiązaniach

> **Sekcja generowana automatycznie** ze stanu Vaulta (`scripts/render_readmes.py`).
> Nie edytuj recznie — zmiany wprowadzaj w rekordach i przegeneruj.

## Predyktory bez wspierającej historii

Hipoteza bez zakotwiczenia w obserwowanej sytuacji pozostaje niezweryfikowana:

_Brak — każdy predyktor wskazuje co najmniej jedną historię._

## Predyktory bez kalibracji

_Brak — każdy predyktor przeszedł co najmniej jedną kalibrację._
<!-- VAULT:GENERATED:END -->
