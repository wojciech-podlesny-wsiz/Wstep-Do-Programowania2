# Zad. 1
# Napisz prosty program, który na podstawie podanej przez Studenta liczby zdobytych punktów,poinformuje go o rezultacie egzaminu.
# Każdy Student, który zdobył powyżej 80 punktów zalicza egzamin w terminie 0.Studenci którzy otrzymali liczbę punków z przedziału 50-80, mogą poprawić jego wynik.
# Studenci, którzy zdobyli poniżej 50 punktów, muszą go poprawić.


punkty = float(input("Podaj liczbę zdobytych punktów: "))

if punkty > 80:
    print("Student zalicza egzamin w terminie 0.!")
elif 50 <= punkty <= 80:
    print("Student może poprawić wynik!")
else:
    print("Student musi poprawić egzamin!")