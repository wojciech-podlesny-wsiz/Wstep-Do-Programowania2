# Zad. 1
# Napisz funkcję, która pozwoli obliczyć kwadrat liczby podanej przez użytkownika.
# Zaprezentuj wywołanie funkcji.

def kwadrat():
    liczba = int(input('Podaj liczbę: '))
    kwadrat_liczby = liczba ** 2
    print(f"{kwadrat_liczby}")

kwadrat()
