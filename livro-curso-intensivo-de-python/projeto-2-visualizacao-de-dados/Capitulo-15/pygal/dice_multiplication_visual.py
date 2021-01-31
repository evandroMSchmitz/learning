import pygal

from die import Die


# Criar dois D6
die_1 = Die()
die_2 = Die()

# Fazer alguns lançamentos e armazena os resultados em uma lista
results = [die_1.roll() * die_2.roll() for roll_num in range(100000)]

# Analisar os resultados
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

# Visualizar os resultados
hist = pygal.Bar()

hist.title = f"Resultados dos rolamentos de dois D6 {len(results)} vezes."
hist.x_labels =  [str(i) for i in range(1, max_result + 1)]
hist.x_title = "Resultados"
hist.y_title = "Frequencia dos Resultados"

hist.add("D6 * D6", frequencies)
hist.render_to_file("die_visual.svg")

# Usando a multiplicação o resultado é curioso. A menor frequência são dos números quadrados (1, 9, 16, 25, 36,  tirando o 4).
# 6, 12 e 4 são os números com a maior frequência, já que tem mais possibilidades de geração.
# os outros multiplos ficam no meio destas duas categorias, pois são mais fáceis de serem gerados que um quadrado, mas
# ainda não tem tantas possibilidades quanto 6, 12 e o 4