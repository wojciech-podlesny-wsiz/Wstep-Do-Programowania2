# Zad. 3
# Napisz program, który:
# a. Wczyta (zmienną) imię oraz wyświetli tekst
# „Witaj” oraz wczytane imię.
# b. Wczyta (zmienną) wiek oraz wyświetli tekst
# „Twój wiek to:” oraz wczytany wiek.
# c. Wczyta (zmienne) imię i nazwisko i
# wyświetli inicjały.
# d. Wczyta łańcuch i wyświetli go pięć razy.
# e. Wczyta
# dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy.
# f. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę
# pierwszego i drugą połowę drugiego.

#a
imie = input("Podaj imię: ")
print("Witaj", imie)

#b
wiek = int(input("Podaj wiek: "))
print("Twój wiek to:", wiek)

#c
imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
print("Inicjały:", imie[0].upper() + "." + nazwisko[0].upper() + ".")

#d
lancuch = input("Podaj łańcuch: ")
print(lancuch * 5)

#e
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
print("Połączone łańcuchy:", lancuch1 + lancuch2)

#f
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polaczony = lancuch1[:len(lancuch1)//2] + lancuch2[len(lancuch2)//2:]
print(polaczony)
