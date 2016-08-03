#!/usr/bin/python

print "-= Sistema AutoEscola =-"
nome = raw_input("Digite seu nome: ") 
idade = input("Digite sua idade: ")

if idade >= 18:
    print "Cliente Cadastrado"
else:
    responsavel = raw_input("Esta acompanhado de responsavel? ")
    if responsavel[0].lower() in "sim": #.lower pega ate maiusculas [0] pega soh primeira letre ex. "S"
        nome_responsavel = raw_input("Digite o nome do responsavel: ")
        print "Cliente Cadastrado!"
    else:
        print "Nao eh possivel efetuar o cadastro!!"
