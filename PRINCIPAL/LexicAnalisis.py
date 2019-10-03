import ply.lex as lex
import sys

#list of tokens names

tokens=["ID",'NUMBER','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN',
        "ASSIGN","SEMMICOLOM","COMMA","COMMENT","DOC","GT","GTE","LT","LTE",
        "EQUAL"]

#list of keywords

keywords={"import":"IMPORT","declare":"DECLARE","procedure":"PROCEDURE",
          "begin":"BEGIN","end":"END","call":"CALL","for":"FOR","loops":"LOOPS",
          "when":"WHEN","then":"THEN","else":"ELSE","case":"CASE"}

#add keywords to tokens

tokens+=list(keywords.values())

#regular expression rules for simple tokens

t_ignore="  \t"
t_ASSIGN= r"="
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_GT=r">"
t_GTE=r">="
t_LT=r"<"
t_LTE=r"<="
t_EQUAL=r"=="
t_SEMMICOLOM=r";"
t_COMMA=r","

#identifing regular expressions

def t_ID(t):
    r'[a-z][a-zA-Z0-9_&!]*'
    if t.value in keywords:
        t.value=t.value.upper()
        t.type=t.value
    return t

def t_DOC(t):
    r'[a-zA-Z_&!]+'
    return t

def t_COMMENT(t):
    r"//.*"
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    sys.exit(1)


#build the lexer
lexer = lex.lex()


#******************************************************************************testing***********************************************************************************#

#data = "//test-este codigo es una prueba\ndeclare var1;\ndeclare var2=15;\nprocedure test1 (var)\nbegin\ncall test2();\nend;"

#input data
#   lexer.input(data)

# Tokenize-print
"""while True:
     tok = lexer.token()
     if not tok:
         break      # No more input
     print(tok)"""