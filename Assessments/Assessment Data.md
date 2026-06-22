# Assessment Data

## Cel dokumentu

Assessment Data stanowi zbiór źródeł pomiarowych wykorzystywanych podczas budowy Cognitive Model.

Dokument nie służy do interpretacji badanego.

Jego celem jest przechowywanie wyników pomiarów, ocen oraz modeli opisujących wybrane aspekty funkcjonowania badanego.

Assessment Data stanowi jedno z dwóch głównych źródeł obserwacyjnych wykorzystywanych podczas budowy modelu.

Drugim źródłem są Stories opisujące rzeczywiste zachowania i doświadczenia.

Żadne z tych źródeł nie jest traktowane jako nadrzędne względem drugiego.

---

## Miejsce w architekturze Vault

```text
Assessment Data      Stories
        ↓               ↓
          Calibration
                ↓
           Predictors
                ↓
        Behavioral Pattern
                ↓
         Cognitive Model
```

Assessment Data opisuje wyniki pomiarów.

Stories opisują rzeczywiste zachowania.

Calibration odpowiada za integrację obu źródeł.

---

## Czym jest Assessment Data?

Assessment Data zawiera wyniki modeli psychologicznych, poznawczych, wartości, talentów oraz innych narzędzi pomiarowych.

Modele te nie opisują całej osoby.

Każdy model mierzy jedynie wybrany fragment rzeczywistości, między innymi:

* cechy osobowości,
* wartości,
* style myślenia,
* preferencje poznawcze,
* talenty,
* siły charakteru.

Żaden pojedynczy model nie powinien być traktowany jako samodzielny opis badanego.

---

## Rola Assessment Data

Assessment Data odpowiada na pytanie:

> Jakie mechanizmy mogą istnieć?

Nie odpowiada natomiast na pytania:

> Jak badany rzeczywiście działa?

> Jak podejmuje decyzje?

> Jak zachowuje się w rzeczywistych sytuacjach?

Na te pytania odpowiadają dopiero Stories oraz późniejsze etapy modelu.

---

## Relacja pomiędzy Assessment Data i Stories

Assessment Data oraz Stories pełnią różne funkcje.

### Assessment Data

Opisuje potencjalne cechy, tendencje oraz mechanizmy.

Przykład:

```text
Wysoki Need for Cognition
```

oznacza, że badany prawdopodobnie lubi angażować się w wysiłek poznawczy.

Nie oznacza jeszcze, że rzeczywiście robi to regularnie.

---

### Stories

Opisują rzeczywiste zachowania.

Przykład:

```text
Wielokrotne budowanie modeli,
analiza problemów,
tworzenie Career Vault.
```

stanowią obserwacje zachowania.

---

### Calibration

Calibration porównuje oba źródła.

Jeżeli Assessment Data oraz Stories wskazują ten sam mechanizm, może zostać utworzony lub wzmocniony Predictor.

Jeżeli pozostają ze sobą w konflikcie, powstaje potrzeba dalszej kalibracji.

---

## Fakty przed deklaracjami

Jedną z podstawowych zasad Career Vault jest:

> Fakty przed deklaracjami.

Assessment Data zawiera głównie deklaracje badanego udzielone podczas wypełniania narzędzi pomiarowych.

Stories zawierają deklaracje badanego dotyczące rzeczywistych zdarzeń.

Oba źródła mogą zawierać błędy poznawcze, uproszczenia oraz ograniczenia pamięci.

Dlatego żadne pojedyncze źródło nie powinno samodzielnie tworzyć Cognitive Model.

Model powinien być budowany wyłącznie na podstawie wzorców pojawiających się w wielu niezależnych źródłach.

---

## Relacja z Predyktorami

Assessment Data nie tworzy Predyktorów bezpośrednio.

Predyhktory powstają podczas procesu Calibration.

Calibration analizuje:

* Assessment Data,
* Stories,
* istniejące Predyktory,
* wcześniejsze kalibracje.

Predictor powinien reprezentować mechanizm wsparty przez więcej niż jedno źródło danych.

---

## Relacja z Behavioral Pattern

Assessment Data nie tworzy Behavioral Pattern bezpośrednio.

Behavioral Pattern powstają na podstawie:

* Predictorów,
* wzorców zachowań występujących w Stories.

Behavioral Pattern nie opisuje pojedynczej cechy.

Opisuje powtarzalny wzorzec działania obserwowany w rzeczywistości.

---

## Cel długoterminowy

Celem Assessment Data nie jest stworzenie profilu psychologicznego badanego.

Jego rolą jest dostarczenie danych wykorzystywanych podczas budowy modelu odpowiadającego na pytania:

* Jak badany podejmuje decyzje?
* Jak rozwiązuje problemy?
* Jak aktualizuje swoje przekonania?
* Jak reaguje na niepewność?
* Jak działa w organizacjach?
* Jakie mechanizmy stoją za jego zachowaniami?

Odpowiedzi na te pytania powstają dopiero na poziomie Cognitive Model.

---

# Modele Osobowości

---

# Big Five Personality Model (BFM)

## Metadane

| Pole                   | Wartość    |
| ---------------------- | ---------- |
| Typ Modelu             | Osobowość  |
| Wiarygodność Naukowa   | 10 / 10    |
| Przydatność dla Modelu | TBD        |
| Data Badania           | 2026-06-18 |
| Status                 | Aktywny    |

---

## Opis

Big Five Personality Model (BFM), zwany również Pięcioczynnikowym Modelem Osobowości, jest jednym z najlepiej przebadanych modeli osobowości we współczesnej psychologii.

Model opisuje osobowość za pomocą pięciu szerokich wymiarów:

* Otwartość na Doświadczenia (Openness)
* Sumienność (Conscientiousness)
* Ekstrawersja (Extraversion)
* Ugodowość (Agreeableness)
* Neurotyczność (Neuroticism)

Model nie opisuje zdolności, inteligencji ani kompetencji. Jego celem jest opis względnie trwałych tendencji psychologicznych i behawioralnych.

---

## Wyniki

| Czynnik                               | Wynik    |
| ------------------------------------- | -------- |
| Neurotyczność (Neuroticism)           | 3.53 / 5 |
| Ekstrawersja (Extraversion)           | 3.30 / 5 |
| Ugodowość (Agreeableness)             | 2.40 / 5 |
| Otwartość na Doświadczenia (Openness) | 2.80 / 5 |
| Sumienność (Conscientiousness)        | 2.80 / 5 |

### Facety

#### Neurotyczność

| Faceta                                        | Wynik |
| --------------------------------------------- | ----- |
| Lęk (Anxiety)                                 | 3.9   |
| Wrogość (Angry Hostility)                     | 3.5   |
| Depresyjność (Depression)                     | 2.9   |
| Samoświadomość społeczna (Self-Consciousness) | 2.7   |
| Impulsywność (Impulsiveness)                  | 4.2   |
| Podatność na stres (Vulnerability)            | 2.7   |

#### Ekstrawersja

| Faceta                                       | Wynik |
| -------------------------------------------- | ----- |
| Ciepło interpersonalne (Warmth)              | 3.9   |
| Towarzyskość (Gregariousness)                | 3.9   |
| Asertywność (Assertiveness)                  | 3.5   |
| Aktywność (Activity)                         | 3.3   |
| Poszukiwanie stymulacji (Excitement-Seeking) | 2.8   |
| Pozytywne emocje (Positive Emotions)         | 3.8   |

#### Ugodowość

| Faceta                                | Wynik |
| ------------------------------------- | ----- |
| Zaufanie (Trust)                      | 2.0   |
| Prostolinijność (Straightforwardness) | 2.3   |
| Altruizm (Altruism)                   | 1.5   |
| Uległość (Compliance)                 | 2.1   |
| Skromność (Modesty)                   | 2.8   |
| Wrażliwość (Tender-Mindedness)        | 2.4   |

#### Otwartość na Doświadczenia

| Faceta                | Wynik |
| --------------------- | ----- |
| Wyobraźnia (Fantasy)  | 1.8   |
| Estetyka (Aesthetics) | 2.8   |
| Uczucia (Feelings)    | 1.9   |
| Działania (Actions)   | 2.4   |
| Idee (Ideas)          | 2.5   |
| Wartości (Values)     | 2.5   |

#### Sumienność

| Faceta                                      | Wynik |
| ------------------------------------------- | ----- |
| Kompetencje (Competence)                    | 2.3   |
| Porządek (Order)                            | 2.3   |
| Obowiązkowość (Dutifulness)                 | 2.5   |
| Dążenie do osiągnięć (Achievement Striving) | 2.5   |
| Samodyscyplina (Self-Discipline)            | 1.4   |
| Rozwaga (Deliberation)                      | 3.3   |

---

## Opis Wyników

### Neurotyczność — umiarkowana

Wynik wskazuje na przeciętną podatność na stres i negatywne emocje. Badany nie wydaje się szczególnie odporny emocjonalnie, ale również nie wykazuje cech wysokiej neurotyczności.

Najbardziej wyróżnia się podwyższona impulsywność przy jednocześnie umiarkowanej podatności na stres.

### Ekstrawersja — umiarkowana

Profil wskazuje na zdolność do funkcjonowania społecznego bez wyraźnej dominacji cech introwertycznych lub ekstrawertycznych.

Badany nie poszukuje intensywnej stymulacji społecznej, ale potrafi funkcjonować komfortowo w relacjach i sytuacjach grupowych.

### Ugodowość — niska

Wynik sugeruje ograniczoną skłonność do automatycznego zaufania, podporządkowywania się lub dostosowywania do innych osób.

Nie musi oznaczać konfliktowości. Może oznaczać niezależność ocen, sceptycyzm wobec cudzych opinii oraz preferowanie własnych standardów oceny sytuacji.

### Otwartość na Doświadczenia — umiarkowanie niska

Wynik nie wskazuje na szczególnie wysokie zainteresowanie doświadczeniami estetycznymi, emocjonalnymi lub fantazyjnymi.

Model sugeruje raczej praktyczne niż eksploracyjne podejście do nowych doświadczeń.

### Sumienność — umiarkowanie niska

Wynik wskazuje na ograniczoną potrzebę utrzymywania stałego porządku, rutyn i dyscypliny.

Jednocześnie podwyższona rozwaga sugeruje, że decyzje nie są podejmowane całkowicie impulsywnie.

---

## Interpretacja

Profil Big Five sugeruje osobę funkcjonującą w sposób bardziej niezależny niż konformistyczny.

Najbardziej charakterystycznymi cechami profilu są:

* niska potrzeba podporządkowywania się opiniom innych,
* ograniczone zaufanie domyślne,
* relatywnie niski poziom organizacji codziennej,
* umiarkowana rozwaga decyzyjna,
* przeciętna potrzeba kontaktów społecznych.

Wyniki nie wskazują na osobę szczególnie napędzaną statusem społecznym, popularnością lub potrzebą aprobaty.

---

## Notatki Badanego

Badany nie identyfikuje się ani z profilem osoby konsekwentnie uporządkowanej, ani z profilem osoby trwale chaotycznej.

Deklaruje występowanie silnej polaryzacji pomiędzy obszarami zainteresowań.

Niektóre obszary życia mogą pozostawać w stanie znacznej dezorganizacji bez odczuwalnego dyskomfortu.

Jednocześnie obszary objęte aktualnym hiperfokusem są organizowane i kontrolowane na bardzo wysokim poziomie szczegółowości.

