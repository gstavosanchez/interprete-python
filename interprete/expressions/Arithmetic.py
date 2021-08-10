from interprete.abstract.Instruccion import Instruccion
from interprete.types.Type import Arithmetic_Operator, Type


class Arithmetic(Instruccion):
    '''
        Instrucciones Aritmeticas

        Parameters
        ----------
        operator: Arithmetic_Operator 
            > Tipo de operacion.

        op_left: Instruccion 
            > Operador Izquierdo.

        op_rigth: Instruccion 
            > Operador Derecho.

        line: num 
            > Linea.

        column: num 
            > Columna.
        
    '''
    def __init__(self, operator, op_left, op_rigth, line, column):
        Instruccion.__init__(self, line, column)
        self.operator = operator
        self.op_left = op_left
        self.op_right = op_rigth

    def execute(self, environment):
        left_value = self.op_left.execute(environment)
        right_value = self.op_right.execute(environment)

        if self.operator == Arithmetic_Operator.SUMA:       # SUMA (+)
            return (left_value) + (right_value)
        elif self.operator == Arithmetic_Operator.RESTA:    # RESTA (-)
            return (left_value) - (right_value)
        elif self.operator == Arithmetic_Operator.POR:      # MULTI (*)
            return (left_value) * (right_value)
        elif self.operator == Arithmetic_Operator.DIV:      # DIVIV (/)
            return (left_value) / (right_value)
        else:
            return 0
