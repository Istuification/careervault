# Kontekst podpinania rekordow

Plik generowany automatycznie przez `scripts/render_wiring.py`.
Nie edytowac recznie — zmiany zostana nadpisane przy kolejnym buildzie.

## Do czego sluzy ten plik

Zawiera **wylacznie szkielet relacyjny** Vaulta: identyfikatory, nazwy,
slowa kluczowe i aktualne powiazania. Nie zawiera tresci rekordow
(`situation`, `actions`, `impact`, `observed_pattern` i podobnych).

Sluzy do jednej decyzji: **pod ktore istniejace rekordy podpiac nowy**
ACH, STORY albo PRED. Nie sluzy do oceny Vaulta, pisania CV ani
wnioskowania o kompetencjach — brak dowodu w tym pliku nie oznacza
braku dowodu w Vaulcie, bo tresc zostala tu celowo pominieta.

**Ten plik nie jest zrodlem do parsowania.** Dlugie listy sa skracane
do kilku pozycji z licznikiem reszty (`(+N)`) — dotyczy to m.in. pola
`obecne:` przy kompetencjach, `slowa kluczowe`, `zakres` i Sygnalow.
Zadna z tych list nie jest zamknieta. Program, ktory potraktuje je jako
kompletne, po cichu odrzuci poprawne pary ACH<->SKILL — bez bledu
i bez sladu w logu.

Maszynowym wejsciem jest `dist/vault.json`: ten sam model, wszystkie
listy w calosci, stabilny `schema_version` i stempel commita.

Stan: 27 ACH (21 zawodowych), 21 SKILL, 11 STORY, 7 DEV, 14 PRED, 13 BP, 3 rol.

---

## Kompetencje (SKILL)

Kolumna `dowody` to liczba ACH juz podpietych pod kompetencje.
Znacznik `SZUKA DOWODOW` przy <= 2, `PRZECIAZONA` przy >= 15.

Podpiecie nowego ACH oznacza dopisanie go do `evidence:` w pliku kompetencji.

### Analytics

**SKILL-016** — Operational Analysis (Advanced) · dowody: 7
  - slowa kluczowe: data analysis, analytics, reporting, kpi, root cause analysis, decision making
  - zakres: operational-analysis, trend-analysis, root-cause-analysis, reporting, decision-support, process-metrics, workforce-analysis, hypothesis-testing (+1)
  - obecne: ACH-004, ACH-005, ACH-010, ACH-011, ACH-012, ACH-015, ACH-P004

### Communication

**SKILL-013** — Public Speaking (Advanced) · dowody: 4
  - slowa kluczowe: public speaking, presentations, communication, facilitation, training, audience engagement
  - zakres: public-speaking, presentation-design, audience-engagement, facilitation, verbal-communication, knowledge-sharing, event-speaking, training-delivery (+1)
  - obecne: ACH-P001, ACH-P002, ACH-P003, ACH-006

**SKILL-017** — Cross-Functional Facilitation (Advanced) · dowody: 11
  - slowa kluczowe: cross-functional facilitation, context translation, internal advisory, problem framing, organizational communication, perspective taking, mediation
  - zakres: context-framing, cross-functional-translation, problem-reframing, informal-advisory, perspective-mediation, trust-building, decision-support, stakeholder-alignment (+1)
  - obecne: ACH-001, ACH-004, ACH-005, ACH-006, ACH-008, ACH-010, ACH-012, ACH-013, ACH-014, ACH-P001 (+1)

**SKILL-018** — Persuasive Communication (Advanced) · dowody: 1 · **SZUKA DOWODOW**
  - slowa kluczowe: persuasive communication, objection handling, cold outreach, rapport building, rejection resilience, active listening, needs discovery, cognitive reframing (+1)
  - zakres: cold-outreach, rapport-building, needs-discovery, objection-handling, cognitive-reframing, socratic-persuasion, rejection-resilience, active-listening (+3)
  - obecne: ACH-P005

### Knowledge

