#!/usr/bin/python

from Modulos.usuarios import ler_banco, escrever_banco
from Modulos.docker import criar_container, remover_container
from Modulos.SSH import executa_comando as ssh_comando #as = alias

def cadastrar_servidor(): #sempre chama o dicionario em funcao da funcao
    pass    
    banco = ler_banco()
    # {"servidores":[]} 
    servidores = {} #dicionario recebe servidores/desc. vazio mesmo         
    servidores ["hostname"] = raw_input("Digite o hostname do server: ")
    # {"servidor":"xxxx"}
    servidores ["descricao"] = raw_input("Digite descricao para o server: ")
    # {"servidores":"xxxx","descricao":"servidor foda!"}
    banco["servidores"].append(servidores)#vai no json e add server no final

    #rotina de criacao dos containers
    cmd = criar_container(servidores["hostname"])
    ssh_comando(cmd)
    
    # {"servidores":[{"servidor":"xxxx","descricao":"servidor foda!"}]}    
    escrever_banco(banco) #grava no arquivo json

def listar_servidor():
    pass    
    banco = ler_banco() #consulta o banco
    for i,u in enumerate(banco.get("servidores")): #pega os hostnames do banco
        print "%s - Host:%s  Desc:%s" % (i, u.get("hostname"), u.get("descricao"))

def remover_servidor():
    pass
    listar_servidor()
    servidor_id = input("Digite o ID do server que deseja remover: ")
    banco = ler_banco()
    
    name = banco["servidores"][servidor_id]["hostname"]
    cmd = remover_container(name)
    ssh_comando(cmd)

    banco["servidores"].pop(servidor_id) #le
    escrever_banco(banco)
