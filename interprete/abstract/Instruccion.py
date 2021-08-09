from abc import ABC, abstractmethod
from interprete.tableSymbol.Enviroment import Enviroment


class Instruccion(ABC):
    def __init__(self, line, column):
        self.line = line
        self.column = column

    @abstractmethod
    def execute(self, environment: Enviroment):
        pass
