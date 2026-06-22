# Predictors

## Cel dokumentu

Predyktory są pierwszą warstwą interpretacyjną modelu poznawczego.

Ich zadaniem jest przekształcenie danych pochodzących z Assessment Data oraz wcześniejszych kalibracji w opis potencjalnych mechanizmów poznawczych, behawioralnych lub decyzyjnych.

Predyktory nie opisują całej osoby.

Predyktory nie są również traktowane jako prawda.

Stanowią robocze modele wyjaśniające obserwowane wzorce zachowań i służą jako budulec dla hipotez oraz Cognitive Model.

---

## Miejsce w architekturze Vault

```text
Assessment Data
       │
       ▼
  Predictors
       │
       ▼
  Hypotheses
       │
       ▼
 Cognitive Model

Stories
       │
       ▼
 Calibration
       │
       ├──────────────► Predictors
       ├──────────────► Hypotheses
       └──────────────► Cognitive Model
```

Assessment Data dostarczają danych pomiarowych.

Predyktory interpretują dane.

Hipotezy łączą wiele predyktorów w bardziej złożone wzorce.

Cognitive Model integruje wszystkie zweryfikowane hipotezy w jeden model działania.

Stories nie wpływają bezpośrednio na predyktory.

Stories stanowią materiał obserwacyjny wykorzystywany podczas procesu kalibracji.

---

## Czym jest predyktor?

Predyktor jest pojedynczym mechanizmem lub wzorcem, który może wyjaśniać określone zachowania, decyzje lub sposoby myślenia.

Przykłady:

* Model-Centric Decision Making
* Evidence-Driven Belief Updating
* Learning-Oriented Exploration
* Fairness-Oriented Evaluation

Predyktor powinien opisywać jeden mechanizm.

Jeżeli predyktor zaczyna opisywać wiele niezależnych mechanizmów, powinien zostać rozdzielony lub zastąpiony dokładniejszym modelem.

---

## Źródła predyktorów

Predyktory mogą być tworzone lub aktualizowane wyłącznie na podstawie:

* Assessment Data,
* wcześniejszych kalibracji.

Stories nie tworzą predyktorów bezpośrednio.

Stories mogą jedynie dostarczyć nowych dowodów uruchamiających proces kalibracji.

---

## Status predyktorów

### Candidate

Mechanizm został zidentyfikowany, ale nie posiada jeszcze wystarczającej liczby dowodów behawioralnych.

### Validated

Mechanizm został potwierdzony przez wiele niezależnych źródeł oraz historię zachowań.

### Deprecated

Mechanizm został zastąpiony przez dokładniejszy model lub utracił wartość wyjaśniającą.

---

## Relacja pomiędzy Assessment Data, Stories i Predyktorami

Assessment Data opisują wyniki pomiarów oraz profile poznawcze.

Stories opisują rzeczywiste zachowania i zdarzenia.

Predyktory są aktualnym stanem interpretacji dostępnych danych.

Stories nie zmieniają predyktorów bezpośrednio.

Zmiany mogą zostać wprowadzone wyłącznie poprzez proces kalibracji.

---

## Relacja pomiędzy predyktorami i hipotezami

Predyktor opisuje pojedynczy mechanizm.

Hipoteza opisuje wzorzec wynikający ze współwystępowania wielu predyktorów.

Pojedynczy predyktor może wspierać wiele hipotez.

Hipotezy powinny być budowane w oparciu o 2–4 predyktory.

Hipotezy stanowią warstwę interpretacyjną wykorzystywaną podczas analizy Stories.

---

## Zasada stabilności predyktora

Kalibracja może:

* zwiększać lub zmniejszać confidence,
* dodawać nowe dowody,
* dodawać nowe zachowania przewidywane,
* dodawać nowe zachowania przeczące,
* doprecyzowywać opis.

Kalibracja nie powinna zmieniać podstawowego znaczenia predyktora.

Jeżeli nowy materiał wskazuje, że predyktor opisuje inny mechanizm niż pierwotnie zakładano, należy utworzyć nowy predyktor lub przeprowadzić formalną migrację modelu.

---

## Struktura predyktora

Każdy predyktor powinien być zapisany jako osobny plik Markdown zawierający metadane YAML oraz sekcje opisowe.

### Metadane

```yaml
---
id: PRED-001
name: Model-Centric Decision Making

status: candidate
confidence: high

created_from:
  - Assessment Data

supporting_stories: []

conflicting_stories: []

related_hypotheses: []

related_calibrations: []

last_updated: 2026-06-22
version: 1.0
---
```

### Elementy predyktora

#### Opis

Opis mechanizmu oraz jego znaczenia.

Odpowiada na pytanie:

> Co ten predyktor opisuje?

---

#### Źródła

Dane i obserwacje wykorzystane podczas tworzenia lub aktualizacji predyktora.

Źródła mogą obejmować:

* Assessment Data,
* wcześniejsze kalibracje.

---

#### Zachowania Przewidywane

Zachowania, które powinny występować, jeśli predyktor jest poprawny.

Odpowiada na pytanie:

> Co powinno być widoczne w rzeczywistości?

---

#### Zachowania Przeczące

Zachowania osłabiające lub podważające predyktor.

Odpowiada na pytanie:

> Co mogłoby wskazywać, że model jest błędny lub niepełny?

---

#### Dowody Potwierdzające

Historie, obserwacje lub kalibracje wspierające predyktor.

---

#### Dowody Przeczące

Historie, obserwacje lub kalibracje pozostające w konflikcie z predyktorem.

---

#### Historia Kalibracji

Lista kalibracji, które wpłynęły na predyktor.

---

#### Ocena

Aktualna ocena jakości predyktora.

Powinna zawierać:

* poziom pewności,
* siłę źródeł pomiarowych,
* siłę źródeł behawioralnych,
* poziom walidacji.

---

#### Notatki

Dodatkowe informacje, ograniczenia interpretacyjne, potencjalne kierunki dalszej kalibracji oraz powiązania z innymi predyktorami.

---

## Weryfikacja jakości

Dobry predyktor:

* opisuje pojedynczy mechanizm,
* posiada źródła,
* generuje przewidywania,
* może zostać sfalsyfikowany,
* wspiera budowę hipotez.

Słaby predyktor:

* opisuje wiele mechanizmów jednocześnie,
* nie posiada źródeł,
* nie generuje przewidywań,
* nie może zostać obalony,
* jest wyłącznie parafrazą wyników testów.

---

## Cel długoterminowy

Celem predyktorów nie jest stworzenie kompletnego opisu osobowości.

Ich rolą jest budowa możliwie użytecznego modelu wyjaśniającego sposób myślenia, podejmowania decyzji, uczenia się oraz funkcjonowania badanego.

Model ma charakter iteracyjny i podlega ciągłej kalibracji wraz z pojawianiem się nowych danych, historii oraz zmian w Assessment Data.
