from interprete.types.Type import Type

class Return:
    def __init__(self, value, type: Type):
        self.value = value
        self.type: Type = type