**SKILL-003** — Knowledge Management (Expert) · dowody: 7
  - slowa kluczowe: knowledge management, documentation, onboarding, knowledge base, information architecture, knowledge transfer
  - zakres: knowledge-capture, knowledge-organization, documentation-design, onboarding-design, knowledge-transfer, information-architecture, technical-documentation
  - obecne: ACH-001, ACH-003, ACH-005, ACH-006, ACH-014, ACH-P004, ACH-P006

**SKILL-006** — Technical Documentation (Expert) · dowody: 6
  - slowa kluczowe: technical documentation, technical writing, procedures, instructions, documentation management, knowledge base
  - zakres: technical-writing, procedure-design, documentation-standardization, technical-instructions, warranty-documentation, process-documentation, knowledge-documentation, information-architecture (+1)
  - obecne: ACH-001, ACH-003, ACH-005, ACH-008, ACH-014, ACH-P004

**SKILL-007** — Training & Enablement (Advanced) · dowody: 9
  - slowa kluczowe: training, onboarding, enablement, knowledge transfer, technical training, partner education
  - zakres: training-design, onboarding-design, knowledge-transfer, workshop-facilitation, partner-enablement, technical-training, curriculum-development, presentation-delivery (+1)
  - obecne: ACH-003, ACH-004, ACH-005, ACH-006, ACH-012, ACH-018, ACH-020, ACH-P001, ACH-P005

### Management

**SKILL-005** — Leadership (Advanced) · dowody: 9
  - slowa kluczowe: leadership, team leadership, people management, mentoring, team development, succession planning
  - zakres: team-coordination, delegation, mentoring, team-development, people-retention, succession-planning, conflict-resolution, decision-making (+1)
  - obecne: ACH-001, ACH-004, ACH-006, ACH-010, ACH-012, ACH-020, ACH-P001, ACH-P002, ACH-P003

**SKILL-011** — Stakeholder Management (Advanced) · dowody: 10
  - slowa kluczowe: stakeholder management, communication, partner management, cross-functional collaboration, coordination, relationship management
  - zakres: stakeholder-alignment, cross-functional-coordination, partner-management, customer-communication, conflict-resolution, expectation-management, relationship-building, requirements-facilitation (+1)
  - obecne: ACH-001, ACH-004, ACH-005, ACH-006, ACH-008, ACH-012, ACH-016, ACH-017, ACH-021, ACH-P002

**SKILL-012** — Change Management (Advanced) · dowody: 8
  - slowa kluczowe: change management, transformation, organizational change, process transformation, organizational development, change leadership
  - zakres: organizational-transformation, process-transformation, change-planning, communication-planning, adoption-support, organizational-stabilization, change-implementation, stakeholder-alignment (+1)
  - obecne: ACH-001, ACH-003, ACH-004, ACH-005, ACH-008, ACH-012, ACH-017, ACH-018

**SKILL-014** — Project Management (Advanced) · dowody: 6
  - slowa kluczowe: project management, planning, execution, coordination, scheduling, risk management
  - zakres: project-planning, scheduling, risk-management, resource-coordination, project-execution, milestone-management, project-documentation, stakeholder-alignment (+2)
  - obecne: ACH-001, ACH-004, ACH-005, ACH-008, ACH-P002, ACH-P003

### Operations

**SKILL-001** — Process Design (Expert) · dowody: 12
  - slowa kluczowe: process design, workflow design, process optimization, business process management, bpm, workflow
  - zakres: process-mapping, workflow-design, process-optimization, process-standardization, process-documentation, bpm, organizational-workflows
  - obecne: ACH-001, ACH-003, ACH-004, ACH-005, ACH-011, ACH-013, ACH-014, ACH-015, ACH-017, ACH-018 (+2)

**SKILL-002** — Operations Management (Advanced) · dowody: 7
  - slowa kluczowe: operations, service operations, organizational scaling, logistics, operational excellence
  - zakres: operational-planning, workflow-management, team-coordination, capacity-planning, service-operations, logistics, operational-analysis, resource-planning
  - obecne: ACH-001, ACH-004, ACH-008, ACH-009, ACH-010, ACH-012, ACH-013

