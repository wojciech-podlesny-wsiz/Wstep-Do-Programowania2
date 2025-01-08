# Zad 2.
# Wygeneruj wykres kołowy przedstawiający procentowy udział różnych kategorii w całkowitej
# sprzedaży.


import matplotlib.pyplot as plt

kategorie = ['Elektronika', 'Odzież', 'Żywność', 'Meble', 'Zabawki']
sprzedane_produkty = [150, 200, 320, 100, 180]

plt.pie(sprzedane_produkty, labels=kategorie, autopct='%1.f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
plt.title('Udział w kategoriach')
plt.show()