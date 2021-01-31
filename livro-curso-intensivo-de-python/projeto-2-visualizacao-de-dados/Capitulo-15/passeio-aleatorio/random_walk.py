from random import choice

class RandomWalk():
    """Uma classe para gerar passeios aleatórios."""

    def __init__(self, num_points=5000, direction_options=[1, -1], distance_options=[0, 1, 2, 3, 4]):
        """Inicializa os atributos de um passeio."""
        self.num_points = num_points

        # Se tiver positivos poderá ir para a frente e cima, se tiver negativos poderá ir para baixo e para trás
        self.direction_options = direction_options
        self.distance_options = distance_options

        # Todos os passeios começam em (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    
    def fill_walk(self):
        """Calcula todos os pontos do passeio."""

        # Continuar dando passos até que o passeio alcance os tamanho desejado
        while len(self.x_values) < self.num_points:

            # Decide a direção a ser seguida e distância a ser percorrida nessa direção
            x_step = self.get_step() # se aqui der 0 existe a possibilidade de movimento vertical

            y_step = self.get_step() # se aqui der 0 existe a possibilidade de movimento horizontal

            # Rejeita movimentos que não vão a lugar nenhum
            if x_step == 0 and y_step == 0:
                continue

            # Calcula os próximos valores de x e de y
            next_x = self.x_values [-1] + x_step
            next_y = self.y_values [-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            

    def get_step(self):
        """Calcula o tamanho do passo que deve ser dado em cada etapa do passeio."""
        direction = choice(self.direction_options)
        distance = choice(self.distance_options)
        return direction * distance 