tokens = ("DATA", "HEADER", "INTEGER")
literals = ['.',  '/']

# Tokens
t_HEADER  = r'^Date.*$'
t_DATA  = r'^[.*]$'

# Ignored characters
t_ignore = " \t"

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Build the lexer
import ply.lex as lex   # ply.lex comes from the ply folder in the PLY download.
lexer = lex.lex()

# Parsing rules

global time_step
time_step = 0

def p_start(t):
    '''start : HEADER 
             | data
    '''
    if len(t) > 2: #This matches the third line in the parser rule, i.e., | DATA float
        print "Saw a ", t[0], ", ", t[1], ", ", t[2], "_~_"

def p_float(t):
    'float : INTEGER "." INTEGER'
    t[0] =  str(t[1]) + str(t[2]) + str(t[3])

def p_date(t):
    'date : INTEGER "/" INTEGER "/" INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3]) + str(t[4]) + str(t[5])

def p_data(t):
    'data : date float float'
    print "On Date: \t\t\t" + str(t[1]) + "\n" + "Amazon's Closing Price: \t" + str(t[2]) + "\n" + "Coca-Cola's Closing Price: \t" + str(t[3]) + "\n"

def p_error(t):
    if t == None:
        print("Syntax error a '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc   # ply.yacc comes from the ply folder in the PLY download.
parser = yacc.yacc()

while True:
    try:
        s = raw_input('')
    except EOFError:
        break
    parser.parse(s)

# To run the parser do the following in a terminal window: echo "Header1 is this~Header2 and that~~Data 1.0~Data 2.0" | tr "~" "\n" | grep -v '^\s*$' | python PLYstarter.py | sed "s/_~_/ which is a float./"
