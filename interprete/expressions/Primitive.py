from interprete.abstract.Instruccion import Instruccion
from interprete.abstract.Return import Return
from interprete.types.Type import Type


class Primitive(Instruccion):
    def __init__(self, value, type, line, column):
        Instruccion.__init__(self, line, column)
        self.value = value
        self.type = type

    def execute(self, environment):
        return self.value
