from datetime import datetime

data_lab = datetime(2024, 12, 10)
data_kolokwium = datetime(2024, 12, 17)
data_dzis = datetime.now()

dni_od_laboratoriow = (data_dzis - data_lab).days
dni_do_kolokwium = (data_kolokwium - data_dzis).days

print(f"Minęło {dni_od_laboratoriow} dni od ostatnich laboratoriów.")
print(f"Do kolokwium zostało {dni_do_kolokwium} dni.")