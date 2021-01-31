import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Continua criando novos passeios aleatórios enquanto o programa estiver ativo
while True:
    # Criar um passeio aleatório
    rw = RandomWalk(5000, distance_options=list(range(0, 9)))
    rw.fill_walk()

    # Definir o tamanho do janela
    plt.figure(figsize=(10, 6))

    # Adicionar pontos no gráfico
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=2)
    
    # Enfatizar o primeiro e o último ponto
    plt.scatter(rw.x_values[0], rw.y_values[0], c="green", s=100) 
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", s=100)

    # Remover os eixos
    # gca retorna os eixos atuais
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    # Mostrar gráfico
    plt.show()

    keep_running = input("Realizar outro passeio? (y/n): ")
    if keep_running == "n":
        break