# -*- coding: utf-8 -*-

def div_decorador(quantidade):

    def _decorar(funcao):
        def decorar(texto):
            return quantidade*"<div>"+funcao(texto)+quantidade*"</div>"
        return decorar

    return _decorar

def p_decorador(funcao):
    def decorar(texto):
        return "<p>"+funcao(texto)+"</p>"
    return decorar

'''
@div_decorador(5)
@p_decorador
'''

@div_decorador(10)
def falar(texto):
    return texto

''''
return_div_decorar = div_decorador(10)
falar = return_div_decorar(falar)
'''



print falar('Essa é a minha função original')
