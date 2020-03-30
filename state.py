"""

    Padrões de Projetos #06
    Live de Python #121
    https://www.youtube.com/watch?v=6kNXFCoQBl0

    Autor: Eduardo Mendes

"""

from abc import ABC, abstractmethod


class Estado(ABC):
    @abstractmethod
    def esquentar(self):
        pass

    def esfriar(self):
        pass

        return self.__class__.__name__


class EstadoLiquido(Estado):
    def esquentar(self):
        return EstadoGasoso()

    def esfriar(self):
        return EstadoSolido()


class EstadoSolido(Estado):
    def esquentar(self):
        return EstadoLiquido()

    def esfriar(self):
        return EstadoSolido()


class EstadoGasoso(Estado):
    def esquentar(self):
        return EstadoGasoso()

    def esfriar(self):
        return EstadoLiquido()


class Elemento:
    def __init__(self):
        self.name = self.__class__.__name__
        self.state = EstadoLiquido()

    def esquentar(self):
        self.state = self.state.esquentar()

    def esfriar(self):
        self.state = self.state.esfriar()

    def __repr__(self):
        return f'{self.name} (estado={self.state})'


class Mercurio(Elemento):
    def __init__(self):
        self.name = 'Mercurio'
        self.state = EstadoLiquido()


class Agua(Elemento):
    def __init__(self):
        self.name = 'Agua'
        self.state = EstadoLiquido()


class Ouro(Elemento):
    def __init__(self):
        super().__init__()
        self.state = EstadoGasoso()


class Chumbo(Elemento):
    pass
