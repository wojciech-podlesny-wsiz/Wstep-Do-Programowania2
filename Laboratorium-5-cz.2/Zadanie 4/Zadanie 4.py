import pandas as pd

employees = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
})

# a)
high_salary = employees[employees['Pensja'] > 5000]
print("Pracownicy z pensją powyżej 5000 PLN:")
print(high_salary)

# b)
sorted_by_age = employees.sort_values(by='Wiek')
print("Pracownicy posortowani według wieku:")
print(sorted_by_age)

# c)
avg_salary_by_position = employees.groupby('Stanowisko')['Pensja'].mean()
print("Średnia pensja według stanowiska:")
print(avg_salary_by_position)

# d)
promotions = pd.DataFrame({
    'ID': [1, 3],
    'Nowe Stanowisko': ['Dyrektor', 'Senior Konsultant']
})
merged_data = pd.merge(employees, promotions, on='ID', how='left')
print("Dane pracowników po awansie:")
print(merged_data)

# e)
output_path = 'employees.csv'
merged_data.to_csv(output_path, index=False)

# f)
read_data = pd.read_csv(output_path)
print("Wczytane dane:")
print(read_data)