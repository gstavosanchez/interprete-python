from enum import Enum


class Type(Enum):
    NULL = 0        # Null (None)
    INT = 1         # Int (Integer)
    FLOAT = 2       # Float (Decimal)
    BOOLEAN = 3     # Boolean (True || False)
    CHAR = 4        # Char ('d')
    STRING = 5      # String ("Cadena")
    ARRAY = 6       # Array ([])
    STRUCT = 7      # Struct


class Arithmetic_Operator(Enum):
    SUMA = 1        # suma (+)
    RESTA = 2       # resta (-)
    POR = 3         # multiplicacion (*)
    DIV = 4         # division (/)
