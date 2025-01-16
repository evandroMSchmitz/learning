import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = r"Capitulo-16\data\death_valley_2014.csv"
# Obter as datas e temperaturas máximas do arquivo
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
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

    # Fazer a plotagem dos dados
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red", alpha=0.5)
    plt.plot(dates, lows, c="blue", alpha=0.5)
    # Fazer um sombreamento da região entre as temperaturas máximas e mínimas
    # Será uma cor mais clara para não atrapalhar a visualização do resto dos dados
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
    # Forçar os limites de X pra não ficar com um espaço em branco entre o primeiro valor e o ultimo
    plt.gca().set_xbound(dates[0], dates[-1])

    # Definir o título
    plt.title("Temperaturas máximas e mínimas diárias -  2014\nVale da Morte, CA", fontsize=24)
    # Definir labels e parâmetros
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate() # desenhar os rótulos de x na diagonal para evitar sobreposição
    plt.ylabel("Temperatura (F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()