# Predictors

## Cel dokumentu

Predyktory są pierwszą warstwą interpretacyjną modelu.

Ich zadaniem jest przekształcenie surowych danych pochodzących z testów, ocen, historii i innych źródeł dowodowych w opis potencjalnych mechanizmów poznawczych, behawioralnych lub decyzyjnych.

Predyktory nie opisują całej osoby.

Predyktory nie są również traktowane jako prawda.

Stanowią robocze modele wyjaśniające obserwowane wzorce zachowań i służą jako budulec dla hipotez oraz Cognitive Model.

---

## Miejsce w architekturze Vault

```text
Evidence Sources
        ↓
    Predictors
        ↓
    Hypotheses
        ↓
  Cognitive Model
```

Evidence Sources dostarczają danych.

Predyktory interpretują dane.

Hipotezy łączą wiele predyktorów w bardziej złożone mechanizmy.

Cognitive Model stanowi najwyższy poziom integracji wszystkich zweryfikowanych hipotez.

---

## Czym jest predyktor?

Predyktor jest pojedynczym mechanizmem lub wzorcem, który może wyjaśniać określone zachowania, decyzje lub sposoby myślenia.

Przykłady:

* Model-Centric Decision Making
* Evidence-Driven Belief Updating
* Learning-Oriented Exploration
* Fairness-Oriented Evaluation

Predyktor powinien opisywać jeden mechanizm.

Jeżeli predyktor zaczyna opisywać wiele niezależnych mechanizmów, powinien zostać rozdzielony lub skalibrowany.

---

## Źródła predyktorów

Predyktory mogą być tworzone na podstawie:

* wyników testów psychometrycznych,
* ocen jakościowych,
* analiz historii,
* kalibracji istniejącego modelu,
* powtarzających się wzorców zachowań.

Każdy predyktor powinien wskazywać źródła, które doprowadziły do jego utworzenia.

---

## Status predyktorów

### Candidate

Mechanizm został zidentyfikowany, ale nie posiada jeszcze wystarczającej liczby dowodów behawioralnych.

### Validated

Mechanizm został potwierdzony przez wiele niezależnych źródeł oraz historię zachowań.

### Deprecated

Mechanizm został zastąpiony przez dokładniejszy model lub utracił wartość wyjaśniającą.

---

## Kalibracja predyktorów

Predyktory są modelami roboczymi i mogą być kalibrowane.

Kalibracja może:

* zmieniać poziom pewności,
* doprecyzowywać opis,
* dodawać nowe dowody,
* dodawać nowe zachowania przewidywane,
* dodawać nowe zachowania przeczące.

Kalibracja nie powinna zmieniać podstawowego znaczenia predyktora.

Jeżeli znaczenie predyktora wymaga zmiany, należy utworzyć nowy predyktor lub przeprowadzić formalną migrację modelu.

---

## Relacja pomiędzy Evidence i Stories

Evidence Sources opisują potencjalne predyspozycje i wzorce.

Stories opisują rzeczywiste zachowania.

Żadne z tych źródeł nie jest automatycznie nadrzędne względem drugiego.

Celem kalibracji jest budowanie modelu, który najlepiej wyjaśnia zarówno wyniki pomiarów, jak i rzeczywiste zachowania.

---

## Relacja pomiędzy predyktorami i hipotezami

Predyktor opisuje pojedynczy mechanizm.

Hipoteza opisuje zależność pomiędzy wieloma predyktorami.

Pojedynczy predyktor może wspierać wiele hipotez.

Hipotezy powinny być budowane w oparciu o 2–4 predyktory.

---

## Weryfikacja jakości

Dobry predyktor:

* opisuje pojedynczy mechanizm,
* posiada źródła,
* generuje przewidywania,
* może zostać obalony przez dowody,
* wspiera budowę hipotez.

Słaby predyktor:

* opisuje wiele różnych mechanizmów jednocześnie,
* nie posiada źródeł,
* nie generuje przewidywań,
* nie może zostać sfalsyfikowany,
* jest jedynie parafrazą wyników testów.

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
  - HEXACO
  - NFC
  - AOT

supporting_stories: []

conflicting_stories: []

related_hypotheses: []

last_updated: 2026-06-22
version: 1.0
---
```

### Sekcje obowiązkowe

#### Opis

Krótki opis mechanizmu oraz jego znaczenia.

Odpowiada na pytanie:

> Co ten predyktor opisuje?

---

#### Źródła

Źródła, które doprowadziły do utworzenia predyktora.

Mogą obejmować:

* testy psychometryczne,
* analizy jakościowe,
* historie,
* wcześniejsze kalibracje.

---

#### Zachowania Przewidywane

Lista zachowań, które powinny występować, jeśli predyktor jest poprawny.

Odpowiada na pytanie:

> Co powinienem zaobserwować w rzeczywistości?

---

#### Zachowania Przeczące

Lista zachowań osłabiających lub podważających predyktor.

Odpowiada na pytanie:

> Co mogłoby wskazywać, że ten model jest błędny lub niepełny?

---

#### Dowody Potwierdzające

Lista historii, obserwacji lub innych dowodów wspierających predyktor.

Przykład:

```text
- STORY-014
- STORY-027
```

---

#### Dowody Przeczące

Lista historii lub obserwacji pozostających w konflikcie z predyktorem.

Przykład:

```text
- STORY-031
```

---

#### Historia Kalibracji

Lista kalibracji, które wpłynęły na predyktor.

Przykład:

```text
- CAL-002
- CAL-011
```

---

#### Ocena

Aktualna ocena jakości predyktora.

Powinna zawierać:

* poziom pewności,
* siłę źródeł psychometrycznych,
* siłę źródeł behawioralnych,
* poziom walidacji.

---

#### Notatki

Dodatkowe informacje, ograniczenia interpretacyjne, potencjalne kierunki dalszej kalibracji oraz powiązania z innymi predyktorami.

---

## Cel długoterminowy

Celem predyktorów nie jest stworzenie kompletnego opisu osobowości.

Ich rolą jest budowa możliwie użytecznego modelu wyjaśniającego sposób myślenia, podejmowania decyzji, uczenia się oraz funkcjonowania badanego.

Model ten ma charakter iteracyjny i podlega ciągłej kalibracji wraz z pojawianiem się nowych danych.
