# Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie spalanie (w litrach na 100 km) i
# wyświetli informację o przewidywanym zużyciu paliwa oraz o szacowanych kosztach podróży (cena paliwa 6.5 zł/l)
# A) Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo (liczba całkowita z zakresu ),
# a użytkownik podawał aktualną cenę paliwa za litr.
# B) Zmodyfikuj zadania 6 tak, aby wyświetlanie wyników wykorzystywało f-string.


droga = float(input("Podaj długość przejechanej drogi w km? "))
średnie_spalanie = float(input("Podaj średnie spalanie w litrach na 100 km? "))

cena_paliwa = 6.5

zuzycie_paliwa = (średnie_spalanie/100) * droga
koszty_podrozy = zuzycie_paliwa * cena_paliwa

print(f"Przewidywanie zużycie paliwa wynosi {zuzycie_paliwa:.2f} litrów.",end="")
print(f"Szacowane koszty podróży wynoszą: {koszty_podrozy:.2f} zł.")

# A

import random
droga = random.randint(100,500)
print(droga)

cena_paliwa = float(input("Podaj aktualną cenę paliwa za litr? "))
średnie_spalanie = float(input("Podaj średnie spalanie litrach na 100 km? "))


zuzycie_paliwa = (średnie_spalanie/100) * droga
koszty_podrozy = zuzycie_paliwa * cena_paliwa

print(f"Przewidywanie zużycie paliwa wynosi {zuzycie_paliwa:.2f} litrów.", end="")
print(f"Szacowane koszty podróży wynoszą: {koszty_podrozy:.2f} zł.")

