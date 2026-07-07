---
id: PRED-013
name: Context-Adaptive Self-Presentation
status: validated
confidence: high
created_from:
- Wywiad jakościowy
- Obserwacje behawioralne (CAL-004)
supporting_stories:
- STORY-010
- STORY-011
conflicting_stories: []
related_hypotheses: []
related_calibrations:
- CAL-001
- CAL-004
last_updated: 2026-07-07
version: 1.2
---

# Opis
Badany wykazuje tendencję do świadomego dostosowywania sposobu prezentowania siebie do kontekstu, roli oraz celu interakcji.
Dostosowanie może obejmować:
- sposób komunikacji,
- poziom formalności,
- eksponowane kompetencje,
- widoczność własnej osoby,
- sposób budowania autorytetu.

Celem nie wydaje się budowanie określonego wizerunku dla samego wizerunku.
Bardziej prawdopodobna interpretacja wskazuje na świadome zarządzanie uwagą otoczenia w sposób wspierający realizację aktualnej roli i celu.

**Asymetria z podłogą uczciwości (CAL-004):** Adaptacja autoprezentacji jest **jednostronnie ograniczona**:
- **Zero inflacji w górę:** Badany deklaruje (i potwierdza to brak jakiegokolwiek kontrprzykładu), że "nie mieści mu się w głowie" zawyżanie własnych kompetencji lub dokonań ("nie chcę być lepszy, niż mam na to dowody"). Superlatywy dotyczące własnej pracy są możliwe wyłącznie instrumentalnie, na jawne żądanie kontekstu (np. wymogi formalne CV, briefu).
- **Dryf w dół:** Obserwowane zaniżanie własnej roli lub dokonań **nie jest mechanizmem adaptacyjnym**, lecz pochodną **funkcyjnego kryterium ukończenia** (powiązane z DEV-007). Badany stosuje asymetryczne kryterium oceny: wobec innych uwzględnia intencje, możliwości i proces, wobec siebie wyłącznie to, czy praca spełniła swoją funkcję.

---

# Źródła
## Analiza Jakościowa
- Badany deklaruje przekonanie, że uwagą należy zarządzać.
- Badany uważa, że różne role wymagają różnych sposobów prezentowania siebie.
- Deklaruje gotowość do zmiany stylu komunikacji, wyglądu lub zachowania, jeśli wymaga tego pełniona funkcja.
- Obecnie świadomie eksponuje rolę osoby wspierającej, pomocnej i facylitującej współpracę.

## Obserwacje Behawioralne (CAL-004)
- Brak jakiegokolwiek udokumentowanego przypadku inflacji autoprezentacji w górę.
- Potwierdzona przez podmiot subiektywna niemożność ("nie mieści mi się w głowie") zawyżania własnej wartości.
- Instrumentalne użycie superlatywów wyłącznie w odpowiedzi na jawne wymogi kontekstu.
- Obserwowany systematyczny dryf autoprezentacji w dół, powiązany z asymetrią kryterium funkcyjnego.

---

# Zachowania Przewidywane
Predyktor przewiduje, że badany będzie:
- dostosowywał sposób komunikacji do odbiorcy,
- zmieniał poziom formalności zależnie od sytuacji,
- eksponował różne aspekty własnych kompetencji w różnych rolach,
- świadomie ograniczał lub zwiększał własną widoczność w zależności od celu (np. rezygnacja z widoczności na rzecz *enablementu* współpracownika),
- traktował autorytet jako narzędzie realizacji celu, a nie wartość samą w sobie,
- **nigdy nie zawyżał własnych dokonań ani kompetencji powyżej poziomu potwierdzonego dowodami**,
- **stosował wobec siebie surowsze kryteria oceny niż wobec współpracowników**.

---

