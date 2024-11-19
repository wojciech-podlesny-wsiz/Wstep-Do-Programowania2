# Zad. 8
# Wyświetl z łańcucha tekst ="Python jest super" znaki o indeksach:
# • Zerowym
# • Ostatnim
# • Co drugi, zaczynając od zerowego
# • Co trzeci zaczynając od pierwszego
# • Od dziesiątego do ostatniego
# • Wyświetl od końca do początku

tekst = "Python jest super"

print(f'Zerowy indeks: {tekst[0]}')
print(f'Ostatni indeks: {tekst[-1]}')
print(f'Co drugi znak od zerowego: {tekst[::2]}')
print(f'Co drugi znak od trzeciego: {tekst[1::3]}')
print(f"Od dziesiątego do ostatniego: {tekst[10:]}")
print(f"Od końca do początku: {tekst[::-1]}")
