# ------------------------------------------------------------
# parser.py
#
# Antonino N. Mione
#
# parsese assignment statements from a simple expression grammar
# give here:
#
# assign => NAME EQUALS expr
# expr => expr PLUS term
# expr => expr MINUS term
# expr => term
# term => term TIMES factor
# term => term DIVIDE factor
# term => factor
# factor => NUMBER
# factor => NAME
# factor => ( expr )
# 
# ------------------------------------------------------------

import ply.yacc as yacc
import exprLexer
import exprLang as ast
import context
import sys

tokens = exprLexer.tokens

start = 'assign'

vars = {};

def p_assign(p):
    '''assign : NAME EQUALS expr'''
    vars[p[1]] = p[3]
    print ('REDUCE : assign : NAME EQUALS expr')
    print (vars[p[1]])
    p[0] = ast.Assign(p[1], p[3])

def p_expr_plus(p):
    '''expr : expr PLUS term'''
    print ('REDUCE : expr : expr PLUS term')
    p[0] = ast.Expr('+', p[1], p[3])

def p_expr_minus(p):
    '''expr : expr MINUS term'''
    print ('REDUCE : expr : expr MINUS term')
    p[0] = ast.Expr('-', p[1], p[3])

def p_expr_term(p):
    '''expr : term'''
    print ('REDUCE : expr : term')
    p[0] = p[1]
	
def p_term_times(p):
    '''term : term TIMES factor'''
    print ('REDUCE : term : term TIMES factor')
    p[0] = ast.Expr('*', p[1], p[3])
    
def p_term_divide(p):
    '''term : term DIVIDE factor'''
    print ('REDUCE : term : term DIVIDE factor')
    p[0] = ast.Expr('/', p[1], p[3])
    
def p_term_factor(p):
    '''term : factor'''
    print ('REDUCE : term : factor')
    p[0] = p[1]
		  
def p_factor(p):
    '''factor : NUMBER'''
    print ('REDUCE : factor : NUMBER')
    p[0] = ast.Number(p[1])

def p_factor_name(p):
    '''factor : NAME'''
    print ('REDUCE : factor : NAME')
    p[0] = ast.Name(p[1])

def p_factor_expr(p):
    '''factor : LPAREN expr RPAREN'''
    print ('REDUCE : factor : LPAREN expr RPAREN')
    p[0] = p[2]

def p_error(p):
    print ("Error parsing")

def print_program(theProgram):
    for line in theProgram:
        print(str(line))

yacc.yacc()

sourceFile = ''
if len(sys.argv) < 2:
    print("No source!")
else:
    sourceFile = sys.argv[1]
print ('Source: ' + sourceFile)

progfile = open(sourceFile, 'r')
data = progfile.readline()
progfile.close()

# data = "a=10+14*20-b"
result = yacc.parse(data)
print(result.toStringNode(0))

ctx = context.Context()

result.compile(ctx)


theProgram = ctx.programCode()
print("Program code:")
print_program(theProgram)
print(str(ctx.constants))
print(str(ctx.variables))

ctx.execute()
theStack = ctx.getStack()

#print("Debug: theStack: " + str(theStack))
print("Variables: " + str(ctx.variables))

