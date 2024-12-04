# Zad 9.
# Napisz funkcję rekurencyjną, która poda n-ty wyraz ciągu Fibonacciego. *Ciąg Fibonacciego to sekwencja liczb,
# w której każdy wyraz (od trzeciego wzwyż) jest sumą dwóch poprzednich wyrazów. Formuła rekurencyjna dla n-tego wyrazu ciągu Fibonacciego jest następująca.


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = 10
print(f"{n}-ty wyraz ciągu Fibonacciego to {fibonacci(n)}")
