# Zad 9. Stwórz listę zakupów jako słownik (artykuł : kwota).
# Wyświetl go i podsumuj wydatki.

lista_zakupow = {
    "chleb": 4.5,
    "mleko": 3.2,
    "ser": 15.0,
    "masło": 8.0
}

print(lista_zakupow)
suma_wydatków = sum(lista_zakupow.values())
print(suma_wydatków)