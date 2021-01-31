import matplotlib.pyplot as plt


x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
# Definir um colormap para os pontos, com base nos valores de y
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=40)

# Definir o título do gráfico
plt.title("Números Quadrados", fontsize=24)
# Nomear os eixos
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Quadrado do Valor", fontsize=14)

# Definir o tamanho dos rótulos e das marcações
plt.tick_params(axis="both", which="major", labelsize=14)

# Definir o intervalo de cada eixo (2 primeiros para x e 2 últimos para y)
plt.axis([0, 1100, 0, 1100000])
# Impedir o uso de notação científica
plt.ticklabel_format(style="plain")

# savar a imagem. Deve ser feito antes do show()
# bbox_inches="tight" elimina espaços extras
#plt.savefig("squares_plot.png", bbox_inches="tight")

plt.show()