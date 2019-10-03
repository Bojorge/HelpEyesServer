import ply.yacc as yacc
import sys
from LexicAnalisis import tokens
from _Main import *
from SemanticAnalisis import *

#error handling from shift/reduce
#analising most right or most left
#(cascade)
precedence=(
    ("right","ID","CALL","BEGIN","DOC"),
    ("right","PROCEDURE"),
    ("right","DECLARE"),
    ("right","ASSIGN"),
    ("left","PLUS","MINUS"),
    ("left","TIMES","DIVIDE"),
    ("left","LPAREN","RPAREN")
    )

#********************************************************************program productions*****************************************************************************#

def p_program(p):
    """program : COMMENT importDeclare block"""
    p[0]=program(p[1],p[2],p[3])


#*************************************************************************block productions*************************************************************************#

def p_block(p):
    """block : varDeclare procedureDeclare statement"""

    p[0]=block(p[1],p[2],p[3])

#**************************************************************************import declare***************************************************************************#
def p_importDeclare1(p):
    """importDeclare : IMPORT DOC SEMMICOLOM importDeclare"""
    p[0]=importDeclare(p[2],p[4])

def p_importDeclare2(p):
    """importDeclare : empty"""
    p[0]=Null()
#*********************************************************************varDeclare productions************************************************************************#

def p_varDeclare1(p):
    """varDeclare : DECLARE varDeclareList SEMMICOLOM varDeclare"""
    p[0]=varDeclare1(p[2],p[4])

def p_varDeclare2(p):
    """varDeclare : empty"""
    p[0]=Null()

def p_varDeclareList1(p):
    """varDeclareList : ID"""
    p[0]=varDeclareList1(p[1])

def p_varDeclareList2(p):
    """varDeclareList : varDeclareList COMMA ID"""
    p[0]=varDeclareList2(p[1],p[3])

def p_varDeclareList3(p):
    """varDeclareList : ID ASSIGN NUMBER"""
    p[0]=varDeclareList3(p[1],p[3])

def p_varDeclareList4(p):
    """varDeclareList : varDeclareList COMMA ID ASSIGN NUMBER"""
    p[0]=varDeclareList4(p[1],p[3],p[5])


#**************************************************************procedureDeclare productions************************************************************************#

def p_procedureDeclare1(p):
    """procedureDeclare : PROCEDURE ID LPAREN parameter RPAREN BEGIN block END SEMMICOLOM procedureDeclare"""
    p[0]=procedureDeclare(p[2],p[4],p[7],p[10])

def p_procedureDeclare2(p):
    """procedureDeclare : empty"""
    p[0]=Null()

def p_parameter1(p):
    """parameter : factor"""
    p[0]=parameter1(p[1])

def p_parameter2(p):
    """parameter : parameter COMMA factor"""
    p[0]=parameter2(p[1],p[3])

def p_parameter3(p):
    """parameter : empty"""
    p[0]=Null()

#*********************************************************************statement productions***********************************************************************#

def p_statement1(p):
    """statement : CALL ID LPAREN parameter RPAREN SEMMICOLOM statement"""

    p[0]=statement1(p[2],p[4],p[7])

def p_statement2(p):
    """statement : ID ASSIGN expression SEMMICOLOM statement"""

    p[0]=statement2(p[1],p[3],p[5])

def p_statement3(p):
    """statement : empty"""

    p[0]=Null()

def p_statement4(p):
    """statement : FOR NUMBER LOOPS statement END SEMMICOLOM statement"""

    p[0]=statement4(p[2],p[4],p[7])

def p_statement5(p):
    """statement : CASE caseList ELSE statement END SEMMICOLOM statement"""

    p[0]=statement5(p[2],p[4],p[7])

def p_statement6(p):
    """statement : ID ASSIGN CALL ID LPAREN parameter RPAREN SEMMICOLOM statement"""
    p[0] = statement6(p[1], p[4], p[6],p[9])

def p_caseList1(p):
    """caseList : WHEN condition THEN statement"""

    p[0]=caseList1(p[2],p[4])

def p_caseList2(p):
    """caseList : WHEN condition THEN statement caseList"""

    p[0]=caseList2(p[2],p[4],p[5])

#***********************************************************************other productions*************************************************************************#

def p_condition(p):
    """condition : expression relation expression"""
    p[0]=condition(p[1],p[2],p[3])

def p_relation1(p):
    """relation : EQUAL"""
    p[0]=relation1(p[1])

def p_relation2(p):
    """relation : GT"""
    p[0]=relation2(p[1])

def p_relation3(p):
    """relation : GTE"""
    p[0] = relation3(p[1])

def p_relation4(p):
    """relation : LT"""
    p[0] = relation4(p[1])

def p_relation5(p):
    """relation : LTE"""
    p[0] = relation5(p[1])

def p_expression1(p):
    """expression : term"""
    p[0]=expression1(p[1])

def p_expression2(p):
    """expression : addOperator term"""
    p[0]=expression2(p[1],p[2])

def p_expression3(p):
    """expression : expression addOperator term"""
    p[0]=expression3(p[1],p[2],p[3])

def p_addOperator1(p):
    """addOperator : PLUS"""
    p[0]=addOperator1(p[1])

def p_addOperator2(p):
    """addOperator : MINUS"""
    p[0] = addOperator2(p[1])

def p_term1(p):
    """term : factor"""
    p[0]=term1(p[1])

def p_term2(p):
    """term : term multiOperator factor"""
    p[0] = term2(p[1],p[2],p[3])

def p_multiOperator1(p):
    """multiOperator : TIMES"""
    p[0]=multiOperator1(p[1])

def p_multiOperator2(p):
    """multiOperator : DIVIDE"""
    p[0] = multiOperator2(p[1])

def p_factor1(p):
    """factor : ID"""
    p[0]=factor1(p[1])

def p_factor2(p):
    """factor : NUMBER"""
    p[0] = factor2(p[1])

def p_factor3(p):
    """factor : LPAREN expression RPAREN"""
    p[0] = factor3(p[2])

def p_empty(p):
    """empty :"""
    pass

def p_error(p):
    print("Error de sintaxis",p)
    print("Error en la linea "+str(p.lineno))
    sys.exit(1)

#**************************************************************************OUTPUT********************************************************************************#

parser= yacc.yacc()
result=parser.parse(readFile("C_input.txt"))

writeFile("C_output.py",result.translate())
runFile("C_output.py")



