from interprete.types.Type import Type


class Symbol:
    '''
        Define a varible
        :param value: value of symbol
        :param symbol_id: id of symbol
        :param symbol_type: type of symbol
    '''

    def __init__(self, value, symbol_id: str, symbol_type: Type):
        self.value = value
        self.symbol_id = symbol_id
        self.symbol_type = symbol_type

    def get_value(self):
        return self.value

    def get_symbol_id(self):
        return self.symbol_id

    def get_symbol_type(self):
        return self.symbol_type

    def set_value(self, value):
        self.value = value

    def set_symbol_id(self, symbol_id: str):
        self.symbol_id = symbol_id

    def set_symbol_type(self, symbol_type: Type):
        self.symbol_type = symbol_type
