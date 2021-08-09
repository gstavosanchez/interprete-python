from interprete.abstract.Instruccion import Instruccion

class Print(Instruccion):
    def __init__(self, expression, line, column):
        Instruccion.__init__(self, line, column)
        self.expression: Instruccion = expression
        
    def execute(self, environment):
        print('Llego al imprimir')
        value = self.expression.execute(environment)
        print(value)