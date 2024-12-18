## Zasady konkursu SRD
### Zespoły
Należy dobrać się w zespoły złożone z maksymalnie 3 osób. Proszę nazwać zespół (nazwa zespołu pojawi się w tabeli z wynikami). Proszę nie używać danych osobowych w nazwach.

### Zbiór danych i cel konkursu
Celem konkursu jest uzyskanie jak największego:
* Grupy 11,13,15 - [**F1-Score**](https://en.wikipedia.org/wiki/F-score)
* Grupy 12,14 - Accuracy

w klasyfikacji zmiennej celu **IsIPA**. Do stworzenia i optymalizacji modelu proszę wykorzystać zbiór danych **IPA.csv**, natomiast finalną predykcję należy wykonać na zbiorze **IPA_test.csv**. Opis zbioru znajduje się w pliku **IPA_description.txt**.


### Wyniki
Wyniki należy przesłać na adres **lkrain@sgh.waw.pl** do końca zajęć danej grupy. W treści maila należy podać nazwę grupy oraz imiona i nazwiska członków - wystarczy mail od jednego członka grupy.

Jako załączniki należy zamieścić:
1. Skrypt/notatnik z wykorzystanym kodem (w dowolnym języku programowania)
2. Plik CSV o nazwie **[nazwa_grupy]_prediction.csv** zawierający jedną kolumnę z 5000 obserwacji (i opcjonalnym nagłówkiem) z wartościami 1/0 lub TRUE/FALSE oznaczających predykcję dla kolejnych wierszy ze zbioru testowego **IPA_test.csv**.

Proszę sprawdzić czy kolejność predykcji zgadza się z kolejnością obserwacji w zbiorze testowym. Proszę również zwrócić uwagę na braki danych w zbiorze testowym - należy je odpowiednio obsłużyć tak, aby otrzymać dokładnie 5000 predykcji.

Tabela z rankingiem zespołów pojawi się na GitHubie w poniższym pliku README. Najlepszy zespół w każdej grupie zajęciowej otrzyma dodatkowe 5 punktów, kolejny 4 punkty, itd.

Życzę powodzenia.

### Wyniki konkursu

Grupa 11

| **Zespół**            | **Punkty** | **F1-Score** | **Model**                                        | **Język** |
|-----------------------|------------|--------------|--------------------------------------------------|-----------|
| Reaktor Nuklearny SMR | 5          | 78,93%       | Ensemble (XGBoost, Boosted Trees, Random Forest) | Python    |
| MR                    | 4          | 75,66%       | Decision Tree                                    | Python    |
| Muchomorki            | 3          | 74,61%       | Logistic Regression                              | Python    |
| TOP Modelarze         | 2          | 70,66%       | Logistic Regression                              | Python    |
| Rower Ojca Mateusza     | 1          | 69,92%       | Logistic Regression                              | Python    |

Grupa 12

| **Zespół**         | **Punkty** | **Accuracy** | **Model**                                   | **Język** |
|--------------------|------------|--------------|---------------------------------------------|-----------|
| Crispy Nuggets     | 5          | 87,06%       | Ensemble (XGBoost, LightGBM, Random Forest) | Python    |
| Dane Osobowe       | 4          | 87,04%       | XGBoost                                     | Python    |
| Banksterzy         | 3          | 86,68%       | XGBoost                                     | Python    |
| Tom i Jerry        | 2          | 86,54%       | Boosted Trees                               | Python    |
| Grupa 3Osobowa     | 1          | 85,98%       | XGBoost                                     | R         |
| Polish Pale Ale    | 1          | 85,98%       | Random Forest                               | Python    |
| Eksplodujący Kotek | 0          | 85,84%       | Random Forest                               | Python    |

Grupa 13

| **Zespół**        | **Punkty** | **F1-Score** | **Model**     | **Język** |
|-------------------|------------|--------------|---------------|-----------|
| Modelarze         | 5          | 78,98%       | XGBoost       | Python    |
| Słodkie Pingwinki | 4          | 78,55%       | Boosted Trees | Python    |
| BGYSMK            | 3          | 78,12%       | XGBoost       | Python    |
| AGJM              | 2          | 77,82%       | Random Forest | Python    |

Grupa 14

| **Zespół**             | **Punkty** | **Accuracy** | **Model** | **Język** |
|------------------------|------------|--------------|-----------|-----------|
| Optymiści              | 5          | 87,48%       | XGBoost   | Python    |
| Cokolwiek              | 4          | 87,04%       | XGBoost   | Python    |
| Cebulaki               | 3          | 86,80%       | XGBoost   | Python    |
| KJN                    | 3          | 86,80%       | XGBoost   | Python    |
| Młodzieżowe Słowo Roku | 1          | 86,58%       | XGBoost   | Python    |
| Goździki               | 0          | 86,24%       | XGBoost   | Python    |

Grupa 15

| **Zespół**        | **Punkty** | **F1-Score** | **Model**     | **Język** |
|-------------------|------------|--------------|---------------|-----------|
| Sigmy             | 5          | 79,15%       | XGBoost       | Python    |
| XYZ               | 4          | 79,10%       | XGBoost       | Python    |
| Malinki           | 3          | 79,06%       | XGBoost       | Python    |
| HMK               | 2          | 79,04%       | XGBoost       | Python    |
| Koty              | 1          | 78,32%       | -             | Python    |
| Aniołki Charliego | 0          | 77,97%       | Random Forest | Python    |
| Pandasy           | 0          | 77,87%       | Boosted Trees | Python    |
| Piwowarzy         | 0          | 76,96%       | XGBoost       | Python    |
