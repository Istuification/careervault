# Hypotheses

## Cel dokumentu

Hipotezy są drugą warstwą interpretacyjną modelu poznawczego.

Ich zadaniem jest łączenie wielu predyktorów w spójne wzorce zachowań, które mogą być obserwowane i weryfikowane w rzeczywistych sytuacjach.

Hipotezy nie są traktowane jako fakty.

Stanowią robocze wyjaśnienia tego, dlaczego określone zachowania pojawiają się w różnych kontekstach.

Hipotezy są głównym narzędziem wykorzystywanym podczas analizy Stories.

Ich poprawność jest stale weryfikowana poprzez proces kalibracji.

---

## Miejsce w architekturze Vault

```text
Assessment Data
        ↓
    Predictors
        ↓
    Hypotheses
        ↓
  Cognitive Model

Stories
        ↓
   Calibration
        ↓
  Predictors
        ↓
   Hypotheses
        ↓
  Cognitive Model
```

Assessment Data dostarczają danych pomiarowych.

Predyktory opisują pojedyncze mechanizmy poznawcze, behawioralne lub decyzyjne.

Hipotezy opisują wzorce wynikające ze współwystępowania wielu predyktorów.

Stories są wykorzystywane do weryfikacji hipotez.

Kalibracja aktualizuje predyktory, hipotezy oraz Cognitive Model na podstawie nowych dowodów.

---

## Czym jest hipoteza?

Hipoteza jest roboczym wyjaśnieniem określonego wzorca zachowań.

Hipoteza nie opisuje pojedynczego mechanizmu.

Hipoteza opisuje sposób współdziałania wielu mechanizmów.

Przykłady:

* Strategic Problem Solving Orientation
* Knowledge-to-Model Pipeline
* Expert-Consultative Leadership Style
* Systems Influence Orientation

Hipoteza powinna wyjaśniać obserwowalne zachowania.

Jeżeli hipoteza nie generuje przewidywań możliwych do sprawdzenia w Stories, nie spełnia swojej funkcji.

---

## Źródła hipotez

Hipotezy są budowane na podstawie istniejących predyktorów.

Typowa hipoteza powinna wykorzystywać od 2 do 4 predyktorów.

Przykład:

```text
PRED-005 Learning-Oriented Exploration
+
PRED-006 Systemic Problem Structuring
+
PRED-001 Model-Centric Decision Making
↓
HYP-001 Knowledge-to-Model Pipeline
```

Hipotezy nie powinny być tworzone bezpośrednio z Assessment Data ani bezpośrednio ze Stories.

---

## Rola hipotez podczas analizy Stories

Hipotezy pełnią rolę warstwy interpretacyjnej.

Podczas analizy Stories należy odpowiedzieć między innymi na pytania:

* Czy w historii widoczne są predyktory składające się na hipotezę?
* Czy historia wspiera hipotezę?
* Czy historia pozostaje z hipotezą w konflikcie?
* Czy historia sugeruje konieczność kalibracji któregoś z predyktorów?

Stories nie aktualizują hipotez bezpośrednio.

Jeżeli analiza Story wskazuje na konflikt lub nowe informacje, uruchamiany jest proces kalibracji.

---

## Status hipotez

### Candidate

Hipoteza została utworzona, ale nie posiada jeszcze wystarczających dowodów behawioralnych.

### Validated

Hipoteza została potwierdzona przez wiele niezależnych historii oraz wspierające predyktory.

### Deprecated

Hipoteza została zastąpiona dokładniejszym modelem lub utraciła wartość wyjaśniającą.

---

## Kalibracja hipotez

Hipotezy nie są kalibrowane bezpośrednio.

Najpierw kalibrowane są predyktory.

Jeżeli kalibracja wpływa na znaczenie, confidence lub strukturę predyktora w sposób mogący wpłynąć na hipotezę, należy przeprowadzić kalibrację pomocniczą hipotezy.

Kalibracja pomocnicza może:

* zmienić confidence hipotezy,
* doprecyzować opis,
* zmodyfikować zachowania przewidywane,
* zmodyfikować zachowania przeczące,
* oznaczyć hipotezę jako wymagającą rewizji.

Kalibracja pomocnicza nie powinna zmieniać podstawowego znaczenia hipotezy bez wyraźnego uzasadnienia.

---

## Relacja pomiędzy predyktorami i hipotezami

Predyktor opisuje pojedynczy mechanizm.

