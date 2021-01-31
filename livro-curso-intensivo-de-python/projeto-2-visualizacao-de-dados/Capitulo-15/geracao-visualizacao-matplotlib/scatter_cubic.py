import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x ** 3 for x in x_values]

# Definir um colormap para os pontos, com base nos valores de y
plt.scatter(x_values, y_values, s=40, edgecolors=None, c=y_values, cmap=plt.cm.GnBu)

# Definir o título do Gráfico
plt.title("Números Cúbicos", fontsize=24)
# Nomear os eixos
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Cubo do Valor", fontsize=14)

# Definir o tamanho dos rótulos e das marcações
plt.tick_params(axis="both", which="major", labelsize=14)

# Definir o intervalo de cada eixo (2 primeiros para x e 2 últimos para y)
plt.axis([0, 5100, 0, 130000000000])
# Impedir o uso de notação científica
plt.ticklabel_format(style="plain")

plt.show()