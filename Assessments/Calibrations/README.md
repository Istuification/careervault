# Calibration

## Cel dokumentu

Calibration jest formalnym procesem aktualizacji Cognitive Model.

Jej zadaniem jest porównywanie dostępnych danych, identyfikowanie zgodności i sprzeczności pomiędzy źródłami oraz dokumentowanie zmian w modelu.

Calibration nie tworzy nowych danych.

Calibration interpretuje istniejące dane i obserwacje w celu zwiększenia trafności modelu.

Każda istotna zmiana w Predictorach, Behavioral Patterns lub Cognitive Model powinna zostać udokumentowana w postaci Calibration Record.

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

Calibration integruje oba źródła i odpowiada za aktualizację modelu.

Predictors opisują mechanizmy.

Behavioral Patterns opisują powtarzalne wzorce zachowań.

Cognitive Model integruje całość w spójny model funkcjonowania badanego.

---

## Dlaczego Calibration istnieje?

Żadne pojedyncze źródło danych nie powinno być traktowane jako prawda.

Assessment Data opisują wyniki pomiarów oraz profile poznawcze.

Stories opisują rzeczywiste zdarzenia i zachowania.

Oba źródła posiadają ograniczenia:

* wyniki badań opisują jedynie wybrane aspekty funkcjonowania,
* Stories mogą zawierać błędy pamięci, interpretacji lub perspektywy,
* pojedyncze obserwacje mogą być przypadkowe lub niereprezentatywne.

Calibration istnieje po to, aby:

* porównywać źródła,
* identyfikować zgodności,
* identyfikować sprzeczności,
* wykrywać nowe wzorce,
* aktualizować model,
* dokumentować proces zmian.

---

## Zasada „Fakty przed deklaracjami”

Jedną z podstawowych zasad Career Vault jest:

> Fakty przed deklaracjami.

Model nie powinien być budowany wyłącznie na podstawie deklaracji badanego ani wyłącznie na podstawie wyników testów.

Każdy istotny element modelu powinien być wsparty przez wiele niezależnych źródeł danych.

Im więcej niezależnych źródeł wspiera dany wniosek, tym wyższy poziom zaufania do modelu.

---

## Co może zrobić Calibration?

Calibration może:

* utworzyć nowy Predictor,

* zmodyfikować istniejący Predictor,

* wycofać Predictor,

* utworzyć nowy Behavioral Pattern,

* zmodyfikować istniejący Behavioral Pattern,

* wycofać Behavioral Pattern,

* zaktualizować Cognitive Model,

* zwiększyć lub zmniejszyć poziom confidence,

* wykryć konflikt pomiędzy źródłami,

* wykryć nowy wzorzec wymagający dalszej analizy,

* wskazać obszary wymagające dodatkowych danych.

Calibration nie powinna zmieniać modelu bez wyraźnego uzasadnienia opartego na dostępnych dowodach.

---

## Struktura Calibration Record

Każda kalibracja powinna być zapisana jako osobny plik Markdown.

### Metadane

```yaml
---
id: CAL-001

name: Predictor-Story Mapping

date: 2026-06-22

status: completed

scope:
  - Predictors
  - Stories

version: 1.0
---
```

---

## Elementy Calibration Record

### Cel

Dlaczego przeprowadzono kalibrację?

Jakie pytanie lub problem miała rozwiązać?

---

### Zakres

Które elementy Vault zostały przeanalizowane?

Przykłady:

* Assessment Data,
* Stories,
* Predictors,
* Behavioral Patterns,
* Cognitive Model.

---

### Analiza

Opis przeprowadzonej analizy.

Powinna zawierać:

* wykorzystane źródła,
* przebieg rozumowania,
* istotne obserwacje,
* zauważone zgodności,
* zauważone konflikty.

---

### Wnioski

Najważniejsze obserwacje wynikające z kalibracji.

Powinny odpowiadać na pytanie:

> Czego dowiedzieliśmy się o modelu?

---

### Zmiany rekomendowane

Zmiany sugerowane przez kalibrację.

Przykłady:

* zwiększenie confidence Predictora,
* doprecyzowanie opisu,
* utworzenie nowego Behavioral Pattern,
* oznaczenie elementu jako wymagającego dalszej obserwacji.

---

### Zmiany wdrożone

Zmiany faktycznie wprowadzone do modelu.

Jeżeli żadna zmiana nie została wdrożona, należy to odnotować.

---

### Otwarte pytania

Elementy wymagające dalszej obserwacji, dodatkowych danych lub kolejnych kalibracji.

---

## Zasada śledzenia zmian

Calibration pełni funkcję historii rozwoju modelu.

Każda istotna zmiana powinna posiadać odpowiadający jej Calibration Record.

Dzięki temu możliwe jest prześledzenie:

* dlaczego zmiana została wprowadzona,
* jakie dowody ją wspierały,
* które elementy modelu zostały zmienione,
* jakie były alternatywne interpretacje.

---

## Relacja z Predictorami

Predictors są najniższą warstwą interpretacyjną modelu.

Calibration odpowiada za ocenę, czy istniejące Predictors nadal najlepiej wyjaśniają dostępne dane.

W wyniku kalibracji Predictor może zostać:

* potwierdzony,
* zmodyfikowany,
* rozdzielony,
* połączony z innym Predictorem,
* wycofany.

---

## Relacja z Behavioral Patterns

Behavioral Patterns opisują powtarzalne wzorce zachowań.

Calibration odpowiada za ocenę, czy wzorce nadal występują w dostępnych Stories oraz czy są wspierane przez Predictors.

W wyniku kalibracji Behavioral Pattern może zostać:

* potwierdzony,
* zmodyfikowany,
* rozszerzony,
* ograniczony,
* wycofany.

---

## Relacja z Cognitive Model

Cognitive Model stanowi najwyższą warstwę interpretacyjną Vault.

Calibration odpowiada za ocenę, czy Cognitive Model nadal najlepiej wyjaśnia:

* Assessment Data,
* Predictors,
* Behavioral Patterns,
* Stories.

Jeżeli model przestaje wyjaśniać dostępne dane, powinien zostać zaktualizowany.

---

## Cel długoterminowy

Celem Calibration nie jest osiągnięcie idealnego modelu.

Jej rolą jest stopniowe zwiększanie trafności Cognitive Model poprzez systematyczne porównywanie modelu z nowymi danymi, obserwacjami i doświadczeniami.

Model powinien ewoluować wraz z pojawianiem się nowych dowodów, zachowując jednocześnie pełną historię zmian i uzasadnień.
