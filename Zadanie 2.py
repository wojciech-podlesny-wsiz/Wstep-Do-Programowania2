# Zad 2
# Napisz program, który wydrukuje do konsoli 10 pierwszych liczb pierwszych rozdzielonych przecinkiem tak jak pokazano poniżej.
# Pamiętaj, że liczba pierwsza - to taka liczba naturalna, która ma dokładnie dwa dzielniki naturalne: jedynkę i samą siebie.
# W rozwiązaniu użyj pętli while oraz instrukcji break Oczekiwany wynik: 2,3,5,7,11,13,17,19,23,29


liczby_pierwsze = []
liczba = 2

while len(liczby_pierwsze) < 10:
    for i in range(2, liczba):
        if liczba % i == 0:
            break
    else:
        liczby_pierwsze.append(liczba)
    liczba += 1

print(",".join(map(str, liczby_pierwsze)))
