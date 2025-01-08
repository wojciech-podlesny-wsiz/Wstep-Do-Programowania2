# Zad 5.
# Utwórz losową macierz o wymiarach 5x5. Znajdź największy i najmniejszy element. (patrz tab4_2d;
# metoda max(), min())
# Wypisz największe elementy w każdym z wierszy (axis = 1) i w każdej z kolumn (axis = 0).
# Policz sumę wartości w poszczególnych wierszach.

import numpy as np

macierz = np.random.randint(1, 101, size=(5, 5))

najwiekszy = macierz.max()
najmniejszy = macierz.min()
najwieksze_wiersze = macierz.max(axis=1)
najwieksze_kolumny = macierz.max(axis=0)
suma_wierszy = macierz.sum(axis=1)


print("Macierz:\n", macierz)
print("Największy element:", najwiekszy)
print("Najmniejszy element:", najmniejszy)
print("Największe elementy w wierszach:", najwieksze_wiersze)
print("Największe elementy w kolumnach:", najwieksze_kolumny)
print("Suma wartości w poszczególnych wierszach:", suma_wierszy)