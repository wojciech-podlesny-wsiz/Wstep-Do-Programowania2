# Zad. 6
# Napisz funkcję, która oblicza pole trójkąta o boku a, b ,c. Pamiętaj o zabezpieczeniu funkcji przed błędnymi danymi i wyjątkami.
# Użyj wzoru Herona. * Do obliczenia pola trójkąta o bokach a, b, c można użyć wzoru Herona: gdzie s to połowa obwodu trójkąta (tzw. Półobwód):
# Do sprawdzenia poprawności danych wprowadzanych przez użytkownika zastosuj strukturę Try & Except try:
# # Kod, który potencjalnie może wywołać wyjątek except ExceptionType: # Kod do wykonania, jeśli wystąpi wyjątek typu ExceptionType


import math

def pole_trojkata(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Podane boki nie spełniają warunku trójkąta.")

        s = (a + b + c) / 2


        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return pole

    except ValueError as e:
        return f"Błąd: {e}"
    except Exception:
        return "Błąd: Nieprawidłowe dane wejściowe."

try:
    a = input("Podaj długość pierwszego boku (a): ")
    b = input("Podaj długość drugiego boku (b): ")
    c = input("Podaj długość trzeciego boku (c): ")


    wynik = pole_trojkata(a, b, c)
    if isinstance(wynik, float):
        print(f"Pole trójkąta wynosi: {wynik:.2f}")
    else:
        print(wynik)
except Exception as e:
    print(f"Nieoczekiwany błąd: {e}")
