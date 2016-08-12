#!/usr/bin/python

from modelv2 import session, Usuario as UsuarioModel #session cursor
class Usuarios:
    id = 0    
    login = ""
    senha = ""    
    
    def cadastrar(self): #sempre chama o dicionario em funcao da funcao
        self.login = raw_input("Digite o login do usuario: ")
        self.senha = raw_input("Digite sua senha: ")
        try:
            u = UsuarioModel(self)
            session.add(u)
            session.commit()
            print "Usuario cadastrado com sucesso!"
    
        except Exception as e:
            session.rollback()
            print "Falhou ao cadastrar usuario: ",e
    
    def listar(self):
        lista_usuario = session.query(UsuarioModel).all()
        for usuario in lista_usuario:
            print "%s -%s"%(usuario.id,usuario.nome)

    def remover(self):
        self.listar()
        indice = input("Digite o ID que deseja remover: ")
        result = session.query(UsuarioModel).filter(UsuarioModel.id==indice).first()
        session.delete(result)
        session.commit()