Badany wskazuje również na wpływ zespołu Aspergera na sposób gospodarowania zasobami poznawczymi. W praktyce może to prowadzić do występowania skrajności pomiędzy zaniedbaniem wybranych obszarów a bardzo wysokim poziomem organizacji innych.

Może to częściowo wpływać na wyniki związane z sumiennością, porządkiem i samodyscypliną.

Ponadto wyniki modelu wykazują częściowe rozbieżności względem modelu HEXACO, szczególnie w obszarach Ugodowości, Otwartości oraz Sumienności. Rozbieżności te wymagają dalszej analizy podczas budowy Cognitive Model.

---

## Ograniczenia Modelu

* Model opisuje szerokie tendencje osobowościowe, a nie rzeczywiste zachowania.
* Model nie uwzględnia wpływu środowiska, doświadczeń życiowych ani kontekstu sytuacyjnego.
* Model nie mierzy zdolności poznawczych, inteligencji ani kompetencji.
* Wyniki opierają się na samoopisie badanego.
* Interpretacja wymaga zestawienia z innymi źródłami danych.
* Zaobserwowano istotne różnice względem wyników HEXACO, co ogranicza możliwość wyciągania jednoznacznych wniosków bez dalszej kalibracji.

---

## Przydatność dla Modelu

TBD


---

# HEXACO Personality Inventory (HEXACO)

## Metadane

| Pole                   | Wartość         |
| ---------------------- | --------------- |
| Typ Modelu             | Osobowość       |
| Wiarygodność Naukowa   | 9.5 / 10        |
| Przydatność dla Modelu | W trakcie oceny |
| Data Badania           | 2026-06-18      |
| Status                 | Aktywny         |

---

## Opis

HEXACO Personality Inventory jest sześcioczynnikowym modelem osobowości rozwijającym klasyczny model Big Five.

Najważniejszą różnicą względem Big Five jest dodanie wymiaru Uczciwość i Pokora (Honesty-Humility), który opisuje stosunek do uczciwości, sprawiedliwości, statusu społecznego oraz wykorzystywania innych ludzi dla własnych korzyści.

Model opisuje osobowość za pomocą sześciu głównych wymiarów:

* Uczciwość i Pokora (Honesty-Humility)
* Emocjonalność (Emotionality)
* Ekstrawersja (Extraversion)
* Ugodowość (Agreeableness)
* Sumienność (Conscientiousness)
* Otwartość na Doświadczenia (Openness to Experience)

Dodatkowo model zawiera skalę Altruizmu.

---

## Wyniki

| Czynnik                | Wynik |
| ---------------------- | ----- |
| Honesty-Humility       | 7.10  |
| Emotionality           | 3.33  |
| Extraversion           | 4.60  |
| Agreeableness          | 6.61  |
| Conscientiousness      | 5.24  |
| Openness to Experience | 5.59  |
| Altruism               | 4.88  |

---

## Rozbicie na Czynniki

### Uczciwość i Pokora (Honesty-Humility)

| Faceta          | Wynik |
| --------------- | ----- |
| Sincerity       | 6.04  |
| Fairness        | 6.76  |
| Greed Avoidance | 7.00  |
| Modesty         | 5.62  |

### Emocjonalność (Emotionality)

| Faceta         | Wynik |
| -------------- | ----- |
| Fearfulness    | 3.74  |
| Anxiety        | 3.20  |
| Dependence     | 3.86  |
| Sentimentality | 4.69  |

### Ekstrawersja (Extraversion)

| Faceta             | Wynik |
| ------------------ | ----- |
| Social Self-Esteem | 3.80  |
| Social Boldness    | 5.84  |
| Sociability        | 4.59  |
| Liveliness         | 4.32  |

### Ugodowość (Agreeableness)

| Faceta      | Wynik |
| ----------- | ----- |
| Forgiveness | 6.80  |
| Gentleness  | 7.10  |
| Flexibility | 4.60  |
| Patience    | 6.21  |

### Sumienność (Conscientiousness)

| Faceta        | Wynik |
| ------------- | ----- |
| Organization  | 5.24  |
| Diligence     | 5.34  |
| Perfectionism | 4.36  |
| Prudence      | 6.09  |

### Otwartość na Doświadczenia (Openness)

| Faceta                 | Wynik |
| ---------------------- | ----- |
| Aesthetic Appreciation | 3.34  |
| Inquisitiveness        | 6.53  |
| Creativity             | 6.09  |
| Unconventionality      | 5.91  |

---

## Opis Wyników

### Uczciwość i Pokora — bardzo wysoka

Najsilniejszy wymiar całego profilu.

Wynik wskazuje na bardzo niską skłonność do manipulowania innymi dla własnych korzyści, wysokie znaczenie uczciwości proceduralnej oraz niewielkie zainteresowanie statusem społecznym, prestiżem lub demonstracją sukcesu.

Szczególnie wysoki wynik Fairness sugeruje silną niechęć do działań postrzeganych jako nieuczciwe lub wykorzystujące innych.

### Emocjonalność — umiarkowanie niska

Wynik sugeruje względnie dobrą odporność na stres i umiarkowaną niezależność emocjonalną.

Jednocześnie podwyższona Sentimentality wskazuje na zdolność tworzenia silnych więzi emocjonalnych oraz empatię wobec innych ludzi.

### Ekstrawersja — umiarkowana

Profil wskazuje na zdolność funkcjonowania w sytuacjach społecznych bez wyraźnej dominacji cech introwertycznych lub ekstrawertycznych.

Wyróżnia się wysoka Social Boldness, sugerująca stosunkowo dużą swobodę w wystąpieniach publicznych, prowadzeniu rozmów lub podejmowaniu inicjatywy społecznej.

### Ugodowość — wysoka

Wynik wskazuje na dużą cierpliwość, skłonność do wybaczania oraz łagodne podejście do innych ludzi.

Jednocześnie umiarkowana Flexibility sugeruje, że gotowość do kompromisu nie oznacza automatycznej rezygnacji z własnego stanowiska.

### Sumienność — umiarkowanie wysoka

Wynik wskazuje na rozwagę, zdolność planowania oraz tendencję do analizowania konsekwencji działań przed podjęciem decyzji.

Najsilniejszą cechą tego obszaru jest Prudence, sugerująca ostrożność decyzyjną oraz preferencję dla przemyślanych działań.

### Otwartość na Doświadczenia — wysoka

Profil wskazuje na dużą ciekawość poznawczą, zainteresowanie nowymi ideami oraz skłonność do poszukiwania nowych sposobów rozwiązywania problemów.

Najbardziej wyróżnia się bardzo wysoka Inquisitiveness oraz Creativity.

Jednocześnie stosunkowo niski wynik Aesthetic Appreciation sugeruje, że zainteresowanie nowością ma charakter bardziej intelektualny niż artystyczny.

---

## Interpretacja

HEXACO przedstawia obraz osoby silnie skoncentrowanej na uczciwości, sprawiedliwości oraz jakości rozumowania.

Profil sugeruje:

* wysoką niezależność od statusu społecznego,
* dużą wagę przywiązywaną do uczciwości i zasad,
* rozwagę decyzyjną,
* wysoką ciekawość poznawczą,
* skłonność do analizowania problemów przed działaniem,
* łagodne i cierpliwe podejście do ludzi,
* gotowość do obrony własnego stanowiska bez potrzeby eskalowania konfliktu.

Model jest spójny z wynikami VIA, Schwartz Value Theory, Actively Open-Minded Thinking (AOT) oraz Comprehensive Intellectual Humility Scale (CIHS).

---

## Notatki Badanego

Wyniki modelu są postrzegane przez badanego jako stosunkowo trafny opis jego sposobu funkcjonowania.

Szczególnie trafne wydają się wyniki związane z ciekawością poznawczą, rozwagą decyzyjną, niewielkim znaczeniem statusu społecznego oraz wysoką wagą przypisywaną uczciwości i sprawiedliwości.

Wymaga dalszej weryfikacji sposób interpretacji wyników związanych z sumiennością w kontekście występowania hiperfokusu oraz nierównomiernego poziomu organizacji pomiędzy różnymi obszarami życia.

---

## Ograniczenia Modelu

* Model opisuje względnie stabilne cechy osobowości, a nie konkretne zachowania.
* Wyniki opierają się na samoopisie badanego.
* Model nie uwzględnia wpływu kontekstu sytuacyjnego.
* Model nie mierzy kompetencji ani poziomu wiedzy.
* Interpretacja wymaga zestawienia z innymi źródłami danych oraz analizą rzeczywistych historii.

---

## Przydatność dla Modelu

W trakcie oceny.

Na obecnym etapie HEXACO stanowi jedno z najbardziej spójnych źródeł danych w całym zbiorze Assessment Data.

Wyniki wykazują wysoką zgodność z wynikami VIA, Schwartz Value Theory, Actively Open-Minded Thinking (AOT) oraz Comprehensive Intellectual Humility Scale (CIHS).

Ostateczna ocena przydatności modelu zostanie przeprowadzona po analizie historii i dowodów behawioralnych.


---

# Modele Wartości

---

# Schwartz Value Theory (SVT)

## Metadane

| Pole                   | Wartość         |
| ---------------------- | --------------- |
| Typ Modelu             | Wartości        |
| Wiarygodność Naukowa   | 10 / 10         |
| Przydatność dla Modelu | W trakcie oceny |
| Data Badania           | 2026-06-18      |
| Status                 | Aktywny         |

---

## Opis

Schwartz Value Theory (SVT) jest jednym z najlepiej przebadanych modeli wartości ludzkich.

Model opisuje wartości jako podstawowe motywacje wpływające na decyzje, priorytety oraz ocenę sytuacji.

W przeciwieństwie do modeli osobowości, które opisują sposób funkcjonowania człowieka, model Schwartza koncentruje się na tym, co człowiek uznaje za ważne i warte realizacji.

Model składa się z dziesięciu podstawowych wartości, które można dodatkowo pogrupować w cztery nadrzędne obszary.

---

## Wyniki

### Wartości Podstawowe

| Wartość                          | Wynik |
| -------------------------------- | ----- |
| Benevolence (Życzliwość)         | 5.50  |
| Tradition (Tradycja)             | 4.75  |
| Conformity (Konformizm)          | 4.75  |
| Universalism (Uniwersalizm)      | 4.50  |
| Self-Direction (Samostanowienie) | 4.00  |
| Security (Bezpieczeństwo)        | 3.00  |
| Stimulation (Stymulacja)         | 2.67  |
| Achievement (Osiągnięcia)        | 2.50  |
| Hedonism (Hedonizm)              | 2.00  |
| Power (Władza)                   | 2.00  |

---

### Wartości Nadrzędne

| Obszar                                               | Wynik |
| ---------------------------------------------------- | ----- |
| Self-Transcendence (Przekraczanie Własnego Interesu) | 5.00  |
| Conservatism (Zachowawczość)                         | 4.17  |
| Openness to Change (Otwartość na Zmianę)             | 3.34  |
| Self-Enhancement (Wzmacnianie Własnego Interesu)     | 2.17  |

---

## Opis Wyników

### Życzliwość (Benevolence) — bardzo wysoka

Najwyższy wynik w całym profilu.

Wskazuje na dużą wagę przypisywaną wspieraniu ludzi znajdujących się w najbliższym otoczeniu, uczciwości wobec innych oraz odpowiedzialności za relacje.

### Tradycja (Tradition) — wysoka

Wynik sugeruje szacunek dla istniejących zasad, norm oraz sprawdzonych sposobów działania.

