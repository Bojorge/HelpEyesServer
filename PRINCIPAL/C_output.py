#//test1-este programa es de prueba para el compilador
from _Main import *
import SemanticAnalisis
import LexicAnalisis

pasos=0
def test(count):
	for x in range(5):
		count=inc(count,2)
		print(count)


def main():
	test(pasos)


main()