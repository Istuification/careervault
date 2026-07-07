# Stories

## Cel

Folder **Stories** zawiera historie zawodowe zbudowane na podstawie osiągnięć zgromadzonych w Career Vault.

Story jest narracyjną warstwą systemu: przekształca fakty i rezultaty zapisane w Achievementach w spójną opowieść o problemie, decyzjach, działaniach i wnioskach.

Stories odpowiadają na pytanie:

> Jak opowiadać o tych doświadczeniach?

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
Jak opowiadać o tych doświadczeniach?

Development Areas
↓
Jakie wzorce rozwojowe obserwuję u siebie?

Identity
↓
Kim jestem jako profesjonalista?
```

Stories nie są źródłem faktów.

Źródłem faktów są Achievements.

Story nadaje faktom strukturę narracyjną potrzebną podczas rozmów rekrutacyjnych, prezentacji doświadczenia oraz analizy wzorców zachowań.

---

# Czym jest Story?

Story opisuje pełny łuk narracyjny: sytuację wyjściową, problem, ograniczenia, cel, podjęte decyzje i działania, napotkane trudności, rezultaty oraz wyciągnięte wnioski.

Struktura rozszerza klasyczny model STAR (Situation, Task, Action, Result) o ograniczenia, wyzwania, lekcje oraz gotowe kąty rozmowy.

Dobra Story:

* opiera się na co najmniej jednym Achievemencie,
* zawiera decyzje i ich uzasadnienia, nie tylko czynności,
* pokazuje napięcie: ograniczenia, opór, trudności,
* kończy się rezultatem oraz wnioskiem,
* da się opowiedzieć w kilka minut podczas rozmowy.

---

# Kiedy tworzyć Story?

Nie każde osiągnięcie zasługuje na osobną historię.

Story powstaje wtedy, gdy istnieje łuk narracyjny: decyzje, napięcie, zwrot akcji lub dojrzała lekcja.

❌ Story jako lustrzane odbicie każdego Achievementu.

To rozwadnia moduł i tworzy szum.

✅ Story tam, gdzie fakty układają się w opowieść z wnioskiem.

Jeżeli Achievement broni się samodzielnie listą działań i rezultatów, nie potrzebuje Story.

---

# Historie o niepełnych sukcesach

Story może dokumentować projekt, który nie zakończył się pełnym sukcesem.

Historia z drugim aktem — w której rozwiązanie zdegradowało się, projekt wstrzymano lub założenia okazały się błędne — bywa cenniejsza niż historia triumfu, pod warunkiem że kończy się konkretną, stosowaną od tamtej pory lekcją.

Warunek: przebieg wydarzeń opisujemy faktograficznie i neutralnie, bez oceniania osób.

---

# Fakty ponad deklaracje

Najważniejsza zasada Career Vault:

> Fakty ponad deklaracje.

Każda liczba, metryka i twierdzenie w Story musi mieć pokrycie w Achievementach lub materiałach źródłowych.

Story nie może twierdzić więcej, niż potwierdzają dowody.

Zasada szczególna: wyceny finansowe nigdy nie znajdują się w Stories. Blok `fin` żyje wyłącznie w Achievementach, a Story odsyła do niego identyfikatorem.

Przykład:

```yaml
results:
  quantitative:
    - Odzyskana produktywność wdrożonej kohorty oszacowana na 140-180 tys. PLN (metodologia: ACH-003, blok fin / FIN-003).
```

---

# Schemat rekordu

Każda Story powinna być zapisana jako osobny plik YAML.

```yaml
id:

title:

summary:

competencies:

behavioral_signals:

situation:

problem:

constraints:

goal:

actions:

challenges:

results:

org:            # opcjonalne

evidence:

lessons_learned:

interview_angles:

cv_bullets:
```

---

# Opis pól

## id

Unikalny identyfikator historii.

Przykłady:

```text
STORY-001
STORY-010
```

Identyfikator powinien pozostać niezmienny przez cały czas życia repozytorium.

---

## title

Tytuł historii.

Powinien zapowiadać oś narracji, nie tylko temat.

Przykład:

```yaml
title: Stabilizacja kooperacji OEM i granica między ugaszeniem pożaru a ułożeniem procesu
```

---

## summary

Skrót całej historii w kilku zdaniach.

Powinien pozwolić czytelnikowi zdecydować, czy chce poznać szczegóły — łącznie z zapowiedzią zwrotu akcji, jeżeli historia go zawiera.

---

## competencies

Kompetencje demonstrowane w historii.

Wartości powinny odpowiadać nazwom kompetencji z modułu `Skills`.

Przykład:

```yaml
competencies:
  - Change Management
  - Process Design
  - Stakeholder Management
```

---

## behavioral_signals

Sygnały postawy i zachowań widoczne w historii.

Stosowany słownik:

```text
ownership
accountability
transparency
solution_orientation
constructive_challenge
feedback_receptiveness
feedback_giving
perspective_taking
psychological_safety
```

Słownik można rozszerzać, ale nowe sygnały powinny być używane konsekwentnie w całym repozytorium.

---

## situation

Kontekst wyjściowy: stan organizacji, otoczenie, moje umiejscowienie w strukturze.

Opisuje świat przed historią.

---

## problem

Sedno problemu do rozwiązania.

Odpowiada na pytanie:

> Co dokładnie nie działało i dlaczego miało to znaczenie?

---

## constraints

Ograniczenia, w których działałem.

Przykład:

```yaml
constraints:
  - Ograniczone zasoby kadrowe
  - Brak formalnie zdefiniowanych procesów
  - Presja terminów rynkowych