Nie oznacza bezrefleksyjnego podporządkowania tradycji, lecz uznawanie wartości rozwiązań, które przetrwały próbę czasu.

### Konformizm (Conformity) — wysoki

Wynik wskazuje na skłonność do ograniczania działań mogących szkodzić innym ludziom lub destabilizować funkcjonowanie grupy.

W tym modelu konformizm nie oznacza braku niezależności myślenia, lecz respektowanie wspólnych zasad współżycia.

### Uniwersalizm (Universalism) — wysoki

Wskazuje na znaczenie dobra wspólnego, sprawiedliwości oraz troski o ludzi wykraczających poza najbliższe otoczenie.

### Samostanowienie (Self-Direction) — umiarkowanie wysokie

Sugeruje potrzebę samodzielnego myślenia oraz podejmowania własnych decyzji.

### Bezpieczeństwo (Security) — umiarkowane

Wynik wskazuje na znaczenie stabilności i przewidywalności, jednak nie jest to dominująca motywacja.

### Stymulacja (Stimulation) — niska

Nie wskazuje na silną potrzebę poszukiwania ekscytacji, ryzyka lub intensywnych doznań.

### Osiągnięcia (Achievement) — niskie

Wynik sugeruje, że sukces i osiągnięcia nie są głównym źródłem motywacji.

### Hedonizm (Hedonism) — bardzo niski

Przyjemność i maksymalizacja osobistej satysfakcji nie wydają się głównym kryterium podejmowania decyzji.

### Władza (Power) — bardzo niska

Najniższy wynik w profilu.

Wskazuje na niewielkie znaczenie kontroli nad innymi ludźmi, prestiżu społecznego lub dominacji.

---

## Interpretacja

Profil wartości wskazuje na osobę, która przy podejmowaniu decyzji koncentruje się przede wszystkim na wpływie swoich działań na innych ludzi oraz na zgodności tych działań z własnymi zasadami.

Najsilniejszym motywatorem nie wydaje się sukces, status ani przyjemność, lecz poczucie działania zgodnego z wartościami.

Szczególnie istotne wydają się:

* uczciwość,
* odpowiedzialność wobec innych,
* sprawiedliwość,
* stabilność relacji,
* poszanowanie zasad.

Jednocześnie profil nie wskazuje na silną potrzebę dominacji, rywalizacji ani zdobywania prestiżu.

Może to wpływać na sposób definiowania sukcesu oraz oceniania własnych osiągnięć.

---

## Notatki Badanego

Badany uznaje wyniki za stosunkowo trafne.

Szczególnie trafne wydają się:

* niska potrzeba statusu społecznego,
* niska motywacja związana z władzą,
* wysoka wartość przypisywana uczciwości,
* wysoka wartość przypisywana sprawiedliwości,
* większe znaczenie użyteczności i sensu działań niż ich prestiżu.

Wymaga dalszej obserwacji sposób interpretacji wysokich wyników w obszarach Tradycji i Konformizmu.

Możliwe jest, że wyniki te odzwierciedlają bardziej szacunek dla sprawdzonych zasad i procedur niż potrzebę podporządkowania się autorytetom lub normom społecznym.

---

## Ograniczenia Modelu

* Model opisuje deklarowane wartości, a nie rzeczywiste zachowania.
* Wysokie znaczenie danej wartości nie oznacza automatycznie działania zgodnego z nią.
* Model nie uwzględnia wpływu sytuacji, środowiska ani ograniczeń zewnętrznych.
* Model nie mierzy zdolności, kompetencji ani cech osobowości.
* Interpretacja wymaga zestawienia z innymi źródłami danych oraz analizą rzeczywistych historii.

---

## Przydatność dla Modelu

W trakcie oceny.

Na obecnym etapie model wykazuje wysoką zgodność z wynikami HEXACO, VIA oraz częściowo z wynikami AOT i CIHS.

Szczególnie istotne dla dalszej budowy Cognitive Model mogą okazać się:

* bardzo niska orientacja na władzę,
* bardzo niska orientacja na hedonizm,
* wysoka orientacja na dobro innych ludzi,
* wysoka orientacja na sprawiedliwość i zasady.

Ostateczna ocena przydatności modelu zostanie przeprowadzona po analizie historii oraz dowodów behawioralnych.


---

# Moral Foundations Theory Questionnaire (MFQ)

## Metadane

| Pole                   | Wartość         |
| ---------------------- | --------------- |
| Typ Modelu             | Wartości        |
| Wiarygodność Naukowa   | 7.5 / 10        |
| Przydatność dla Modelu | W trakcie oceny |
| Data Badania           | 2026-06-18      |
| Status                 | Aktywny         |

---

## Opis

Moral Foundations Theory (MFT) jest teorią psychologiczną opisującą intuicyjne fundamenty moralne wykorzystywane przez ludzi podczas oceniania zachowań, decyzji i sytuacji społecznych.

W przeciwieństwie do modeli osobowości, które opisują sposób funkcjonowania człowieka, MFQ koncentruje się na tym, jakie zasady moralne są spontanicznie uznawane za ważne.

Model nie mierzy moralności jako takiej. Mierzy raczej wrażliwość na określone rodzaje argumentów moralnych.

---

## Wyniki

| Fundament Moralny                  | Percentyl |
| ---------------------------------- | --------- |
| Purity (Czystość)                  | 84.17     |
| Equality (Równość)                 | 82.16     |
| Authority (Autorytet)              | 69.05     |
| Care (Troska)                      | 62.54     |
| Proportionality (Proporcjonalność) | 44.96     |
| Loyalty (Lojalność Grupowa)        | 21.47     |

---

## Rozbicie na Fundamenty Moralne

### Czystość (Purity)

Dotyczy potrzeby ochrony rzeczy uznawanych za wartościowe, właściwe lub godne szacunku przed degradacją, zepsuciem lub naruszeniem.

### Równość (Equality)

Dotyczy potrzeby równego traktowania ludzi, równego głosu, równego dostępu do szans oraz sprzeciwu wobec niesprawiedliwych nierówności.

### Autorytet (Authority)

Dotyczy znaczenia struktur, zasad, kompetencji oraz szacunku wobec uzasadnionej hierarchii.

### Troska (Care)

Dotyczy potrzeby ochrony ludzi przed krzywdą oraz reagowania na cierpienie innych.

### Proporcjonalność (Proportionality)

Dotyczy przekonania, że nagrody, konsekwencje i korzyści powinny być proporcjonalne do wkładu, wysiłku lub zasług.

### Lojalność Grupowa (Loyalty)

Dotyczy identyfikacji z grupą, wspólnotą lub zespołem oraz gotowości do stawiania interesu grupy ponad interes jednostki.

---

## Opis Wyników

### Czystość — bardzo wysoka

Najwyższy wynik w całym profilu.

Może wskazywać na dużą wagę przypisywaną integralności systemów, zasad, procesów lub idei.

W praktyce nie musi oznaczać religijnego lub konserwatywnego rozumienia czystości.

Może przejawiać się jako niechęć wobec działań postrzeganych jako psujące, degradujące lub naruszające coś wartościowego.

### Równość — bardzo wysoka

Wynik wskazuje na silną potrzebę sprawiedliwego traktowania ludzi oraz niechęć wobec arbitralnych przywilejów.

Jest spójny z wysokim wynikiem Fairness w modelu HEXACO oraz wysokim Benevolence i Universalism w modelu Schwartza.

### Autorytet — podwyższony

Wynik sugeruje uznawanie znaczenia zasad, kompetencji oraz uzasadnionych struktur odpowiedzialności.

Nie musi oznaczać bezwarunkowego posłuszeństwa wobec osób posiadających formalną władzę.

### Troska — umiarkowanie wysoka

Wynik wskazuje na ponadprzeciętną wrażliwość na krzywdę innych ludzi oraz znaczenie ochrony osób narażonych na negatywne konsekwencje działań.

### Proporcjonalność — przeciętna

Wynik sugeruje umiarkowane znaczenie zasady „wkład powinien odpowiadać nagrodzie”.

Nie jest to dominujący element profilu moralnego.

### Lojalność Grupowa — niska

Najniższy wynik w całym profilu.

Wskazuje na niewielką skłonność do uznawania przynależności grupowej jako samodzielnego argumentu moralnego.

Przynależność do grupy nie wydaje się być wystarczającym uzasadnieniem dla określonych działań lub decyzji.

---

## Interpretacja

Profil moralny sugeruje osobę oceniającą sytuacje przede wszystkim przez pryzmat:

* sprawiedliwości,
* integralności zasad,
* jakości procesów,
* wpływu na ludzi.

Jednocześnie stosunkowo niewielkie znaczenie wydaje się mieć sam fakt przynależności do grupy.

Profil nie wskazuje na moralność opartą na lojalności plemiennej lub identyfikacji grupowej.

Znacznie większe znaczenie wydają się mieć zasady oraz sposób działania niż interes konkretnej grupy.

---

## Notatki Badanego

TODO

---

## Ograniczenia Modelu

* Model mierzy intuicje moralne, a nie rzeczywiste zachowania.
* Wyniki nie określają poziomu moralności badanego.
* Interpretacja zależy od kontekstu kulturowego.
* Model nie mierzy cech osobowości ani kompetencji.
* Poszczególne fundamenty mogą przyjmować różne znaczenia w zależności od sposobu interpretacji przez badanego.

---

## Przydatność dla Modelu

W trakcie oceny.

Model wykazuje wysoką zgodność z wynikami HEXACO i Schwartz Value Theory w obszarach związanych ze sprawiedliwością, uczciwością i dobrem innych ludzi.

Szczególnie interesujące dla dalszej analizy są:

* bardzo wysoka Równość,
* bardzo wysoka Czystość,
* wysoki Autorytet,
* bardzo niska Lojalność Grupowa.

Wymagają one dalszej weryfikacji na podstawie historii i rzeczywistych zachowań.


---

# Modele Sił Charakteru

---

# Values in Action Character Strengths (VIA)

## Metadane

| Pole                   | Wartość         |
| ---------------------- | --------------- |
| Typ Modelu             | Siły Charakteru |
| Wiarygodność Naukowa   | 8 / 10          |
| Przydatność dla Modelu | W trakcie oceny |
| Data Badania           | 2026-06-18      |
| Status                 | Aktywny         |

---

## Opis

Values in Action Character Strengths (VIA) jest modelem psychologii pozytywnej opisującym charakter człowieka poprzez zestaw 24 sił charakteru.

Model nie opisuje osobowości, zdolności ani kompetencji.

Jego celem jest identyfikacja naturalnych sposobów działania oraz cech charakteru, które człowiek najczęściej wykorzystuje podczas podejmowania decyzji, rozwiązywania problemów i budowania relacji.

Siły charakteru pogrupowane są w sześć głównych cnót:

* Mądrość (Wisdom)
* Odwaga (Courage)
* Humanitaryzm (Humanity)
* Sprawiedliwość (Justice)
* Umiarkowanie (Temperance)
* Transcendencja (Transcendence)

---

## Wyniki

### Ranking Sił Charakteru