**SKILL-010** — Service Operations (Advanced) · dowody: 5
  - slowa kluczowe: service operations, service management, technical service, workflow management, service processes, operational excellence
  - zakres: service-process-design, service-workflow-management, ticket-management, service-coordination, service-scaling, service-analysis, service-standardization, workforce-planning (+1)
  - obecne: ACH-003, ACH-004, ACH-007, ACH-010, ACH-012

**SKILL-015** — Organizational Design (Advanced) · dowody: 7
  - slowa kluczowe: organizational design, organizational development, workforce planning, organizational structure, governance, scaling
  - zakres: organizational-analysis, role-design, responsibility-mapping, information-flow-design, workforce-planning, organizational-scaling, governance-design, knowledge-system-design (+1)
  - obecne: ACH-001, ACH-003, ACH-004, ACH-008, ACH-010, ACH-012, ACH-P004

### Product

**SKILL-004** — Product Management (Advanced) · dowody: 10
  - slowa kluczowe: product management, product development, product launch, warranty systems, technical products, stakeholder management
  - zakres: product-development, product-introduction, stakeholder-management, product-documentation, warranty-management, partner-enablement, product-lifecycle-management, requirements-gathering (+1)
  - obecne: ACH-005, ACH-006, ACH-008, ACH-010, ACH-014, ACH-013, ACH-015, ACH-016, ACH-017, ACH-018

### Product & Business

**SKILL-019** — Business Analysis & Requirements Engineering (Advanced) · dowody: 5
  - slowa kluczowe: business analysis, requirements engineering, requirements gathering, stakeholder workshops, functional specification, gap analysis
  - zakres: requirements-gathering, stakeholder-interviews, scope-definition, solution-architecture-design, specification-writing, vendor-selection, gap-analysis, business-case-framing
  - obecne: ACH-016, ACH-005, ACH-011, ACH-015, ACH-019

### Systems

**SKILL-008** — Business Systems (Advanced) · dowody: 7
  - slowa kluczowe: business systems, crm, systems integration, digital transformation, operations systems, process support
  - zakres: business-systems-design, crm-management, systems-integration, systems-administration, requirements-analysis, digitalization, operational-systems, workflow-automation (+1)
  - obecne: ACH-001, ACH-002, ACH-004, ACH-005, ACH-007, ACH-009, ACH-013

**SKILL-009** — Workflow Automation (Advanced) · dowody: 9
  - slowa kluczowe: workflow automation, process automation, workflow, automation, process optimization, operational efficiency
  - zakres: workflow-design, process-automation, business-rules-design, task-automation, information-flow-design, operational-automation, workflow-optimization
  - obecne: ACH-001, ACH-002, ACH-004, ACH-005, ACH-007, ACH-013, ACH-015, ACH-018, ACH-P006

**SKILL-020** — AI Tooling & Automation (Advanced) · dowody: 2 · **SZUKA DOWODOW**
  - slowa kluczowe: ai tooling, prompt engineering, generative ai, llm, ai automation, ai agents
  - zakres: prompt-engineering, ai-agent-orchestration, llm-workflow-design, data-preparation-for-ai, ai-tool-selection, ai-adoption
  - obecne: ACH-015, ACH-P006

**SKILL-021** — Systems Thinking (Expert) · dowody: 6
  - slowa kluczowe: systems thinking, systems architecture, root cause analysis, dependency analysis, information architecture, process architecture, systems design
  - zakres: systems-mapping, dependency-analysis, root-cause-analysis, problem-reframing, information-architecture, data-modeling, systems-design
  - obecne: ACH-002, ACH-003, ACH-010, ACH-016, ACH-P004, ACH-P006

---

## Historie (STORY)

Podpiecie nowego ACH oznacza dopisanie go do `evidence.achievement_ids:`.
Historia opisuje zwykle jedno spojne wydarzenie — nowy ACH pasuje tylko
wtedy, gdy stanowi jej czesc, a nie gdy dotyczy podobnego tematu.

