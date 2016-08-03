#!/usr/bin/python

def parametros_dinamicos(*args): #para parametros comuns somente!
#p. cara parametro sera uma tupla e acessaremos por posicoes
    print args

parametros_dinamicos("Alan")
parametros_dinamicos("Alan","Paiva")
parametros_dinamicos("Alan","P","Paiva")


def exemplo_api(**kwargs): #obrigatoriamente precisa ser um dicionario!
    print kwargs.get("nome") #para capturar somente nome .get("nome")

exemplo_api(nome="alan")
exemplo_api(nome="alan",sobrenome="paiva")
