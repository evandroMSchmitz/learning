import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, "-o", linewidth=2)

# Definir o título do Gráfico
plt.title("Números Quadrados", fontsize=24)
# Nomear os eixos
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Quadrado do Valor", fontsize=14)

# Definir o tamanho dos rótulos e das marcações
plt.tick_params(axis="both", labelsize=14)

# Apresentar um gird para ajudar na visualização
plt.grid(True, linestyle=":")

plt.show()