import pygal

from die import Die


# Criar um D6
die = Die()

# Fazer alguns lançamentos e armazena os resultados em uma lista
results = [die.roll() for roll_num in range(1000)]

# Analisar os resultados
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

# Visualizar os resultados
hist = pygal.Bar()

hist.title = f"Resultados dos rolamentos de um D6 {len(results)} vezes."
hist.x_labels = [str(i) for i in range(1, die.num_sides + 1)]
hist.x_title = "Resultados"
hist.y_title = "Frequencia dos Resultados"

hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")