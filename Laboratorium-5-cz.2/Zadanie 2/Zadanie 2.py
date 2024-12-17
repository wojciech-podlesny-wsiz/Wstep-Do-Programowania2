import pandas as pd

data = pd.read_csv("demografia.csv", decimal=',', na_values=['NA', 'n/a', 'NaN'])

max_growth_2022 = data.loc[data['2022'].idxmax(skipna=True), 'KRAJ']
print("Kraj z największym przyrostem ludności w 2022 roku:", max_growth_2022)