**STORY-001** — Transformacja organizacji pracy działu Instal/Solar
  - ACH: ACH-001
  - zasila DEV: DEV-002, DEV-005, DEV-006
  - zasila BP: BP-001, BP-002, BP-003, BP-004, BP-005, BP-006, BP-007, BP-008, BP-009, BP-010, BP-011, BP-012
  - zasila PRED: PRED-001, PRED-002, PRED-003, PRED-004, PRED-005, PRED-006, PRED-009, PRED-010, PRED-011, PRED-012, PRED-014

**STORY-002** — Restrukturyzacja i stabilizacja działu serwisu
  - ACH: ACH-004
  - zasila DEV: DEV-005, DEV-006
  - zasila BP: BP-001, BP-002, BP-004, BP-005, BP-006, BP-009, BP-010, BP-011
  - zasila PRED: PRED-001, PRED-002, PRED-003, PRED-004, PRED-005, PRED-006, PRED-007, PRED-009, PRED-010, PRED-011, PRED-012, PRED-014

**STORY-003** — Projekt i wdrożenie systemu gwarancyjnego opartego na współpracy producentów, instalatorów i serwisu
  - ACH: ACH-005, ACH-006, ACH-014, ACH-013
  - zasila BP: BP-001, BP-002, BP-004, BP-005, BP-006, BP-008, BP-009, BP-010, BP-012
  - zasila PRED: PRED-001, PRED-002, PRED-003, PRED-004, PRED-005, PRED-006, PRED-009, PRED-010, PRED-011, PRED-012, PRED-014

**STORY-004** — Projektowanie modelu działania serwisu przy braku danych historycznych
  - ACH: ACH-004, ACH-010
  - zasila DEV: DEV-002, DEV-003, DEV-005, DEV-006
  - zasila BP: BP-001, BP-002, BP-003, BP-004, BP-005, BP-006, BP-007, BP-008, BP-010, BP-011, BP-012
  - zasila PRED: PRED-001, PRED-002, PRED-003, PRED-004, PRED-005, PRED-006, PRED-008, PRED-009, PRED-010, PRED-011, PRED-012, PRED-014

**STORY-005** — Stworzenie systemu przechwytywania i skalowania wiedzy eksperckiej
  - ACH: ACH-003, ACH-004
  - zasila DEV: DEV-002, DEV-003, DEV-005, DEV-006
  - zasila BP: BP-001, BP-002, BP-004, BP-005, BP-006, BP-008, BP-009, BP-010, BP-011, BP-012
  - zasila PRED: PRED-001, PRED-002, PRED-003, PRED-004, PRED-005, PRED-006, PRED-007, PRED-009, PRED-010, PRED-011, PRED-012, PRED-014

**STORY-006** — Wprowadzenie nowego produktu PV na rynek w warunkach wysokiej niepewności
  - ACH: ACH-009
  - zasila DEV: DEV-003, DEV-004, DEV-005, DEV-006
  - zasila BP: BP-001, BP-002, BP-003, BP-004, BP-005, BP-006, BP-007, BP-008, BP-009, BP-010, BP-011, BP-012
  - zasila PRED: PRED-001, PRED-002, PRED-003, PRED-004, PRED-005, PRED-006, PRED-009, PRED-010, PRED-011, PRED-012, PRED-014

**STORY-007** — Standaryzacja ofertowania i kalkulacji rentowności instalacji PV
  - ACH: ACH-011
  - zasila DEV: DEV-002, DEV-003
  - zasila BP: BP-001, BP-002, BP-005, BP-006, BP-007, BP-008, BP-012
  - zasila PRED: PRED-001, PRED-002, PRED-003, PRED-004, PRED-005, PRED-006, PRED-009, PRED-010, PRED-011, PRED-012, PRED-014

