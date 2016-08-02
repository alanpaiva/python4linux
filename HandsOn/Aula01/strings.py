#!/usr/bin/python


nome = "Guido Van Rossum"
idade = 59

print "O criador do python se chama:"+nome
print "A idade dele eh:",idade

print "O criador do python se chama: "+nome+" a idade eh:",idade

print "O criador do python se chama: %s a idade eh: %s"%(nome,idade)

#print "select "+coluna+","+coluna2+","+coluna3+" from produtos"
#print "select %s from produtos"\nome 

nome = raw_input("Digite o seu nome: ") #se digitar numero, teremos erro
idade = input("Digite a sua idade: ") #se digitar string, teremos erro
