# Behavioral Patterns

## Cel dokumentu

Behavioral Patterns stanowią pierwszą warstwę interpretacji zachowań zaobserwowanych w Career Vault.

Ich zadaniem jest identyfikacja powtarzalnych mechanizmów działania występujących w wielu niezależnych sytuacjach.

Behavioral Pattern opisuje:

```text
Trigger
↓
Internal Process
↓
Observable Behaviors
↓
Outcomes
```

Behavioral Pattern nie jest:

* cechą osobowości,
* talentem,
* kompetencją,
* archetypem,
* pojedynczym mechanizmem poznawczym.

Behavioral Pattern jest powtarzalnym wzorcem zachowania obserwowanym w rzeczywistych sytuacjach.

Stanowi podstawową jednostkę analizy behawioralnej wykorzystywaną do budowy Predictorów oraz Cognitive Model.

---

# Miejsce w architekturze Vault

```text
Assessment Data
Stories
Achievements
Skills
Development Areas

        ↓

Behavioral Patterns

        ↓

Predictors

        ↓

Cognitive Model
```

Assessment Data dostarczają danych pomiarowych.

Stories dostarczają obserwacji zachowań.

Achievements dostarczają dowodów rezultatów.

Skills dostarczają informacji o rozwiniętych zdolnościach.

Development Areas dostarczają informacji o ograniczeniach oraz powtarzalnych trudnościach.

Behavioral Patterns integrują wszystkie źródła dowodowe w obserwowalne wzorce działania.

Predictors wyjaśniają mechanizmy generujące te wzorce.

Cognitive Model integruje całość w spójny model funkcjonowania badanego.

---

# Czym jest Behavioral Pattern?

Behavioral Pattern jest powtarzalnym mechanizmem zachowania obserwowanym wielokrotnie w niezależnych sytuacjach.

Powinien odpowiadać na pytanie:

> Co badany regularnie robi, gdy znajduje się w określonych warunkach?

Przykłady:

* Od Chaosu do Modelu Operacyjnego
* Usprawniaj To, Co Istnieje, Zanim To Zastąpisz
* Bierz Problem Na Siebie
* Tłumacz Między Funkcjami
* Ucz Się Poprzez Wejście w Problem

Behavioral Pattern musi opisywać zachowanie możliwe do zaobserwowania.

Nie powinien opisywać wyłącznie cech osobowości ani stanów wewnętrznych.

---

# Źródła Behavioral Patterns

Behavioral Patterns mogą być budowane na podstawie:

* Stories,
* Achievements,
* Skills,
* Development Areas,
* Assessment Data.

Hierarchia dowodów:

```text
1. Stories
2. Achievements
3. Development Areas
4. Assessment Data
5. Skills
```

Stories są głównym źródłem dowodów.

Behavioral Pattern nie powinien być tworzony wyłącznie na podstawie Assessment Data.

Behavioral Pattern nie powinien być tworzony na podstawie pojedynczej Story.

Do utworzenia wzorca wymagane są wielokrotne obserwacje podobnego zachowania.

---

# Rola Behavioral Patterns

Behavioral Patterns odpowiadają na pytanie:

> Jak badany zachowuje się w rzeczywistych sytuacjach?

Są warstwą obserwacyjną.

Nie próbują wyjaśniać przyczyn zachowania.

Ich celem jest dokumentowanie regularnie występujących wzorców działania.

Przykład:

```text
Wiele Stories

↓

Powtarzalne zachowanie:

"Bierze odpowiedzialność za problemy bez właściciela"

↓

Behavioral Pattern:

Bierz Problem Na Siebie
```

---

# Relacja pomiędzy Behavioral Patterns i Predictorami

Behavioral Pattern opisuje zachowanie.

Predictor opisuje mechanizm.

Przykład:

```text
Behavioral Pattern

Bierz Problem Na Siebie

↓

Predictors

Responsibility Internalization
Initiative Under Ambiguity
Low Ownership Diffusion
```

Behavioral Pattern jest obserwacją.

Predictor jest hipotezą wyjaśniającą.

Jeden Behavioral Pattern może być wspierany przez wiele Predictorów.

Jeden Predictor może wspierać wiele Behavioral Patterns.

Predictory nie są wymagane do identyfikacji Behavioral Pattern.

Mogą zostać dodane podczas późniejszej analizy.

---

# Relacja pomiędzy Behavioral Patterns i Cognitive Model

Behavioral Patterns nie wyjaśniają zachowania.