| Pozycja | Siła Charakteru                                                          |
| ------- | ------------------------------------------------------------------------ |
| 1       | Rozsądek (Judgment)                                                      |
| 2       | Skromność (Humility)                                                     |
| 3       | Mądrość / Szerokie Horyzonty (Perspective)                               |
| 4       | Poczucie Humoru (Humor)                                                  |
| 5       | Wdzięczność (Gratitude)                                                  |
| 6       | Zdolność do Przebaczania (Forgiveness)                                   |
| 7       | Ciekawość (Curiosity)                                                    |
| 8       | Roztropność (Prudence)                                                   |
| 9       | Zespołowość (Teamwork)                                                   |
| 10      | Sprawiedliwość (Fairness)                                                |
| 11      | Energia Życiowa (Zest)                                                   |
| 12      | Zdolność do Kochania (Love)                                              |
| 13      | Wytrwałość (Perseverance)                                                |
| 14      | Odwaga (Bravery)                                                         |
| 15      | Życzliwość (Kindness)                                                    |
| 16      | Kreatywność (Creativity)                                                 |
| 17      | Inteligencja Społeczna (Social Intelligence)                             |
| 18      | Samoregulacja (Self-Regulation)                                          |
| 19      | Pasja Zdobywania Wiedzy (Love of Learning)                               |
| 20      | Nadzieja (Hope)                                                          |
| 21      | Podziw dla Piękna i Doskonałości (Appreciation of Beauty and Excellence) |
| 22      | Szczerość / Autentyczność (Honesty)                                      |
| 23      | Poczucie Sensu (Spirituality / Meaning)                                  |
| 24      | Zdolności Przywódcze (Leadership)                                        |

---

## Opis Wyników

### Rozsądek (Judgment) — bardzo wysoki

Najwyższy wynik całego profilu.

Wskazuje na silną potrzebę analizowania problemów z wielu perspektyw, oceniania argumentów oraz unikania pochopnych wniosków.

Charakterystyczna jest gotowość do zmiany stanowiska pod wpływem nowych dowodów.

### Skromność (Humility) — bardzo wysoka

Wynik sugeruje niewielką potrzebę eksponowania własnych osiągnięć oraz niską orientację na status społeczny.

Jest silnie zgodny z wysokim Honesty-Humility w modelu HEXACO.

### Mądrość / Szerokie Horyzonty (Perspective) — bardzo wysoka

Wskazuje na tendencję do patrzenia na problemy w szerszym kontekście oraz integrowania wielu punktów widzenia.

### Poczucie Humoru — wysokie

Sugestia naturalnej skłonności do wykorzystywania humoru jako narzędzia budowania relacji i radzenia sobie z trudnościami.

### Wdzięczność — wysoka

Wskazuje na zdolność dostrzegania pozytywnych aspektów życia oraz doceniania wsparcia otrzymywanego od innych ludzi.

### Zdolność do Przebaczania — wysoka

Sugeruje niewielką skłonność do długotrwałego utrzymywania urazy oraz gotowość do dawania ludziom kolejnych szans.

### Ciekawość — wysoka

Potwierdza silną orientację poznawczą widoczną również w HEXACO, AOT oraz Need for Cognition.

### Roztropność — wysoka

Wskazuje na ostrożność decyzyjną i tendencję do analizowania konsekwencji działań.

---

## Interpretacja

Profil VIA przedstawia osobę, której najmocniejsze strony koncentrują się wokół:

* jakości rozumowania,
* analizowania problemów,
* oceny argumentów,
* szerokiego spojrzenia na sytuacje,
* sprawiedliwości,
* pokory intelektualnej,
* rozwagi decyzyjnej.

Wynik nie sugeruje osoby motywowanej przywództwem, dominacją lub statusem.

Znacznie większą rolę odgrywają:

* zrozumienie sytuacji,
* trafność ocen,
* uczciwość,
* jakość decyzji.

Profil jest wyjątkowo spójny z wynikami HEXACO, Actively Open-Minded Thinking (AOT), Comprehensive Intellectual Humility Scale (CIHS) oraz Schwartz Value Theory.

---

## Notatki Badanego

TODO

---

## Ograniczenia Modelu

* Model mierzy deklarowane siły charakteru, a nie rzeczywiste zachowania.
* Wyniki opierają się na samoopisie badanego.
* Model nie mierzy kompetencji ani poziomu wiedzy.
* Ranking nie oznacza, że niższe cechy są nieobecne.
* Interpretacja wymaga zestawienia z innymi źródłami danych oraz analizą historii.

---

## Przydatność dla Modelu

W trakcie oceny.

Na obecnym etapie VIA jest jednym z najbardziej spójnych źródeł danych w całym zbiorze Assessment Data.

Najsilniejsze sygnały pojawiają się wokół:

* jakości rozumowania,
* gotowości do rewizji poglądów,
* szerokiego spojrzenia na problemy,
* pokory,
* rozwagi decyzyjnej,
* sprawiedliwości.

Model wykazuje bardzo wysoką zgodność z HEXACO, AOT, CIHS oraz Schwartz Value Theory.

Ostateczna ocena przydatności modelu zostanie przeprowadzona po analizie historii i dowodów behawioralnych.


---

# Modele Stylu Myślenia

---

# Need for Cognition (NFC)

## Metadane

| Pole                   | Wartość         |
| ---------------------- | --------------- |
| Typ Modelu             | Styl Myślenia   |
| Wiarygodność Naukowa   | 8.5 / 10        |
| Przydatność dla Modelu | W trakcie oceny |
| Data Badania           | 2026-06-18      |
| Status                 | Aktywny         |

---

## Opis

Need for Cognition (NFC) jest modelem opisującym indywidualną skłonność do angażowania się w wysiłek poznawczy.

Model nie mierzy inteligencji, wiedzy ani zdolności analitycznych.

Mierzy natomiast stopień, w jakim człowiek:

* lubi myśleć,
* lubi analizować problemy,
* czerpie satysfakcję z rozumowania,
* angażuje się w złożone zagadnienia poznawcze.

Osoby z wysokim NFC częściej podejmują decyzje na podstawie analizy argumentów, natomiast osoby z niskim NFC częściej opierają się na autorytetach, intuicjach lub uproszczonych heurystykach.

---

## Wyniki

| Skala              | Wynik   |
| ------------------ | ------- |
| Need for Cognition | 4.2 / 5 |

---

## Opis Wyników

### Need for Cognition — wysoki

Wynik wskazuje na ponadprzeciętną skłonność do angażowania się w złożone procesy myślowe.

Badany prawdopodobnie:

* odczuwa satysfakcję z analizowania problemów,
* preferuje zrozumienie mechanizmu działania zamiast zapamiętywania gotowych odpowiedzi,
* częściej poszukuje przyczyn niż objawów,
* wykazuje zainteresowanie modelami, zależnościami i strukturami.

Wysoki wynik nie oznacza większej inteligencji.

Oznacza natomiast większą motywację do korzystania z posiadanych zdolności poznawczych.

---

## Interpretacja

Profil wskazuje na osobę, która traktuje myślenie jako aktywność wartościową samą w sobie.

Rozwiązywanie problemów nie wydaje się być wyłącznie narzędziem prowadzącym do celu.

Sam proces analizy może stanowić źródło satysfakcji i zaangażowania.

W praktyce może przejawiać się to poprzez:

* budowanie modeli rzeczywistości,
* potrzebę rozumienia zależności,
* zadawanie pytań wykraczających poza bezpośredni problem,
* preferowanie głębokiego zrozumienia nad szybkim działaniem.

---

## Notatki Badanego

Wynik jest postrzegany jako trafny.

Badany wykazuje silną tendencję do rozkładania problemów na elementy składowe oraz budowania modeli wyjaśniających zjawiska.

W praktyce przejawia się to między innymi poprzez:

* tworzenie Career Vault,
* budowę Cognitive Model,
* zainteresowanie systemami decyzyjnymi,
* dążenie do identyfikowania zależności przyczynowo-skutkowych.

Jednocześnie analiza nie jest celem samym w sobie.

W większości przypadków służy zwiększeniu trafności decyzji, lepszemu zrozumieniu problemu lub uporządkowaniu chaosu informacyjnego.

---

## Ograniczenia Modelu

* Model nie mierzy inteligencji.
* Model nie mierzy wiedzy eksperckiej.
* Model nie mierzy jakości rozumowania.
* Wysoki wynik nie gwarantuje trafnych wniosków.
* Model opisuje motywację do myślenia, a nie skuteczność myślenia.
* Wyniki opierają się na samoopisie badanego.

---

## Przydatność dla Modelu

W trakcie oceny.

Na obecnym etapie model wykazuje bardzo wysoką zgodność z:

* HEXACO (Inquisitiveness),
* VIA (Judgment, Perspective, Curiosity),
* Actively Open-Minded Thinking (AOT),
* Comprehensive Intellectual Humility Scale (CIHS).

Need for Cognition może stanowić jedno z kluczowych źródeł wyjaśniających, dlaczego badany naturalnie angażuje się w analizę problemów, budowę modeli oraz porządkowanie złożonych informacji.

Ostateczna ocena przydatności modelu zostanie przeprowadzona po analizie historii i dowodów behawioralnych.


---

# Need for Closure Scale (NFCS)

## Metadane

| Pole                   | Wartość         |
| ---------------------- | --------------- |
| Typ Modelu             | Styl Myślenia   |
| Wiarygodność Naukowa   | 8.5 / 10        |
| Przydatność dla Modelu | W trakcie oceny |
| Data Badania           | 2026-06-18      |
| Status                 | Aktywny         |

---

## Opis

Need for Closure Scale (NFCS) mierzy potrzebę osiągania jednoznacznych odpowiedzi oraz tolerancję wobec niepewności i wieloznaczności.

Model opisuje stopień, w jakim człowiek odczuwa potrzebę:

* podejmowania decyzji,
* zamykania otwartych kwestii,
* redukowania niepewności,
* przechodzenia od analizy do działania.

Osoby z wysokim wynikiem zwykle preferują szybkie domknięcie problemu i większą stabilność przekonań.

Osoby z niskim wynikiem częściej tolerują niejednoznaczność, utrzymują wiele możliwych wyjaśnień oraz dłużej pozostają w fazie eksploracji.

---

## Wyniki

| Skala            | Wynik   |
| ---------------- | ------- |
| Need for Closure | 3.0 / 6 |

---

## Opis Wyników

### Need for Closure — umiarkowany

Wynik znajduje się blisko środka skali.

Nie wskazuje ani na silną potrzebę szybkiego domykania problemów, ani na szczególnie wysoką tolerancję niepewności.

Profil sugeruje zdolność funkcjonowania zarówno w trybie eksploracji, jak i w trybie decyzyjnym.

Badany wydaje się zdolny do utrzymywania niejednoznaczności przez pewien czas, ale jednocześnie nie wykazuje tendencji do niekończącej się analizy.

---

## Interpretacja

Profil sugeruje równowagę pomiędzy eksploracją a domknięciem poznawczym.

W praktyce może oznaczać:

* gotowość do zbierania dodatkowych informacji przed podjęciem decyzji,
* brak potrzeby natychmiastowego formułowania opinii,
* zdolność do funkcjonowania przy częściowej niepewności,
* jednoczesną gotowość do zakończenia analizy po osiągnięciu satysfakcjonującego poziomu zrozumienia.

Wynik jest szczególnie interesujący w zestawieniu z wysokim Need for Cognition.

Sugeruje on, że analiza nie jest napędzana potrzebą redukcji niepewności, lecz autentyczną potrzebą zrozumienia problemu.

---

## Notatki Badanego

Badany deklaruje, że po wyrobieniu sobie stanowiska zwykle przestaje aktywnie poszukiwać kolejnych informacji.

Powrót do dalszej analizy następuje najczęściej w sytuacji pojawienia się nowych danych, argumentów lub przesłanek podważających istniejący model.

W praktyce może to oznaczać, że proces analizy przebiega w dwóch etapach:

1. Intensywna eksploracja problemu.
2. Tymczasowe zamknięcie modelu i przejście do działania.

Ponowna eksploracja następuje dopiero po pojawieniu się sygnału wskazującego na potrzebę rewizji wcześniejszych założeń.

---

## Ograniczenia Modelu

* Model nie mierzy jakości decyzji.
* Model nie mierzy inteligencji ani wiedzy.
* Wyniki opierają się na samoopisie badanego.
* Potrzeba domknięcia może różnić się pomiędzy obszarami życia.
* Model nie uwzględnia wpływu kontekstu sytuacyjnego.

---

## Przydatność dla Modelu

W trakcie oceny.

Model wykazuje wysoką zgodność z wynikami:

* Need for Cognition (NFC),
* Actively Open-Minded Thinking (AOT),
* Comprehensive Intellectual Humility Scale (CIHS),
* VIA (Judgment i Prudence).

Szczególnie istotne może być wyjaśnienie relacji pomiędzy:

* wysoką potrzebą analizy,
* wysoką otwartością poznawczą,
* umiarkowaną potrzebą domknięcia.

Połączenie tych cech może odgrywać istotną rolę w sposobie podejmowania decyzji przez badanego.

Ostateczna ocena przydatności modelu zostanie przeprowadzona po analizie historii i dowodów behawioralnych.


---

# Comprehensive Intellectual Humility Scale (CIHS)

## Metadane

| Pole                   | Wartość         |
| ---------------------- | --------------- |
| Typ Modelu             | Styl Myślenia   |
| Wiarygodność Naukowa   | 8.5 / 10        |
| Przydatność dla Modelu | W trakcie oceny |
| Data Badania           | 2026-06-18      |
| Status                 | Aktywny         |

---

## Opis

Comprehensive Intellectual Humility Scale (CIHS) mierzy pokorę intelektualną.

Model nie bada skromności społecznej ani niskiej samooceny.

Jego celem jest ocena sposobu, w jaki człowiek odnosi się do własnej omylności, ograniczeń wiedzy oraz odmiennych poglądów innych ludzi.

Pokora intelektualna nie oznacza braku pewności siebie.

Oznacza zdolność do uznania możliwości własnego błędu przy jednoczesnym zachowaniu zaufania do własnego rozumowania.

---

## Wyniki

### Wynik Ogólny

| Skala                 | Wynik    |
| --------------------- | -------- |
| Intellectual Humility | 81 / 110 |
| Średnia               | 3.68 / 5 |

Interpretacja ogólna: **wysoki poziom pokory intelektualnej**.

---

## Rozbicie na Podskale

| Podskala                             | Wynik    |
| ------------------------------------ | -------- |
| Independence of Intellect and Ego    | 4.00 / 5 |
| Openness to Revising One's Viewpoint | 4.40 / 5 |
| Respect for Others' Viewpoints       | 4.17 / 5 |
| Lack of Intellectual Overconfidence  | 2.33 / 5 |

---

## Opis Wyników

### Niezależność Intelektu od Ego (Independence of Intellect and Ego) — wysoka

Wynik wskazuje na zdolność oddzielania krytyki poglądów od oceny własnej osoby.

Niezgoda lub krytyka nie są automatycznie interpretowane jako atak osobisty.

Pozwala to prowadzić dyskusję skoncentrowaną na argumentach zamiast na obronie własnego wizerunku.

### Otwartość na Rewizję Poglądów (Openness to Revising One's Viewpoint) — bardzo wysoka

Najwyższy wynik w całym profilu.

Wskazuje na dużą gotowość do zmiany stanowiska po pojawieniu się nowych danych lub mocnych argumentów.

Wynik sugeruje, że przekonania są traktowane bardziej jako robocze modele niż element tożsamości wymagający obrony za wszelką cenę.

### Szacunek dla Perspektyw Innych Ludzi (Respect for Others' Viewpoints) — wysoki

Wskazuje na uznawanie wartości odmiennych punktów widzenia nawet wtedy, gdy nie prowadzą one do zmiany własnego stanowiska.

Profil sugeruje gotowość do wysłuchania argumentów oraz próbę zrozumienia sposobu rozumowania drugiej osoby.

### Brak Nadmiernej Pewności Intelektualnej (Lack of Intellectual Overconfidence) — niski

Najniższy wynik w całym profilu.

Nie oznacza zamknięcia na argumenty.

Wskazuje natomiast na dużą pewność własnych ocen oraz wysoki próg dowodowy wymagany do zmiany stanowiska.

Profil sugeruje osobę, która jest gotowa zmienić zdanie, ale oczekuje silnych argumentów i wysokiej jakości uzasadnienia.

---

## Interpretacja

Profil wskazuje na nietypową kombinację:

* wysokiej pokory intelektualnej,
* wysokiej otwartości na zmianę poglądów,
* wysokiego szacunku dla innych perspektyw,
* jednocześnie wysokiej pewności własnych osądów.

Na pierwszy rzut oka cechy te mogą wydawać się sprzeczne.

W praktyce sugerują one osobę, która:

* nie traktuje swoich poglądów jako niepodważalnych,
* aktywnie dopuszcza możliwość błędu,
* jest gotowa zmienić zdanie,
* ale wymaga wysokiej jakości argumentacji i dowodów.

Profil nie odpowiada stereotypowi osoby niezdecydowanej lub nadmiernie sceptycznej wobec własnych ocen.

Bliższy jest obrazowi osoby posiadającej własne modele rzeczywistości, które podlegają ciągłej walidacji i aktualizacji.

---

## Notatki Badanego

Badany wskazuje, że zmiana stanowiska nie następuje często, ponieważ rzadko spotyka argumenty lub dane spełniające wymagany próg jakości.

Nie wynika to z niechęci do zmiany zdania, lecz z wysokich wymagań wobec jakości rozumowania i dowodów.

Po wypracowaniu modelu lub stanowiska dalsza analiza zwykle ustaje do momentu pojawienia się nowych przesłanek podważających wcześniejsze założenia.

Badany deklaruje gotowość do rewizji poglądów, jednak proces ten wymaga przedstawienia argumentów uznanych za istotne i dobrze uzasadnione.

---

## Ograniczenia Modelu

* Model opiera się na samoopisie badanego.
* Nie mierzy rzeczywistej jakości rozumowania.
* Nie mierzy trafności przekonań.
* Wysoka pokora intelektualna nie gwarantuje poprawności wniosków.
* Wyniki mogą zależeć od poziomu samoświadomości badanego.
* Interpretacja wymaga zestawienia z innymi źródłami danych.

---

## Przydatność dla Modelu

W trakcie oceny.

Na obecnym etapie model wykazuje bardzo wysoką zgodność z:

* Actively Open-Minded Thinking (AOT),
* Need for Cognition (NFC),
* VIA (Judgment, Perspective, Humility),
* HEXACO (Honesty-Humility, Openness).

Szczególnie istotna wydaje się kombinacja:

* wysokiej gotowości do zmiany zdania,
* wysokiego szacunku dla odmiennych perspektyw,
* wysokiej pewności własnych ocen.

Może ona stanowić ważny element wyjaśniający sposób podejmowania decyzji przez badanego.

Ostateczna ocena przydatności modelu zostanie przeprowadzona po analizie historii i dowodów behawioralnych.

---

# Actively Open-Minded Thinking (AOT)

## Metadane

| Pole                   | Wartość         |
| ---------------------- | --------------- |
| Typ Modelu             | Styl Myślenia   |
| Wiarygodność Naukowa   | 8.5 / 10        |
| Przydatność dla Modelu | W trakcie oceny |
| Data Badania           | 2026-06-18      |
| Status                 | Aktywny         |

---

## Opis

Actively Open-Minded Thinking (AOT) jest modelem opisującym sposób przetwarzania informacji, oceniania argumentów oraz podejmowania decyzji.

Model mierzy stopień, w jakim człowiek:

* aktywnie poszukuje alternatywnych wyjaśnień,
* rozważa argumenty przeciw własnym przekonaniom,
* testuje własne założenia,
* jest gotowy do aktualizacji modeli rzeczywistości pod wpływem nowych danych.

AOT nie mierzy inteligencji, wiedzy ani kompetencji.

Opisuje natomiast jakość procesu poznawczego wykorzystywanego podczas rozwiązywania problemów i formułowania wniosków.

---

## Wyniki

### Wynik Ogólny

| Skala                         | Wynik    |
| ----------------------------- | -------- |
| Actively Open-Minded Thinking | 64 / 75  |
| Średnia                       | 4.27 / 5 |

Interpretacja ogólna: **wysoki poziom aktywnie otwartego myślenia**.

---

## Opis Wyników

### Aktywne Poszukiwanie Kontrargumentów — wysokie

Wynik wskazuje na gotowość do analizowania argumentów niezgodnych z własnymi przekonaniami.

Profil sugeruje świadome poszukiwanie słabych punktów własnych modeli i założeń.

### Orientacja na Trafność Wniosków — wysoka

Badany wydaje się przywiązywać większą wagę do jakości rozumowania niż do obrony wcześniej przyjętego stanowiska.

W procesie decyzyjnym większe znaczenie ma trafność modelu niż zgodność z wcześniejszymi przekonaniami.

### Gotowość do Rewizji Poglądów — wysoka

Wynik wskazuje na otwartość na zmianę stanowiska pod wpływem nowych danych i argumentów.

Przekonania nie są traktowane jako element tożsamości wymagający ochrony za wszelką cenę.

### Poszukiwanie Alternatywnych Wyjaśnień — wysokie

Profil sugeruje naturalną tendencję do analizowania różnych możliwych interpretacji tej samej sytuacji.

Zanim zostanie przyjęte jedno wyjaśnienie, rozważane są konkurencyjne hipotezy.

---

## Interpretacja

Profil wskazuje na osobę aktywnie testującą własne przekonania.

Proces rozumowania wydaje się opierać bardziej na budowie i walidacji modeli niż na obronie wcześniej przyjętych stanowisk.

W praktyce może przejawiać się poprzez:

* analizowanie różnych perspektyw,
* poszukiwanie kontrprzykładów,
* identyfikowanie słabych punktów własnych założeń,
* budowanie modeli przyczynowo-skutkowych,
* aktualizowanie poglądów po pojawieniu się nowych danych.

Jednocześnie wysoki wynik nie oznacza nieograniczonej eksploracji.

Proces poszukiwania informacji wydaje się mieć charakter celowy i ukierunkowany na poprawę jakości modelu.

---

## Notatki Badanego

Badany deklaruje wysoką gotowość do analizowania argumentów przeczących własnym przekonaniom.

Jednocześnie po wypracowaniu satysfakcjonującego modelu dalsze poszukiwanie informacji zwykle ustaje.

Powrót do analizy następuje najczęściej po pojawieniu się:

* nowych danych,
* nowych argumentów,
* nowych okoliczności,
* sygnałów wskazujących na potencjalne błędy modelu.

W praktyce proces poznawczy wydaje się przebiegać w cyklu:

1. Intensywna eksploracja.
2. Budowa modelu.
3. Tymczasowe domknięcie.
4. Powrót do analizy po pojawieniu się nowych przesłanek.

Opis ten jest zgodny z deklaracjami badanego uzyskanymi podczas omawiania wyników testu.

---

## Ograniczenia Modelu

