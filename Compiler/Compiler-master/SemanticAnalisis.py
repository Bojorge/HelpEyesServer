#str with the new code
newCode=""
global main
main=False
#the parent class
class Node():
    pass

#***************************************************************PROGRAM CLASS**************************************************************************#

class program(Node):
    """program : COMMENT importDeclare block"""
    def __init__(self,comment,importDeclare,block):
        self.comment=comment
        self.importDeclare = importDeclare
        self.block=block


    def translate(self):
        global newCode

        importDeclare = self.importDeclare.translate(0)
        block= self.block.translate(0)

        newCode+="#"+self.comment+"\nfrom _Main import *\n"
        newCode+=importDeclare+"\n"+block
        if(main==True):
            newCode+="\nmain()"

        return newCode


#******************************************************************BLOCK CLASS*************************************************************************#

class block(Node):
    """block : varDeclare procedureDeclare statement"""
    def __init__(self,varDeclare,procedureDeclare,statement):
        self.varDeclare=varDeclare
        self.procedureDeclare = procedureDeclare
        self.statement = statement

    def translate(self,ident):


        varDeclare=self.varDeclare.translate(ident)
        procedureDeclare=self.procedureDeclare.translate(ident)
        statement=self.statement.translate(ident)

        return varDeclare+procedureDeclare+statement



#*****************************************************************IMPORT CLASS*************************************************************************#

class importDeclare(Node):
    """importDeclare : IMPORT DOC SEMMICOLOM importDeclare"""
    def __init__(self,doc,importDeclare):
        self.doc=doc
        self.importDeclare=importDeclare

    def translate(self,x):

        importDeclare=self.importDeclare.translate(0)

        return "import "+self.doc+"\n"+importDeclare

#****************************************************************DECLARE CLASSES***********************************************************************#

class varDeclare1(Node):
    """varDeclare : DECLARE varDeclareList SEMMICOLOM varDeclare"""

    def __init__(self,varDeclareList,varDeclare):
        self.varDeclareList=varDeclareList
        self.varDeclare=varDeclare

    def translate(self,ident):

        varDeclareList=self.varDeclareList.translate(ident)
        varDeclare=self.varDeclare.translate(ident)

        return varDeclareList+"\n"+varDeclare

class varDeclareList1(Node):
    """varDeclareList : ID"""

    def __init__(self,id):
        self.id=id

    def translate(self,ident):

        return "\t"*ident+self.id+"=0"

class varDeclareList2(Node):
    """varDeclareList : varDeclareList COMMA ID"""

    def __init__(self, varDeclareList, id):
        self.varDeclareList=varDeclareList
        self.id=id

    def translate(self,ident):

        varDeclareList=self.varDeclareList.translate(ident)

        return "\t"*ident+self.id+"=0\n"+varDeclareList

class varDeclareList3(Node):
    """varAssignList : ID ASSIGN NUMBER"""
    def __init__(self,id,number):
        self.id=id
        self.number=number

    def translate(self,ident):

        return "\t"*ident+self.id+"="+str(self.number)

class varDeclareList4(Node):
    """varAssignList : varDeclareList COMMA ID ASSIGN NUMBER"""
    def __init__(self,varDeclareList,id,number):
        self.varDeclareList=varDeclareList
        self.id=id
        self.number=number

    def translate(self,ident):

        varDeclareList=self.varDeclareList.translate(ident)

        return varDeclareList+"\n"+"<\t"*ident+self.id+"="+str(self.number)


#****************************************************************PROCEDURE CLASS***********************************************************************#

class procedureDeclare(Node):
    """procedureDeclare : PROCEDURE ID LPAREN parameter RPAREN BEGIN block END SEMMICOLOM procedureDeclare"""

    def __init__(self,id,parameter,block,procedureDeclare):
        self.id=id
        self.parameter=parameter
        self.block=block
        self.procedureDeclare=procedureDeclare
        if(self.id=="main"):
            global main
            main=True

    def translate(self,ident):

        parameter=self.parameter.translate(0)
        block=self.block.translate(ident+1)
        procedureDeclare=self.procedureDeclare.translate(ident)

        return "\t"*ident+"def "+self.id+"("+parameter+"):\n"+block+"\n"+procedureDeclare

class parameter1(Node):
    """parameter : factor"""
    def __init__(self,factor):
        self.factor=factor
    def translate(self,x):
        factor=self.factor.translate()

        return factor

class parameter2(Node):
    """parameter : parameter COMMA factor"""
    def __init__(self, parameter,factor):
        self.factor= factor
        self.parameter = parameter

    def translate(self,x):
        factor=self.factor.translate()
        parameter = self.parameter.translate(0)

        return parameter+","+factor

#**************************************************************STATEMENT CLASSES***********************************************************************#

class statement1(Node):
    """statement : CALL ID LPAREN parameter RPAREN SEMMICOLOM statement"""
    def __init__(self,id,parameter,statement):
        self.id=id
        self.parameter=parameter
        self.statement=statement

    def translate(self,ident):
        parameter=self.parameter.translate(0)
        statement=self.statement.translate(ident)

        return "\t"*ident+self.id+"("+parameter+")\n"+statement

class statement2(Node):
    """statement : ID ASSIGN expression SEMMICOLOM statement"""

    def __init__(self,id,expression,statement):
        self.id=id
        self.expression=expression
        self.statement=statement

    def translate(self,ident):

        expression=self.expression.translate()
        statement=self.statement.translate(ident)

        return "\t"*ident+self.id+"="+expression+"\n"+statement

