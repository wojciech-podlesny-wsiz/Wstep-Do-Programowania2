import pandas as pd

data = pd.read_csv("demografia.csv", decimal=',', na_values=['NA', 'n/a', 'NaN'])
print(data)