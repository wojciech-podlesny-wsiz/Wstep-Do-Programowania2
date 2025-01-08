# Zad 4.
# Utwórz 8-elementową listę składającą się z wartościach będących kolejnymi potęgami liczby 2 - [128
# 64 32 16 8 4 2 1].
# Na podstawie tej listy utwórz tablice ndarray o nazwie wagi.
# Utwórz drugą 8-elementową tablicę ndarray wypełnioną zerami i jedynkami (losowo) o nazwie
# liczba_bin.
# Napisz funkcję wartosc_liczby_bin(), która oblicza wartość liczby binarnej na podstawie listy wagi i listy
# liczba_bin. (funkcja konwertuje liczbę binarną na system dziesiętny)

import numpy as np

potegi_dwa = [128, 64, 32, 16, 8, 4, 2, 1]
wagi = np.array(potegi_dwa)
liczba_bin = np.random.choice([0, 1], size=8)


def wartosc_liczby_bin(wagi, liczba_bin):
    return np.sum(wagi * liczba_bin)

print("Wagi:", wagi)
print("Liczba binarna:", liczba_bin)
print("Wartość liczby binarnej:", wartosc_liczby_bin(wagi, liczba_bin))