* Model opiera się na samoopisie badanego.
* Nie mierzy trafności wniosków.
* Nie mierzy inteligencji ani wiedzy.
* Wysoki wynik nie gwarantuje poprawnych decyzji.
* Model opisuje sposób podejścia do argumentów, a nie jakość argumentacji.
* Interpretacja wymaga zestawienia z innymi źródłami danych.

---

## Przydatność dla Modelu

W trakcie oceny.

Na obecnym etapie AOT jest jednym z najbardziej spójnych źródeł danych w całym zbiorze Assessment Data.

Model wykazuje wysoką zgodność z:

* Comprehensive Intellectual Humility Scale (CIHS),
* Need for Cognition (NFC),
* VIA (Judgment, Perspective),
* HEXACO (Openness to Experience, Inquisitiveness).

Szczególnie istotne wydają się:

* aktywne poszukiwanie kontrargumentów,
* gotowość do rewizji poglądów,
* orientacja na jakość rozumowania,
* budowanie modeli opartych na dowodach.

Ostateczna ocena przydatności modelu zostanie przeprowadzona po analizie historii i dowodów behawioralnych.


---

# Modele Talentów

---

# CliftonStrengths (Gallup)

## Metadane

| Pole                   | Wartość                                 |
| ---------------------- | --------------------------------------- |
| Typ Modelu             | Talenty i preferowane sposoby działania |
| Wiarygodność Naukowa   | 5.5 / 10                                |
| Przydatność dla Modelu | Wysoka                                  |
| Data Badania           | 2026-06-17                              |
| Status                 | Aktywny                                 |

---

## Opis

CliftonStrengths (dawniej StrengthsFinder) jest modelem identyfikującym naturalne talenty oraz preferowane sposoby działania.

Model nie mierzy osobowości, inteligencji, wiedzy ani kompetencji.

Jego celem jest określenie wzorców myślenia, odczuwania i działania, które pojawiają się spontanicznie oraz mogą zostać rozwinięte w mocne strony.

Gallup zakłada, że największy potencjał rozwoju wynika z rozwijania naturalnych talentów, a nie wyłącznie z eliminowania słabości.

---

## Wyniki

### Dominująca Domena

**Myślenie Strategiczne (Strategic Thinking)**

Najsilniejszą domeną profilu jest Myślenie Strategiczne.

---

### Ranking Talentów

| Pozycja | Talent                               |
| ------- | ------------------------------------ |
| 1       | Uczenie się (Learner)                |
| 2       | Pryncypialność (Belief)              |
| 3       | Strateg (Strategic)                  |
| 4       | Współzależność (Connectedness)       |
| 5       | Analityk (Analytical)                |
| 6       | Odpowiedzialność (Responsibility)    |
| 7       | Bliskość (Relator)                   |
| 8       | Indywidualizacja (Individualization) |
| 9       | Rozwijanie Innych (Developer)        |
| 10      | Intelekt (Intellection)              |
| 11      | Dyscyplina (Discipline)              |
| 12      | Bezstronność (Consistency)           |
| 13      | Organizator (Arranger)               |
| 14      | Naprawianie (Restorative)            |
| 15      | Empatia (Empathy)                    |
| 16      | Osiąganie (Achiever)                 |
| 17      | Maksymalista (Maximizer)             |
| 18      | Kontekst (Context)                   |
| 19      | Zgodność (Harmony)                   |
| 20      | Zbieranie (Input)                    |
| 21      | Wiara w Siebie (Self-Assurance)      |
| 22      | Optymista (Positivity)               |
| 23      | Wizjoner (Futuristic)                |
| 24      | Ukierunkowanie (Focus)               |
| 25      | Komunikatywność (Communication)      |
| 26      | Odkrywczość (Ideation)               |
| 27      | Rozwaga (Deliberative)               |
| 28      | Elastyczność (Adaptability)          |
| 29      | Aktywator (Activator)                |
| 30      | CZAR (Woo)                           |
| 31      | Rywalizacja (Competition)            |
| 32      | Poważanie (Significance)             |
| 33      | Integrator (Includer)                |
| 34      | Dowodzenie (Command)                 |

---

## Opis Wyników

### Top 5 Talentów

#### Uczenie się (#1)

Najsilniejszy talent w profilu.

Wskazuje na motywację do zdobywania wiedzy, rozwijania kompetencji i pogłębiania zrozumienia. Satysfakcję przynosi nie tylko rezultat, ale również sam proces uczenia się.

#### Pryncypialność (#2)

Silna orientacja na wartości, zasady i poczucie celu.

Decyzje często oceniane są przez pryzmat zgodności z wewnętrznym systemem wartości.

#### Strateg (#3)

Naturalna zdolność dostrzegania możliwych ścieżek działania, scenariuszy i alternatywnych rozwiązań.

Talent ten wspiera podejmowanie decyzji w warunkach niepewności.

#### Współzależność (#4)

Skłonność do dostrzegania zależności pomiędzy ludźmi, wydarzeniami i systemami.

Wysoka potrzeba rozumienia szerszego kontekstu sytuacji.

#### Analityk (#5)

Naturalna potrzeba rozumienia przyczyn, zależności i mechanizmów.

Silna orientacja na logikę, dowody oraz analizę danych.

---

### Pozostałe Talenty z Top 10

#### Odpowiedzialność (#6)

Silne poczucie zobowiązania wobec podjętych deklaracji i obowiązków.

#### Bliskość (#7)

Preferencja budowania głębokich relacji opartych na zaufaniu zamiast szerokiej sieci powierzchownych kontaktów.

#### Indywidualizacja (#8)

Naturalna zdolność dostrzegania indywidualnych różnic pomiędzy ludźmi.

#### Rozwijanie Innych (#9)

Skłonność do dostrzegania potencjału innych osób i wspierania ich rozwoju.

#### Intelekt (#10)

Potrzeba refleksji, analizowania oraz prowadzenia pogłębionych procesów myślowych.

---

## Interpretacja

Profil Gallupa wskazuje na dominację talentów związanych z:

* uczeniem się,
* analizą,
* budowaniem modeli,
* rozumieniem zależności,
* podejmowaniem decyzji,
* wspieraniem rozwoju innych ludzi.

Najsilniejsza domena — Myślenie Strategiczne — pojawia się konsekwentnie w całym profilu.

Wysokie pozycje talentów takich jak:

* Uczenie się,
* Strateg,
* Analityk,
* Intelekt,

sugerują preferencję dla pracy koncepcyjnej, analitycznej i systemowej.

Jednocześnie wysokie pozycje:

* Pryncypialności,
* Odpowiedzialności,
* Bliskości,
* Rozwijania Innych,

wskazują na silny komponent wartościowy i relacyjny.

Profil nie wskazuje na naturalną potrzebę dominacji, rywalizacji ani zdobywania statusu społecznego.

Najniżej sklasyfikowane zostały:

* Dowodzenie,
* Poważanie,
* Rywalizacja,
* CZAR.

Może to sugerować preferowanie wpływu poprzez wiedzę, argumentację i relacje zamiast formalnego autorytetu lub pozycji.

---

## Notatki Badanego

TBD

---

## Ograniczenia Modelu

* Model nie mierzy osobowości.
* Model nie mierzy inteligencji.
* Model nie mierzy kompetencji.
* Model nie przewiduje skuteczności zawodowej.
* Wyniki opierają się na autodeklaracji.
* Gallup posiada ograniczone wsparcie naukowe w porównaniu do modeli takich jak Big Five lub HEXACO.
* Talenty opisują preferowane sposoby działania, a nie rzeczywiste zachowania.

---

## Przydatność dla Modelu

### Ocena Wstępna

**Wysoka**

Model dostarcza wartościowych informacji o naturalnych preferencjach poznawczych i behawioralnych badanego.

Szczególnie istotne dla budowy Cognitive Model wydają się talenty:

* Uczenie się,
* Strateg,
* Analityk,
* Pryncypialność,
* Intelekt.

Profil jest spójny z wynikami:

* HEXACO,
* VIA,
* Need for Cognition,
* Actively Open-Minded Thinking,
* Comprehensive Intellectual Humility Scale,
* Schwartz Value Theory.

Gallup może stanowić istotne źródło danych przy identyfikacji predyktorów dotyczących sposobu uczenia się, analizowania problemów, podejmowania decyzji oraz rozwoju innych ludzi.

Ostateczna ocena przydatności modelu zostanie przeprowadzona po analizie historii i dowodów behawioralnych.

---

# CliftonStrengths (Gallup)

## Metadane

| Pole                   | Wartość                                 |
| ---------------------- | --------------------------------------- |
| Typ Modelu             | Talenty i preferowane sposoby działania |
| Wiarygodność Naukowa   | 5.5 / 10                                |
| Przydatność dla Modelu | Wysoka                                  |
| Data Badania           | 2026-06-17                              |
| Status                 | Aktywny                                 |

---

## Opis

CliftonStrengths (dawniej StrengthsFinder) jest modelem identyfikującym naturalne talenty oraz preferowane sposoby działania.

Model nie mierzy osobowości, inteligencji, wiedzy ani kompetencji.

Jego celem jest określenie wzorców myślenia, odczuwania i działania, które pojawiają się spontanicznie oraz mogą zostać rozwinięte w mocne strony.

Gallup zakłada, że największy potencjał rozwoju wynika z rozwijania naturalnych talentów, a nie wyłącznie z eliminowania słabości.

---

## Wyniki

### Dominująca Domena

**Myślenie Strategiczne (Strategic Thinking)**

Najsilniejszą domeną profilu jest Myślenie Strategiczne.

---

### Ranking Talentów

| Pozycja | Talent                               |
| ------- | ------------------------------------ |
| 1       | Uczenie się (Learner)                |
| 2       | Pryncypialność (Belief)              |
| 3       | Strateg (Strategic)                  |
| 4       | Współzależność (Connectedness)       |
| 5       | Analityk (Analytical)                |
| 6       | Odpowiedzialność (Responsibility)    |
| 7       | Bliskość (Relator)                   |
| 8       | Indywidualizacja (Individualization) |
| 9       | Rozwijanie Innych (Developer)        |
| 10      | Intelekt (Intellection)              |
| 11      | Dyscyplina (Discipline)              |
| 12      | Bezstronność (Consistency)           |
| 13      | Organizator (Arranger)               |
| 14      | Naprawianie (Restorative)            |
| 15      | Empatia (Empathy)                    |
| 16      | Osiąganie (Achiever)                 |
| 17      | Maksymalista (Maximizer)             |
| 18      | Kontekst (Context)                   |
| 19      | Zgodność (Harmony)                   |
| 20      | Zbieranie (Input)                    |
| 21      | Wiara w Siebie (Self-Assurance)      |
| 22      | Optymista (Positivity)               |
| 23      | Wizjoner (Futuristic)                |
| 24      | Ukierunkowanie (Focus)               |
| 25      | Komunikatywność (Communication)      |
| 26      | Odkrywczość (Ideation)               |
| 27      | Rozwaga (Deliberative)               |
| 28      | Elastyczność (Adaptability)          |
| 29      | Aktywator (Activator)                |
| 30      | CZAR (Woo)                           |
| 31      | Rywalizacja (Competition)            |
| 32      | Poważanie (Significance)             |
| 33      | Integrator (Includer)                |
| 34      | Dowodzenie (Command)                 |

---

## Opis Wyników

### Top 5 Talentów

#### Uczenie się (#1)

Najsilniejszy talent w profilu.

Wskazuje na motywację do zdobywania wiedzy, rozwijania kompetencji i pogłębiania zrozumienia. Satysfakcję przynosi nie tylko rezultat, ale również sam proces uczenia się.