**STORY-008** — Zatrzymanie niekontrolowanego skalowania operacji PV
  - ACH: ACH-012
  - zasila DEV: DEV-002, DEV-003
  - zasila BP: BP-001, BP-002, BP-003, BP-004, BP-005, BP-007, BP-008, BP-010, BP-011, BP-012
  - zasila PRED: PRED-001, PRED-002, PRED-003, PRED-004, PRED-005, PRED-006, PRED-008, PRED-009, PRED-010, PRED-011, PRED-012, PRED-014

**STORY-009** — Budowa zespołu serwisowego po kryzysie kadrowym
  - ACH: ACH-012
  - zasila DEV: DEV-001
  - zasila BP: BP-001, BP-002, BP-004, BP-005, BP-006, BP-007, BP-008, BP-009, BP-010, BP-012
  - zasila PRED: PRED-001, PRED-002, PRED-003, PRED-004, PRED-005, PRED-006, PRED-007, PRED-008, PRED-009, PRED-010, PRED-011, PRED-012, PRED-014

**STORY-010** — Paszportyzacja produktów - od chaosu numerów seryjnych do fundamentu danych dla serwisu i sprzedaży
  - ACH: ACH-015
  - zasila DEV: DEV-007
  - zasila BP: BP-001, BP-002, BP-004, BP-005, BP-007, BP-008
  - zasila PRED: PRED-010, PRED-013

**STORY-011** — Stabilizacja kooperacji OEM i granica między ugaszeniem pożaru a ułożeniem procesu
  - ACH: ACH-017
  - zasila DEV: DEV-007
  - zasila BP: BP-001, BP-002, BP-004, BP-005, BP-006, BP-008, BP-011
  - zasila PRED: PRED-007, PRED-013, PRED-014

---

## Obszary rozwoju (DEV)

Podpiecie oznacza dopisanie do `sources.achievements:` albo `sources.stories:`.
DEV opisuje slabosc lub obszar do poprawy — podpina sie tu ACH pokazujacy
prace nad tym obszarem, nie kazdy ACH z tej samej dziedziny.

**DEV-001** — Leadership Through Accountability · Active Development
  - ACH: ACH-012 · STORY: STORY-009 · SKILL: SKILL-005, SKILL-011

**DEV-002** — Personal Capacity Management · Active Development
  - ACH: ACH-012 · STORY: STORY-001, STORY-004, STORY-005, STORY-007, STORY-008 · SKILL: SKILL-002

**DEV-003** — Delegation and Leverage · Active Development
  - ACH: — · STORY: STORY-004, STORY-005, STORY-006, STORY-007, STORY-008 · SKILL: SKILL-001, SKILL-003, SKILL-021

**DEV-004** — Commercial Discovery · Emerging Development Area
  - ACH: ACH-008, ACH-011, ACH-013, ACH-014 · STORY: STORY-006 · SKILL: SKILL-004, SKILL-011, SKILL-002, SKILL-001

**DEV-005** — Assertiveness and Difficult Conversations · Active Development
  - ACH: ACH-001, ACH-004, ACH-006, ACH-008, ACH-010, ACH-013 · STORY: STORY-001, STORY-002, STORY-004, STORY-005, STORY-006 · SKILL: SKILL-017, SKILL-011, SKILL-003

**DEV-006** — Boundary Management · Active Development
  - ACH: ACH-001, ACH-004, ACH-006, ACH-008, ACH-010, ACH-013, ACH-014 · STORY: STORY-001, STORY-002, STORY-004, STORY-005, STORY-006 · SKILL: SKILL-017, SKILL-003, SKILL-005, SKILL-011

**DEV-007** — Asymmetric Self-Valuation · Active Development (Fresh Awareness)
  - ACH: ACH-015, ACH-016, ACH-019 · STORY: STORY-010, STORY-011 · SKILL: SKILL-001, SKILL-019, SKILL-004

---

## Wzorce behawioralne (BP)

Podpiecie oznacza dopisanie do `derived_from.achievements:` albo
`derived_from.stories:` we frontmatterze pliku `.md`.

