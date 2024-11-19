# Zad 1
# Napisz program, który będzie kontrolować zużycie paliwa w samolocie. Przed rozpoczęciem każdej jednostki czasu wydrukuj do konsoli informację
# o pozostałych jednostkach paliwa. Gdy paliwo zostanie wyczerpane, wydrukuj do konsoli informacje 'Konie lotu.'.  Masz do dyspozycji następujące dane.:
# • ilość paliwa w samolocie w litrach • ilość paliwa zużywanego na sekundę w litrach • czas lotu w sekunadach

paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Pozostało {paliwo} litrów paliwa. Czas lotu: {czas} sekund.")
    paliwo -= paliwo_zuzyte_na_s
    czas += 1
print("Koniec lotu.")