#### Pryncypialność (#2)

Silna orientacja na wartości, zasady i poczucie celu.

Decyzje często oceniane są przez pryzmat zgodności z wewnętrznym systemem wartości.

#### Strateg (#3)

Naturalna zdolność dostrzegania możliwych ścieżek działania, scenariuszy i alternatywnych rozwiązań.

Talent ten wspiera podejmowanie decyzji w warunkach niepewności.

#### Współzależność (#4)

Skłonność do dostrzegania zależności pomiędzy ludźmi, wydarzeniami i systemami.

Wysoka potrzeba rozumienia szerszego kontekstu sytuacji.

#### Analityk (#5)

Naturalna potrzeba rozumienia przyczyn, zależności i mechanizmów.

Silna orientacja na logikę, dowody oraz analizę danych.

---

### Pozostałe Talenty z Top 10

#### Odpowiedzialność (#6)

Silne poczucie zobowiązania wobec podjętych deklaracji i obowiązków.

#### Bliskość (#7)

Preferencja budowania głębokich relacji opartych na zaufaniu zamiast szerokiej sieci powierzchownych kontaktów.

#### Indywidualizacja (#8)

Naturalna zdolność dostrzegania indywidualnych różnic pomiędzy ludźmi.

#### Rozwijanie Innych (#9)

Skłonność do dostrzegania potencjału innych osób i wspierania ich rozwoju.

#### Intelekt (#10)

Potrzeba refleksji, analizowania oraz prowadzenia pogłębionych procesów myślowych.

---

## Interpretacja

Profil Gallupa wskazuje na dominację talentów związanych z:

* uczeniem się,
* analizą,
* budowaniem modeli,
* rozumieniem zależności,
* podejmowaniem decyzji,
* wspieraniem rozwoju innych ludzi.

Najsilniejsza domena — Myślenie Strategiczne — pojawia się konsekwentnie w całym profilu.

Wysokie pozycje talentów takich jak:

* Uczenie się,
* Strateg,
* Analityk,
* Intelekt,

sugerują preferencję dla pracy koncepcyjnej, analitycznej i systemowej.

Jednocześnie wysokie pozycje:

* Pryncypialności,
* Odpowiedzialności,
* Bliskości,
* Rozwijania Innych,

wskazują na silny komponent wartościowy i relacyjny.

Profil nie wskazuje na naturalną potrzebę dominacji, rywalizacji ani zdobywania statusu społecznego.

Najniżej sklasyfikowane zostały:

* Dowodzenie,
* Poważanie,
* Rywalizacja,
* CZAR.

Może to sugerować preferowanie wpływu poprzez wiedzę, argumentację i relacje zamiast formalnego autorytetu lub pozycji.

---

## Notatki Badanego

TBD

---

## Ograniczenia Modelu

* Model nie mierzy osobowości.
* Model nie mierzy inteligencji.
* Model nie mierzy kompetencji.
* Model nie przewiduje skuteczności zawodowej.
* Wyniki opierają się na autodeklaracji.
* Gallup posiada ograniczone wsparcie naukowe w porównaniu do modeli takich jak Big Five lub HEXACO.
* Talenty opisują preferowane sposoby działania, a nie rzeczywiste zachowania.

---

## Przydatność dla Modelu

### Ocena Wstępna

**Wysoka**

Model dostarcza wartościowych informacji o naturalnych preferencjach poznawczych i behawioralnych badanego.

Szczególnie istotne dla budowy Cognitive Model wydają się talenty:

* Uczenie się,
* Strateg,
* Analityk,
* Pryncypialność,
* Intelekt.

Profil jest spójny z wynikami:

* HEXACO,
* VIA,
* Need for Cognition,
* Actively Open-Minded Thinking,
* Comprehensive Intellectual Humility Scale,
* Schwartz Value Theory.

Gallup może stanowić istotne źródło danych przy identyfikacji predyktorów dotyczących sposobu uczenia się, analizowania problemów, podejmowania decyzji oraz rozwoju innych ludzi.

Ostateczna ocena przydatności modelu zostanie przeprowadzona po analizie historii i dowodów behawioralnych.


---

# Analiza Międzymodelowa

## Cel

Celem niniejszej sekcji jest identyfikacja obszarów zgodności, niezgodności oraz powtarzających się wzorców występujących pomiędzy poszczególnymi źródłami danych zgromadzonymi w dokumencie Assessment Data.

Analiza nie ma na celu tworzenia ostatecznych wniosków dotyczących badanego.

Jej zadaniem jest:

* identyfikacja potencjalnych predyktorów,
* wskazanie obszarów wymagających dalszej weryfikacji,
* wykrycie sprzeczności pomiędzy modelami,
* przygotowanie danych wejściowych dla kolejnych etapów budowy Cognitive Model.

Wszystkie wnioski zawarte w tej sekcji mają charakter roboczy i mogą zostać zmienione w wyniku analizy historii, dowodów behawioralnych oraz późniejszej kalibracji modelu.

---

# Najsilniejsze Źródła Danych

## Wysoka wartość naukowa i wysoka zgodność

| Model                                            | Waga Naukowa  | Waga dla Modelu |
| ------------------------------------------------ | ------------- | --------------- |
| HEXACO                                           | Bardzo wysoka | Bardzo wysoka   |
| Schwartz Value Theory                            | Bardzo wysoka | Wysoka          |
| Need for Cognition (NFC)                         | Wysoka        | Bardzo wysoka   |
| Actively Open-Minded Thinking (AOT)              | Wysoka        | Bardzo wysoka   |
| Comprehensive Intellectual Humility Scale (CIHS) | Wysoka        | Bardzo wysoka   |

---

## Uzupełniające źródła danych

| Model                     | Waga Naukowa   | Waga dla Modelu   |
| ------------------------- | -------------- | ----------------- |
| VIA Character Strengths   | Średnio-wysoka | Wysoka            |
| Moral Foundations Theory  | Średnia        | Średnia           |
| CliftonStrengths (Gallup) | Niska-średnia  | Wysoka praktyczna |
| Big Five                  | Bardzo wysoka  | Średnia           |

---

# Obszary Wysokiej Zgodności

## 1. Silna Orientacja Poznawcza

### Źródła

* Need for Cognition
* AOT
* CIHS
* HEXACO
* VIA
* Gallup

### Powtarzające się sygnały

* wysoka ciekawość poznawcza,
* potrzeba rozumienia zjawisk,
* budowanie modeli rzeczywistości,
* zainteresowanie zależnościami przyczynowo-skutkowymi,
* satysfakcja płynąca z procesu uczenia się.

### Pewność

**Bardzo wysoka**

---

## 2. Decyzje Oparte na Modelach i Argumentach

### Źródła

* VIA (Judgment)
* AOT
* CIHS
* NFC
* HEXACO (Prudence)
* Gallup (Strategic, Analytical)

### Powtarzające się sygnały

* analiza przed działaniem,
* poszukiwanie przyczyn zamiast objawów,
* budowanie modeli sytuacji,
* ocena jakości argumentów,
* preferencja rozwiązań opartych na zrozumieniu problemu.

### Pewność

**Bardzo wysoka**

---

## 3. Niska Orientacja na Status i Dominację

### Źródła

* Schwartz
* HEXACO
* VIA
* Gallup

### Powtarzające się sygnały

* niska motywacja związana z prestiżem,
* niewielkie znaczenie statusu społecznego,
* brak potrzeby dominacji,
* brak potrzeby rywalizacji dla samej rywalizacji.

### Pewność

**Wysoka**

---

## 4. Wysoka Orientacja na Uczciwość i Sprawiedliwość

### Źródła

* HEXACO
* Schwartz
* VIA
* Moral Foundations Theory

### Powtarzające się sygnały

* wysoka wrażliwość na uczciwość,
* znaczenie sprawiedliwego traktowania,
* respektowanie zasad,
* niechęć wobec działań postrzeganych jako nieuczciwe.

### Pewność

**Wysoka**

---

## 5. Gotowość do Aktualizacji Poglądów

### Źródła

* AOT
* CIHS
* VIA (Judgment)

### Powtarzające się sygnały

* otwartość na nowe dane,
* gotowość do rewizji stanowiska,
* wysoka wartość przypisywana trafności modelu.

### Pewność

**Wysoka**

### Dodatkowa obserwacja

Aktualizacja poglądów wydaje się następować na poziomie modelu rzeczywistości, a nie na poziomie pojedynczych opinii.

Badany nie deklaruje częstej zmiany zdania, jednak opisuje szybkie aktualizowanie modeli po pojawieniu się wystarczająco wiarygodnych danych.

---

# Obszary Umiarkowanej Zgodności

## 1. Rozwijanie Innych Ludzi

### Źródła

* Gallup (Developer)
* Schwartz (Benevolence)
* VIA

### Obserwacja

Pojawia się tendencja do wspierania rozwoju innych ludzi, jednak obecnie brakuje wystarczającej liczby dowodów behawioralnych pozwalających ocenić znaczenie tego wzorca.

### Pewność

**Średnia**

---

## 2. Myślenie Systemowe

### Źródła

* Gallup (Connectedness)
* Gallup (Strategic)
* Gallup (Analytical)
* HEXACO (Inquisitiveness)

### Obserwacja

Badany wykazuje tendencję do postrzegania problemów jako elementów większych systemów oraz do analizowania wzajemnych zależności.

Wymaga dalszej walidacji na podstawie rzeczywistych historii.

### Pewność

**Średnia**

---

# Obszary Pozornej Sprzeczności

## 1. Tradycja i Konformizm (Schwartz)

### Wyniki

* Tradition: wysoki
* Conformity: wysoki

### Potencjalna sprzeczność

Wynik wydaje się niezgodny z:

* wysokim AOT,
* wysokim CIHS,
* wysokim Judgment,
* wysoką niezależnością poznawczą.

### Wyjaśnienie

Analiza jakościowa wskazuje, że wyniki te prawdopodobnie nie odzwierciedlają potrzeby podporządkowania się normom społecznym lub autorytetom.

Bardziej prawdopodobna interpretacja:

* szacunek dla sprawdzonych rozwiązań,
* szacunek dla procedur posiadających uzasadnienie,
* preferencja rozumienia zasad przed ich bezrefleksyjnym stosowaniem.

### Status

**Wstępnie wyjaśnione**

---

## 2. Authority vs Loyalty (MFT)

### Wyniki

* Authority: wysokie
* Loyalty: niskie

### Potencjalna sprzeczność

Nietypowa kombinacja w ramach Moral Foundations Theory.

### Wyjaśnienie

Analiza wskazuje, że autorytet jest postrzegany przede wszystkim przez pryzmat:

* kompetencji,
* odpowiedzialności,
* funkcji organizacyjnej.

Jednocześnie nie występuje silna orientacja plemienna ani grupowa.

Hierarchia jest akceptowana jako mechanizm organizacyjny, a nie jako źródło moralnej lojalności.

### Status

**Wstępnie wyjaśnione**

---

## 3. Leadership (VIA) vs Wpływ na Otoczenie

### Wyniki

* Leadership: bardzo nisko

### Obserwacja

Badany nie wykazuje potrzeby zarządzania ludźmi ani zajmowania formalnych stanowisk przywódczych.

Jednocześnie przejawia silną tendencję do:

* porządkowania problemów,
* projektowania rozwiązań,
* wpływania na jakość decyzji.

### Wyjaśnienie

Preferowaną rolą wydaje się:

* ekspert,
* architekt rozwiązania,
* konsultant,
* doradca.

Nie zaś:

