#!/usr/bin/python


#sem saber a funcao lambda:
'''
def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

print soma(2,2)
print subtracao(2,2)
print multiplicacao(2,2)'''

#com lambda: p. quem trabalha com calculo e map reduce..
soma = lambda a,b: (a+b)
subtracao = lambda a,b: (a-b)
multiplicacao = lambda a,b: (a*b)

print soma(2,2)
print subtracao(2,2)
print multiplicacao(2,2)
