import pandas as pd

students = pd.DataFrame({
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
})

# a)
high_grade_students = students[students['Ocena'] > 4]
print("Studenci z oceną powyżej 4:")
print(high_grade_students)

# b)
sorted_students = students.sort_values(by='Wiek')
print("Studenci posortowani według wieku:")
print(sorted_students)

# c)
avg_age_by_grade = students.groupby('Ocena')['Wiek'].mean()
print("Średnia wieku według ocen:")
print(avg_age_by_grade)

# d)
improved_grades = pd.DataFrame({
    'Nr_albumu': [2, 5],
    'Ocena Poprawkowa': [4.0, 3.5]
})
merged_students = pd.merge(students, improved_grades, on='Nr_albumu', how='left')
print("Protokół ocen po poprawie:")
print(merged_students)

# e)
students_output_path = 'students.csv'
merged_students.to_csv(students_output_path, index=False)

# f)
students_read_data = pd.read_csv(students_output_path)
print("Wczytane dane studentów:")
print(students_read_data)

# g)
new_student = pd.DataFrame({
    'Nr_albumu': [6],
    'Imię': ['Piotr'],
    'Nazwisko': ['Kowalczyk'],
    'Ocena': [4.7],
    'Wiek': [22]
})
students = pd.concat([students, new_student], ignore_index=True)
print("Zaktualizowane dane studentów:")
print(students)

# h)
unique_grades = students['Ocena'].unique()
print("Unikalne wartości ocen:", unique_grades)

# i)
count_grade_5 = students[students['Ocena'] == 5].shape[0]
print("Liczba studentów z oceną 5:", count_grade_5)