* kierownik,
* menedżer,
* formalny lider.

### Status

**Wstępnie wyjaśnione**

---

# Obszary Wymagające Kalibracji

## 1. Kontekstualna Sumienność (Hiperfokus)

### Źródła

- Big Five Personality Model
- HEXACO Personality Inventory
- CliftonStrengths (Gallup)
- Wywiad jakościowy
- Przyszła analiza historii

### Obserwacja

Największa rozbieżność pomiędzy modelami występuje w obszarze sumienności.

Big Five sugeruje umiarkowanie niski poziom sumienności, szczególnie w zakresie:

- samodyscypliny,
- porządku,
- konsekwentnej organizacji działań.

Jednocześnie HEXACO wskazuje na umiarkowanie wysoką sumienność, szczególnie w obszarach:

- rozwagi,
- planowania,
- organizacji,
- analizowania konsekwencji działań.

Dodatkowo Gallup wskazuje na obecność talentów takich jak:

- Responsibility,
- Strategic,
- Analytical,
- Discipline,
- Learner.

Analiza jakościowa oraz obserwowane zachowania nie są zgodne z profilem osoby o konsekwentnie niskiej sumienności.

### Hipoteza

Badany nie wykazuje jednolitego poziomu sumienności we wszystkich obszarach życia.

Zasoby związane z organizacją, planowaniem, wytrwałością i kontrolą jakości wydają się aktywowane selektywnie.

Najwyższy poziom organizacji pojawia się w sytuacjach, które:

- są uznawane za ważne,
- posiadają wysoką wartość poznawczą,
- rozwiązują realny problem,
- mają znaczenie strategiczne,
- znajdują się w obszarze aktualnego zainteresowania lub hiperfokusu.

Jednocześnie obszary uznane za mało istotne mogą pozostawać w stanie względnej dezorganizacji bez odczuwania istotnego dyskomfortu.

### Wstępna Interpretacja

Obserwowane wyniki mogą sugerować, że sumienność nie funkcjonuje jako stała cecha aktywna we wszystkich kontekstach.

Bardziej prawdopodobny jest model selektywnej aktywacji zasobów poznawczych i wykonawczych.

W praktyce może to prowadzić do sytuacji, w których ten sam badany prezentuje:

- bardzo wysoki poziom organizacji,
- bardzo wysoki poziom szczegółowości,
- bardzo wysoką jakość wykonania,

w jednych obszarach życia,

oraz:

- niski poziom organizacji,
- odkładanie działań,
- ograniczone zaangażowanie,

w innych.

### Status

**Wymaga dalszej walidacji na podstawie historii i dowodów behawioralnych.**

---

## 2. Ugodowość a Tolerancja Błędów Poznawczych

### Źródła

- Big Five Personality Model
- HEXACO Personality Inventory
- VIA Character Strengths
- Schwartz Value Theory
- Moral Foundations Theory
- Wywiad jakościowy

### Obserwacja

Wyniki modeli osobowościowych przedstawiają częściowo odmienne obrazy ugodowości.

Big Five sugeruje umiarkowanie niski poziom ugodowości.

Jednocześnie HEXACO wskazuje na wysokie wyniki w obszarach:

- Forgiveness,
- Gentleness,
- Patience.

Podobny obraz pojawia się w:

- Benevolence (Schwartz),
- Care (MFQ),
- Forgiveness (VIA),
- Humility (VIA).

Analiza jakościowa wskazuje dodatkowo, że badany jest częściej postrzegany jako osoba życzliwa niż konfliktowa.

Jednocześnie deklaruje bardzo niski poziom tolerancji wobec:

- błędów logicznych,
- niespójności argumentacyjnych,
- błędnych modeli rzeczywistości,
- nieuzasadnionych założeń.

### Hipoteza

Rozbieżność może wynikać z faktu, że badany oddziela ocenę człowieka od oceny jego argumentów, decyzji lub sposobu rozumowania.

Krytyka kierowana jest najczęściej wobec:

- modelu,
- procesu,
- założenia,
- argumentacji,

a nie wobec osoby.

W efekcie zachowanie może być odbierane jako wymagające lub konfrontacyjne pomimo braku negatywnych intencji interpersonalnych.

### Wstępna Interpretacja

Najbardziej prawdopodobna interpretacja wskazuje na połączenie:

- wysokiej tolerancji wobec ludzi,
- wysokiej cierpliwości,
- wysokiej skłonności do wybaczania,

przy jednocześnie:

- niskiej tolerancji dla błędów poznawczych,
- niskiej tolerancji dla słabej argumentacji,
- wysokich wymaganiach wobec jakości rozumowania.

Może to wyjaśniać rozbieżności pomiędzy wynikami Big Five i HEXACO.

### Status

**Wymaga dalszej walidacji na podstawie historii, relacji zawodowych oraz rzeczywistych sytuacji konfliktowych.**

---

## 3. Pewność Własnych Ocen a Otwartość na Zmianę Zdania

### Źródła

- AOT
- CIHS
- VIA
- Need for Cognition
- Wywiad jakościowy

### Obserwacja

Modele wskazują jednocześnie na:

- wysoką otwartość poznawczą,
- wysoką gotowość do rewizji poglądów,
- wysoką pokorę intelektualną.

Jednocześnie badany deklaruje, że stosunkowo rzadko doświadcza sytuacji, w których inni ludzie przekonują go do zmiany stanowiska.

Dodatkowo podskala Lack of Intellectual Overconfidence w CIHS uzyskała najniższy wynik spośród wszystkich podskal.

### Hipoteza

Badany nie wykazuje niskiej otwartości na zmianę poglądów.

Wykazuje natomiast wysoki próg dowodowy wymagany do aktualizacji istniejącego modelu.

Zmiana stanowiska nie następuje często nie dlatego, że jest blokowana emocjonalnie, lecz dlatego, że rzadko pojawiają się argumenty uznane za wystarczająco mocne.

### Wstępna Interpretacja

Przekonania wydają się funkcjonować jako modele robocze.

Model pozostaje aktywny do momentu pojawienia się danych lub argumentów zdolnych znacząco zwiększyć jego trafność.

W praktyce może to prowadzić do połączenia:

- wysokiej pewności własnych ocen,
- wysokiej gotowości do aktualizacji modelu,
- stosunkowo rzadkich zmian stanowiska.

Pozornie cechy te mogą wydawać się sprzeczne, jednak są zgodne z wynikami AOT, CIHS oraz wywiadu jakościowego.

### Status

**Wstępnie wyjaśnione, wymaga dalszej obserwacji.**

---

## 4. Tradycja i Konformizm a Niezależność Poznawcza

### Źródła

- Schwartz Value Theory
- AOT
- CIHS
- VIA
- Wywiad jakościowy

### Obserwacja

Model Schwartza wskazuje podwyższone wyniki dla:

- Tradition,
- Conformity.

Jednocześnie pozostałe modele wskazują na:

- wysoką niezależność poznawczą,
- wysoką otwartość na zmianę poglądów,
- wysoką gotowość do kwestionowania założeń,
- wysoką orientację na argumenty i dowody.

### Hipoteza

Wysokie wyniki Tradycji i Konformizmu nie odzwierciedlają potrzeby podporządkowania się normom społecznym lub autorytetom.

Bardziej prawdopodobna interpretacja wskazuje na szacunek wobec:

- sprawdzonych rozwiązań,
- skutecznych procedur,
- zasad posiadających uzasadnienie,
- struktur wspierających funkcjonowanie systemów.

### Wstępna Interpretacja

Badany nie wydaje się kierować zasadą:

> „Tak należy robić, ponieważ zawsze tak robiono.”

Znacznie bliższe wydaje się podejście:

> „Jeżeli coś działa, należy rozumieć dlaczego działa, a następnie ulepszać to tylko wtedy, gdy istnieją ku temu wystarczające przesłanki.”

### Status

**Wstępnie wyjaśnione, wymaga dalszej walidacji na podstawie historii i decyzji organizacyjnych.**

---

# Powtarzające się Motywy

## Motyw 1

### Rozumienie przed działaniem

Badany wykazuje silną tendencję do budowania modelu sytuacji przed podjęciem decyzji.

---

## Motyw 2

### Trafność ponad status

Ocena sytuacji wydaje się opierać przede wszystkim na jakości argumentów i rozwiązań, a nie na pozycji społecznej ich autora.

---

## Motyw 3

### Zasady ponad plemienność

Decyzje wydają się częściej wynikać z zasad, wartości i logiki niż z lojalności wobec konkretnej grupy.

---

## Motyw 4

### Uczenie się jako mechanizm działania

Proces zdobywania wiedzy i rozumienia stanowi istotny element funkcjonowania badanego.

---

## Motyw 5

### Aktualizacja modeli rzeczywistości

Badany wydaje się traktować przekonania jako modele robocze podlegające aktualizacji wraz z pojawianiem się nowych danych.

---

## Motyw 6

### Selektywna Aktywacja Zasobów

Wysoka jakość działania pojawia się przede wszystkim tam, gdzie badany uznaje zadanie za ważne, interesujące lub strategiczne. Nie jest to profil stałej, równomiernej organizacji, lecz raczej profil selektywnego uruchamiania pełnej mocy poznawczej i wykonawczej.

---

# Wstępni Kandydaci na Predyktory

Poniższe pozycje nie stanowią jeszcze predyktorów.

Są kandydatami do dalszej analizy.

1. Model-Centric Decision Making
2. Evidence-Driven Belief Updating
3. Fairness-Oriented Evaluation
4. Principle-Based Decision Making
5. Learning-Oriented Exploration
6. Systemic Problem Structuring
7. Low Status Motivation
8. Selective Cognitive Reopening
9. Expert-over-Manager Preference
10. Proven-System Optimization
11. Stakes-Adjusted Evidence Threshold
12. Tolerance for People vs Cognitive Errors
13. Strategic Self-Presentation / Attention Management
14. Supportive Facilitation Orientation

---

# Wnioski

Pomimo wykorzystania wielu różnych modeli psychologicznych, poznawczych i wartościowych, większość źródeł wskazuje na zaskakująco spójny obraz badanego.

Najsilniejszym wspólnym wzorcem jest orientacja na rozumienie rzeczywistości poprzez budowanie modeli, analizowanie zależności oraz podejmowanie decyzji opartych na argumentach i wartościach.

Znacznie mniejsze znaczenie wydają się mieć:

* status społeczny,
* dominacja,
* rywalizacja,
* formalne przywództwo.

Wysokie znaczenie mają natomiast:

* uczciwość,
* sprawiedliwość,
* jakość rozumowania,
* odpowiedzialność,
* ciągłe doskonalenie modeli rzeczywistości.

Analiza wskazuje, że kolejnym etapem projektu powinno być przejście od opisu wyników testów do budowy predyktorów, hipotez oraz ich walidacji na podstawie rzeczywistych historii i dowodów behawioralnych.

---

# Historia Wersji

## v1.0

Pierwsza wersja repozytorium źródeł dowodowych dla Cognitive Model.

### Wykorzystane źródła

* Gallup CliftonStrengths
* Big Five Personality Model (BFM)
* HEXACO Personality Inventory (HEXACO)
* Values in Action Character Strengths (VIA)
* Schwartz Value Theory (SVT)
* Moral Foundations Theory Questionnaire (MFQ)
* Need for Cognition (NFC)
* Need for Closure Scale (NFCS)
* Comprehensive Intellectual Humility Scale (CIHS)
* Actively Open-Minded Thinking (AOT)
