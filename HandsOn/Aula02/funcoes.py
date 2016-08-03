#!/usr/bin/python

usuarios = []
def cadastrar_usuario(nome,descricao=""): 
# associa um valor p. descricao, nome eh obrigatorio. obrig sempre sao os primeiros..!
    global usuarios # declara o que esta fora.. (nao da p. fazer se estiver em outra funcao)
    for u in usuarios:
        if  u == nome:
            print "Usuario ja cadastrado"
            break
    else:
        usuarios.append(nome) #add usuario1 a lista

    print "Cadastrado usuario: "+nome

    print "Descricao: "+descricao
    return nome # sempre que tiver um return, temos um valor associado a funcao..

usuario1 = cadastrar_usuario("Alan")
usuario2 = cadastrar_usuario("Joao")
usuario3 = cadastrar_usuario("Joao")


print usuarios

