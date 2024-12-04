# Zad 10. dodatkowe
# Napisz funkcję, która otrzymuje dwa obiekty iterowalne (sekwencje) i zwraca listę wspólnych dla obu obiektów wartości.
# *Wykorzystaj konwersję do zbiorów podanych sekwencji oraz operację przecięcia wiedząc, że operator &
# dla zbiorów zwraca przecięcie, czyli elementy występujące w obu zbiorach.



def wspolne_elementy(seq1, seq2):
    return list(set(seq1) & set(seq2))



lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
print(f"Wspólne elementy: {wspolne_elementy(lista1, lista2)}")
