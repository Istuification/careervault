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

summary:

competencies:
  -
  -
  -

situation:
problem:
constraints:

goal:

actions:
  -
  -
  -
  -

challenges:
  -
  -

results:
  quantitative:
    -
    -
  qualitative:
    -
    -

evidence:
  achievement_ids:
    -
  supporting_materials:
    -

lessons_learned:
  -
  -

interview_angles:
  -
  -
  -

cv_bullets:
  -
  -
```

---

# Opis pól

## Metadata

### `id`

Unikalny identyfikator historii.

Format:

```yaml
id: STORY-001
```

Powinien być stabilny i niezmienny po utworzeniu dokumentu.

---

### `title`

Krótka nazwa historii.

Powinna opisywać osiągnięty rezultat lub główny temat projektu.

Przykłady:

```yaml
title: Process Documentation System Implementation
title: Customer Support Reorganization
title: Product Launch Coordination
```

Unikaj nazw stanowisk i nazw firm.

---

## Overview

### `summary`

Jedno- lub dwuzdaniowe streszczenie historii.

Powinno odpowiadać na pytanie:

> Co zostało osiągnięte i dlaczego było istotne?

Przykład:

```yaml
summary: >
  Designed and implemented a centralized process documentation system
  that standardized operational knowledge across multiple departments.
```

Powinno być możliwe do wykorzystania jako skrót historii w wyszukiwaniu lub RAG.

---

## Competencies

### `competencies`

Lista kompetencji zaprezentowanych podczas realizacji historii.

Przykład:

```yaml
competencies:
  - Process Improvement
  - Stakeholder Management
  - Documentation
```

Powinny opisywać umiejętności wykazane w praktyce, a nie deklarowane przez autora.
Preferowane jest używanie kompetencji występujących w katalogu Skills.

Dobre źródła kompetencji:

* działania opisane w `actions`
* wyzwania opisane w `challenges`
* osiągnięte rezultaty

---

## Context

### `situation`

Opis sytuacji początkowej.

Powinien odpowiadać na pytania:

* W jakim środowisku działała organizacja?
* Co było stanem wyjściowym?
* Dlaczego temat był ważny?

Przykład:

```yaml
situation: >
  Operational knowledge was distributed across departments and largely
  undocumented, making onboarding and delegation difficult.
```

---

### `problem`

Precyzyjne określenie problemu biznesowego.

Powinien odpowiadać na pytanie:

> Co konkretnie wymagało rozwiązania?

Przykład:

```yaml
problem: >
  The organization lacked standardized documentation, creating risks
  related to employee turnover and inconsistent execution of processes.
```

Jeden problem może wynikać z szerszej sytuacji opisanej w `situation`.

---

### `constraints`

Ograniczenia wpływające na realizację projektu.

Mogą obejmować:

* ograniczenia czasowe
* ograniczenia budżetowe
* brak zasobów
* zależności między działami
* wymagania prawne
* ograniczenia technologiczne

Przykład:

```yaml
constraints:
  - No dedicated project team
  - Limited availability of subject matter experts
  - Tight implementation deadline
```

---

### `goal`

Cel biznesowy projektu.

Powinien odpowiadać na pytanie:

> Co miało zostać osiągnięte?

Przykład:

```yaml
goal: >
  Create a scalable documentation framework that improves operational
  consistency and supports employee onboarding.
```

Cel powinien być możliwie konkretny.

---

## Execution

### `actions`

Najważniejsze działania wykonane przez autora.

To kluczowa sekcja całej historii.

Każdy punkt powinien opisywać:

* decyzję
* inicjatywę
* działanie
* wdrożenie
* koordynację

Przykład:

```yaml
actions:
  - Conducted process discovery interviews
  - Designed a documentation standard
  - Built a centralized repository
  - Coordinated reviews with stakeholders
```

Opisuj własny wkład, a nie działania całego zespołu.

---

### `challenges`

Najważniejsze trudności napotkane podczas realizacji.

Powinny odpowiadać na pytania:

* Co utrudniało realizację?
* Jakie ryzyko występowało?
* Co wymagało dodatkowego wysiłku?

Przykład:

```yaml
challenges:
  - Resistance from process owners
  - Incomplete documentation sources
```

Sekcja szczególnie przydatna podczas generowania odpowiedzi STAR.

---

## Results

### `results.quantitative`

Mierzalne rezultaty projektu.

Preferowane dane:

* liczby
* procenty
* kwoty
* czasy
* wielkość zespołów
* liczba użytkowników
* liczba klientów

Przykład:

```yaml
quantitative:
  - Created 50 procedures
  - Covered 6 departments
  - Supported 70 employees
```

Jeżeli istnieją wiarygodne liczby, powinny znaleźć się właśnie tutaj. 
Jeżeli autor pamięta istnienie mierzalnego rezultatu, ale nie zna dokładnej wartości, należy oznaczyć potencjalną lukę informacyjną do późniejszego uzupełnienia.
---

### `results.qualitative`

Rezultaty niemierzalne lub trudne do zmierzenia.

Przykład:

```yaml
qualitative:
  - Improved process consistency
  - Reduced dependency on key employees
  - Increased organizational transparency
```

Opisują wartość biznesową, której nie da się łatwo wyrazić liczbami.

---

## Evidence

### `evidence.achievement_ids`

Lista Achievementów, na których opiera się historia.

Przykład:

```yaml
achievement_ids:
  - ACH-001
  - ACH-004
```

Story powinno być możliwe do zweryfikowania poprzez powiązane Achievementy.

---

### `evidence.supporting_materials`

Materiały wspierające historię.

Przykłady:

```yaml
supporting_materials:
  - onboarding-guide.pdf
  - process-template.docx
  - project-plan.xlsx
```

Mogą to być dokumenty, prezentacje, procedury, raporty lub inne artefakty.

---

## Reflection

### `lessons_learned`

Najważniejsze wnioski wyniesione z projektu.

Powinny odpowiadać na pytanie:

> Czego nauczyłem się dzięki tej sytuacji?

Przykład:

```yaml
lessons_learned:
  - Early stakeholder involvement reduces resistance
  - Documentation requires clear ownership
```

Sekcja szczególnie przydatna podczas rozmów kwalifikacyjnych.

---

## Interview Preparation

### `interview_angles`

Kategorie pytań rekrutacyjnych, do których historia może zostać wykorzystana.

Przykład:

```yaml
interview_angles:
  - Leadership
  - Stakeholder Management
  - Change Management
```

Pozwala AI szybko dopasować historię do pytania rekrutacyjnego.

---

## CV Generation

### `cv_bullets`

Najkrótsze możliwe podsumowania historii.

Powinny być gotowe do użycia w CV.

Przykład:

```yaml
cv_bullets:
  - Designed and implemented a process documentation framework covering six departments.
  - Created over 50 procedures and work instructions supporting operational standardization.
```

Każdy punkt powinien:

* zaczynać się od czasownika działania,
* opisywać rezultat,
* być możliwy do wykorzystania bez dodatkowej edycji.


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
