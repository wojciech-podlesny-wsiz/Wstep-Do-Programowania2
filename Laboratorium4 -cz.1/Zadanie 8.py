# Zad 8. Załóżmy, że pracujesz nad systemem wojskowym dotyczącym planowania
# operacji wojskowych.  Podana jest poniższa krotka:
# stopnie = ( "Szeregowy", "Kapral", "Sierżancie",
# "Porucznik", "Kapitan", "Major", "Pułkownik", )
# Wykonaj poniższe kroki: - wyznacz liczbę wszystkich
# stopni wojskowych i przypisz do zmiennej ilość_stopnii,
# - znajdź indeks krotki dla elementu "Major" i przypisz
# do zmiennej Major_index, - sprawdź, czy wartość "Pułkownik"
# znajduje się w krotce stopnie i przypisz do zmiennej Pułkownik_wstepowanie.
# W wydrukuj otrzymane zmienne do konsoli w podanej kolejności.

stopnie = ("Szeregowy", "Kapral", "Sierżancie", "Porucznik", "Kapitan", "Major", "Pułkownik")

ilość_stopni = len(stopnie)
Major_index = stopnie.index("Major")
Pułkownik_wstepowanie = "Pułkownik" in stopnie

print(ilość_stopni)
print(Major_index)
print(Pułkownik_wstepowanie)
