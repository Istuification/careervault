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

```yaml
id:

title:

period:
  start:
  end:

summary:

problem:

approach:

skills:

themes:

actions:

result:

impact:

importance:
```

---

# Opis pól

## id

Unikalny identyfikator rekordu.

Przykłady:

```text
ACH-001
ACH-014
ACH-P003
```

Identyfikator powinien pozostać niezmienny przez cały czas życia repozytorium.

---

## title

Krótka nazwa osiągnięcia.

Powinna jasno wskazywać czego dotyczy rekord.

---

## period

Okres realizacji osiągnięcia.

Przykład:

```yaml
period:
  start: 2023
  end: current
```

lub

```yaml
period:
  start: 2020
  end: 2023
```

Career Vault przechowuje daty domyślnie na poziomie lat.

---

## summary

Krótki opis osiągnięcia.

Powinien odpowiadać na pytanie:

> Co zostało osiągnięte?

---

## problem

Jaki problem, potrzeba lub wyzwanie doprowadziło do realizacji osiągnięcia?

---

## approach

W jaki sposób podszedłem do rozwiązania problemu?

Opis głównej strategii działania.

---

## skills

Lista kompetencji wykorzystanych podczas realizacji.

Przykład:

```yaml
skills:
  - process-design
  - leadership
  - operations-management
```

---

## themes

Lista głównych tematów związanych z osiągnięciem.

Przykład:

```yaml
themes:
  - transformation
  - automation
  - knowledge-management
```

---

## actions

Najważniejsze działania wykonane podczas realizacji.

Przykład:

```yaml
actions:
  - analiza procesu
  - stworzenie dokumentacji
  - wdrożenie nowego workflow
```

---

## result

Bezpośredni rezultat osiągnięcia.

Co zostało dostarczone lub wdrożone?

---

## impact

Wpływ biznesowy, organizacyjny lub operacyjny.

Preferowane są rezultaty mierzalne.

Przykład:

```yaml
impact:
  - skrócenie czasu realizacji
  - zmniejszenie liczby błędów
  - poprawa jakości danych
```

---

## importance

Znaczenie osiągnięcia w skali od 1 do 10.

### 10

Osiągnięcie definiujące karierę.

### 8–9

Bardzo ważne osiągnięcie.

### 6–7

Istotne osiągnięcie.

### 1–5

Osiągnięcie wspierające.

---

# Pola opcjonalne

## related_tools

Narzędzia wykorzystane podczas realizacji.

Przykład:

```yaml
related_tools:
  - Bitrix24
  - Excel
  - Wiki.js
```

---

## evidence

Dodatkowe informacje potwierdzające osiągnięcie.

Przykład:

```yaml
evidence:
  - wdrożono w całej organizacji
  - wykorzystywane przez kilka działów
```

---

## related_stories

Powiązane Stories.

Przykład:

```yaml
related_stories:
  - STORY-005
```

---

## related_development_areas

Powiązane Development Areas.

Przykład:

```yaml
related_development_areas:
  - DEV-001
```

---

## notes

Dodatkowy kontekst wymagający wyjaśnienia.

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
