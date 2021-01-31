import pygal

from random_walk import RandomWalk


# Continua criando novos passeios aleatórios enquanto o programa estiver ativo
while True:
    # Criar um passeio aleatório
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Adicionar pontos no gráfico
    point_numbers = list(range(rw.num_points))

    # criando a lista de valores customidados
    # o atributo color foi usado para fazer um gradiente de azul
    values = [ {"value": (rw.x_values[i], rw.y_values[i]), "color": f"rgba(0, 0, {i / (rw.num_points-1) * 255}, 1)"} for i in range(rw.num_points)]

    # Criar um scatter plot
    # stroke=False remove a linha ligando os pontos
    # show_x_labels=False e show_y_labels=False esconde os eixos
    # show_legend=False esconde a legenda
    scatter = pygal.XY(stroke=False, show_x_labels=False, show_y_labels=False, show_legend=False)
    scatter.add("Caminho", values, dots_size=5)
    
    # Enfatizar o primeiro e o último ponto
    first_dot = [{"value": (rw.x_values[0], rw.y_values[0]), "color": "green"}]
    scatter.add("Inicio", first_dot, dots_size=10) 
    last_dot = [{"value": (rw.x_values[-1], rw.y_values[-1]), "color": "red"}]
    scatter.add("Fim", last_dot, dots_size=10)

    # Salvar o gráfico
    scatter.render_to_file("rw_visual.svg")

    keep_running = input("Realizar outro passeio? (y/n): ")
    if keep_running == "n":
        break