# Zadanie

W `py_strings.py` zaimplementuj zestaw funkcji, który będzie wykonywał następujące operacje:

1. będzie budowała nowy string „od tyłu” i go zwracała
    ```python
    def reverse(text: str) -> str:
    ```

1. będzie zamieniała małą literę na dużą na początku każdego słowa i zwróci nowy string
    ```python
    def first_to_upper(text: str) -> str:
    ```

1. będzie liczyła samogłoski w podanym stringu i zwróci ich liczbę
    ```python
    def count_vowels(text: str) -> int:
    ```

1. będzie sprawdzała czy w stringu są cyfry; jeżeli tak, niech liczy ich sumę i ją zwróci
    ```python
    def sum_digits(text: str) -> int:
    ```

1. będzie sprawdzała, czy dany string `str` zawiera dany ciąg `substr`, zwraca pozycję licząc od 0 lub -1 jeśli brak
    ```python
    def search_substr(text: str, sub: str) -> int:
    ```

# Instrukcje

1. Zrób fork tego repozytorium klikajać w przycisk `Fork` w prawym górnym roku tej strony. Potwierdz domyślne wartości na następnym ekranie.
1. Sklonuj twoje repozytorium lokalnie. Wybierz zielony przycisk `Code`, w zakładce `Local` wybierz `SSH`, skopiuj string.
1. W lokalnym terminalu wpisz:
    ```bash
    git clone [tutaj wklej skopiowany link]

1. W terminalu wykonaj polecania:
    ```bash
    cd py_strings
    make
    . ../venv/bin/activate
    make test
    make check
    ```
    Spowoduje to stworzenie środowiska virtualnego i uruchomienie testów. Projekt początkowy będzie miał sporo błędów i ostrzeżeń. Testy możesz uruchamiać za pomocą `make test`.
    
    `make check` uruchomi kilka programów sprawdzajaćych jakość napisanego kodu. Komunikaty błędów mogą pomóć Ci ulepszyć kod.

1. W ramach pracy nad projektem powinieneś edytować tylko plik `py_strings.py`, pozostałe pliki powinny być nieedytowane.

1. W pliku `py_strings.py` postaraj się edytować tylko to co zastąpić ma wyrażenie `pass`. Staraj się nie zmieniać nic w definicji funckji oraz w dokumentacji.

1. Po naniesieniu zmian, wykonaj:
    ```bash
    git add -p
    ```
    i zatwierdz wszystkie zmiany za pomocą klawisza `y` lub odrzuć dzięki `n` jeśli nie chcesz danej zmiany wysyłać. Następnie:
    ```bash
    git commit
    ```
    Otworzy się edytor, wpisz treść wiadomości do commita i zapisz i zamknij plik. Następnie:
    ```bash
    git push
    ```
    aby wysłać zmiany na serwer gita.
