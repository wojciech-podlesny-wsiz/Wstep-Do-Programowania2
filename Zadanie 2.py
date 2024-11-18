# Zad. 2
# Napisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia wbudowanych funkcji

x = float(input("Podaj liczbę x: "))
y = float(input("Podaj liczbę y: "))
z = float(input("Podaj liczbę z: "))

if x > y:
    x,y = y,x
if  x > z:
    x,z = z,x
if y > z:
    y,z = z,y

print("Liczba w kolejności od najmniejszej do największej: ", x,y,z)

