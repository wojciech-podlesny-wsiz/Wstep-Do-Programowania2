# Zad. 6
# Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby ujemnej, następuję wyjście z pętli.



while True:
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba < 0:
        print("Podano liczbę ujemną. Koniec pętli")
        break
    else:
        print(f'Podano liczbe: {liczba}')
