import pygal

from die import Die


# Criar três D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Fazer alguns lançamentos e armazena os resultados em uma lista
results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(1000)]

# Analisar os resultados
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result + 1)]

# Visualizar os resultados
hist = pygal.Bar()

hist.title = f"Resultados dos rolamentos de três D6 {len(results)} vezes."
hist.x_labels =  [str(i) for i in range(3, max_result + 1)]
hist.x_title = "Resultados"
hist.y_title = "Frequencia dos Resultados"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file("die_visual.svg")