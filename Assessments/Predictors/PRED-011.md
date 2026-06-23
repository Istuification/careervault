---
id: PRED-011
name: Stakes-Adjusted Evidence Threshold
status: validated
confidence: high
created_from:
  - AOT
  - CIHS
  - NFCS
  - Wywiad jakościowy
supporting_stories:
  - STORY-004
  - STORY-006
  - STORY-008
  - STORY-001
  - STORY-002
  - STORY-003
  - STORY-007
  - STORY-005
  - STORY-009
conflicting_stories: []
related_hypotheses: []
related_calibrations:
  - CAL-001
last_updated: 2026-06-23
version: 1.1
---

# Opis

Badany dostosowuje poziom wymaganych dowodów i głębokość analizy do przewidywanego kosztu błędu.

Nie dąży do maksymalnej możliwej pewności we wszystkich sytuacjach.

Zamiast tego ocenia relację pomiędzy:

- kosztem pozyskania dodatkowych informacji,
- potencjalnym kosztem błędnej decyzji,
- wartością szybkiego działania,
- poziomem pozostałej niepewności.

W rezultacie decyzje o niskiej wadze mogą być podejmowane przy relatywnie ograniczonej ilości danych, podczas gdy decyzje strategiczne wymagają znacznie wyższego poziomu pewności.

---

# Źródła

## Evidence Sources

- Actively Open-Minded Thinking (AOT)
- Comprehensive Intellectual Humility Scale (CIHS)
- Need for Closure Scale (NFCS)

## Analiza Jakościowa

- Badany deklaruje preferencję dla redukcji niepewności przed podjęciem decyzji.
- Jednocześnie nie wykazuje potrzeby osiągania maksymalnej pewności za wszelką cenę.
- W przypadku decyzji strategicznych akceptuje wyższy koszt analizy w zamian za zmniejszenie ryzyka błędu.
- W przypadku decyzji operacyjnych preferuje działanie po osiągnięciu wystarczającego poziomu zrozumienia.

Przykład deklarowany:

> Jeżeli decyzja może generować bardzo wysokie straty, preferowane jest pozyskanie dodatkowych danych nawet kosztem opóźnienia działania.

---

# Zachowania Przewidywane

Predyktor przewiduje, że badany będzie:

- zwiększał zakres analizy wraz ze wzrostem ryzyka decyzji,
- podejmował szybkie decyzje w sytuacjach niskiego ryzyka,
- inwestował znacznie więcej czasu w decyzje strategiczne niż operacyjne,
- oceniał opłacalność zdobywania dodatkowych informacji,
- akceptował niepewność w sytuacjach o ograniczonych konsekwencjach,
- dążył do redukcji niepewności w sytuacjach o wysokim koszcie błędu.

---

# Zachowania Przeczące

Predyktor zostałby osłabiony przez regularne występowanie zachowań takich jak:

- stosowanie identycznego poziomu analizy niezależnie od stawki decyzji,
- chroniczne przeciąganie decyzji o niskim znaczeniu,
- podejmowanie decyzji strategicznych przy bardzo ograniczonych danych,
- ignorowanie kosztu potencjalnego błędu podczas planowania działań.

---

# Dowody Potwierdzające

Matryca Predictor ↔ Story wskazuje następujące Stories wspierające ten Predictor:

- STORY-004 — Projektowanie modelu działania serwisu przy braku danych historycznych (3; silne wsparcie)
- STORY-006 — Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewności (3; silne wsparcie)
- STORY-008 — Zatrzymanie niekontrolowanego skalowania operacji PV (3; silne wsparcie)
- STORY-001 — Transformacja organizacji pracy działu Instal/Solar (2; umiarkowane wsparcie)
- STORY-002 — Restrukturyzacja i stabilizacja działu serwisu (2; umiarkowane wsparcie)
- STORY-003 — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu (2; umiarkowane wsparcie)
- STORY-007 — Standaryzacja ofertowania i kalkulacji rentowności instalacji PV (2; umiarkowane wsparcie)
- STORY-005 — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej (1; słaby sygnał pomocniczy)
- STORY-009 — Budowa zespołu serwisowego po kryzysie kadrowym (1; słaby sygnał pomocniczy)

---

# Dowody Przeczące

Brak.

Oczekuje na analizę historii.

---

# Historia Kalibracji

- CAL-001 — Predictor ↔ Story Mapping Review (2026-06-22)
  - Zweryfikowano przypisania Stories w matrycy.
  - Zaktualizowano confidence, status i poziom walidacji zgodnie z kalibracją.

---

# Ocena

## Pewność

Wysoka

## Siła Źródeł Psychometrycznych

Średnia

## Siła Źródeł Behawioralnych

Wysoka

## Poziom Walidacji

Wysoki

Predyktor ma regularne wsparcie w Stories i pozostaje spójnym mechanizmem wspierającym model.

---

# Notatki

Predyktor nie opisuje ostrożności ani awersji do ryzyka.

Opisuje sposób zarządzania niepewnością.

Najbardziej prawdopodobny wzorzec działania można opisać jako:

1. Oszacuj koszt błędu.
2. Oszacuj koszt zdobycia dodatkowych informacji.
3. Określ wymagany poziom pewności.
4. Podejmij decyzję po osiągnięciu odpowiedniego progu dowodowego.

Predyktor może stanowić mechanizm wyjaśniający współwystępowanie:

- wysokiego AOT,
- wysokiej pokory intelektualnej,
- umiarkowanej potrzeby domknięcia poznawczego.

Na obecnym etapie jest to jeden z najbardziej obiecujących kandydatów do walidacji na podstawie rzeczywistych historii decyzyjnych.

Wysokość progu dowodowego zależy od stawki decyzji; CAL-001 wzmacnia ten wzorzec w Stories o różnym poziomie ryzyka.
