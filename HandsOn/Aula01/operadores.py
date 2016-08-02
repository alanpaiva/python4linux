#!/usr/bin/python


a = 2
b = 3

print "Soma: ",a+b
print "Subtracao: ",a-b
print "Multiplicacao: ",a*b
print "Divisao: ",a/b
print "Resto: ",a%b

''' a++ #soma antes da operacao
    ++a #soma depois da operacao'''

a =a+1 #quer incrementar +1
print a

if a>b:
    print a, " > ",b
if b>a:
    print b, " > ",a
if a == b:
    print a, " = ",b

usuario = "alan.paiva"
senha = "opaopa"

if usuario == "alan.paiva" and senha == "opaopa":
    print "Autenticacao com sucesso!"
else:
    print "Falhou ao autenticar!"







