from interprete.tableSymbol.symbol import Symbol
from interprete.types import Type


class Enviroment:
    '''
        Define el Entorno

        Parameters
        ----------
        previous_enviroment: Enviroment 
            > entorno anterior.
    '''

    def __init__(self, previous_enviroment=None):
        self.previous = previous_enviroment
        self.variables: dict = {}
        self.functions: dict = {}

    def set_variable(self, var_id: str, value, var_type: Type):
        env: Enviroment = self
        new_symbol = Symbol(value, var_id, var_type)
        while env != None:
            if var_id in env.variables.keys():
                env.variables[var_id] = new_symbol
                return
            env = env.previous
        self.variables[var_id] = new_symbol

    def get_variable(self, var_id: str):
        env: Enviroment = self
        while env != None:
            if var_id in env.variables.keys():
                return env.variables[var_id]

            env = env.previous
        return None

    # def set_function(self, )
    def get_global(self):
        env: Enviroment = self
        while env.previous != None:
            env = env.previous
        return env
