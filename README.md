# Career Vault

> 🔗 **Szybki dostęp:** [Strona projektu](https://istuification.github.io/careervault/) · [Wersja dla AI/LLM (jeden plik tekstowy)](https://istuification.github.io/careervault/vault-full.txt)

## Cel

Career Vault to osobista baza wiedzy zawodowej oraz model poznawczy opisujący sposób podejmowania decyzji, rozwój kompetencji i doświadczeń zawodowych.

Repozytorium stanowi pojedyncze źródło prawdy dla:

* generowania CV,
* przygotowania do rozmów kwalifikacyjnych,
* budowy profilu LinkedIn,
* analizy kompetencji,
* planowania rozwoju zawodowego,
* budowy portfolio osiągnięć,
* współpracy z systemami AI,
* systemów typu RAG,
* zarządzania wiedzą o własnej karierze.

Celem Career Vault nie jest przechowywanie gotowych dokumentów aplikacyjnych.

Celem jest budowanie trwałej bazy faktów, dowodów, doświadczeń i wniosków, które mogą być wielokrotnie wykorzystywane w różnych kontekstach zawodowych.

---

# Filozofia Career Vault

## Fakty ponad deklaracje

Career Vault opiera się na dowodach, a nie opiniach.

Przykład:

❌ Jestem dobrym liderem

✅ Przeprowadziłem restrukturyzację działu serwisu oraz ustabilizowałem jego funkcjonowanie

Każda kompetencja powinna być możliwa do powiązania z konkretnymi osiągnięciami, projektami lub doświadczeniami.

---

## Jedno źródło informacji

Każda informacja powinna posiadać jedno główne miejsce przechowywania.

Przykładowo:

* historia zatrudnienia należy do Experience,
* osiągnięcia należą do Achievements,
* kompetencje należą do Skills,
* narracje należą do Stories,
* obszary rozwoju należą do Development Areas,
* okresy bez udokumentowanych osiągnięć należą do Context Entries.

Należy unikać duplikowania informacji pomiędzy modułami.

---

## Wielokrotne wykorzystanie

Career Vault powinien umożliwiać tworzenie różnych materiałów na podstawie tych samych danych.

Przykładowe zastosowania:

* CV,
* profil LinkedIn,
* portfolio zawodowe,
* odpowiedzi na pytania rekrutacyjne,
* analiza kompetencji,
* plan rozwoju zawodowego,
* profile eksperckie,
* prezentacje doświadczenia.

Repozytorium przechowuje wiedzę źródłową.

Dokumenty końcowe są generowane na jej podstawie.

---

## Podejście długoterminowe

Career Vault jest projektem rozwijanym przez całą karierę zawodową.

Pliki powinny zawierać informacje trwałe, możliwe do wykorzystania również za wiele lat.

Repozytorium powinno z czasem zwiększać swoją wartość, a nie poziom skomplikowania.

---

## Warstwa poznawcza

Career Vault nie przechowuje wyłącznie faktów dotyczących kariery zawodowej.

Zawiera również moduł **Assessment**, którego celem jest budowa modelu wyjaśniającego sposób podejmowania decyzji, rozwiązywania problemów oraz przetwarzania informacji.

Assessment wykorzystuje dane zgromadzone w całym Career Vault oraz wyniki ustrukturyzowanych narzędzi pomiarowych do identyfikacji mechanizmów poznawczych, powtarzalnych wzorców zachowań oraz budowy rozwijanego w czasie Cognitive Model.

Podczas gdy pozostałe moduły odpowiadają przede wszystkim na pytanie:

> **Co wydarzyło się w mojej karierze?**

Assessment odpowiada na pytanie:

> **Dlaczego najprawdopodobniej działałem właśnie w taki sposób i jak mogę działać w przyszłości?**


---

## Warstwa interpretacyjna

Career Vault przechowuje nie tylko dane źródłowe, ale również ich interpretację.

Funkcję tę pełnią dokumenty takie jak:

* Identity
* AI Interpretation Guide

Ich zadaniem nie jest dostarczanie nowych faktów.

Ich rolą jest synteza informacji pochodzących z pozostałych modułów oraz identyfikowanie wzorców pojawiających się w historii zawodowej.

Dzięki temu zarówno ludzie, jak i systemy AI mogą szybciej zrozumieć znaczenie zgromadzonych danych oraz ograniczyć ryzyko błędnej interpretacji pojedynczych doświadczeń.

---

# Model wiedzy Career Vault

Career Vault przechowuje wiedzę na wielu poziomach abstrakcji.

```text
Experience
↓
Kontekst kariery

Achievements
↓
Dowody osiągnięć

Skills
↓
Kompetencje wynikające z osiągnięć

Stories
↓
Narracje opisujące doświadczenia

Development Areas
↓
Powtarzalne wzorce rozwojowe

Identity
↓
Profesjonalna tożsamość wynikająca z całości zgromadzonej wiedzy
```

Każda warstwa odpowiada na inne pytanie i pełni inną rolę.

---

# Struktura repozytorium

```text
CareerVault/

├── README.md
├── About.md
├── Identity.md
├── AI Interpretation Guide.md
├── Experience.md
├── Assessments/
│   ├── README.md
│   ├── Assessment Data.md
│   ├── Cognitive model.md
│   ├── Calibrations/
│   ├── Predictors/
│   ├── Behavioral Patterns/
│
├── Achievements/
│   ├── README.md
│   ├── ACH-001.yaml
│   └── ...
│
├── Skills/
│   ├── README.md
│   ├── SKILL-001.yaml
│   └── ...
│
├── Stories/
│   ├── README.md
│   ├── STORY-001.yaml
│   └── ...
│
├── Development Areas/
│   ├── README.md
│   ├── DEV-001.yaml
│   └── ...
│
├── Context Entries/
│   ├── README.md
│   ├── CTX-001.yaml
│   └── ...
│
└── scripts/
    ├── vault_model.py
    ├── build_index.py
    └── build_vault.py
```

---

# Elementy Career Vault

## Identity

Odpowiada na pytanie:

> Kim jestem jako profesjonalista?

Zawiera między innymi:

* profil zawodowy,
* archetypy zawodowe,
* wartości zawodowe,
* mocne strony,
* branże,
* styl pracy,
* języki,
* certyfikaty,
* zainteresowania zawodowe,
* obszary rozwoju.

Identity jest warstwą syntetyzującą wiedzę zgromadzoną w pozostałych modułach.

---

## Experience

Odpowiada na pytanie:

> Gdzie zdobywałem doświadczenie?

Zawiera:

* historię zatrudnienia,
* pełnione role,
* zakresy odpowiedzialności,
* rozwój kariery.

Experience dostarcza kontekstu.

Nie jest głównym źródłem osiągnięć.

---

## Achievements

Odpowiadają na pytanie:

> Co osiągnąłem?

Są podstawowym źródłem dowodów w Career Vault.

Zawierają:

* projekty,
* usprawnienia,
* transformacje,
* wdrożenia,
* rezultaty biznesowe,
* wpływ organizacyjny,
* mierzalne efekty.

Achievements stanowią fundament całego repozytorium.

---

## Skills

Odpowiadają na pytanie:

> Co potrafię i jakie mam na to dowody?

Każdy Skill powinien być powiązany z odpowiednimi Achievementami.

Skills pełnią rolę warstwy kompetencyjnej pomiędzy osiągnięciami a materiałami końcowymi.

---

## Stories

Odpowiadają na pytanie:

> Jak opowiadać o swoim doświadczeniu?

Stories opisują doświadczenia w formie narracji.

Każda Story powinna być powiązana z jednym lub większą liczbą Achievementów.

Stories służą do:

* rozmów kwalifikacyjnych,
* rozmów rozwojowych,
* ocen okresowych,
* prezentowania doświadczenia zawodowego,
* pracy z AI.

Stories nie są źródłem prawdy.

Źródłem prawdy pozostają Achievementy.

---

## Development Areas

Odpowiadają na pytanie:

> Jakie wzorce obserwuję u siebie i nad czym świadomie pracuję?

Development Areas dokumentują:

* powtarzalne wzorce zachowań,
* obszary rozwoju,
* ryzyka zawodowe,
* mocne strony wynikające z danego wzorca,
* kluczowe lekcje zawodowe.

Development Areas nie są listą wad.

Stanowią uporządkowany zapis doświadczeń rozwojowych wynikających z analizy Stories i Achievementów.

---

## Context Entries

Odpowiadają na pytanie:

> Dlaczego ten okres kariery nie posiada udokumentowanych Achievementów?

Context Entries opisują etapy kariery, które świadomie nie wygenerowały materiału dowodowego — role wykonawcze, początki kariery, krótkie epizody zawodowe, okresy adaptacji.

Ich zadaniem jest zachowanie ciągłości osi czasu bez przypisywania tym okresom znaczenia, którego nie posiadają.

Context Entry nie jest źródłem dowodów.

Nie służy do wyprowadzania kompetencji, uzasadniania Predictorów, Behavioral Patterns ani Cognitive Model. Zapisuje wyłącznie to, co autor pamięta, oddzielając fakty od interpretacji i zachowując niepewność tam, gdzie ona występuje.

Każdy rekord kończy się polem `do_not_use_as: evidence`, które stanowi podstawową zasadę interpretacji całego artefaktu.

---

## AI Interpretation Guide

Odpowiada na pytanie:

> Jak interpretować zgromadzone informacje?

AI Interpretation Guide jest dokumentem przeznaczonym przede wszystkim dla systemów AI.

Opisuje:

* dominujące wzorce zawodowe,
* preferowany sposób działania,
* charakterystyczne kompetencje,
* typowe role organizacyjne,
* mocne strony,
* ograniczenia interpretacyjne,
* rekomendowany sposób analizy repozytorium.

AI Interpretation Guide nie jest źródłem nowych informacji.

Jest warstwą interpretacyjną opartą na istniejących danych.

---

# Relacje pomiędzy modułami

Career Vault jest systemem powiązanych informacji.

Przykładowa zależność:

```text
Experience
↓
Achievement
↓
Skill
↓
Story
↓
Development Area
↓
Identity
```

Dzięki temu każda informacja może zostać prześledzona do źródła.

---

# Hierarchia informacji

Przy analizie doświadczenia oraz generowaniu materiałów zawodowych należy stosować następującą kolejność:

1. Achievements
2. Skills
3. Stories
4. Development Areas
5. Experience
6. Identity

Achievements pozostają głównym źródłem dowodów.

Pozostałe moduły dostarczają interpretacji, kontekstu lub sposobu prezentacji informacji.

Context Entries świadomie znajdują się poza tą hierarchią. Nie są źródłem dowodów i nie należy wykorzystywać ich do wyprowadzania kompetencji ani wniosków — pełnią wyłącznie funkcję kontekstu chronologicznego.

---

# Współpraca z AI

Career Vault od początku był rozwijany we współpracy z modelami językowymi (LLM).

Modele AI nie były wykorzystywane jako narzędzie do automatycznego generowania treści, lecz jako partner analityczny wspierający proces dokumentowania doświadczeń, porządkowania wiedzy, krytycznej analizy oraz projektowania architektury całego repozytorium.

Każdy element Career Vault pozostaje odpowiedzialnością autora.

AI pełniło rolę:

- sparring partnera podczas analizy doświadczeń,
- recenzenta pomagającego wykrywać niespójności,
- współprojektanta struktury wiedzy,
- narzędzia wspierającego formalizację wiedzy ukrytej,
- akceleratora procesu iteracyjnego doskonalenia repozytorium.

Jedną z podstawowych zasad projektu było traktowanie modeli AI jako uczestnika procesu poznawczego, a nie źródła prawdy.

Wszystkie istotne wnioski były wielokrotnie weryfikowane, konfrontowane z dowodami oraz testowane przy użyciu różnych modeli językowych i odmiennych sposobów analizy.

Dzięki temu Career Vault nie jest wyłącznie bazą wiedzy przeznaczoną do współpracy z AI.

Jest również przykładem, w jaki sposób człowiek i modele językowe mogą wspólnie budować uporządkowaną, opartą na dowodach reprezentację wiedzy zawodowej.

## Rekomendowany sposób wykorzystania przez AI

Podczas analizy repozytorium zaleca się następującą kolejność:

1. Zapoznaj się z **AI Interpretation Guide**, aby zrozumieć metodologię analizy.
2. Przeanalizuj **Identity** w celu poznania syntetycznego obrazu zawodowego.
3. W razie potrzeby przeanalizuj moduł **Assessment**, aby zrozumieć model poznawczy i mechanizmy decyzyjne.
4. Zweryfikuj wnioski na podstawie **Achievements**, **Stories**, **Skills** oraz **Experience**.
5. Uwzględnij **Development Areas**, aby zachować pełny i zrównoważony obraz.
6. W razie potrzeby sięgnij po **Context Entries**, aby wyjaśnić luki w osi czasu — wyłącznie jako kontekst, nigdy jako dowód.
7. Dopiero na tej podstawie generuj odpowiedzi, rekomendacje lub dokumenty.

Przykładowe zastosowania obejmują:

- generowanie CV i profili LinkedIn,
- przygotowanie do rozmów kwalifikacyjnych,
- analizę kompetencji i doświadczenia,
- planowanie rozwoju zawodowego,
- dopasowanie do ról i stanowisk,
- coaching oraz mentoring wspierany przez AI,
- budowę agentów AI i systemów typu RAG opartych na Career Vault.

---

# Konwencje danych

## Identyfikatory

Każdy rekord powinien posiadać unikalny identyfikator.

Przykłady:

```text
ACH-001
SKILL-001
STORY-001
DEV-001
```

Identyfikatory powinny być niezmienne w czasie.

---

## Daty

Dla okresów należy stosować format:

```yaml
period:
  start: 2023-09
  end: current
```

lub

```yaml
period:
  start: 2020-02
  end: 2023-04
```

Domyślnie Career Vault przechowuje daty na poziomie lat.

Miesiące powinny być stosowane wyłącznie wtedy, gdy mają znaczenie biznesowe lub historyczne.

---

## Zasady jakości

Podczas dodawania nowych informacji:

1. Opieraj się na faktach i dowodach.
2. Preferuj mierzalne rezultaty.
3. Unikaj duplikowania informacji.
4. Zachowuj spójne nazewnictwo.
5. Łącz Skills z Achievementami.
6. Łącz Stories z Achievementami.
7. Łącz Development Areas ze Stories i Achievementami.
8. Oddzielaj fakty od interpretacji.
9. Preferuj jakość nad ilość.
10. Rozwijaj repozytorium stopniowo.

---

# Najważniejsza zasada

Career Vault przechowuje wiedzę na różnych poziomach abstrakcji.

Experience opisuje kontekst kariery.

Achievements opisują faktyczne osiągnięcia.

Skills opisują kompetencje potwierdzone osiągnięciami.

Stories pokazują, jak o doświadczeniach opowiadać.

Development Areas pokazują, jakie wzorce rozwojowe wynikają z doświadczeń.

Identity opisuje profesjonalną tożsamość wynikającą z całości zgromadzonej wiedzy.

Context Entries zachowują pamięć o okresach, które nie wygenerowały dowodów — bez udawania, że je posiadają.

Najważniejszym źródłem prawdy pozostają Achievementy.
