# -*- coding: utf-8 -*-

class Pessoa:

	attrs = {
		'email': None,
		'telefone': None,
		'altura': None,
		'peso': None,
		'nacionalidade': None
	}

	separator = '-'

	def __init__(self, nome):
		self.nome = nome

	def setAttr(self, attr, value):
		self.attrs[attr] = str(value)
		return self

	def perfil(self):
		print self.nome

		for attr in self.attrs:
			if ( self.attrs[attr] ):
				print '-----'
				print attr.lower()+" -> "+self.attrs[attr]

	def __getitem__(self, chave):
		return self.attrs[chave]

	class Car:
		def __init__(self, marca):
			Pessoa.car = marca


# execute
p = Pessoa('Luan Oliveira')

# setando o atributo attrs que é um dicionário através de um metodo
p.setAttr('email', 'xxxxx@gmail.com')
p.setAttr('telefone', '(84) 9999.9999')

# também setando, mas agora o metodo retorna a própria instância
p.setAttr('altura', 1.75).setAttr('peso', 70).setAttr('nacionalidade', 'Brasileiro')

p.Car('citroen')

print p['email']

#p.perfil()