# Zad. 4 dodatkowe
# Jesteś menagerem drużyny piłkarskiej i chcesz obliczyć łączny wynik drużyny na podstawie liczby strzelonych przez nią bramek i ewentualnie zdobytych dodatkowych punktów.
# Napisz program, który dokona stosownych kalkulacji po wprowadzeniu liczby goli zdobytych przez drużynę.  Utworzone są dwie zmienne gol i bonus, gdzie gol to liczba całkowita
# reprezentująca liczbę bramek zdobytych przez drużynę, a bonus to liczba całkowita reprezentująca wszelkie możliwe punkty bonusowe dla drużyny. Następnie użyj instrukcji
# warunkowej do obliczenia całkowitego wyniku zespołu zgodnie z następującymi zasadami: - każda zdobyta bramka to 10 punktów, - jeśli drużyna zdobędzie więcej niż 5 bramek,
# zdobywa dodatkowe 5 punktów bonusowych, - jeśli drużyna zdobędzie więcej niż 10 bramek, zdobywa dodatkowe 10 punktów bonusowych

# a) Po zdobyciu 5 goli drużyna otrzymuje 5 punktów bonusowych.
# Jeśli drużyna zdobędzie więcej niż 10 goli, to otrzyma za nie 10 punktów bonusowych dodatkowo Oblicz całkowity wynik drużyny, dodając punkty zdobyte ze zdobytych bramek i wszelkie stosowne punkty bonusowe.
# Wynik wydrukuj do konsoli.

# b) Punkty bonusowe po przekroczeniu 5 i 10 punktów są sumowane, tzn. po przekroczeniu więcej niż 10 bramek drużyna zdobywa obydwa bonusy.
# Oblicz całkowity wynik drużyny, dodając punkty zdobyte ze zdobytych bramek i wszelkie stosowne punkty bonusowe. Wynik wydrukuj do konsoli.


# a)

gol = int(input("Podaj liczbę zdobytych bramek: "))
bonus = 0

punkty_za_bramki = gol * 10


if gol > 10:
    bonus = 10
elif gol > 5:
    bonus = 5
else:
    bonus = 0

wynik_całkowity = punkty_za_bramki + bonus
print("Całkowity wynik drużyny to: ", wynik_całkowity)

# b)

gol = int(input("Podaj liczbę zdobytych bramek: "))
bonus = 0

punkty_za_bramki = gol * 10


if gol > 10:
 bonus = 15

if gol > 5:
    bonus = 5

wynik_całkowity = punkty_za_bramki + bonus
print("Całkowity wynik drużyny to: ", wynik_całkowity)