Behavioral Patterns opisują zachowanie.

Cognitive Model odpowiada na pytanie:

> Dlaczego te wzorce występują?

Behavioral Patterns stanowią główne źródło dowodów wykorzystywane podczas budowy Cognitive Model.

---

# Status Behavioral Patterns

## Candidate

Wzorzec został zidentyfikowany, ale wymaga dalszych obserwacji.

## Validated

Wzorzec został wielokrotnie zaobserwowany w niezależnych sytuacjach i posiada silne wsparcie dowodowe.

## Deprecated

Wzorzec utracił wartość wyjaśniającą lub został zastąpiony dokładniejszym modelem.

---

# Zasada stabilności Behavioral Pattern

Kalibracja może:

* zwiększać lub zmniejszać confidence,
* dodawać nowe dowody,
* dodawać nowe Stories,
* doprecyzowywać opis wzorca,
* rozszerzać zakres zachowań objętych wzorcem.

Kalibracja nie powinna zmieniać podstawowego znaczenia wzorca.

Jeżeli nowy materiał wskazuje na odmienny mechanizm zachowania, należy utworzyć nowy Behavioral Pattern.

---

# Struktura Behavioral Pattern

Każdy Behavioral Pattern powinien być zapisany jako osobny plik Markdown.

---

## Metadane

```yaml
---
id: BP-001

name: Od Chaosu do Modelu Operacyjnego

status: candidate
confidence: high

derived_from:
  stories:
    - STORY-001
    - STORY-004

  achievements:
    - ACH-001

  skills:
    - SKILL-002

  development_areas: []

  assessment_data:
    - AD-001
---
```

---

# Elementy Behavioral Pattern

## Opis

Opis podstawowego mechanizmu zachowania.

Odpowiada na pytanie:

> Co regularnie robi badany?

---

## Wyzwalacz

Jakie warunki aktywują wzorzec?

---

## Proces Wewnętrzny

Jak wygląda typowa sekwencja rozumowania lub działania prowadząca do zachowania?

---

## Obserwowalne Zachowania

Co może zaobserwować osoba zewnętrzna?

Powinny być to zachowania możliwe do zweryfikowania.

---

## Typowe Rezultaty

Jakie konsekwencje zwykle generuje wzorzec?

Należy uwzględniać zarówno skutki pozytywne, jak i negatywne.

---

## Dowody Wspierające

Dowody wykorzystane do identyfikacji wzorca.

Powinny być grupowane według źródła:

* Stories
* Achievements
* Skills
* Development Areas
* Assessment Data

---

## Potencjalne Tryby Niepowodzenia

Jakie ryzyka pojawiają się przy nadmiernym lub niewłaściwym zastosowaniu wzorca?

Dobry Behavioral Pattern powinien wskazywać własne ograniczenia.

---

## Ocena

Krótka interpretacja behawioralna.

Powinna odpowiadać na pytanie:

> Jakich zachowań możemy spodziewać się w przyszłości, jeśli wzorzec jest poprawny?

---

## Notatki

Miejsce na:

* niepewności interpretacyjne,
* konkurencyjne hipotezy,
* braki dowodowe,
* powiązania z innymi Behavioral Patterns.

---

# Weryfikacja jakości

Dobry Behavioral Pattern:

* opisuje rzeczywiste zachowanie,
* występuje w wielu niezależnych sytuacjach,
* posiada wyraźny Trigger,
* posiada wyraźny Internal Process,
* posiada obserwowalne zachowania,
* generuje przewidywania,
* może zostać sfalsyfikowany,
* posiada udokumentowane dowody.

Słaby Behavioral Pattern:

* jest parafrazą cechy osobowości,
* opisuje wyłącznie kompetencję,
* nie posiada wsparcia w Stories,
* nie generuje przewidywań,
* nie można go obalić,
* nie wskazuje potencjalnych trybów niepowodzenia.

---

# Cel długoterminowy

Celem Behavioral Patterns nie jest wyjaśnianie działania badanego.

Ich rolą jest dokumentowanie powtarzalnych zachowań obserwowanych w rzeczywistych sytuacjach.

Behavioral Patterns stanowią główną warstwę dowodową Career Vault, łączącą dane źródłowe z modelami interpretacyjnymi.

Dzięki temu Cognitive Model może być budowany na podstawie obserwowalnych zachowań, a nie wyłącznie deklaracji, testów psychometrycznych lub subiektywnych interpretacji.
