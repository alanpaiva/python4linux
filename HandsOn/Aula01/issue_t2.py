#!/usr/bin/python

user = "alan.paiva"
passw = "opaopa"

login = raw_input("Digite login de usuario: ")
key = raw_input("Digite senha: ")

if (login == user) and (key == passw):
    print "Usuario autenticado com sucesso!"
    print "Seja Bem Vindo %s "%login
else:
    print "Senha ou usuario invalido!"
