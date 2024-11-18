# Zad. 1:
# A) Sprawdź w interpreterze typ wyników określonych działań - type( x ) i wyjaśnij, co
# oznaczają poszczególne operatory?


x = 1 + 2
print(type(x))  # Operator '+' to dodawanie , zwraca liczbę całkowitą <class 'int'>

x = 1 + 4.5
print(type(x)) # Operator '+' to dodawanie , zwraca liczbę zmiennoprzecinkową <class 'float'>

x = 3/2
print(type(x)) #  Operator '/' to dzielenie zmiennoprzecinkowe , zwraca liczbę zmiennoprzecinkową <class 'float'>

x = 4/2
print(type(x))  # Operator '/' to dzielenie zmiennoprzecinkowe , zwraca liczbę zmiennoprzecinkową <class 'float'>

x = 3//2
print(type(x))  # Operator '//' to dzielenie całkowite , zwraca liczbę całkowitą  <class 'int'>

x = -3 // 2
print(type(x))  # Operator '//' to dzielenie całkowite , zwraca liczbę całkowitą <class 'int'>

x = 11 % 2
print(type(x))  # Operator '%' to modulo(reszta z dzielenia) , zwraca liczbę całkowitą <class 'int'>

x = 2 ** 10
print(type(x))  # Operator '**' to potęgowanie , zwraca liczbę całkowitą <class 'int'>

x = 8 ** (1/3)
print(type(x))   # Operator '**' to potęgowanie , zwraca liczbę zmiennoprzecinkową <class 'float'> #


# B) Sprawdź i wyjaśnij działanie następujących instrukcji:


print(int(3.0) ) # ta instrukcja konwertuje liczbę zmiennoprzecinkową do liczby całkowitej int

print(float(3))  # ta instrukcja konwertuje liczbę całkowitą do liczby zmiennoprzecinkowej float

print(float("3")) # ta instrukcja konwertuje  ciąg znaków na liczbę zmiennoprzecinkową float

print(str(12.4)) # instrukcja konwertuje liczbę zmiennoprzecinkową na ciąg znaków string

print(bool(0))  # instrukcja  konwertuje 0 na wartość logiczną false
