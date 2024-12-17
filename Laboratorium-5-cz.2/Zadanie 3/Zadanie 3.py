import pandas as pd

data = pd.read_csv("demografia.csv", decimal=',', na_values=['NA', 'n/a', 'NaN'])


all_years_max = data.drop(columns=['KRAJ']).max().max()
max_year = data.drop(columns=['KRAJ']).max().idxmax()
max_country = data.loc[data[max_year].idxmax(), 'KRAJ']

print("Największy przyrost ludności w całej tabeli:", all_years_max)
print("Kraj:", max_country, ", Rok:", max_year)