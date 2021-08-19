from enum import Enum


class Type(Enum):
    NOTHING = 0     # Null (None)
    INT64 = 1       # Int (Integer)
    FLOAT64 = 2     # Float (Decimal)
    BOOLEAN = 3     # Boolean (True || False)
    CHAR = 4        # Char ('d')
    STRING = 5      # String ("Cadena")
    ARRAY = 6       # Array ([])
    STRUCT = 7      # Struct


class Arithmetic_Operator(Enum):
    SUMA = 1        # Suma (+)
    RESTA = 2       # Resta (-)
    POR = 3         # Multiplicacion (*)
    DIV = 4         # Division (/)
    POT = 5         # Potencia (^)


class Function_Natives(Enum):
    PARSE = 1       # Parse(Float64, "3.123")   -> 3.123
    TRUNC = 2       # Trunc(Int64, 3.999999)    -> 3
    FLOAT_F = 3     # Float(34)                 -> 34.0
    STRING_F = 4    # string([1, 2, 3])         -> "[1, 2, 3]"
    TYPEOF = 5      # typeof(5 * 5)             -> Int64


def get_TYPE(type: Type):
    if type == Type.INT64:
        return 'Int64'
    elif type == Type.FLOAT64:
        return 'Float64'
    elif type == Type.BOOLEAN:
        return 'Bool'
    elif type == Type.STRING:
        return 'String'
    elif type == Type.CHAR:
        return 'Char'
    elif type == Type.ARRAY:
        return 'Array'
    elif type == Type.STRUCT:
        return 'Struct'
    else:
        return 'Nothing'


def get_typeof(value):
    # Int
    if isinstance(value, int):
        return get_TYPE(Type.INT64)
    # Float
    elif isinstance(value, float):
        return get_TYPE(Type.FLOAT64)
    # Bool
    elif isinstance(value, bool):
        return get_TYPE(Type.BOOLEAN)
    # String || CHAR
    elif isinstance(value, str):
        if len(value) == 1:
            return get_TYPE(Type.CHAR)
        else:
            return get_TYPE(Type.STRING)
    # Array
    elif isinstance(value, list):
        return get_TYPE(Type.ARRAY)
    else:
        return 'Nothing'
