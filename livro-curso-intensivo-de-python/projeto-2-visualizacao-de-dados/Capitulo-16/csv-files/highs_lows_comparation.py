import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename_death_valley = r"Capitulo-16\data\death_valley_2014.csv"
filename_sitka = r"Capitulo-16\data\sitka_weather_2014.csv"

def read_file_data(filename):
# Obter as datas e temperaturas máximas do arquivo
    dates, highs, lows = [], [], []
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, "está com falta de dados (missing data)")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    
    return dates, highs, lows

dates_dv, highs_dv, lows_dv = read_file_data(filename_death_valley)
dates_st, highs_st, lows_st = read_file_data(filename_sitka)

# Fazer a plotagem dos dados
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_dv, highs_dv, c="#ff0000", label="Temperatura Máxima Vale da Morte")
plt.plot(dates_dv, lows_dv, c="#ee8787", label="Temperatura Mínima Vale da Morte")

plt.plot(dates_st, highs_st, c="#0000ff", label="Temperatura Máxima Sitka")
plt.plot(dates_st, lows_st, c="#9587ee", label="Temperatura Mínima Sitka")

# Fazer um sombreamento da região entre as temperaturas máximas e mínimas
# Será uma cor mais clara para não atrapalhar a visualização do resto dos dados
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor="red", alpha=0.1)
plt.fill_between(dates_st, highs_st, lows_st, facecolor="blue", alpha=0.1)
# Forçar os limites de X pra não ficar com um espaço em branco entre o primeiro valor e o ultimo
plt.gca().set_xbound(dates_dv[0], dates_dv[-1])

# Definir o título
plt.title("Temperaturas máximas e mínimas diárias -  2014\nVale da Morte, CA VS Sitka, AK", fontsize=24)
# Definir labels e parâmetros
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() # desenhar os rótulos de x na diagonal para evitar sobreposição
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()