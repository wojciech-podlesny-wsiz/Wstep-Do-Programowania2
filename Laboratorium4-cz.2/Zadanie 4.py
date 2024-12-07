# Zad. 4
# Napisz funkcję, obliczającą średnią z listy liczb. Zaprezentuj wywołanie funkcji.

def oblicz_srednia(lista):
    return sum(lista) / len(lista) if lista else 0


liczby = [10, 20, 30, 40]
print(f"Średnia liczb to {oblicz_srednia(liczby)}")
