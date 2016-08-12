#!/usr/bin/python

from modelv2 import session, Servidor as ServidorModel #session cursor
class Servidores:
    id=0
    nome=""
    descricao=""
    ip=""

    def cadastrar(self): #sempre chama o dicionario em funcao da funcao
        self.nome = raw_input("Digite o hostname do server: ")
        self.descricao = raw_input("Digite descricao para o server: ")
        self.ip. = raw_input("Digite IP para o server: ")    

        try:
            s = ServidorModel(self)
            session.add(s)
            session.commit()
            print "Servidor cadastrado com sucesso!"
        except Exception as e:
            session.rollback()
            print "Falhou ao cadastrar servidor: ",e    

    def listar_servidor():
        lista_servidor = session.query(ServidorModel).all()
        for servidor in lista_servidor:
            print "%s %s %s %s"%(servidor.id,servidor.nome,servidor.descricao,servidor.ip)

    def remover_servidor():
        listar_servidor()
        indice = input("Digite o ID que deseja remover: ")
        result = session.query(ServidorModel).filter(ServidorModel.id==indice).first()
        session.delete(result)
        session.commit()
