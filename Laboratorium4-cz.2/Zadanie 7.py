# Zad 7.
# Napisz funkcję rekurencyjną obliczania potęgę n’tego stopnia liczby a, wartości dla argumentów funkcji podaje użytkownik.

def potega(a, n):

    if n == 0:
        return 1
    elif n < 0:
        return 1 / potega(a, -n)
    else:
        return a * potega(a, n - 1)


a = float(input("Podaj podstawę potęgi (a): "))
n = int(input("Podaj wykładnik potęgi (n): "))


wynik = potega(a, n)
print(f"Wynik potęgowania {a}^{n} wynosi: {wynik}")
