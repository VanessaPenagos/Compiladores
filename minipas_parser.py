import ply.yacc as yacc
from minipas_lexer import tokens
import minipas_lexer
import sys

VERBOSE = 1

def p_program(p):
	'program : PROGRAM ID PCOMA USES ID PCOMA contenido'
	pass

def p_contenido(p):
	'contenido : declaracion_variables declaraciones'
	pass

def p_declaracion_variables(p):
	'''declaracion_variables : vacio
							 | declaracion_variable'''
	pass

def p_declaracion_variable(p):
	'''declaracion_variable : VAR dec DPUN type PCOMA
						    | VAR dec DPUN type PCOMA declaracion_variable'''
	pass

def p_dec(p):
	'''dec : ID
		   | ID COMA dec'''
	pass

def p_type(p):
	'''type : type_simple
			| type_array'''
	pass

def p_type_array(p):
	'type_array : ARRAY CORI rango CORD OF type_simple'
	pass

def p_rango(p):
	'rango : CNUM PUNTO PUNTO CNUM'
	pass

def p_type_simple(p):
	'''type_simple : INT
				   | STR
				   | BOOL
				   | FLOAT
				   | CHAR'''
	pass

def p_declaraciones(p):
	'declaraciones : declaraciones_compuesta'
	pass

def p_declaraciones_compuesta(p):
	'declaraciones_compuesta : BEGIN decla END'
	pass

def p_decla(p):
	'''decla : declaracion
			 | decla declaracion'''
	pass

def p_declaracion(p):
	'''declaracion : declaracion_simple
				   | declaracion_estructurada'''
	pass

def p_declaracion_simple(p):
	'''declaracion_simple : asignacion
						  | lectura
						  | escritura'''
	pass

def p_declaracion_estructurada(p):
	'''declaracion_estructurada : declaraciones_compuesta
								| declaracion_if
								| declaracion_while
								| declaracion_for
								'''
	pass

def p_declaracion_if(p):
	'''declaracion_if : IF expresion THEN declaracion
					  | IF expresion THEN declaracion ELSE declaracion'''
	pass

def p_declaracion_while(p):
	'declaracion_while : WHILE expresion DO declaracion'
	pass

def p_declaracion_for(p):
	'declaracion_for : FOR asignacion TO expresion DO declaracion'

def p_asignacion(p):
	'asignacion : ID ASIG expresion PCOMA'
	pass

def p_lectura_1(p):
	'lectura : READ PARI ID PARD PCOMA'
	pass

def p_lectura_2(p):
	'lectura : READLN PARI ID PARD PCOMA'
	pass

def p_escritura_1(p):
	'escritura : WRITE PARI exp PARD PCOMA'
	pass

def p_escritura_2(p):
	'escritura : WRITELN PARI exp PARD PCOMA'
	pass

def p_exp(p):
	'''exp : expresion
		   | expresion COMA exp'''
	pass

def p_expresion(p):
	'''expresion : expresion_simple
				 | expresion_simple operador_relacional expresion'''
	pass

def p_expresion_simple(p):
	'''expresion_simple : signo termino
						| signo termino adicion expresion_simple'''
	pass

def p_signo(p):
	'''signo : vacio
			 | MAS
			 | MENOS'''
	pass

def p_termino(p):
	'''termino : factor
			   | factor multipicacion termino'''
	pass

def p_factor(p):
	'''factor : CNUM
			  | STRING
			  | ID
			  | NUM
			  | PARI expresion PARD
			  | NOT factor'''
	pass

def p_adicion(p):
	'''adicion : MAS
			   | MENOS
			   | OR'''
	pass

def p_multipicacion(p):
	'''multipicacion : POR
					 | DIV
					 | AND'''
	pass

def p_operador_relacional(p):
	'''operador_relacional : EQ
						   | LT
						   | GT
						   | GE
						   | LE'''
	pass

def p_vacio(p):
	'vacio :'
	pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL TOKEN  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'evaluacion'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("No se encontraron errores sintacticos")
	#input()
