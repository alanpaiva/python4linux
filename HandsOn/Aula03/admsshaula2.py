#!/usr/bin/python

usuarios = []
senhas = []
servidores = []

# controla acesso e provisionamento dos servidores

#Parte 2 - criando funcoes
def switch(x): #funcao switch com parametro  = x
    try:
        dicionario_funcoes ={1:cadastrar_sysadmin,
                             2:listar_sysadmin,
                             3:remover_sysadmin,
                             4:cadastrar_servidor}
        dicionario_funcoes[x]() #posso chamar d 2 maneiras:.get ou c/ os"[]"
    except Exception as e:
        print "Opcao invalida",e
    finally: #qualquer erro que der, sempre vai ser executado excep e try!
        print "Processando a requisicao..."

def cadastrar_sysadmin(): #sempre chama o dicionario em funcao da funcao
    global usuarios
    global senhas
    login = raw_input("Digite o login do usuario: ")
    senha = raw_input("Digite sua senha:")
    usuarios.append(login)
    senhas.append(senha)
#    print "Cadastrando sysadmin.."

def listar_sysadmin():
    global usuarios # usar variaveis com mesmo nome sem sobrescrever o valor de uma variavel existente.
    for i,u in enumerate(usuarios):
        print "%s - %s"%(i,u) #i = enumerate
'''    for u in usuarios: 
         print usuarios.index(u),u (Forma que eu cheguei..)'''
    #1 - alan
    #2 - opaopa
    #3 - eita
#    print "Listando sysadmin.."

def remover_sysadmin():
    listar_sysadmin()
    id = input ("Digite o ID que deseja remover: ")
    global usuarios
    print ("Usuario " + usuarios[id] +" removido!!")    
    usuarios.pop(id)
    senhas.pop(id)

def cadastrar_servidor():
    global usuarios   
    global senhas 
    print "-= Autenticar Usuario =-"
    login = raw_input("Digite o login do usuario: ")
    senha = raw_input("Digite sua senha:")
    for usuario in usuarios:
        if usuario == login:
           indice = usuarios.index(usuario)
           if usuarios[indice] == login and senhas[indice] == senha:
               print "Usuario autenticado!"
               break
           else:
               print "Falha na autenticacao!"
               break
     #   server = raw_input("Digite o ip servidor: ")
     #   servidores.append(server)
        print ("Servidor cadastrado com sucesso!")    
    else:
       print "Usuario nao encontrado! :("
    
    
#    print "Removendo sysadmin"

#Parte 1 - cadastrar opcoes e utilizar IF para selecao..
print "1- Cadastrar sysadmin"
print "2- Listar sysadmins"
print "3- Remover sysadmin"
print "4- Cadastrar servidores"
print "5- Listar servidores"
print "6- Remover servidor"
print "7- Sair!"

#Parte 3 - colocando o while p. ficar infinito
while True: 
    opcao = int(raw_input("Digite a opcao desejada: "))
    switch(opcao)
    if opcao == 7:
        break

'''opcao = int(raw_input("Digite a opcao desejada: ")) #int( ) eh p. pegar o valor inteiro, senao sempre cai no else :)

if opcao ==1:
    print "Chamar a funcao de cadastro do sysadmin"
elif opcao ==2: # se eh so uma das opcoes, utilizar elif
    print "Funcao listar sysadmins"
elif opcao ==3:
    print "Remover um sysadmin"

elif opcao ==4:
    print "Cadastrar servidores" 
elif opcao ==5:
    print "Listar servidores" 
elif opcao ==6:
    print "Remover servidor"
else:
    print "Opcao invalida" '''
