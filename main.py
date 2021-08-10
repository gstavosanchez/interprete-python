import grammar.grammar as g
from interprete.tableSymbol.Enviroment import Enviroment

ast = g.parse()
global_envrioment = Enviroment(None)

try:
    for instruccion in ast:
        instruccion.execute(global_envrioment)
except Exception:
    print('Error en la ejecucion')
    print(Exception)
