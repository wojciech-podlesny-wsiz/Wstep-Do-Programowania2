# Zad. 4 dodatkowe
# Napisz program, który wczyta od użytkownika zdanie. Wypisz z niego wszystkie litery w kolejności alfabetycznej,
# a następnie wypisze których litera alfabetu nie zawiera.

zdanie = input("Podaj zdanie: ")

litery = sorted([litera.lower() for litera in zdanie if litera.isalpha()])
print("Litery w kolejności alfabetycznej:", "".join(litery))

alfabet = set("abcdefghijklmnoprstuwyz")
uzyte_litery = set(litery)
brakujace_litery = alfabet - uzyte_litery
print("Brakujące litery:", "".join(sorted(brakujace_litery)))