**BP-001** — Od Chaosu do Modelu Operacyjnego · validated · very high
  - zrodla: STORY STORY-001, STORY-002, STORY-003, STORY-004, STORY-005, STORY-006, STORY-007, STORY-008, STORY-009, STORY-010, STORY-011 · ACH ACH-001, ACH-002, ACH-003, ACH-004, ACH-005, ACH-007, ACH-008, ACH-009, ACH-010, ACH-011, ACH-012, ACH-013, ACH-014, ACH-015, ACH-017, ACH-019, ACH-P001, ACH-P002, ACH-P003, ACH-P004

**BP-002** — Usprawniaj To, Co Istnieje, Zanim To Zastąpisz · validated · very high
  - zrodla: STORY STORY-001, STORY-002, STORY-003, STORY-004, STORY-005, STORY-006, STORY-007, STORY-008, STORY-009, STORY-010, STORY-011 · ACH ACH-001, ACH-002, ACH-003, ACH-004, ACH-005, ACH-007, ACH-008, ACH-010, ACH-011, ACH-012, ACH-013, ACH-014, ACH-015, ACH-017, ACH-019

**BP-003** — Zamknij Szybko, Otwórz Ponownie Przy Nowych Dowodach · candidate · medium
  - zrodla: STORY STORY-001, STORY-004, STORY-006, STORY-008 · ACH ACH-004, ACH-010, ACH-011, ACH-012, ACH-013, ACH-016

**BP-004** — Tłumacz Między Funkcjami · validated · very high
  - zrodla: STORY STORY-001, STORY-002, STORY-003, STORY-004, STORY-005, STORY-006, STORY-008, STORY-009, STORY-010, STORY-011 · ACH ACH-001, ACH-004, ACH-005, ACH-006, ACH-008, ACH-012, ACH-013, ACH-014, ACH-016, ACH-017, ACH-019, ACH-P001, ACH-P002, ACH-P003, ACH-P004

**BP-005** — Bierz Problem Na Siebie · validated · very high
  - zrodla: STORY STORY-001, STORY-002, STORY-003, STORY-004, STORY-005, STORY-006, STORY-007, STORY-008, STORY-009, STORY-010, STORY-011 · ACH ACH-001, ACH-002, ACH-003, ACH-004, ACH-005, ACH-007, ACH-008, ACH-010, ACH-011, ACH-012, ACH-013, ACH-014, ACH-015, ACH-017, ACH-019, ACH-P001, ACH-P002, ACH-P003, ACH-P004

**BP-006** — Zamieniaj Wiedzę Ukrytą w Wspólną Infrastrukturę · validated · very high
  - zrodla: STORY STORY-001, STORY-002, STORY-003, STORY-004, STORY-005, STORY-006, STORY-007, STORY-009, STORY-011 · ACH ACH-003, ACH-005, ACH-006, ACH-009, ACH-013, ACH-014, ACH-015, ACH-017, ACH-019, ACH-P004

**BP-007** — Diagnozuj Operacje Za Pomocą Danych · validated · very high
  - zrodla: STORY STORY-001, STORY-004, STORY-006, STORY-007, STORY-008, STORY-009, STORY-010 · ACH ACH-004, ACH-010, ACH-011, ACH-012, ACH-013, ACH-014, ACH-015

**BP-008** — Prototypuj, Następnie Stabilizuj · validated · very high
  - zrodla: STORY STORY-001, STORY-003, STORY-004, STORY-005, STORY-006, STORY-007, STORY-008, STORY-009, STORY-010, STORY-011 · ACH ACH-001, ACH-003, ACH-004, ACH-005, ACH-006, ACH-007, ACH-008, ACH-011, ACH-012, ACH-013, ACH-014, ACH-015, ACH-018

**BP-009** — Ucz, Dopóki Inni Nie Potrafią Działać Samodzielnie · validated · very high
  - zrodla: STORY STORY-002, STORY-003, STORY-005, STORY-006, STORY-009, STORY-001 · ACH ACH-003, ACH-004, ACH-005, ACH-006, ACH-009, ACH-012, ACH-014, ACH-020, ACH-P001, ACH-P002, ACH-P003

