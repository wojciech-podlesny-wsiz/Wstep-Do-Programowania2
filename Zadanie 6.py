# Zad. 6
# Napisz skrypt w Pythonie, który sprawdza, czy litera wprowadzona przez użytkownika jest duża czy mała

litera = input("Podaj literę: ")

if litera.isupper():
    print("Litera jest duża!")
elif litera.islower():
    print("Litera jest mała!")
else:
    print("Wprowadzony znak nie jest literą!")
