# Career Vault

## Cel

Career Vault to osobista baza wiedzy zawodowej służąca do gromadzenia, organizowania i wyszukiwania informacji o doświadczeniu, osiągnięciach, kompetencjach oraz rozwoju zawodowym.

Repozytorium stanowi pojedyncze źródło prawdy dla:

* generowania CV,
* przygotowania do rozmów kwalifikacyjnych,
* analizy kompetencji,
* planowania rozwoju zawodowego,
* budowy portfolio osiągnięć,
* współpracy z systemami AI,
* zarządzania wiedzą o własnej karierze.

Celem Career Vault nie jest przechowywanie gotowych CV, lecz budowanie trwałej bazy faktów, dowodów i doświadczeń, które mogą być wielokrotnie wykorzystywane w różnych kontekstach.

---

# Główne założenia

## Fakty ponad deklaracje

Repozytorium powinno opierać się na dowodach, a nie opiniach.

Przykład:

❌ „Jestem dobrym liderem”

✅ „Przeprowadziłem transformację działu i ustabilizowałem jego pracę”

Każda kompetencja powinna być możliwa do powiązania z konkretnymi osiągnięciami.

---

## Jedno źródło informacji

Każda informacja powinna mieć jedno główne miejsce przechowywania.

Przykładowo:

* historia zatrudnienia należy do Experience,
* osiągnięcia należą do Achievements,
* kompetencje należą do Skills,
* historie STAR należą do Stories.

Należy unikać duplikowania informacji pomiędzy plikami.

---

## Wielokrotne wykorzystanie

Career Vault powinien umożliwiać tworzenie różnych materiałów na podstawie tych samych danych:

* CV,
* profilu LinkedIn,
* listów motywacyjnych,
* odpowiedzi na pytania rekrutacyjne,
* portfolio zawodowego,
* analiz kompetencji.

Repozytorium przechowuje fakty i dowody. Dokumenty końcowe są tworzone na ich podstawie.

---

## Podejście długoterminowe

Career Vault jest projektem rozwijanym przez całą karierę zawodową.

Pliki powinny zawierać informacje trwałe i wartościowe również za kilka lat.

---

# Struktura repozytorium

```text
CareerVault/

├── README.md
├── Identity.md
├── Experience.md
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
└── Stories/
    ├── README.md
    ├── STAR-001.yaml
    └── ...
```

---

# Elementy Career Vault

## Identity

Odpowiada na pytanie:

> Kim jestem jako profesjonalista?

Zawiera między innymi:

* profil zawodowy,
* mocne strony,
* branże,
* styl pracy,
* języki,
* certyfikaty,
* zainteresowania zawodowe.

Identity opisuje tożsamość zawodową.

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

Są najważniejszą częścią Career Vault.

Zawierają:

* projekty,
* usprawnienia,
* transformacje,
* wdrożenia,
* rezultaty biznesowe,
* wpływ organizacyjny,
* mierzalne efekty.

Achievements stanowią główne źródło dowodów kompetencji.

---

## Skills

Odpowiadają na pytanie:

> Co potrafię i jakie mam na to dowody?

Każdy skill powinien być powiązany z odpowiednimi achievementami.

Skills pełnią rolę warstwy kompetencyjnej pomiędzy osiągnięciami a dokumentami końcowymi.

---

## Stories

Odpowiadają na pytanie:

> Jak opowiadać o swoim doświadczeniu?

Stories są historiami przygotowanymi według modelu STAR:

* Situation
* Task
* Action
* Result

Każda Story powinna być powiązana z jednym lub większą liczbą achievementów.

Stories służą do:

* rozmów kwalifikacyjnych,
* rozmów rozwojowych,
* ocen okresowych,
* prezentowania doświadczenia zawodowego,
* pracy z AI.

Stories nie są źródłem prawdy.

Źródłem prawdy pozostają Achievementy.

Stories są sposobem przedstawiania osiągnięć w formie narracji.

---

# Hierarchia informacji

Przy generowaniu materiałów zawodowych należy stosować następującą kolejność:

1. Achievements
2. Skills
3. Stories
4. Experience
5. Identity

Achievements są głównym źródłem dowodów.

Skills opisują kompetencje wynikające z osiągnięć.

Stories pomagają przedstawić osiągnięcia w formie narracji.

Experience dostarcza kontekstu.

Identity opisuje profil zawodowy.

---

# Współpraca z AI

Career Vault został zaprojektowany tak, aby mógł współpracować z systemami AI, bazami wiedzy oraz rozwiązaniami typu RAG.

Rekomendowany proces:

1. Określenie wymaganych kompetencji.
2. Wyszukanie odpowiednich skills.
3. Odnalezienie powiązanych achievements.
4. Wyszukanie odpowiednich stories.
5. Wygenerowanie dokumentu lub odpowiedzi.

Przykładowe zastosowania:

* generowanie CV,
* przygotowanie do rozmów kwalifikacyjnych,
* analiza kompetencji,
* planowanie rozwoju zawodowego,
* identyfikacja luk kompetencyjnych.

---

# Konwencje danych

## Struktura rekordów

Career Vault wykorzystuje wspólną filozofię:

- pola obowiązkowe zawierają informacje niezbędne do zrozumienia rekordu,
- pola opcjonalne służą do przechowywania dodatkowego kontekstu,
- brak pola oznacza brak dostępnych informacji, a nie błąd.

Szczegółowe schematy znajdują się w README poszczególnych folderów.

---

## Daty w Experience, Achievements i Stories

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

Career Vault przechowuje daty domyślnie na poziomie lat.

Dokładne miesiące powinny być używane wyłącznie wtedy, gdy mają istotne znaczenie.

---

## Doświadczenie w Skills

Dla opisu doświadczenia należy stosować format:

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

## Identyfikatory

Każdy rekord powinien posiadać unikalny identyfikator.

Przykłady:

```text
ACH-001
ACH-P001

SKILL-001

STAR-001
```

Identyfikatory powinny być niezmienne w czasie.

---

# Zasady utrzymania

Podczas dodawania nowych informacji:

1. Opieraj się na faktach i dowodach.
2. Preferuj mierzalne rezultaty.
3. Unikaj duplikatów.
4. Zachowuj spójne nazewnictwo.
5. Łącz skille z achievementami.
6. Łącz stories z achievementami.
7. Rozwijaj repozytorium stopniowo.

Career Vault powinien z czasem stawać się coraz bardziej wartościowy, a nie coraz bardziej skomplikowany.

---

# Najważniejsza zasada

Stanowiska opisują, gdzie pracowałem.

Achievements opisują, co osiągnąłem.

Skills opisują, jakie kompetencje potwierdzają osiągnięcia.

Stories opisują, jak o tych osiągnięciach opowiadać.

To osiągnięcia są podstawowym źródłem wartości Career Vault.
