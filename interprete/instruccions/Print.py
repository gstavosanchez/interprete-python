from interprete.abstract.Instruccion import Instruccion


class Print(Instruccion):
    '''
        Instruccion Print

        Parameters
        ----------
        expression: Instruccion 
            > Expresion a ejecutar.

        line: num 
            > Linea.

        column: num 
            > Columna.

        new_line: bool
            > Si es salto de linea, parametro opcional

    '''

    def __init__(self, expression, line, column, new_line: bool=False):
        Instruccion.__init__(self, line, column)
        self.expression: Instruccion = expression
        self.new_line = new_line

    def execute(self, environment):
        value = self.expression.execute(environment)
        if self.new_line:
            # Con salto de linea
            print(value)
        else:
            # Sin salto de liena
            print(value, end="")
