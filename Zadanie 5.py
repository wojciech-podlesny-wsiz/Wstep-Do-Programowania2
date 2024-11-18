# # Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód oraz wyświetla wyniki na ekranie.
#
a = float(input("Podaj  długość  pierwszego boku prostokąta? "))
b = float(input("Podaj  długość  drugiego boku prostokąta? "))

pole = a * b
obwód = 2 * (a + b)


print(f"Pole prostokąta wynosi: {(pole)}")
print(f"Obwód prostokąta wynosi: {(obwód)}")