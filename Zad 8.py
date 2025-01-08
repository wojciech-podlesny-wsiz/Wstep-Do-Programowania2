# Zad 8.
# Stwórz macierz o wymiarach 5x5 o losowych wartościach, a następnie wybierz elementy, które
# są większe niż 20 i wypisz ich liczbę. Policz średnią dla całejtablicy

import numpy as np

macierz_losowa = np.random.randint(0, 50, size=(5, 5))
wieksze_niz_20 = macierz_losowa[macierz_losowa > 20]
liczba_wiekszych_niz_20 = len(wieksze_niz_20)
srednia_macierzy = macierz_losowa.mean()

print("Losowa macierz 5x5:\n", macierz_losowa)
print("Liczba elementów większych niż 20:", liczba_wiekszych_niz_20)
print("Średnia wartość w macierzy:", srednia_macierzy)


