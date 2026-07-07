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

Achievement opisuje rezultat, zmianę lub wpływ wykraczający poza samo wykonywanie obowiązków.

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

## Struktura rekordu

### Pola obowiązkowe

```yaml
id:
title:

period:
  start:
  end:

company:
roles:

situation:
actions:
impact:

skills:
themes:

importance:
```

### Pola opcjonalne

```yaml
category:
evidence:
metrics:
related_tools:
star_candidates:
notes:
```

---

## Opis pól

### id

Unikalny identyfikator rekordu.

Przykład:

```yaml
id: ACH-001
```

---

### title

Krótka nazwa osiągnięcia.

Powinna opisywać rezultat lub inicjatywę.

Przykład:

```yaml
title: Wdrożenie systemu KPI dla działu handlowego
```

---

### period

Okres, w którym osiągnięcie miało miejsce.

Przykład:

```yaml
period:
  start: 2022-01
  end: 2022-12
```

Jeżeli osiągnięcie trwało przez dłuższy okres, należy podać pełny zakres.

---

### company

Organizacja, w której osiągnięcie zostało zrealizowane.

Przykład:

```yaml
company: KIPI
```

---

### roles

Stanowiska lub role pełnione podczas realizacji osiągnięcia.

Przykład:

```yaml
roles:
  - Product Manager
  - Operations Manager
```

---

### situation

Krótki opis sytuacji wyjściowej.

Odpowiada na pytanie:

> W jakim kontekście wystąpiło osiągnięcie?

Przykład:

```yaml
situation: >
  Firma nie posiadała spójnego systemu raportowania wyników sprzedaży.
```

---

### actions

Opis podjętych działań.

Odpowiada na pytanie:

> Co konkretnie zrobiłem?

Przykład:

```yaml
actions:
  - Zmapowałem proces sprzedaży.
  - Zdefiniowałem kluczowe wskaźniki.
  - Wdrożyłem cykliczne raportowanie.
```

---

### impact

Opis rezultatów i efektów działań.

Odpowiada na pytanie:

> Co zmieniło się dzięki tym działaniom?

Przykład:

```yaml
impact:
  - Zwiększono przejrzystość procesu sprzedaży.
  - Skrócono czas przygotowania raportów.
  - Ułatwiono identyfikację problemów operacyjnych.
```

---

### skills

Kompetencje potwierdzane przez achievement.

Wartości powinny odpowiadać identyfikatorom z modułu `Skills`.

Przykład:

```yaml
skills:
  - process-design
  - workflow-automation
  - data-analysis
```

---

### themes

Tematy lub obszary, których dotyczy achievement.

Themes opisują kontekst, a nie kompetencje.

Przykład:

```yaml
themes:
  - operations
  - reporting
  - sales
```

---

### importance

Ocena znaczenia achievementu.

Rekomendowana skala:

```yaml
importance: 10
```

Gdzie:

| Wartość | Znaczenie                |
| ------- | ------------------------ |
| 9–10    | Kluczowe osiągnięcie     |
| 7–8     | Bardzo ważne osiągnięcie |
| 5–6     | Istotne osiągnięcie      |
| 1–4     | Osiągnięcie pomocnicze   |

Pole służy do priorytetyzacji przy budowie CV, Stories i analizie AI.

---

### category

Opcjonalna kategoria nadrzędna.

Przykłady:

```yaml
category: operations
```

```yaml
category: leadership
```

```yaml
category: product
```
### fin (opcjonalne)

Lista analiz finansowych rekordu. Każda analiza zawiera: `id` (FIN-XXX),
`value_type` (Capacity Release / Cost Avoidance / Reduced Lead Time /
Strategic Enablement), wycenę (`estimated_value`, `quantified` lub
`unit_value_pln`), `calculation` (jawny wzór), `assumptions` (wszystkie
założenia), `confidence` oraz obowiązkową notę: "Szacunek własny metodą X;
nie są to dane księgowe firmy". Wartości podajemy w widełkach,
zaokrąglając konserwatywnie. Nie sumujemy nakładających się oszczędności.

### org (opcjonalne)

Sekcja opisująca zmianę zdolności organizacji: `operational` / `strategic`
lub `capability: from -> to`. Stosowana tam, gdzie zmiana modelu działania
jest wartością samą w sobie, niezależną od wyceny finansowej.
---

### evidence

Dowody potwierdzające achievement.

Mogą to być:

* raporty,
* dashboardy,
* procedury,
* prezentacje,
* dokumentacja,
* wyniki biznesowe,
* inne artefakty pracy.

Przykład:

```yaml
evidence:
  - KPI dashboard
  - Monthly sales report
  - Internal process documentation
```

---

### metrics

Mierzalne wyniki achievementu.

Przykład:

```yaml
metrics:
  reporting_time:
    before: 4h
    after: 20m

  conversion_rate:
    improvement: "+18%"
```

---

### related_tools

Narzędzia wykorzystane podczas realizacji.

Przykład:

```yaml
related_tools:
  - Excel
  - Power BI
  - ERP
```

---

### star_candidates

Elementy szczególnie przydatne przy budowie Story.

Przykład:

```yaml
star_candidates:
  - problem: brak raportowania
  - action: wdrożenie KPI
  - result: szybsze decyzje
```

---

### notes

Dodatkowe informacje pomocnicze.

Pole nie powinno zawierać kluczowych danych, które powinny znaleźć się w polach głównych.

---

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

