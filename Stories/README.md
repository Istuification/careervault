# Stories

## Cel

Folder **Stories** zawiera historie zawodowe przygotowane na podstawie Achievementów zgromadzonych w Career Vault.

Stories przekształcają fakty, rezultaty i osiągnięcia w uporządkowane narracje pokazujące:

* sposób myślenia,
* podejmowanie decyzji,
* rozwiązywanie problemów,
* wykorzystywane kompetencje,
* wpływ biznesowy,
* wyciągnięte wnioski.

Stories są zoptymalizowane pod:

* rozmowy kwalifikacyjne,
* przygotowanie odpowiedzi STAR,
* portfolio zawodowe,
* profile zawodowe,
* analizę kompetencji,
* współpracę z AI i systemami RAG.

Stories nie są źródłem prawdy.

Źródłem prawdy pozostają Achievementy.

---

# Rola Stories w Career Vault

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
Jak wyglądały rzeczywiste sytuacje stojące za osiągnięciami?

Development Areas
↓
Jakie wzorce rozwojowe można zaobserwować?

Identity
↓
Kim jestem jako profesjonalista?
```

Stories pełnią rolę warstwy narracyjnej.

Ich zadaniem jest połączenie kontekstu, decyzji, działań i rezultatów w historię możliwą do opowiedzenia drugiej osobie.

---

# Czym jest Story?

Story opisuje pojedynczą sytuację zawodową posiadającą:

* wyraźny problem,
* konkretny cel,
* podjęte działania,
* osiągnięty rezultat,
* wyciągnięte wnioski.

Story nie opisuje stanowiska.

Story nie opisuje zakresu obowiązków.

Story opisuje sytuację, która pokazuje sposób działania autora.

---

# Stories a model STAR

Stories wykorzystują rozszerzony model STAR.

Klasyczny STAR:

```text
Situation
Task
Action
Result
```

Model stosowany w Career Vault:

```text
Situation
↓
Problem
↓
Constraints
↓
Goal
↓
Actions
↓
Challenges
↓
Results
↓
Lessons Learned
```

Dzięki temu każda Story może zostać łatwo przekształcona do klasycznej odpowiedzi STAR, jednocześnie zachowując znacznie więcej informacji przydatnych podczas analizy doświadczenia.

---

# Fakty ponad deklaracje

Najważniejsza zasada Career Vault:

> Fakty ponad deklaracje.

Story nie służy do opisywania cech charakteru.

Story służy do pokazywania ich poprzez działania.

Przykład:

❌ Jestem dobrym liderem.

✅ Przeprowadziłem reorganizację działu serwisu, utrzymałem kluczowych ekspertów i ustabilizowałem dział w okresie wysokiej rotacji.

Kompetencje powinny wynikać z historii.

Nie odwrotnie.

---

# Jedna Story = jedna historia

Każda Story powinna opisywać jeden główny problem lub wyzwanie.

Dobre przykłady:

* transformacja działu,
* wdrożenie systemu,
* uruchomienie produktu,
* rozwiązanie kryzysu,
* stworzenie nowego procesu,
* przeprowadzenie reorganizacji.

Nie należy łączyć wielu niezależnych historii w jeden rekord.

---

# Schemat rekordu

Każda Story powinna być zapisana jako osobny plik YAML.

```yaml
id:

title:

summary:

competencies:

situation:

problem:

constraints:

goal:

actions:

challenges:

results:
  quantitative:
  qualitative:

evidence:
  achievement_ids:
  supporting_materials:

lessons_learned:

interview_angles:

cv_bullets:
```

---

# Opis pól

## id

Unikalny identyfikator historii.

Przykład:

```yaml
id: STORY-001
```

Identyfikator powinien być stabilny i niezmienny.

---

## title

Krótka nazwa historii.

Powinna opisywać osiągnięty rezultat lub główny temat.

Przykłady:

```text
Transformacja organizacji pracy działu Instal/Solar
Projektowanie modelu działania serwisu
Wprowadzenie produktu PV Stand na rynek
```

---

## summary

Krótki opis historii.

Powinien odpowiadać na pytanie:

> Co zostało osiągnięte i dlaczego było ważne?

Powinien umożliwiać szybkie zrozumienie historii bez czytania całego dokumentu.

---

## competencies

Kompetencje zaprezentowane podczas realizacji historii.

Preferowane jest wykorzystanie kompetencji istniejących w module Skills.

Przykład:

```yaml
competencies:
  - Process Design
  - Systems Thinking
  - Stakeholder Management
