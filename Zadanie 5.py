# Zad. 5
# a) Odczytaj podany plik notwania_gieldowe.txt zawierający dane dotyczące notowań kilku spółek. Wydrukuj każdą linię do konsoli.
# b) Dopisz do pliku notwania_gieldowe.txt, w kolejnej linii dane dotyczące nowej spółki: ALR, 113.
# Wydrukuj każdą linię ponownie do konsoli.

# a)
with open("notowania_giełdowe.txt", "r") as plik:
    for line in plik:
      print(line)


# b)

notowanie_gełdowe = open("notowania_giełdowe.txt", "a")

notowanie_gełdowe.write("ALR,113")
notowanie_gełdowe.close()

notowanie_gełdowe = open("notowania_giełdowe.txt", "r")
print(notowanie_gełdowe.read())
notowanie_gełdowe.close()