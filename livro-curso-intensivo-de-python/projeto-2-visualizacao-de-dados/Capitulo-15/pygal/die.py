from random import randint


class Die():
    """Uma classe que representa um único dado"""


    def __init__(self, num_sides:int=6):
        """Iniciar o dado com um número de lados. Por padrão 6."""
        self.num_sides = num_sides


    def roll(self) -> int:
        """Realiza a rolagem do dado. Devolve um valor aleatório entre 1 e o número de lados do dado."""
        return randint(1, self.num_sides)