```

---

## goal

Cel działania sformułowany z perspektywy momentu startu.

---

## actions

Podjęte działania i decyzje wraz z uzasadnieniami.

Odpowiada na pytanie:

> Co zrobiłem i dlaczego właśnie tak?

Działania opisujemy w pierwszej osobie, z zachowaniem uczciwej atrybucji pracy zespołowej.

---

## challenges

Trudności napotkane po drodze: opór, zmiany warunków, konflikty priorytetów.

To pole buduje wiarygodność historii — opowieść bez trudności brzmi jak laurka.

---

## results

Rezultaty historii.

Forma rekomendowana — z podziałem:

```yaml
results:
  quantitative:
    - Skrócono czas osiągnięcia samodzielności z 8-9 do 2-3 miesięcy.
  qualitative:
    - Zmniejszono zależność od pojedynczych osób.
```

Dla krótszych historii dopuszczalna jest płaska lista.

Rezultatem może być również uczciwie opisany drugi akt (degradacja rozwiązania, wstrzymanie projektu), jeżeli prowadzi do lekcji.

---

## org

Pole opcjonalne.

Opisuje zmianę zdolności organizacji, którą opowiada historia. Stosowane tylko tam, gdzie zmiana modelu działania jest wartością samą w sobie, niezależną od wyceny finansowej — nie jako pole obowiązkowe każdej Story.

Dopuszczalne formy:

```yaml
org:
  operational:
    - przejście z zarządzania intuicyjnego na oparte na danych
    - stworzenie pierwszego systemu KPI dla serwisu
  strategic:
    - poprawa retencji specjalistów
    - odejście od liniowego skalowania kosztów
```

lub

```yaml
org:
  capability:
    from: organizacja zależna od ludzi (people-dependent)
    to: organizacja zależna od systemu (system-dependent)
```

Wyceny finansowe nigdy nie trafiają do `org` — blok `fin` żyje wyłącznie w Achievementach.

---

## evidence

Powiązanie historii z dowodami.

Przykład:

```yaml
evidence:
  achievement_ids:
    - ACH-003
  supporting_materials:
    - Workflow serwisowe
    - Materiały onboardingowe
```

### achievement_ids

Identyfikatory Achievementów, na których opiera się historia.

Każda Story powinna wskazywać co najmniej jeden Achievement.

### supporting_materials

Artefakty wspierające: dokumentacja, diagramy, materiały szkoleniowe.

---

## lessons_learned

Wnioski wyciągnięte z historii.

Najcenniejsze są lekcje:

* stosowane od tamtej pory w praktyce,
* wynikające również z błędów i niepełnych sukcesów,
* sformułowane jako zasady, nie ogólniki.

Przykład:

```yaml
lessons_learned:
  - Wdrożenie jest skończone, gdy proces przeżyje odejście dowolnej pojedynczej osoby.
```

---

## interview_angles

Kąty, pod jakimi historia może być opowiadana podczas rozmów.

Przykład:

```yaml
interview_angles:
  - Change Management
  - Process decoupling - rozdzielanie zależnych procesów
  - Dojrzałość operacyjna - wnioski z niepełnego sukcesu
```

Jedna historia zwykle obsługuje kilka różnych pytań rekrutacyjnych.

---

## cv_bullets

Gotowe punkty do wykorzystania w CV lub aplikacjach.

Przykład:

```yaml
cv_bullets:
  - Przejąłem odpowiedzialność za dział serwisu i przeprowadziłem jego stabilizację organizacyjną.
```

Punkty powinny być zgodne z liczbami zapisanymi w Achievementach.

---

# Zasady anonimizacji

Career Vault jest repozytorium publicznym.

1. Osoby opisujemy przez role i funkcje, nie przez nazwiska.
2. Partnerów, kooperantów i klientów opisujemy rodzajowo (np. "podwykonawca OEM", "partner technologiczny").
3. Nie publikujemy danych wrażliwych organizacji: cen, marż, danych klientów, treści umów.
4. Przebieg konfliktów i trudności opisujemy faktograficznie, bez oceniania osób i ich intencji.

---

# Relacje z pozostałymi modułami

## Experience

Dostarcza kontekstu kariery.

## Achievements

Stanowią źródło faktów, liczb i wycen (blok `fin`).

## Skills

Historie pokazują kompetencje w praktyce; pole `competencies` odwołuje się do nazw Skills.

## Stories

Przekształcają fakty w narrację gotową do opowiedzenia.

## Development Areas

Historie — zwłaszcza ich lekcje i drugie akty — stanowią materiał źródłowy dla wzorców rozwojowych.

## Identity

Stanowi syntezę narracji, kompetencji i doświadczeń zgromadzonych w Career Vault.

---

# Zasady utrzymania

1. Każda Story opiera się na co najmniej jednym Achievemencie.
2. Story nie twierdzi więcej, niż potwierdzają dowody.
3. Nie twórz Story dla każdego Achievementu — tylko tam, gdzie istnieje łuk narracyjny.
4. Liczby w Story muszą być zgodne z liczbami w Achievementach.
5. Wyceny finansowe wyłącznie przez odesłanie do bloku `fin` w Achievementach.
6. Sekcję `org` stosuj oszczędnie — tam, gdzie zmiana zdolności organizacji jest sednem historii.
7. Zachowuj uczciwą atrybucję pracy zespołowej.
8. Dokumentuj również niepełne sukcesy, jeżeli niosą lekcję.
9. Przestrzegaj zasad anonimizacji.
10. Aktualizuj historie, gdy Achievementy źródłowe zyskują nowe fakty.

---

# Najważniejsza zasada

Story nie tworzy faktów.

Story nadaje faktom strukturę opowieści.

Jeżeli historia potrzebuje faktu, którego nie ma w Achievementach — najpierw uzupełnij Achievement, dopiero potem opowiadaj.