**BP-010** — Kwestionuj Logikę, Nie Człowieka · validated · very high
  - zrodla: STORY STORY-001, STORY-002, STORY-003, STORY-004, STORY-005, STORY-006, STORY-008, STORY-009 · ACH ACH-001, ACH-004, ACH-005, ACH-006, ACH-008, ACH-012, ACH-014

**BP-011** — Warunkowa Absorpcja Z Jawnym Trade-offem · candidate · high
  - zrodla: STORY STORY-011, STORY-008, STORY-002, STORY-001, STORY-004, STORY-005, STORY-006 · ACH ACH-017, ACH-020, ACH-008, ACH-012, ACH-013, ACH-014

**BP-012** — Ucz Się Poprzez Wejście w Problem · validated · very high
  - zrodla: STORY STORY-001, STORY-004, STORY-005, STORY-006, STORY-007, STORY-008, STORY-009, STORY-003 · ACH ACH-007, ACH-008, ACH-010, ACH-011, ACH-013, ACH-014

**BP-013** — Modelowanie Ludzi Przez Testy Zachowań · candidate · medium-high
  - zrodla: STORY — · ACH ACH-020

---

## Predyktory (PRED)

Podpiecie oznacza dopisanie STORY do `supporting_stories:` albo
`conflicting_stories:`. Historia sprzeczna jest tak samo wartosciowa
jak wspierajaca — predyktor bez zadnej sprzecznej jest slabo skalibrowany.

**PRED-001** — Model-Centric Decision Making · validated · very high
  - wspierajace: STORY-001, STORY-002, STORY-004, STORY-006, STORY-008, STORY-003, STORY-005, STORY-007, STORY-009
  - sprzeczne: —

**PRED-002** — Evidence-Driven Belief Updating · validated · very high
  - wspierajace: STORY-004, STORY-006, STORY-008, STORY-003, STORY-005, STORY-007, STORY-009, STORY-001, STORY-002
  - sprzeczne: —

**PRED-003** — Fairness-Oriented Evaluation · validated · high
  - wspierajace: STORY-002, STORY-003, STORY-004, STORY-005, STORY-008, STORY-009, STORY-001, STORY-006, STORY-007
  - sprzeczne: —

**PRED-004** — Principle-Based Decision Making · validated · very high
  - wspierajace: STORY-003, STORY-008, STORY-009, STORY-001, STORY-002, STORY-004, STORY-007, STORY-005, STORY-006
  - sprzeczne: —

**PRED-005** — Learning-Oriented Exploration · candidate · high
  - wspierajace: STORY-004, STORY-005, STORY-006, STORY-007, STORY-008, STORY-001, STORY-002, STORY-003, STORY-009
  - sprzeczne: —

**PRED-006** — Systemic Problem Structuring · validated · very high
  - wspierajace: STORY-001, STORY-002, STORY-003, STORY-004, STORY-005, STORY-006, STORY-007, STORY-008, STORY-009
  - sprzeczne: —

**PRED-007** — Low Status Motivation · validated · high
  - wspierajace: STORY-011, STORY-002, STORY-005, STORY-009
  - sprzeczne: —

**PRED-008** — Selective Cognitive Reopening · candidate · medium
  - wspierajace: STORY-004, STORY-008, STORY-009
  - sprzeczne: —

**PRED-009** — Expert-over-Manager Preference · validated · very high
  - wspierajace: STORY-001, STORY-002, STORY-003, STORY-004, STORY-005, STORY-006, STORY-007, STORY-008, STORY-009
  - sprzeczne: —

**PRED-010** — Proven-System Optimization · validated · high
  - wspierajace: STORY-001, STORY-002, STORY-003, STORY-005, STORY-007, STORY-008, STORY-004, STORY-006, STORY-009, STORY-010
  - sprzeczne: —

**PRED-011** — Stakes-Adjusted Evidence Threshold · validated · high
  - wspierajace: STORY-004, STORY-006, STORY-008, STORY-001, STORY-002, STORY-003, STORY-007, STORY-005, STORY-009
  - sprzeczne: —