class statement4(Node):
    """statement : FOR NUMBER LOOPS statement END SEMMICOLOM statement"""
    def __init__(self, number,statement,statement2):
        self.number=number
        self.statement=statement
        self.statement2=statement2

    def translate(self,ident):
        statement=self.statement.translate(ident+1)
        statement2=self.statement2.translate(ident)

        return "\t"*ident+"for x in range("+str(self.number)+"):\n"+statement+"\n"+statement2

class statement5(Node):
    """statement : CASE caseList ELSE statement END SEMMICOLOM statement"""
    def __init__(self, caseList,statement,statement2):
        self.caselist=caseList
        self.statement=statement
        self.statement2=statement2

    def translate(self,ident):
        caseList=self.caselist.translate(ident)
        statement=self.statement.translate(ident+1)
        statement2=self.statement2.translate(ident)

        return caseList+"\n"+"\t"*ident+"else:\n"+statement+"\n"+statement2

class statement6(Node):
    """statement : ID ASSIGN CALL ID LPAREN parameter RPAREN SEMMICOLOM statement"""
    def __init__(self,id, id2,parameter,statement):
        self.id=id
        self.id2=id2
        self.parameter=parameter
        self.statement=statement

    def translate(self,ident):

        parameter=self.parameter.translate(0)
        statement=self.statement.translate(ident)
        return "\t"*ident+self.id+"="+self.id2+"("+parameter+")\n"+statement

class caseList1(Node):
    """caseList : WHEN condition THEN statement SEMMICOLOM"""
    def __init__(self,condition,statement):
        self.condition=condition
        self.statement=statement

    def translate(self,ident):
        condition=self.condition.translate()
        statement=self.statement.translate(ident+1)

        return "\t"*ident+"if ("+condition+"):\n"+statement

class caseList2(Node):
    """caseList : WHEN condition THEN statement SEMMICOLOM caseList"""
    def __init__(self, condition,statement,caseList):
        self.condition = condition
        self.statement = statement
        self.caseList=caseList

    def translate(self,ident):
        condition=self.condition.translate()
        statement=self.statement.translate(ident+1)
        caseList=self.caseList.translate(ident)

        return "\t"*ident+"if ("+condition+"):\n"+statement+"\n"+caseList

#****************************************************************OTHER CLASSES*************************************************************************#
class Null(Node):

    def __init__(self):
        self.type="void"

    def setIdent(self,x):
        pass

    def translate(self,x):
        return ""

class condition(Node):
    """condition : expression relation expression"""
    def __init__(self, expression,relation, expression2):
        self.expression=expression
        self.relation=relation
        self.expression2=expression2

    def translate(self):

        expression=self.expression.translate()
        relation=self.relation.translate()
        expression2=self.expression2.translate()

        return expression+relation+expression2

class relation1(Node):
    """relation : EQUAL"""
    def __init__(self, equal):
        self.equal=equal
    def translate(self):

        return "=="

class relation2(Node):
    """relation : GT"""
    def __init__(self,gt):
        self.gt=gt

    def translate(self):
        return ">"

class relation3(Node):
    """relation : GTE"""
    def __init__(self,gte):
        self.gte=gte

    def translate(self):
        return ">="

class relation4(Node):
    """relation : LT"""
    def __init__(self, lt):
        self.lt=lt

    def translate(self):
        return "<"

class relation5(Node):
    """relation : LTE"""
    def __init__(self, lte):
        self.lte

    def translate(self):
        return "<="

class expression1(Node):
    """expression : term"""
    def __init__(self, term):
        self.term=term

    def translate(self):
        term=self.term.translate()
        return term

class expression2(Node):
    """expression : addOperator term"""
    def __init__(self, addOperator, term):
        self.addOperator=addOperator
        self.term=term

    def translate(self):
        addOperator=self.addOperator.translate()
        term=self.term.translate()
        return addOperator+term

class expression3(Node):
    """expression : expression addOperator term"""
    def __init__(self ,expression, addOperator, term):
        self.expression=expression
        self.addOperator=addOperator
        self.term=term

    def translate(self):
        expression=self.expression.translate()
        addOperator=self.addOperator.translate()
        term=self.term.translate()
        return expression+addOperator+term

class addOperator1(Node):
    """addOperator : PLUS"""
    def __init__(self, plus):
        self.plus=plus

    def translate(self):
        return "+"

class addOperator2(Node):
    """addOperator : MINUS"""
    def __init__(self, minus):
        self.minus=minus

    def translate(self):
        return "-"

class term1(Node):
    """term : factor"""
    def __init__(self, factor):
        self.factor=factor

    def translate(self):
        factor=self.factor.translate()
        return factor

class term2(Node):
    """term : term multiOperator factor"""
    def __init__(self, term,multiOperator, factor):
        self.term=term
        self.multiOperator=multiOperator
        self.factor=factor

    def translate(self):
        term=self.term.translate()
        multiOperator=self.multiOperator.translate()
        factor=self.factor.translate()
        return term+multiOperator+factor

class multiOperator1(Node):
    """multiOperator : TIMES"""
    def __init__(self, times):
        self.times=times

    def translate(self):
        return "*"

class multiOperator2(Node):
    """multiOperator : DIVIDE"""
    def __init__(self,divide):
        self.divide=divide

    def translate(self):
        return "/"

class factor1(Node):
    """factor : ID"""
    def __init__(self, id):
        self.id=id

    def translate(self):
        return self.id

class factor2(Node):
    """factor : NUMBER"""
    def __init__(self, number):
        self.number=str(number)

    def translate(self):
        return self.number

class factor3(Node):
    """factor : LPAREN expression RPAREN"""
    def __init__(self, expression):
        self.expression=expression

    def translate(self):
        expression=self.expression.translate()
        return "("+expression+")"
