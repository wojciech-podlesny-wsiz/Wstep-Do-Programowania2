# Zad 7.
# Utwórz macierz o wymiarach 5x5 wypełnioną początkowo zerami. Na każdym brzegu macierzy
# ustaw jedynki (góra, dół, lewo, prawo). Napisz funkcję zamieniającą zera na jedynki i odwrotnie.

import numpy as np

macierz_5x5 = np.zeros((5, 5))
macierz_5x5[0, :] = 1
macierz_5x5[-1, :] = 1
macierz_5x5[:, 0] = 1
macierz_5x5[:, -1] = 1

def zamien_zera_jedynki(macierz):
    return 1 - macierz

print("Macierz 5x5 z jedynkami na brzegach:\n", macierz_5x5)
macierz_zmieniona = zamien_zera_jedynki(macierz_5x5)
print("Macierz po zamianie zer na jedynki i odwrotnie:\n", macierz_zmieniona)

