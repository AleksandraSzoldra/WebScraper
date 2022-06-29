#WebScraper

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|indentyfikator opinii|div.js_product-review["data-entry-id"]|opinion_id|str|
|autor opinii|span.user-post__author-name|author|str
|rekomendacja|span.user-post__author-recomendation > em|recommendation||
|liczba gwiazdek|span.user-post__score-count|stars||
|tresc opinii|div.user-post__text|content||
|lista zalet|div[class$="positives"] ~ div.reviews-feature__item|pros||
|lista wad|div[class$="negatives"] ~ div.reviews-feature__item|cons||
|dla ilu osób przydatne|span[id^=votes-yes"] button.vote-yes > span <br> data-total-yes["data-total-vote"]|useful||
|dla ilu osób nieprzydatne|span[id^=votes-no"] button.vote-no > span <br> data-total-no["data-total-vote"]|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)["datetime"]|publish_date||
|data zakupu|span.user-post__published > time:nth-child(2)["datetime"]|purchase_date|| 

Etapy pracy nad projektem 
1. Pobranie do pojedynczych zmiennych składowych pojedynczej opinii
2. Zapisanie wszystkich składowych pojedynczej opinii do słownika
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i zapisanie ich na liście
4. Zapisanie wszystkich opinii z listy do pliku .json
5. Pobranie wszystkich opinii o produkcie i zapisanie ich na liście w postaci słowników
6. Dodanie możliwości podania kodu produktu przez użytkownika
7. Optymalizacja kodu a. utworzenie funkcji do ekstrakcji elementów strony b. utworzenie słownika selektorów c. użycie dictionary comprehension do pobrania składowych pojedynczej opinii na podstawie słownika selektorów
8. Analiza pobranych opinii dla konkretnego produktu a. wyliczenie podstawowych statystyk: - liczba wszystkich opinii liczba opinii dla których podano zalety - liczba opinii dla których podano wady - średnia opcena produktu b. przygotowanie wykresów: - udział poszczególnych rekomendacji w ogólnej liczbie opinii - histogram występowania poszczególnych ocen 

Biblioteki: 

- os - moduł poszukuje wbudowanych modułów zależnych od systemu operacyjnego, takich jak mac czy posix, a następnie eksportuje odnalezione w nich funkcje i dane. 
- json - jest to format danych niezależny od używanego języka. Pochodzi z JavaScript, ale wiele współczesnych języków programowania ma możliwość generowania i odczytu danych w formacie JSON – w tym oczywiście Python. 
- request - biblioteka requests służy do obsługi protokołu HTTP - wysyłania żądań, odbierania odpowiedzi itd. 
- pandas - szybkie, wydajne, elastyczne i łatwe w użyciu narzędzie do analizy i manipulacji danymi typu open source,
zbudowany na bazie języka programowania Python. 
- numpy - jest fundamentalną biblioteką do obliczeń naukowych. 
- BeautifulSoup - to prosta biblioteka, która przede wszystkim służy do wyciągania danych z dokumentów HTML i XML. 
- matplotlib - to kompleksowa biblioteka do tworzenia statycznych, animowanych i interaktywnych wizualizacji w Pythonie. 
- py_compile - udostępnia funkcję do generowania pliku kodu bajtowego z pliku źródłowego oraz inną funkcję używaną, gdy plik źródłowy modułu jest wywoływany jako skrypt.
- certifi - zapewnia starannie wyselekcjonowany zbiór certyfikatów głównych Mozilli do weryfikowania wiarygodności certyfikatów SSL podczas weryfikacji tożsamości hostów TLS. Został wyodrębniony z projektu Requests.
- charset-normalizer - biblioteka, która pomaga czytać tekst z nieznanego kodowania zestawu znaków. 
- idna - obsługa protokołu Internationalized Domain Names in Applications (IDNA) zgodnie z RFC 5891 . Jest to najnowsza wersja protokołu, czasami nazywana „IDNA 2008”. 
- soup sieve - biblioteka selektorów CSS zaprojektowana do użytku z Beautiful Soup 4. Ma na celu zapewnienie wybierania, dopasowywania i filtrowania przy użyciu nowoczesnych selektorów CSS. 
- urllib3 to potężny, przyjazny dla użytkownika klient HTTP dla Pythona. Duża część ekosystemu Pythona już używa urllib3. urllib3 oferuje wiele krytycznych funkcji, których brakuje w standardowych bibliotekach 







