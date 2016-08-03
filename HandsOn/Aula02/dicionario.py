#!/usr/bin/python

produtos = {"nome":"Celular",
           "preco": 998.97,
           "caracteristicas":["tela","cor","tamanho","bateria"]}
'''
print produtos.get("nome") #duas formas para mostrar o produto e preco.. (sempre que for buscar um valor)
print produtos["preco"] # (sempre que for modificar)

produtos["nome"] = "Galaxy J5" #3 faz a modificacao conforme sugestao acima
print produtos

print produtos.get("caracteristicas")
print produtos.get("caracteristicas")[3] # mostra a opcao da lista das caracteristicas 

produtos["caracteristicas"][1] = "dimensoes" # substituindo o valor da posicao 1 cor p. dimensoes
print produtos
print produtos.get("caracteristicas")

produtos["caracteristicas"].append("cor") # adicionando a cor no final da lista
print produtos

produtos ["nota"] = 4.8 #adicionando um valor para nota, se usar .get da erro, nao vai add o valor..
print produtos
print produtos.keys() # traz uma lista para cada uma das chaves desse dicionario..
print produtos.values() # traz os valores das chaves desse dicionario.. '''

for k in produtos.keys(): #demonstra os valores para cada chave com a string chave e valor..
    print "Chave: ",k
    print "Valor: ",produtos.get(k)
