# Stories

## Cel

Folder **Stories** zawiera historie przygotowane według modelu STAR (Situation, Task, Action, Result).

Stories służą do przekształcania osiągnięć zapisanych w Career Vault w gotowe narracje, które mogą zostać wykorzystane podczas:

* rozmów kwalifikacyjnych,
* rozmów rozwojowych,
* ocen okresowych,
* prezentacji doświadczenia zawodowego,
* pracy z systemami AI.

Stories nie są źródłem prawdy.

Źródłem prawdy pozostają Achievementy.

Stories są sposobem przedstawiania osiągnięć w formie narracji.

---

# Rola Stories w Career Vault

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

Stories są ostatnią warstwą systemu.

Ich zadaniem jest zamiana faktów, działań i rezultatów na spójną historię pokazującą sposób myślenia, podejmowania decyzji i rozwiązywania problemów.

---

# Model STAR

Każda Story powinna wykorzystywać model STAR.

## Situation

Opis sytuacji lub problemu.

Odpowiada na pytanie:

> Jaki był kontekst?

---

## Task

Opis celu, odpowiedzialności lub wyzwania.

Odpowiada na pytanie:

> Co należało osiągnąć?

---

## Action

Opis konkretnych działań.

Odpowiada na pytanie:

> Co zrobiłem?

Sekcja Action jest najważniejszą częścią Story.

To właśnie ona pokazuje kompetencje oraz sposób działania.

---

## Result

Opis rezultatów.

Odpowiada na pytanie:

> Jaki był efekt?

Preferowane są rezultaty mierzalne.

---

# Schemat rekordu

Każda Story powinna być zapisana jako osobny plik YAML.

```yaml
id:

title:

achievement:

skills:

themes:

period:
  start:
  end:

situation:

task:

actions:

result:

key_takeaway:
```

---

# Opis pól

## id

Unikalny identyfikator historii.

Przykłady:

```text
STAR-001
STAR-002
STAR-015
```

Identyfikator powinien pozostać niezmienny przez cały czas życia repozytorium.

---

## title

Krótka nazwa historii.

Powinna jednoznacznie wskazywać, czego dotyczy Story.

Przykład:

```text
Transformacja działu Instal/Solar
```

---

## achievement

Powiązane achievementy stanowiące źródło faktów.

Przykład:

```yaml
achievement:
  - ACH-001
```

lub

```yaml
achievement:
  - ACH-003
  - ACH-014
```

Każda Story musi być powiązana z co najmniej jednym Achievementem.

---

## skills

Kompetencje wykorzystywane w historii.

Przykład:

```yaml
skills:
  - SKILL-001
  - SKILL-002
  - SKILL-012
```

---

## themes

Tematy przewodnie historii.

Przykład:

```yaml
themes:
  - leadership
  - change-management
  - transformation
```

Themes pomagają wyszukiwać historie odpowiadające konkretnym pytaniom.

---

## period

Okres, którego dotyczy historia.

Przykład:

```yaml
period:
  start: 2023
  end: 2025
```

lub

```yaml
period:
  start: 2025
  end: current
```

Career Vault przechowuje daty domyślnie na poziomie lat.

---

## situation

Opis sytuacji wyjściowej.

Powinien być krótki i skupiony na kontekście.

---

## task

Opis celu lub problemu do rozwiązania.

Powinien jasno wskazywać odpowiedzialność.

---

## actions

Lista najważniejszych działań.

Przykład:

```yaml
actions:
  - przeanalizowanie procesu
  - stworzenie dokumentacji BPMN
  - wdrożenie nowego workflow
```

---

## result

Rezultaty osiągnięte dzięki działaniom.

Przykład:

```yaml
result:
  - skrócenie czasu realizacji
  - poprawa jakości danych
  - standaryzacja procesu
```

---

## key_takeaway

Najważniejszy wniosek płynący z historii.

Powinien odpowiadać na pytanie:

> Czego nauczyła mnie ta sytuacja?

---

# Zasady tworzenia Stories

## Jedna Story = jedna historia

Każda Story powinna opisywać jeden konkretny przykład.

Dobra Story:

* transformacja działu,
* wdrożenie systemu,
* rozwiązanie kryzysu,
* przeprowadzenie zmiany organizacyjnej.

Nie należy łączyć wielu niezależnych sytuacji w jedną historię.

---

## Story musi mieć źródło

Każda Story musi być powiązana z co najmniej jednym Achievementem.

Story nie może zawierać informacji, których nie da się potwierdzić w Achievementach.

---

## Skupienie na działaniach

Największa wartość Story znajduje się w sekcji Action.

To właśnie ona pokazuje:

* sposób myślenia,
* podejmowanie decyzji,
* kompetencje,
* podejście do problemów.

---

## Rezultat jest obowiązkowy

Każda Story musi kończyć się rezultatem.

Preferowane są:

* liczby,
* oszczędności,
* skrócenie czasu,
* poprawa jakości,
* wzrost efektywności,
* poprawa organizacji.

---

# Typowe zastosowania

Stories powinny umożliwiać szybkie przygotowanie odpowiedzi na pytania takie jak:

* Opowiedz o największym sukcesie zawodowym.
* Opowiedz o trudnej zmianie organizacyjnej.
* Opowiedz o sytuacji kryzysowej.
* Opowiedz o projekcie, z którego jesteś najbardziej dumny.
* Opowiedz o konflikcie w zespole.
* Opowiedz o błędzie, który popełniłeś.
* Opowiedz o wdrożeniu nowego rozwiązania.
* Opowiedz o sytuacji wymagającej przywództwa.

Jedna Story może odpowiadać na wiele różnych pytań.

---

# Relacja do pozostałych elementów Career Vault

## Identity

Opisuje profil zawodowy.

## Experience

Dostarcza kontekstu.

## Achievements

Stanowią źródło faktów.

## Skills

Opisują kompetencje wykorzystane w historii.

## Stories

Przekształcają osiągnięcia w narrację STAR.

---

# Zasady utrzymania

1. Każda Story musi być powiązana z Achievementem.
2. Nie twórz Story bez dowodów.
3. Nie duplikuj treści Achievementów.
4. Skupiaj się na działaniach i decyzjach.
5. Pokazuj rezultaty.
6. Łącz Stories ze Skills.
7. Aktualizuj Stories wraz z rozwojem Career Vault.
8. Preferuj jakość nad liczbę historii.

---

# Najważniejsza zasada

Achievement opisuje fakty.

Story opisuje te same fakty w formie historii, którą można opowiedzieć drugiej osobie.
