#!/usr/bin/python

PI = 3.14 #sempre letras maiusculas, valor nao eh alterado
numero = 1
dolar = 3.23
texto = "Curso de Python"
dicionario = {"dinossauro":"animal prehistorico",
              "cebola":"cebola e um temperoo",
              "4Linux":3057,
              "produtos":["tenis","sapato","sandalia"]} #lista

notas = [5, 6.5, 7, 10, 9.5]
materias = ["portugues","matematica","historia","geografia","artes"]

tupla = ("param1","param2","param3")

print "Historico do aluno"
print zip(materias,notas) #traz os valores das duas listas ordenados por ordem dos parametros 
print "========================"
print dicionario.get("produtos")
print "========================"
print "Valor 0 da tupla: ",tupla[0]

print "========================"
print "ASPAS\""
print "Opcao1\nOpcao2"
