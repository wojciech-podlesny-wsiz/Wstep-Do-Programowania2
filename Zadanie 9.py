# Napisz kalkulator, który wyświetli wyniki dodawania, odejmowania, mnożenia, dzielenia i potęgowania 2
# liczb podanych przez użytkownika.


a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

dodawanie = a + b
odejmowanie = a - b
mnożenie =  a * b
potegowanie = a ** b

if b == 0:
    print("Nie można dzielić przez 0")
else:
    dzielenie = a / b
    print(f"Wynik dzielenia to {dzielenie:.2f}")

print(f"Wynik dodawania to {dodawanie:.2f}")
print(f"Wynik odejmowania to {odejmowanie:.2f}")
print(f"Wynik mnożenia to {mnożenie:.2f}")
print(f"Wynik potęgowania to {potegowanie:.2f}")





