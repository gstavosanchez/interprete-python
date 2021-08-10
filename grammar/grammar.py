reservadas = {
    'print': 'RPRINT',
    # 'var': 'RVAR',
    # 'true': 'RTRUE'
}
tokens = [
    # 'PCOMA',
    'PARA',
    'PARC',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    # 'ID'
] + list(reservadas.values())

# TOKENS
# t_PCOMA     = r';'
t_PARA = r'\('
t_PARC = r'\)'
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIV = r'\/'

# -------------- -> TOKEN DECIMAL <- -------------- 
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print('Float value too large %d', t.value)
        t.value = 0
    return t


# -------------- -> TOKEN ENTERO <- -------------- 
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('Integer value too large %d', t.value)
        t.value = 0
    return t
    
# -------------- -> TOKEN ID <- -------------- 
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
    return t

# -------------- -> TOKEN CADENA <- -------------- 
def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# -------------- -> COMENTARIOS <- -------------- 
# Múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = "\t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Compute column.
#     input is the input text string
#     token is a token instance


def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# ANALIZADOR LEXICO
import interprete.ply.lex as lex
lexer = lex.lex()

# Asociacion de operadores y precedencia
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'DIV', 'POR'),
    # ('right','UMENOS'),
)

# Definicion de la gramatica
# Clases Abstractas
from interprete.expressions.Arithmetic import Arithmetic
from interprete.expressions.Primitive import Primitive
from interprete.instruccions.Print import Print
from interprete.types.Type import Arithmetic_Operator, Type


def p_init(t):
    'init           : instrucciones'
    t[0] = t[1]


def p_instrucciones_lista(t):
    'instrucciones      : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones      : instruccion'
    t[0] = [t[1]]
# -------------- -> PRODUCCION INSTRUCCION <- --------------


def p_instruccion(t):
    'instruccion        : imprimir_instr'
    t[0] = t[1]


# -------------- -> PRODUCCION IMPRIMIR <- --------------
def p_instruccion_imprimir(t):
    'imprimir_instr     : RPRINT PARA expresion PARC'
    t[0] = Print(t[3], t.lineno(1), find_column(input, t.slice[1]))


# -------------- -> PRODUCCION EXPRESION <- --------------
def p_expresion_binaria(t):
    '''
    expresion           : expresion MAS expresion
                        | expresion MENOS expresion
                        | expresion POR expresion
                        | expresion DIV expresion
    '''
    if t[2] == '+':
        t[0] = Arithmetic(Arithmetic_Operator.SUMA, t[1], t[3],
                          t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Arithmetic(Arithmetic_Operator.RESTA, t[1],
                          t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Arithmetic(Arithmetic_Operator.POR, t[1], t[3],
                          t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/':
        t[0] = Arithmetic(Arithmetic_Operator.DIV, t[1], t[3],
                          t.lineno(2), find_column(input, t.slice[2]))


def p_expresion_agrupacion(t):
    'expresion          : PARA expresion PARC'
    t[0] = t[2]


def p_expresion_numerica(t):
    '''
    expresion           : ENTERO
                        | DECIMAL
                        | CADENA
    '''
    if len(t) == 2:
        if isinstance(t[1], int):
            t[0] = Primitive(int(t[1]), Type.INT, t.lineno(1),
                             find_column(input, t.slice[1]))
        elif isinstance(t[1], float):
            t[0] = Primitive(float(t[1]), Type.FLOAT, t.lineno(
                1), find_column(input, t.slice[1]))
        elif isinstance(t[1], str):
            t[0] = Primitive(str(t[1]), Type.STRING, t.lineno(1),
                             find_column(input, t.slice[1]))


def p_error(t):
    print(f"Produccion:{t}")
    print("Error sintáctico en '%s'" % t.value)

import interprete.ply.yacc as yacc

parser = yacc.yacc()

input: str = ''


def parse():
    f = open('./entrada.txt', 'r')
    input_string = f.read()
    global lexer
    global parser
    lexer = lex.lex()
    parser = yacc.yacc()
    global input
    input = input_string
    return parser.parse(input_string)


