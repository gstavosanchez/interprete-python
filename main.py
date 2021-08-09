import grammar as g
from interprete.tableSymbol.Enviroment import Enviroment


ast = g.parse()
global_envrioment = Enviroment(None)

try:
    for instruccion in ast:
        instruccion.excute(global_envrioment)
except:
    print('Error al ejecutar la instruccion')
