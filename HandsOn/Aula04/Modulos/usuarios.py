#!/usr/bin/python

import json #modulo para trabalhar com JSON

def ler_banco():
    with open("banco.json","r") as f: #abrindo arquivo p. leitura (r)
        banco = json.loads(f.read()) #lemos uma string, converte p. json (dicionario) e grava na variavel
    return banco 

def escrever_banco(dado):
    with open("banco.json","w") as f: #f=file mas pode ser qqc coisa!
        dado = json.dumps(dado) #pega um dicionario e converte em string
        f.write(dado)    


def cadastrar_usuario(): #sempre chama o dicionario em funcao da funcao
    banco = ler_banco()
    usuario = {} #dicionario recebe user e pass. vazio mesmo         
    usuario ['login'] = raw_input("Digite o login do usuario: ")
    usuario ['senha'] = raw_input("Digite sua senha:")
    banco ['usuarios'].append(usuario)#vai no json e add usuario no final
    escrever_banco(banco) #grava no arquivo json

#    print "Cadastrando sysadmin.."

def listar_usuario():
    for i,u in enumerate(usuarios):
        print "%s - %s"%(i,u) #i = enumerate

def remover_usuario():
    listar_usuario()
    id = input ("Digite o ID que deseja remover: ")
    print ("Usuario " + usuarios[id] +" removido!!")    
    usuarios.pop(id)
    senhas.pop(id)

