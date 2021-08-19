from interprete.abstract.Instruccion import Instruccion
from interprete.types.Type import Function_Natives, Type, get_typeof


class Native(Instruccion):
    '''
        Instrucciones Funciones Nativas

        Parameters
        ----------
        type: Function_Natives 
            > Tipo de operacion.

        to_convert: Type 
            > Nuevo tipo del valor 

        vale: Instruccion 
            > Valor a convertir.

        line: num 
            > Linea.

        column: num 
            > Columna.

    '''
    def __init__(self, type, to_convert, value, line, column):
        Instruccion.__init__(self, line, column)
        self.type = type
        self.to_convert = to_convert
        self.value: Instruccion = value

    def execute(self, environment):
        value = self.value.execute(environment)
        if self.to_convert:
            # -------------- -> PARSE <- --------------
            if self.type == Function_Natives.PARSE:
                # Parse(Float64, "3.123")   -> 3.123
                if isinstance(value, str):
                    # Float64
                    if self.to_convert == Type.FLOAT64:
                        return float(value)
                    # Int64
                    elif self.to_convert == Type.INT64:
                        return int(value)
                    else:
                        print('ERROR the TYPE  is not numerical:' + str(value))
                        return
                else:
                    print('ERROR AL CONVERT:' + str(value))
                    return
            # -------------- -> TRUNC <- --------------
            elif self.type == Function_Natives.TRUNC:
                # Trunc(Int64, 3.999999)    -> 3
                if isinstance(value, float):
                    return int(value)
        else:
            # -------------- -> FLOAT <- --------------
            if self.type == Function_Natives.FLOAT_F:
                # Float(34)                 -> 34.0
                if isinstance(value, int):
                    return float(value)
                else:
                    print("VALUE must be integer type: " + str(value))
                    return
            # -------------- -> STRING <- --------------
            elif self.type == Function_Natives.STRING_F:
                return str(value)
            # -------------- -> TYPEOF <- --------------
            elif self.type == Function_Natives.TYPEOF:
                return get_typeof(value)
            else:
                print('ERROR AL CONVERT2:' + str(value))
                return
        return 'No se pudo ejuctar la operacion'
