# Zad 4. dodatkowe
# Zamówiłeś w restauracji z grupą x przyjaciół, n potraw (liczbę zamówionych dań i liczbę gości,
# za każdym razem wskazuje  użytkownik), następnie dla każdej potrawy podajesz jej cenę.
# Korzystając z pętli while napisz program, który pozwoli obliczyć średnią cenę zamówionej potrawy.
# Podziel sprawiedliwe rachunek miedzy wszystkich gości.


liczba_gosci = int(input("Podaj liczbę gości (w tym Ciebie): "))
liczba_potraw = int(input("Podaj liczbę zamówionych potraw: "))
suma_cen = 0
potrawa = 1

while potrawa <= liczba_potraw:
    cena = float(input(f"Podaj cenę potrawy {potrawa}: "))
    suma_cen += cena
    potrawa += 1

srednia_cena = suma_cen / liczba_potraw
rachunek_na_osobe = suma_cen / liczba_gosci

print(f"Średnia cena potrawy: {srednia_cena:.2f} zł")
print(f"Rachunek na osobę: {rachunek_na_osobe:.2f} zł")
