# Stwórz listę z imionami 4 osób.
# a. Posortuj ją alfabetycznie i wyświetl,
# b. Dodaj na końcu dwie osoby i pobierz ostatnią z nich poleceniem pop().
# c. Na pozycji 3 dodaj jeszcze jedną osobę.
# d. Odwróć kolejność na liście i zdubluj ją.

# a
imiona = ["Wojtek", "Marek", "Kuba", "Piotr"]
imiona.sort()
print(imiona)

# b
imiona.extend(["Katarzyna", "Tomasz"])
print(imiona)
ostatnia_osoba = imiona.pop()
print(imiona)
print(ostatnia_osoba)

# c
imiona.insert(2, "Ewa")
print(imiona)

# d
imiona.reverse()
imiona = imiona * 2
print(imiona)
