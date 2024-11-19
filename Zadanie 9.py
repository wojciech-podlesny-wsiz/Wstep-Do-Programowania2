# Zad. 9
# Napisz programy, które:
# • Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
# • Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to: ” oraz wczytany  wiek.
# • Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
# • Wczyta łańcuch i wyświetli go pięć razy.
# • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa  łańcuchy.
# • Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę
#


imie = input("Podaj swoje imię: ")
print(f"Witaj, {imie}!")


wiek = int(input("Podaj swój wiek: "))
print(f"Twój wiek to: {wiek}.")


imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
inicjaly = imie[0].upper() + nazwisko[0].upper()
print(f"Twoje inicjały to: {inicjaly}")


lancuch = input("Podaj łańcuch: ")
print(lancuch * 5)

lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polaczony = lancuch1 + lancuch2
print(polaczony)


lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
polaczony_polowy = lancuch1[:len(lancuch1)//2] + lancuch2[:len(lancuch2)//2]
print(f"Połączony łańcuch z pierwszych połówek: {polaczony_polowy}")
