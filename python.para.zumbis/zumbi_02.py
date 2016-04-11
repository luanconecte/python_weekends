nome = input("Nome: ")
velocidade = int(input("Qual a velocidade do carro? "))

if ( velocidade > 110 ) :
	kmAcima = (velocidade-110)
	multa = float(kmAcima*5)
	print("# %s foi multado(a) em R$ %d por andar a %dkm/h, %dkm/h acima da velocidade permitida." %(nome, multa, velocidade, kmAcima))
else :
	print("Que legal, você está na velocidade correta.")