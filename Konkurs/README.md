## Zasady konkursu SRD
### Zespoły
Należy dobrać się w zespoły złożone z maksymalnie 3 osób. Proszę nazwać zespół (nazwa zespołu pojawi się w tabeli z wynikami). Proszę nie używać danych osobowych w nazwach.

### Zbiór danych i cel konkursu
Celem konkursu jest uzyskanie jak największego [**F1-Score**](https://en.wikipedia.org/wiki/F-score) w klasyfikacji zmiennej celu **IsIPA**. Do stworzenia i optymalizacji modelu proszę wykorzystać zbiór danych **IPA.csv**, natomiast finalną predykcję należy wykonać na zbiorze **IPA_test.csv**. Opis zbioru znajduje się w pliku **IPA_description.txt**.


### Wyniki
Wyniki należy przesłać na adres **lkrain@sgh.waw.pl** do końca zajęć danej grupy. W treści maila należy podać nazwę grupy oraz imiona i nazwiska członków - wystarczy mail od jednego członka grupy.

Jako załączniki należy zamieścić:
1. Skrypt/notatnik z wykorzystanym kodem (w dowolnym języku programowania)
2. Plik CSV o nazwie **[nazwa_grupy]_prediction.csv** zawierający jedną kolumnę z 5000 obserwacji (i opcjonalnym nagłówkiem) z wartościami 1/0 lub TRUE/FALSE oznaczających predykcję dla kolejnych wierszy ze zbioru testowego **IPA_test.csv**.

Proszę sprawdzić czy kolejność predykcji zgadza się z kolejnością obserwacji w zbiorze testowym. Proszę również zwrócić uwagę na braki danych w zbiorze testowym - należy je odpowiednio obsłużyć tak, aby otrzymać dokładnie 5000 predykcji.

Tabela z rankingiem zespołów pojawi się na GitHubie w poniższym pliku README. Najlepszy zespół w każdej grupie zajęciowej otrzyma dodatkowe 5 punktów, kolejny 4 punkty, itd.

Życzę powodzenia.