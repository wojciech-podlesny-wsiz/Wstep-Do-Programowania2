# Zad 1.
# Stwórz wykres słupkowy przedstawiający ilość sprzedanych produktów w różnych kategoriach.


import matplotlib.pyplot as plt

kategorie = ['Elektronika', 'Odzież', 'Żywność', 'Meble', 'Zabawki']
sprzedane_produkty = [150, 200, 320, 100, 180]

plt.bar(kategorie, sprzedane_produkty)
plt.show()