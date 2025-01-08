# Zad 6
# Utwórz tablicę wypełnioną zerami 3x3. Wypełnij zaznaczone obszary tablicy jedynkami

import numpy as np

tablica = np.zeros((3, 3), dtype=int)
tablica[0, :] = 1
tablica[:, 0] = 1
print("Tablica z jedynkami:\n", tablica)
