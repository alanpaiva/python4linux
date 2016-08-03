#!/usr/bin/python (onde o python esta instalado)
#
# Feito por: Alan Paiva
# Data: 01/Ago/2016
# Email: alan.spaiva@gmail.com
#

''' 
chamado de TheDoc ('''...''') readthedocs.org:
O objetivo desse script e fazer a autenticacao dos usuarios no sistema.
O script tambem faz integracao com mysql e postgresql
'''
print "== Sistema de Autenticacao =="
print "Digite seu usuario: "

usuario = raw_input()
senha = raw_input("Digite sua senha: ")
print "Autenticando o usuario: "+usuario

if senha == "opaopa":
    print "Autenticado com sucesso!"
else:
    print "Falhou ao autenticar!"