```

---

## situation

Opis sytuacji wyjściowej.

Powinien odpowiadać na pytanie:

> W jakim kontekście działałem?

---

## problem

Precyzyjne określenie problemu biznesowego.

Powinien odpowiadać na pytanie:

> Co wymagało rozwiązania?

---

## constraints

Najważniejsze ograniczenia.

Przykłady:

* ograniczenia czasowe,
* ograniczenia zasobów,
* brak wiedzy,
* konflikty między działami,
* ograniczenia organizacyjne.

---

## goal

Cel biznesowy lub organizacyjny.

Powinien odpowiadać na pytanie:

> Co miało zostać osiągnięte?

---

## actions

Najważniejsza sekcja całej historii.

Opisuje działania autora.

Każdy punkt powinien opisywać:

* decyzję,
* inicjatywę,
* analizę,
* wdrożenie,
* koordynację,
* rozwiązanie problemu.

Opisuj własny wkład.

Nie działania całego zespołu.

---

## challenges

Najważniejsze trudności napotkane podczas realizacji.

Powinny pokazywać:

* ryzyka,
* konflikty,
* ograniczenia,
* niepewność,
* sytuacje wymagające adaptacji.

---

## results

Rezultaty osiągnięte dzięki działaniom.

### quantitative

Mierzalne rezultaty.

Przykłady:

* liczby,
* procenty,
* czas,
* koszty,
* wielkość zespołu,
* liczba klientów.

### qualitative

Rezultaty jakościowe.

Przykłady:

* poprawa jakości,
* poprawa współpracy,
* większa przewidywalność,
* ograniczenie ryzyka,
* zwiększenie skalowalności.

---

## evidence

Powiązane źródła.

### achievement_ids

Achievementy będące źródłem historii.

Każda Story musi być powiązana z co najmniej jednym Achievementem.

### supporting_materials

Materiały wspierające.

Przykłady:

* procedury,
* workflow,
* dokumentacja,
* prezentacje,
* instrukcje,
* raporty.

---

## lessons_learned

Najważniejsze wnioski wyniesione z realizacji.

Powinny odpowiadać na pytanie:

> Czego nauczyłem się dzięki tej sytuacji?

Sekcja szczególnie ważna dla Development Areas.

---

## interview_angles

Kategorie pytań rekrutacyjnych, do których historia może zostać wykorzystana.

Przykład:

```yaml
interview_angles:
  - Leadership
  - Change Management
  - Ownership
```

---

## cv_bullets

Najkrótsze możliwe podsumowania historii.

Powinny być gotowe do wykorzystania w CV, LinkedIn lub portfolio.

Każdy punkt powinien:

* zaczynać się od działania,
* zawierać rezultat,
* być zrozumiały bez dodatkowego kontekstu.

---

# Relacje z pozostałymi modułami

## Experience

Dostarcza kontekstu kariery.

## Achievements

Stanowią źródło faktów i dowodów.

## Skills

Opisują kompetencje wykorzystywane w historii.

## Stories

Pokazują sposób działania, podejmowania decyzji oraz osiągania rezultatów.

## Development Areas

Powstają na podstawie analizy wielu Stories i Achievementów.

## Identity

Stanowi syntezę wzorców widocznych w całym Career Vault.

---

# Zasady utrzymania

1. Każda Story musi być powiązana z Achievementem.
2. Nie twórz Story bez dowodów.
3. Skupiaj się na decyzjach i działaniach.
4. Pokazuj wpływ biznesowy.
5. Dodawaj rezultaty ilościowe, gdy są dostępne.
6. Dokumentuj najważniejsze wnioski.
7. Łącz Stories ze Skills.
8. Łącz Stories z Development Areas, gdy stanowią ich źródło.
9. Preferuj jakość nad liczbę historii.

---

# Najważniejsza zasada

Achievement opisuje co zostało osiągnięte.

Story opisuje jak myślałem, jakie decyzje podejmowałem, jakie działania wykonałem i dlaczego osiągnąłem taki rezultat.
