#!/usr/bin/python

animais = ["gato","cachorro","tartaruga","papagaio","lagarto"]
mamifero = []
aves = []
print "Lista de aves: ",aves
aves.append("canario") # adicina um item na lista que esta vazia acima..
print "Lista de aves: ",aves

print "Total de aves: ",len(aves)
animais.remove("papagaio") # removendo um item..
print "Lista de animais: ",animais
aves.insert(0,"papagaio") # adicionando um item na lista aves com posicao 0..
print "Lista de aves: ",aves
aves.pop(1) # remove o item #1 da lista..
print "Lista de aves: ",aves
print "Tartaruga esta no indice: ",animais.index("tartaruga") #mostra em qual posicao do indice esta tartaruga
animais.reverse() #sobrescreve a variavel com lista invertida..
print "Lista de animais: ",animais
