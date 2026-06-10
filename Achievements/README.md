# Achievements

## Cel

Folder **Achievements** zawiera najważniejsze osiągnięcia zawodowe i prywatne zgromadzone w ramach Career Vault.

Achievement jest pojedynczym, możliwym do udokumentowania osiągnięciem, projektem, usprawnieniem, wdrożeniem, transformacją lub zmianą, która wywarła zauważalny wpływ na organizację, zespół, produkt, proces lub rozwój osobisty.

Achievements stanowią główne źródło dowodów w całym Career Vault.

Jeżeli Experience dostarcza kontekstu, a Skills opisują kompetencje, to Achievements odpowiadają na pytanie:

> Co faktycznie zostało osiągnięte?

---

# Rola Achievements w Career Vault

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

Achievements są fundamentem całego systemu.

Wszystkie pozostałe moduły powinny opierać się na informacjach zapisanych w Achievementach.

---

# Czym jest Achievement?

Achievement opisuje konkretną sytuację, projekt, usprawnienie lub rezultat osiągnięty w określonym kontekście.

Dobry Achievement:

* opisuje rzeczywisty problem lub potrzebę,
* zawiera kontekst biznesowy,
* pokazuje podjęte działania,
* wskazuje zastosowane kompetencje,
* opisuje rezultat,
* dokumentuje wpływ,
* może zostać wykorzystany jako dowód doświadczenia.

Achievement nie opisuje obowiązków.

Achievement opisuje rezultat wykraczający poza standardowy zakres odpowiedzialności.

---

# Fakty ponad deklaracje

Najważniejsza zasada Career Vault:

> Fakty ponad deklaracje.

Przykład:

❌ Jestem dobrym liderem.

✅ Przeprowadziłem restrukturyzację działu serwisu oraz ustabilizowałem jego funkcjonowanie.

Kompetencje powinny wynikać z osiągnięć.

Nie odwrotnie.

---

# Rodzaje Achievementów

## Zawodowe

Identyfikator:

```text
ACH-001
ACH-002
...
```

Dotyczą doświadczenia zawodowego, działalności biznesowej, projektów organizacyjnych, wdrożeń, produktów oraz inicjatyw realizowanych w pracy.

---

## Prywatne

Identyfikator:

```text
ACH-P001
ACH-P002
...
```

Dotyczą działań realizowanych poza pracą zawodową.

Mogą dokumentować kompetencje rozwijane poprzez:

* działalność społeczną,
* organizację wydarzeń,
* hobby,
* projekty prywatne,
* aktywność edukacyjną.

---

# Poziomy wpływu

Achievement może dotyczyć różnych poziomów oddziaływania.

## Indywidualny

Wpływ na własną pracę lub efektywność.

Przykład:

* stworzenie własnego narzędzia automatyzującego pracę.

---

## Zespołowy

Wpływ na sposób pracy zespołu.

Przykład:

* usprawnienie workflow działu.

---

## Działowy

Wpływ na funkcjonowanie całego działu.

Przykład:

* restrukturyzacja działu serwisu.

---

## Organizacyjny

Wpływ na funkcjonowanie całej organizacji.

Przykład:

* wdrożenie systemu wykorzystywanego przez wiele działów.

---

# Schemat rekordu

Każdy Achievement powinien zawierać następujące pola:

### Pola obowiązkowe

```yaml
id:
title:
summary:

situation:
actions:
impact:

skills:
```

### Pola opcjonalne

```yaml
metrics:
related_experience:
related_stories:
related_tools:
notes:
```

---

# Opis pól

### title

Krótka nazwa osiągnięcia.

Powinna opisywać rezultat lub inicjatywę.

Przykład:

```yaml
title: Wdrożenie systemu KPI dla działu handlowego
```

---

### summary

Jedno- lub dwuzdaniowe podsumowanie osiągnięcia.

Powinno pozwalać szybko zrozumieć sens rekordu bez czytania szczegółów.

Przykład:

```yaml
summary: >
  Zaprojektowałem i wdrożyłem system KPI dla działu handlowego,
  który umożliwił monitorowanie efektywności procesu sprzedaży
  i identyfikację głównych wąskich gardeł.
```

---

### situation

Krótki opis sytuacji wyjściowej.

Odpowiada na pytanie:

> W jakim kontekście wystąpiło osiągnięcie?

Przykład:

```yaml
situation: >
  Firma nie posiadała spójnego systemu monitorowania efektywności sprzedaży.
```

---

### actions

Opis wykonanych działań.

Odpowiada na pytanie:

> Co konkretnie zrobiłem?

Przykład:

```yaml
actions:
  - Zidentyfikowałem kluczowe etapy procesu sprzedaży.
  - Zaprojektowałem zestaw KPI.
  - Wdrożyłem cykliczne raportowanie.
```

---

### impact

Opis efektów.

Odpowiada na pytanie:

> Co zmieniło się dzięki tym działaniom?

Przykład:

```yaml
impact:
  - Kierownictwo uzyskało bieżący wgląd w efektywność sprzedaży.
  - Ułatwiono identyfikację problemów procesowych.
  - Powstała podstawa do dalszej optymalizacji działań.
```

---

### skills

Kompetencje potwierdzane przez achievement.

Nazwy powinny pochodzić z modułu Skills.

Przykład:

```yaml
skills:
  - Data Analysis
  - KPI Design
  - Process Improvement
```

---

### metrics (opcjonalne)

Mierzalne rezultaty osiągnięcia.

Przykład:

```yaml
metrics:
  reporting_time:
    before: 4h
    after: 20m

  sales_growth:
    value: "+18%"
```

---

### related_experience (opcjonalne)

Powiązane stanowiska lub role.

Przykład:

```yaml
related_experience:
  - EXP-003
```

---

### related_stories (opcjonalne)

Story wykorzystujące dany achievement jako dowód.

Przykład:

```yaml
related_stories:
  - STORY-002
```

---

### related_tools (opcjonalne)

Narzędzia wykorzystane podczas realizacji.

Przykład:

```yaml
related_tools:
  - Excel
  - Power BI
  - ERP
```

---

### notes (opcjonalne)

Dodatkowy kontekst, obserwacje lub informacje pomocnicze.

Nie powinny zawierać kluczowych danych nieobecnych w głównych sekcjach.

---

# Relacje z pozostałymi modułami

## Experience

Dostarcza kontekstu kariery.

## Achievements

Stanowią źródło dowodów.

## Skills

Opisują kompetencje potwierdzone Achievementami.

## Stories

Przekształcają Achievementy w narrację.

## Development Areas

Powstają na podstawie analizy wielu Achievementów i Stories.

## Identity

Stanowi syntezę wiedzy zgromadzonej w całym Career Vault.

---

# Zasady utrzymania

1. Jeden Achievement powinien opisywać jedno osiągnięcie.
2. Preferuj rezultaty zamiast obowiązków.
3. Preferuj fakty zamiast opinii.
4. Unikaj duplikowania informacji.
5. Dodawaj mierzalne rezultaty, gdy są dostępne.
6. Łącz Achievementy ze Skills.
7. Łącz Achievementy ze Stories.
8. Łącz Achievementy z Development Areas, jeśli stanowią ich źródło.
9. Aktualizuj rekordy, gdy pojawią się nowe informacje.
10. Preferuj jakość nad ilość.

---

# Najważniejsza zasada

Achievement nie opisuje tego, za co odpowiadałem.

Achievement opisuje to, co udało mi się osiągnąć.

Jeżeli czegoś nie można powiązać z konkretnym osiągnięciem, nie powinno stanowić podstawy do budowania kompetencji, narracji ani wniosków rozwojowych.
