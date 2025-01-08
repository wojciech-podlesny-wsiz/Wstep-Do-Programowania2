# Zad 3.
# Przedstaw dane na wykresie punktowym, gdzie oś X to czas, a oś Y to prędkość chwilowa pojazdu

import matplotlib.pyplot as plt

czas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
predkosc = [0, 5, 15, 20, 25, 30, 28, 27, 29, 30]

plt.scatter(czas, predkosc)
plt.show()
