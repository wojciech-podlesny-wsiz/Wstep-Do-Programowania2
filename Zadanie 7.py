# Narysuj schemat blokowy algorytmu i napisz program rozwiązywania rownania liniowego ax + b = 0 , gdzie a i b są wspołczynnikami
# podawanymi przez uzytkownika

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))

# ax + b = 0


if a == 0:
    if b == 0:
        print("Nieskonczenie wiele rozwiazan")
    else:
        print("Brak rozwiązań")
else:
    x = -b/a
    print(f"Rozwiązanie to:{x}")

