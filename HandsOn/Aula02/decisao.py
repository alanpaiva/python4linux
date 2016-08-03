#!/usr/bin/python
'''
idade = 18
pais = True

if idade >= 18:
    print "Pode tirar habilitacao!"
elif pais == True:
    print "Pode tirar habilitacao!"
else:
    print "Nao tem idade suficiente."

#parte 4 sobre FOR
#for(x = 0 X <= 10, x++) Maneira tradicional em outras linguagens

for x in range(0,10): #valores de 0 ate 9
    print x

produtos = ["camisa","tenis","calca","bermuda","chapeu"]
for p in produtos:
    if "bermuda" == p: # se encontrar bermuda, jah cai no break, caso contrario msg nao encontrado..
        print p+" encontrada"
        break
else:
    print "Produto nao encontrado!"
'''
for letra in "python": #encontra um item em uma determinada lista (item em um banco de dados)
    if letra == "t":
        print letra+ " encontrada!"
        continue # lista informacao ate encontrar o dado desejado..
    else:
        print letra 
    print " Testando a instrucao continue!"
