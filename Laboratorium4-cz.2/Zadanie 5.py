# Zad. 5
# Napisz funkcję, która na podstawie podanej wagi i wzrostu oblicza i zwraca wskaźnik BMI, a następnie informuje użytkownika
# w jakim jest zakresie.  *Wskaźnika Body Mass Index (BMI) oblicza się na podstawie dwóch danych: wzrostu i aktualna masa ciała.
# Należy podzielić wagę wyrażoną w kilogramach przez wzrost podniesiony do kwadratu, wyrażony w metrach, czyli w skrócie BMI = kg / m2.
# Uzyskany wynik należy porównać z zakresami wartości BMI. Klasyfikacja BMI dla osób dorosłych wygląda następująco: • niedowaga – BMI poniżej 18,5.
# Tutaj rozróżnia się trzy podkategorie, • pożądana masa ciała – BMI od 18,5 do 24,9, • nadwaga – BMI od 25 do 29,9, • otyłość – BMI powyżej 30.
# Obecnie wyróżnia się otyłość I stopnia – od 30 do 34,9, II stopnia – od 35 do 39,9, oraz III stopnia – powyżej 40.

def bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    if bmi < 18.5:
        status = "niedowaga"
    elif bmi < 25:
        status = "pożądana masa ciała"
    elif bmi < 30:
        status = "nadwaga"
    else:
        status = "otyłość"
    return bmi, status


waga = float(input("Podaj wagę (kg): "))
wzrost = float(input("Podaj wzrost (m): "))
bmi, status = bmi(waga, wzrost)
print(f"BMI: {bmi:.2f}, Status: {status}")
