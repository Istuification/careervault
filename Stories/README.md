# Stories

## Cel

Folder **Stories** zawiera historie przygotowane według modelu STAR (Situation, Task, Action, Result).

Stories służą do przekształcania osiągnięć zapisanych w Career Vault w spójną narrację, którą można wykorzystać podczas rozmów kwalifikacyjnych, ocen okresowych, rozmów rozwojowych oraz współpracy z systemami AI.

Stories nie są źródłem prawdy.

Źródłem prawdy pozostają Achievementy.

Stories są sposobem przedstawiania osiągnięć w formie historii.

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

Stories są ostatnią warstwą.

Ich zadaniem jest zamiana faktów i rezultatów na zrozumiałą narrację.

---

# Model STAR

Każda Story powinna wykorzystywać model STAR.

## Situation

Opis sytuacji lub problemu.

Odpowiada na pytanie:

> Jaki był kontekst?

---

## Task

Opis odpowiedzialności lub celu.

Odpowiada na pytanie:

> Co należało osiągnąć?

---

## Action

Opis podjętych działań.

Odpowiada na pytanie:

> Co konkretnie zrobiłem?

---

## Result

Opis rezultatów.

Odpowiada na pytanie:

> Jaki był efekt?

Preferowane są rezultaty mierzalne.

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

Każda Story powinna być powiązana z co najmniej jednym Achievementem.

Przykład:

```yaml
achievement:
  - ACH-003
```

lub

```yaml
achievement:
  - ACH-003
  - ACH-014
```

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
* usprawnienia,
* skrócenie czasu,
* wzrost jakości,
* poprawa organizacji.

---

# Struktura pliku

Każda Story powinna być zapisana jako osobny plik YAML.

Przykład:

```yaml
id: STAR-001

title: Transformacja działu Instal/Solar

achievement:
  - ACH-001

skills:
  - SKILL-001
  - SKILL-002
  - SKILL-012

themes:
  - leadership
  - change-management
  - operations

situation: >
  Opis sytuacji.

task: >
  Opis celu.

actions:
  - działanie 1
  - działanie 2
  - działanie 3

result:
  - rezultat 1
  - rezultat 2

key_takeaway: >
  Najważniejszy wniosek płynący z historii.
```

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

Jedna Story może odpowiadać na wiele różnych pytań.

---

# Relacja do pozostałych elementów Career Vault

## Achievement

Źródło faktów.

## Skill

Źródło kompetencji.

## Story

Źródło narracji.

Najpierw powstaje Achievement.

Następnie na jego podstawie tworzony jest Skill.

Dopiero później tworzona jest Story.

---

# Zasady utrzymania

1. Każda Story musi mieć powiązanie z Achievementem.
2. Nie twórz Story bez dowodów.
3. Nie duplikuj treści Achievementów.
4. Skupiaj się na decyzjach i działaniach.
5. Pokazuj rezultaty.
6. Aktualizuj Stories, gdy pojawią się nowe informacje.
7. Preferuj jakość nad liczbę historii.

Celem nie jest stworzenie dużej liczby Stories.

Celem jest stworzenie zestawu historii, które najlepiej pokazują doświadczenie, kompetencje i sposób działania.
