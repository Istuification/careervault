# Achievements

## Cel

Folder **Achievements** zawiera najważniejsze osiągnięcia zawodowe i prywatne zgromadzone w ramach Career Vault.

Achievement jest pojedynczym, możliwym do udokumentowania rezultatem, projektem, usprawnieniem, wdrożeniem lub zmianą, która miała zauważalny wpływ na organizację, zespół, produkt, proces lub życie prywatne.

Achievements stanowią główne źródło dowodów w całym Career Vault.

---

# Rola Achievements w Career Vault

Career Vault składa się z pięciu warstw:

```text
Identity
↓
Kim jestem?

Experience
↓
Gdzie zdobyłem doświadczenie?

Achievements
↓
Co osiągnąłem?

Skills
↓
Jakie kompetencje pokazują te osiągnięcia?

Stories
↓
Jak o tym opowiadać?
```

Achievements są fundamentem całego systemu.

Wszystkie pozostałe elementy powinny opierać się na zawartych tutaj informacjach.

---

# Czym jest Achievement?

Achievement opisuje konkretny rezultat osiągnięty w określonym czasie.

Dobry Achievement:

* opisuje rzeczywiste działanie,
* posiada kontekst,
* wskazuje zastosowane kompetencje,
* zawiera rezultaty,
* może być wykorzystany jako dowód doświadczenia.

Przykłady:

* transformacja działu,
* wdrożenie systemu,
* stworzenie procesu,
* organizacja wydarzenia,
* budowa bazy wiedzy,
* usprawnienie organizacji.

---

# Fakty ponad deklaracje

Achievements powinny opierać się na faktach.

Przykład:

❌ „Jestem dobrym liderem”

✅ „Przeprowadziłem reorganizację działu serwisu i ustabilizowałem jego pracę”

Kompetencje powinny wynikać z osiągnięć, a nie odwrotnie.

---

# Rodzaje Achievementów

## Zawodowe

Identyfikator:

```text
ACH-001
ACH-002
...
```

Dotyczą doświadczenia zawodowego, działalności biznesowej oraz projektów realizowanych w pracy.

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

# Schemat rekordu

Każdy Achievement powinien zawierać następujące pola:

```yaml
id:

title:

period:
  start:
  end:

summary:

skills:

themes:

actions:

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

Lista najważniejszych działań podjętych podczas realizacji.

Przykład:

```yaml
actions:
  - przeanalizowanie procesu
  - stworzenie dokumentacji
  - wdrożenie nowego workflow
```

---

## impact

Rezultaty osiągnięcia.

Preferowane są rezultaty mierzalne.

Przykład:

```yaml
impact:
  - 70% mniej błędów
  - skrócenie czasu realizacji
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
  - Wiki.js
  - Excel
```

---

## evidence

Dodatkowe informacje potwierdzające osiągnięcie.

Przykład:

```yaml
evidence:
  - wdrożono w całej organizacji
  - objęto 250 partnerów
```

---

## notes

Dodatkowy kontekst wymagający wyjaśnienia.

Przykład:

```yaml
notes:
  - daty są przybliżone
  - projekt realizowany samodzielnie
```

---

# Relacja do pozostałych elementów Career Vault

## Experience

Dostarcza kontekstu.

## Achievements

Dostarczają dowodów.

## Skills

Grupują osiągnięcia w kompetencje.

## Stories

Przekształcają osiągnięcia w narrację STAR.

---

# Zasady utrzymania

1. Jeden Achievement powinien opisywać jedno osiągnięcie.
2. Preferuj rezultaty zamiast obowiązków.
3. Preferuj fakty zamiast opinii.
4. Unikaj duplikowania informacji.
5. Dodawaj mierzalne rezultaty, gdy są dostępne.
6. Łącz Achievementy ze Skillami.
7. Aktualizuj rekordy, gdy pojawią się nowe informacje.

---

# Najważniejsza zasada

Achievement nie opisuje tego, za co odpowiadałem.

Achievement opisuje to, co udało mi się osiągnąć.
