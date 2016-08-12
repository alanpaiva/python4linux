#!/usr/bin/python

from servidor import Servidor
from IPMI import IPMI

class Fisico(Servidor,IPMI):
    slot_ocupado = 1
    slot_memoria = 4
    slot_disco = 4
    slot_disco_ocupado = 1

    def __init__(self,cpu=1,memoria=1024,disco=512): #def. paramt. nao obrigat
        self.cpu = cpu
        self.memoria = memoria
        self.disco = disco

    def contratar_cpu(self,cpu):
        print "Faca um upgrade de maquina.."

    def contratar_memoria(self,memoria): #polimorfismo
        if self.slot_ocupado < self.slot_memoria:
            self.memoria += memoria
            self.slot_ocupado += 1
        else:
            print "Voce nao tem mais slots disponiveis.."

    def contratar_disco(self,disco):
        if self.slot_disco_ocupado < self.slot_disco:
            self.disco += disco
            self.slot_disco_ocupado += 1
        else:
            print "Voce nao tem mais slots disponiveis.."

if __name__ == '__main__':
    fisico = Fisico()
    fisico.acessar()
    fisico.contratar_cpu(3)
    fisico.contratar_memoria(1024)
    fisico.contratar_disco(50)
