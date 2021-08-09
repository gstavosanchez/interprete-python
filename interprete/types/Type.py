from enum import Enum


class Type(Enum):
    NULL = 0
    INT = 1
    FLOAT = 2
    BOOLEAN = 3
    CHAR = 4
    STRING = 5
    ARRAY = 6
    STRUCT = 7


class Arithmetic_Operator(Enum):
    SUMA = 1    # suma (+)
    RESTA = 2   # resta (-)
    POR = 3     # multiplicacion (*)
    DIV = 4     # division (/)
