# Zad. 3
# Zmienna Nazwa_pliku przechowującej jego nazwę. Sprawdź, czy plik o podanej nazwie jest z rozszerzeniem '.xlsx'. Nazwa_pliku= 'Raport_maj.xlsx'
# Wydrukuj do konsoli 'Tak' jeśli to prawda, przeciwnie 'Nie'.

Nazwa_pliku = 'Raport_maj.xlsx'

if Nazwa_pliku.endswith(".xlsx"):
    print("Tak")
else:
    print("Nie")