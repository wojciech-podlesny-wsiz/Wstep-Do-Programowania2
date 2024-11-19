# Zad. 7 dodatkowe
# A) Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik).
# Wprowadzamy liczbę punktów dla każdego studenta.  Napisz program, który obliczy średnią
# liczbę punktów w grupie z wykorzystaniem pętli while.
# Zastosuj instrukcje continue w programie tak, aby po podaniu liczby punktów spoza  przedziału
# 0 – 100 pomijać dalsze wykonywanie pętli.Sprawdź działanieprogramu.
#
# B)
# Następnie zmień pętlę na nieskończoną, czyli taką której warunek zawsze jest prawdziwy.Zakończ
# działanie pętli przy użyciu instrukcji break.Obie wersje zadnia proszę zamieścić w sprawozdaniu.
#
#

n = int(input("Podaj liczbę studentów: "))
suma_punktow = 0
licznik = 0

while licznik < n:
    punkty = int(input(f"Podaj punkty dla studenta {licznik + 1}: "))
    if punkty < 0 or punkty > 100:
        print("Nieprawidłowa liczba punktów, pomijanie studenta.")
        continue
    suma_punktow += punkty
    licznik += 1

srednia = suma_punktow / n
print(f"Średnia liczba punktów w grupie: {srednia:.2f}")

#B

suma_punktow = 0
licznik = 0

while True:
    punkty = int(input(f"Podaj punkty dla studenta {licznik + 1} (lub -1 aby zakończyć): "))
    if punkty == -1:
        break
    if punkty < 0 or punkty > 100:
        print("Nieprawidłowa liczba punktów, pomijanie studenta.")
        continue
    suma_punktow += punkty
    licznik += 1

if licznik > 0:
    srednia = suma_punktow / licznik
    print(f"Średnia liczba punktów w grupie: {srednia:.2f}")
else:
    print("Nie podano żadnych punktów.")
