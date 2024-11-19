# Zad 3
# Mając podana listę ulic w danej dzielnicy i wiedząc, że na każdej ulicy znajduje się 5 bloków mieszkalnych,
# a w każdym z nich jest 10 lokali, wypisz listę wszystkich adresów w dzielnicy.
# Lista ulic w dzielnicy: • Jagodowa,  • Lipowa,  • Kwiatowa, • Kasztanowa, • Polna.


streets= ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
blocks = [1,2,3,4,5]
flats = ['/1','/2','/3','/4','/5','/6','/7','/8','/9','/10']

for street in streets:
    for block in blocks:
        for flat in flats:
         print(f"{street} {block} {flat}")

