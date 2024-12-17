import random

zakres_min = int(input("Podaj dolny zakres: "))
zakres_max = int(input("Podaj górny zakres: "))

krotka = tuple(random.randint(zakres_min, zakres_max) for _ in range(10))

iloczyn = 1
for liczba in krotka:
    iloczyn *= liczba

srednia_geometryczna = iloczyn ** (1 / len(krotka))
print(f"Krotka: {krotka}")
print(f"Średnia geometryczna: {srednia_geometryczna}")