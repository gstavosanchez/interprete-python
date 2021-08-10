from interprete.abstract.Instruccion import Instruccion

class Print(Instruccion):
    '''
        Instruccion Print

        Parameters
        ----------
        expression: Instruccion 
            > Expresion a ejecutra.
            
        line: num 
            > Linea.

        column: num 
            > Columna.
        
    '''
    def __init__(self, expression, line, column):
        Instruccion.__init__(self, line, column)
        self.expression: Instruccion = expression
        
    def execute(self, environment):
        value = self.expression.execute(environment)
        print(value)