import ply.lex as lex
import sys

# list of tokens
 tokens = (
    #PALABRAS RESERVADAS
    'ARRAY',
    'BEGIN',
    'VAR',
    'USES',
    'END',
    'PROGRAM',
    'CONST',

    #I/O
    'WRITE',
    'READ',

    #CICLOS
    'WHILE',
    'DO',
    'FOR',
    'TO',
    'DOWNTO',
    'REPEAT',
    'UNTIL',

    #CONDICIONES
    'IF',
    'THEN',
    'ELSE',
    'CASE',

    #FUNCIONES
    'FUNTION',

    #SIMBOLOS

    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'ASIG',   #Asignacion
    'PUNTO',
    'PYCOMA',
    'DOSPTS', #Dos puntos
    'COMI',
    'IGUAL',
    'MENOR',
    'MENIGU', #Menor o igual
    'MAYOR',
    'MAYIGU', #Mayor o igual
    'PARAB',  #Parentesis que abre
    'PARCE',  #Parentesis que cierra
    'CORAB',  #Corchete abre
    'CORCE'   #Corchete cierra
    'LLAVEA'  #Llave que abre
    'LLAVEC'  #Llave que cierra
    'NOT'
    'DIF'
    'OR'
    'AND'
    #OTROS
    'ID',
    'NUMERO',
 )




#Regular expressions and simple tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_ASIG = r':='
t_PUNTO = r'\.'
t_PYCOMA = r';'
t_DOSPTS = r':'
t_COMI = r'\''   #---------------
t_IGUAL = r'='
t_MENOR = r'<'
t_MENIGU = r'<='
t_MAYOR = r'>'
t_MAYIGU = r'>='
t_PARAB = r'\('
t_PARCE = r'\)'
t_CORAB = r'\['
t_CORCE = r'\]'
t_LLAVEA = r'{'
t_LLAVEC = r'}'
t_NOT = r'not'
t_DIF = r'!='
t_OR = r'or'
t_AND = r'and'

#wiiiiiiiiiiiiiiiiiiiiiiiiiii

#Funciones

def t_integer(t):
    r'((-)?(\d+))'
    t.value= int(t.value)
    return t


def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_FLOAT(t):
    r'((\d+)(\.\d+(e(-)?\d+)?))'
    t.value= float(t.value)
    return t

def t_COMENTARIO(t):
    r'({)'
