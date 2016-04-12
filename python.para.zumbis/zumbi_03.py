#coding: utf-8
'''
comentários
de
várias
linhas
'''
a = int(input("Entre com o valor de a: "))
b = int(input("Entre com o valor de b: "))
c = int(input("Entre com o valor de c: "))

'''
if ( numero1 > numero2 and numero1 > numero3 ):
	print("Número %d é maior que %d e %d" %(numero1, numero2, numero3))
elif (numero2 > numero1 and numero2 > numero3):
	print("Número %d é maior que %d e %d" %(numero2, numero1, numero3))
elif (numero3 > numero1 and numero3 > numero2):
	print("Número %d é maior que %d e %d" %(numero3, numero2, numero1))
'''



if a >= b and a >= c:
	print("A: %d" %a)
elif b >= c:
	print("B: %d" %b)
else:
	print("C: %d" %c)