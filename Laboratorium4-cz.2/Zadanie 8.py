# Zad 8.
# Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
# B. Zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.  *Użyj parametru *args,
# który łączy wszystkie dodatkowe (nadmiarowe) argumenty pozycyjne, niebędące słowami kluczowymi podczas wywoływania funkcji,
# w krotkę. W Pythonie *args pozwala funkcji przyjmować zmienną liczbę argumentów pozycyjnych, które są przekazywane jako krotka (tuple).
# Dzięki temu można przekazać dowolną liczbę dodatkowych argumentów do funkcji bez konieczności definiowania ich z góry.

#A

def wyswietl_parametry(*args):
    for arg in args:
        print(arg)
wyswietl_parametry(1, 2, 3)


#B
def maksymalna_wartosc(*args):
    return max(args) if args else None
print(f"Maksymalna wartość: {maksymalna_wartosc(1, 2, 3, 10, 9)}")
