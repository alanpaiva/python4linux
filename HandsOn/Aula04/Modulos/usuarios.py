#!/usr/bin/python

import json #modulo para trabalhar com JSON

def ler_banco():
    with open("banco.json","r") as f: #abrindo arquivo p. leitura (r)
        #print type (f.read())        
        banco = json.loads(f.read()) #lemos uma string, converte p. json (dicionario) e grava na variavel
    return banco 

def escrever_banco(dado):
    with open("banco.json","w") as f: #f=file mas pode ser qqc coisa!
        dado = json.dumps(dado) #pega um dicionario e converte em string
        f.write(dado)    


def cadastrar_usuario(): #sempre chama o dicionario em funcao da funcao
    banco = ler_banco()
    # {"usuarios":[]} 
    usuario = {} #dicionario recebe user e pass. vazio mesmo         
    usuario ['login'] = raw_input("Digite o login do usuario: ")
    # {"login":"alan"}
    usuario ['senha'] = raw_input("Digite sua senha: ")
    # {"login":"alan","senha":"123"}
    banco ['usuarios'].append(usuario)#vai no json e add usuario no final
    # {"usuarios":[{"login":"alan","senha":"123"}]}
    escrever_banco(banco) #grava no arquivo json

def listar_usuario():
    banco = ler_banco() #consulta o banco
    for i,u in enumerate(banco.get("usuarios")): #pega os usuarios do banco
        print "%s -%s"%(i,u.get("login"))

def remover_usuario():
    listar_usuario()
    indice = input("Digite o ID que deseja remover: ")
    banco = ler_banco()    
    banco["usuarios"].pop(indice) #le
    escrever_banco(banco)    
