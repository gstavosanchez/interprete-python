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
        self.operator: Arithmetic_Operator = operator
        self.op_left = op_left
        self.op_right = op_rigth

    def execute(self, environment):
        left_value = self.op_left.execute(environment)
        right_value = self.op_right.execute(environment)

        # -------------- -> SUMA (+) <- -------------- 
        if self.operator == Arithmetic_Operator.SUMA:
            # number + number = number
            if not isinstance(left_value, str) and not isinstance(right_value, str):
                return left_value + right_value
            else:
                print('ERROR +')
        # -------------- -> RESTA (-) <- -------------- 
        elif self.operator == Arithmetic_Operator.RESTA:
            # number - number = number
            if not isinstance(left_value, str) and not isinstance(right_value, str):
                return left_value - right_value
            else:
                print('ERROR -')
        # -------------- -> MULTI (*) <- -------------- 
        elif self.operator == Arithmetic_Operator.POR:
            # number * number = number
            if not isinstance(left_value, str) and not isinstance(right_value, str):
                return left_value * right_value
            # string * string = string
            else:
                return left_value + right_value
        # -------------- -> DIV (/) <- -------------- 
        elif self.operator == Arithmetic_Operator.DIV:
            # number / number = number
            if not isinstance(left_value, str) and not isinstance(right_value, str):
                return left_value / right_value
            else:
                print('ERROR /')

        # -------------- -> POT (^) <- -------------- 
        elif self.operator == Arithmetic_Operator.POT:
            # number ^ number = number
            if not isinstance(left_value, str) and not isinstance(right_value, str):
                return (pow(left_value, right_value))
            # string ^ int = string
            elif isinstance(left_value, str) and isinstance(right_value, int):
                return self.resolve_pow_str(left_value, right_value)
            else:
                print('ERROR ^')
        else:
            return 0

    def resolve_pow_str(self, string:str, exp: int):
        string_aux: str = ''
        i: int = 0
        while i < exp:
            string_aux += string
            i += 1
        return string_aux