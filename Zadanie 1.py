# Zad. 1  Utwórz listę: Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21],
# przetestuj działanie wszystkich zaprezentowanych operacji na listach,
# a ich wynik wyświetl w konsoli.

Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
lista2 = [24, 28, 30]

print(Moja_lista[0])
print(Moja_lista[-1])
print(len(Moja_lista))
print(max(Moja_lista))
print(min(Moja_lista))
print(sum(Moja_lista))
print(sorted(Moja_lista))

Moja_lista.append(6)
print(Moja_lista)

Moja_lista.insert(3, 5)
print(Moja_lista)

ostatni_element = Moja_lista.pop()
print(ostatni_element)

Moja_lista.reverse()
print(Moja_lista)

listaLaczona = Moja_lista + lista2
print(listaLaczona)

listaMnozona = Moja_lista * 5
print(listaMnozona)

print(listaLaczona[:5])
print(listaLaczona[3:])
print(listaLaczona[2:8:2])
print(listaLaczona[::-1])