# Zachowania Przeczące
Predyktor zostałby osłabiony przez regularne wystęgowanie zachowań takich jak:
- identyczny styl działania niezależnie od kontekstu,
- całkowity brak refleksji nad odbiorem społecznym,
- niezdolność do dostosowania komunikacji do odbiorcy,
- odrzucanie zmian sposobu prezentacji siebie niezależnie od sytuacji,
- **regularne zawyżanie własnej roli, wkładu lub kompetencji w komunikacji zewnętrznej**,
- **używanie superlatywów wobec własnej pracy bez wyraźnego kontekstowego przymusu**.

---

# Dowody Potwierdzające
## Stories
- STORY-010 — Paszportyzacja produktów (autoprezentacja jako PM-a budującego infrastrukturę, bez inflacji własnego autorstwa)
- STORY-011 — Stabilizacja kooperacji OEM (celowa rezygnacja z widoczności przy przekazaniu tematu nowemu PM-owi)

## Obserwacje z CAL-004
- Deklaracja podmiotu potwierdzona przez brak kontrprzykładów w całej bazie dowodowej Vault.
- Instrumentalne użycie superlatywów wyłącznie na żądanie kontekstu (np. CV, brief).
- Asymetria kryterium ukończenia jako źródło dryfu w dół (powiązane z DEV-007).

---

# Dowody Przeczące
Brak.

---

# Historia Kalibracji
- CAL-001 — Predictor ↔ Story Mapping Review (2026-06-22). Predictor oznaczony jako wymagający dalszej walidacji behawioralnej.
- CAL-004 — Post-Expansion Recalibration (2026-07-07). **Predyktor zweryfikowany behawioralnie.** Potwierdzono asymetrię autoprezentacji:
  - Twarda podłoga uczciwości (brak inflacji w górę),
  - Dryf w dół jako efekt funkcyjnego kryterium ukończenia (powiązanie z DEV-007),
  - Instrumentalne użycie superlatywów wyłącznie na żądanie kontekstu.
  - Zmieniono status z `candidate` na `validated`, podniesiono confidence do `high`.

---

# Ocena
## Pewność
Wysoka
## Siła Źródeł Psychometrycznych
Niska (oparte głównie na analizie jakościowej i obserwacjach)
## Siła Źródeł Behawioralnych
Wysoka
## Poziom Walidacji
Wysoki

Predyktor został zweryfikowany behawioralnie w CAL-004 poprzez brak kontrprzykładów inflacji oraz potwierdzenie asymetrii autoprezentacji przez podmiot.

---

# Notatki
Predyktor nie opisuje manipulacji ani budowania fałszywego wizerunku.
Opisuje świadome dostosowywanie sposobu prezentowania siebie do kontekstu i celu działania.

Kluczowym doprecyzowaniem z CAL-004 jest odkrycie **twardej podłogi uczciwości** - adaptacja autoprezentacji nigdy nie idzie w stronę inflacji. Jest to silnie skorelowane z PRED-003 (Fairness-Oriented Evaluation) oraz z rygorystyczną epistemologią Vault ("fakty ponad deklaracje"), którą badany stosuje również wobec samego siebie.

Obserwowany dryf w dół nie jest mechanizmem adaptacyjnym ani niską samooceną w klasycznym sensie. Jest **artefaktem funkcyjnego kryterium ukończenia** opisanego w DEV-007 - badany wobec siebie uwzględnia wyłącznie funkcję (czy praca zadziałała), pomijając intencje, wysiłek i proces, które uwzględnia u innych. To źródło systematycznego niedoceniania własnej pracy, a nie celowej strategii autoprezentacyjnej.

Predyktor silnie powiązany z:
- PRED-003 (Fairness-Oriented Evaluation) - granica uczciwości komunikacyjnej,
- PRED-007 (Low Status Motivation) - instrumentalne traktowanie widoczności,
- PRED-014 (Supportive Facilitation Orientation) - rezygnacja z widoczności na rzecz *enablementu*,
- DEV-007 (Samoocena i wycena własnej pracy) - źródło dryfu w dół.