Hipoteza opisuje wzorzec wynikający ze współdziałania wielu mechanizmów.

Pojedynczy predyktor może wspierać wiele hipotez.

Pojedyncza hipoteza może wykorzystywać wiele predyktorów.

Predyktory są budulcem hipotez.

Hipotezy nie zastępują predyktorów.

---

## Zasada stabilności hipotezy

Kalibracja może:

* zwiększać lub zmniejszać confidence,
* dodawać nowe dowody,
* doprecyzowywać mechanizm,
* rozwijać zachowania przewidywane,
* rozwijać zachowania przeczące.

Kalibracja nie powinna zmieniać podstawowego celu hipotezy.

Jeżeli nowy materiał wskazuje, że hipoteza opisuje inny wzorzec niż pierwotnie zakładano, należy rozważyć utworzenie nowej hipotezy.

---

## Struktura hipotezy

Każda hipoteza powinna być zapisana jako osobny plik Markdown zawierający metadane YAML oraz sekcje opisowe.

### Metadane

```yaml
---
id: HYP-001
name: Knowledge-to-Model Pipeline

status: candidate
confidence: medium

based_on:
  - PRED-001
  - PRED-005
  - PRED-006

supporting_stories: []

conflicting_stories: []

related_calibrations: []

last_updated: 2026-06-22
version: 1.0
---
```

---

## Elementy hipotezy

### Opis

Krótki opis wzorca zachowań wyjaśnianego przez hipotezę.

Odpowiada na pytanie:

> Co wyjaśnia ta hipoteza?

---

### Mechanizm

Opis współpracy pomiędzy predyktorami.

Odpowiada na pytanie:

> Jak działa ten wzorzec?

Przykład:

```text
Eksploracja wiedzy
↓
Strukturyzacja informacji
↓
Budowa modelu
↓
Podejmowanie decyzji
```

---

### Predyktory składowe

Opis roli każdego predyktora w hipotezie.

Przykład:

```text
PRED-005 → dostarcza nowych informacji

PRED-006 → organizuje informacje

PRED-001 → buduje model decyzyjny
```

---

### Zachowania przewidywane

Lista zachowań, które powinny występować, jeśli hipoteza jest poprawna.

Odpowiada na pytanie:

> Co powinienem zaobserwować w rzeczywistości?

---

### Zachowania przeczące

Lista zachowań osłabiających lub podważających hipotezę.

Odpowiada na pytanie:

> Co mogłoby wskazywać, że ten model jest błędny lub niepełny?

---

### Pytania walidacyjne

Pytania wykorzystywane podczas analizy Stories.

Przykład:

* Czy badany aktywnie poszukiwał informacji?
* Czy uporządkował problem przed działaniem?
* Czy zbudował model sytuacji?
* Czy decyzja wynikała z modelu?

---

### Dowody potwierdzające

Historie, obserwacje lub kalibracje wspierające hipotezę.

---

### Dowody przeczące

Historie, obserwacje lub kalibracje pozostające w konflikcie z hipotezą.

---

### Historia kalibracji

Lista kalibracji, które wpłynęły na hipotezę.

---

### Ocena

Aktualna ocena jakości hipotezy.

Powinna zawierać:

* poziom pewności,
* liczbę wspierających predyktorów,
* liczbę wspierających historii,
* liczbę historii przeczących,
* poziom walidacji.

---

### Notatki

Dodatkowe informacje, ograniczenia interpretacyjne, potencjalne kierunki dalszej kalibracji oraz powiązania z innymi hipotezami.

---

## Weryfikacja jakości

Dobra hipoteza:

* opiera się na wielu predyktorach,
* generuje przewidywania,
* może zostać sfalsyfikowana,
* pomaga interpretować Stories,
* wnosi nową wartość wyjaśniającą ponad pojedyncze predyktory.

Słaba hipoteza:

* jest jedynie listą predyktorów,
* nie generuje przewidywań,
* nie może zostać obalona,
* nie pomaga analizować Stories,
* nie wnosi nowego poziomu interpretacji.

---

## Cel długoterminowy

Celem hipotez nie jest stworzenie pełnego modelu człowieka.

Ich rolą jest identyfikowanie i testowanie wzorców zachowań wynikających ze współdziałania wielu mechanizmów opisanych przez predyktory.

Zweryfikowane hipotezy stanowią podstawę do budowy i kalibracji Cognitive Model.
