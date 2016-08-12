#!/usr/bin/python

from Modulos.docker import Docker
from modelv2 import session, Servidor as ServidorModel #session cursor
import json

class Servidores:
    id=0
    nome=""
    descricao=""
    ip=""

    def cadastrar(self): #sempre chama o dicionario em funcao da funcao
        self.nome = raw_input("Digite o hostname do server: ")
        self.descricao = raw_input("Digite descricao para o server: ")
        self.ip = raw_input("Digite IP para o server: ")    

        try:
            # instancia dos objetos SSH e Docker
            docker = Docker()
            docker.criar(self.nome)
            container = docker.pegar_ip(self.nome)
            container = json.loads(container)
            self.ip = container[0].get("NetworkSettings").get("IPAddress")
            s = ServidorModel(self)
            session.add(s)
            session.commit()
        except Exception as e:
            session.rollback()
            print "Falhou ao cadastrar servidor: ",e    

    def listar(self):
        lista_servidor = session.query(ServidorModel).all()
        for servidor in lista_servidor:
            print "%s %s %s %s"%(servidor.id,
                                 servidor.nome,
                                 servidor.descricao,
                                 servidor.ip)

    def exec_comando_servidor(self):
        self.listar()
        servidor_id  = input("Digite o id do servidor: ")
        servidor = session.query(ServidorModel) \
                          .filter_by(id=servidor_id).first()
        cmd = raw_input("Digite o comando a ser executado: ")
        docker = Docker()
        print docker.shell(servidor.nome,cmd)

    def remover(self):
        docker = Docker()
        self.listar()
        servidor_id = input("Digite o ID que deseja remover: ")

        try:
            servidor = session.query(ServidorModel) \
                              .filter_by(id=servidor_id).first()
            docker.remover(servidor.nome)
            session.delete(servidor)
            session.commit()
            print "Servidor removido com sucesso!"
        except Exception as e:
            session.rollback()
            print "Falhou ao remover servidor: ",e