**PRED-012** — Tolerance for People vs Cognitive Errors · validated · very high
  - wspierajace: STORY-001, STORY-002, STORY-003, STORY-005, STORY-009, STORY-004, STORY-006, STORY-008, STORY-007
  - sprzeczne: —

**PRED-013** — Context-Adaptive Self-Presentation · validated · high
  - wspierajace: STORY-010, STORY-011
  - sprzeczne: —

**PRED-014** — Supportive Facilitation Orientation · validated · very high
  - wspierajace: STORY-001, STORY-002, STORY-005, STORY-009, STORY-003, STORY-004, STORY-006, STORY-008, STORY-007, STORY-011
  - sprzeczne: —

---

## Role (Experience.md)

Nowy ACH zawodowy musi trafic do sekcji `### <Rola>` w `Experience.md`,
inaczej walidacja zglosi go jako nieprzypisanego. ACH prywatne (`ACH-P*`)
sa z tego wymogu zwolnione.

**KOOR** — Koordynator ds. Montaży · 2020-09 – 2023-09 · 8 ACH
**KIER** — p.o. Kierownika Serwisu · 2023-09 – 2025-01 · 6 ACH
**PM** — Product Manager / Business Analyst · 2025-01 – obecnie · 8 ACH

---

## Sygnaly

Nie sa to bledy walidacji — to miejsca, w ktorych struktura Vaulta
moze wymagac uwagi przy najblizszym podpinaniu.

**Kompetencje o slabym pokryciu** — kandydaci przy najblizszym ACH:
  - SKILL-018 (Persuasive Communication): 1 dowodow
  - SKILL-020 (AI Tooling & Automation): 2 dowodow

**ACH podpiete pod > 6 kompetencji** — sprawdzic, czy kazde podpiecie ma pokrycie w tresci:
  - ACH-005: 13 kompetencji (SKILL-001, SKILL-003, SKILL-004, SKILL-006, SKILL-007, SKILL-008 (+7))
  - ACH-004: 13 kompetencji (SKILL-001, SKILL-002, SKILL-005, SKILL-007, SKILL-008, SKILL-009 (+7))
  - ACH-001: 12 kompetencji (SKILL-001, SKILL-002, SKILL-003, SKILL-005, SKILL-006, SKILL-008 (+6))
  - ACH-012: 9 kompetencji (SKILL-002, SKILL-005, SKILL-007, SKILL-010, SKILL-011, SKILL-012 (+3))
  - ACH-010: 8 kompetencji (SKILL-002, SKILL-004, SKILL-005, SKILL-010, SKILL-015, SKILL-016 (+2))
  - ACH-008: 8 kompetencji (SKILL-002, SKILL-004, SKILL-006, SKILL-011, SKILL-012, SKILL-014 (+2))
  - ACH-003: 8 kompetencji (SKILL-001, SKILL-003, SKILL-006, SKILL-007, SKILL-010, SKILL-012 (+2))
  - ACH-006: 7 kompetencji (SKILL-003, SKILL-004, SKILL-005, SKILL-007, SKILL-011, SKILL-013 (+1))

**ACH bez STORY i bez DEV** — istnieja jako fakt, ale nie maja
narracji, ktora mozna opowiedziec na rozmowie:
  - ACH-002, ACH-007, ACH-018, ACH-020, ACH-021, ACH-P001, ACH-P002, ACH-P003, ACH-P004, ACH-P005, ACH-P006

**BP opierajace sie na jednym zrodle** — wzorzec z jednego
przypadku jest hipoteza, nie wzorcem:
  - BP-013

**PRED bez historii sprzecznej** — brak kontrprzykladu oznacza,
ze predyktor nie byl testowany na granicy:
  - PRED-001, PRED-002, PRED-003, PRED-004, PRED-005, PRED-006, PRED-007, PRED-008, PRED-009, PRED-010, PRED-011, PRED-012, PRED-013, PRED-014

---

_Wygenerowano 2026-07-24 12:25 · commit 6f00043_
