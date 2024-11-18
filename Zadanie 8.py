# Narysuj schemat blokowy algorytmu i napisz program rozwiązywania rownania kwadratowego ax2 + bx + c = 0,
# gdzie a, b i c są wspo łczynnikami podawanymi przez uzytkownika.

import math

# ax2 + bx + c = 0

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

if a == 0:
    print("To nie jest równanie kwadratowe")
else:
    delta = b ** 2 - (4 * a * c)
    if delta < 0:
        print("Równanie nie ma rozwiązań rzeczywistych")
    elif delta == 0:
        x0 = -b /( 2 * a)
        print(f"Równanie ma jedno rozwiązanie: {x0}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Równanie ma dwa rozwiązania : {x1} oraz {x2}")

