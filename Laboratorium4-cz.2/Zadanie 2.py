# Zad. 2
# Napisz funkcję odwracającą string.

def odwroc_string(tekst):
    return tekst[::-1]

tekst = input("Podaj tekst: ")
odwrocony_tekst = odwroc_string(tekst)
print(f"Odwrócony tekst: {odwrocony_tekst}")
