#!/usr/bin/python
#
# define objeto de conexao com a base
from sqlalchemy import create_engine
# importa os metodos que criam a estrutura do banco
from sqlalchemy.ext.declarative import declarative_base
# importa os metodos para definir a estrutura do banco
from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime
# importa o metodo para abrir uma sessao ( transaction )
from sqlalchemy.orm import sessionmaker, relationship #Abrir sessao:
from random import randint
from datetime import datetime

# linha que conecta com o banco
#engine = create_engine("sqlite:///banco.db") 
    #substituir String255 -> String
#engine = create_engine("postgresql://loja:4linux@localhost/loja2")       
    #substituir String255 -> String
engine = create_engine("mysql://loja:4linux@localhost/loja2")
# instancia do objeto para criar estrutura do banco
Base = declarative_base()
# cria objeto sessionmaker
Session = sessionmaker()
# define em qual banco deve abrir a sessao
Session.configure(bind=engine)
# abre conexao de sessao, ( define o cursor )
session = Session()

usuario_servidor = Table('usuario_servidor', #nome tabela q ficara no banco
                         Base.metadata, # cria a tabela dentro do bancoo
                       Column('usuario_id',Integer,ForeignKey('usuario.id')),
                       #coluna tipo inteiro chave estrangeira usuario
                       Column('servidor_id',Integer,ForeignKey('servidor.id'))
                       #coluna tipo inteiro chave estrangeira servidor
                         )

class Usuario(Base): #criando tabelas
    __tablename__ = 'usuario' #cria classe
    id = Column(Integer, primary_key=True) #id = primarykey
    nome = Column(String(255))
    senha = Column(String(255))
    servidor = relationship("Servidor",secondary=usuario_servidor)
    #tem relacionamento com o Servidor abaixo
    token = relationship("Token")

    def __init__(self,usuario_cls): #cls abreviacao de class
        print "Executando construtor de: ",__name__
        self.nome = usuario_cls.login
        self.senha = usuario_cls.senha
    

class Servidor(Base): #criando tabelas
    __tablename__ = 'servidor' #cria classe
    id = Column(Integer, primary_key=True) #id = primarykey
    nome = Column(String(255))
    descricao = Column(String(255))
    ip = Column(String(255))

    def __init__(self,servidor_cls): #cls abreviacao de class
        print "Executando construtor de: ",__name__
        self.nome = servidor_cls.nome
        self.descricao = servidor_cls.descricao
        self.ip = servidor_cls.ip

class Token(Base):
    __tablename__ = 'token'
    id = Column(Integer,primary_key=True)
    usuario_id = Column(Integer,ForeignKey("usuario.id"))
    servidor_id = Column(Integer,ForeignKey("servidor.id"))
    token = Column(String(255),default=str(randint(1000,9999)))
    motivo = Column(String(255),nullable=False)
    data = Column(DateTime,default=datetime.now())
    servidor = relationship("Servidor")
    usuario = relationship("Usuario")


if __name__ == '__main__':
    # cria a estrutura do banco:
    Base.metadata.create_all(engine) #uma vez criado, nao cria novamente
    novo_token = Token()
    novo_token.motivo = "Atualizacao de seguranca do servidor"
    usuario = session.query(Usuario).filter_by(id=2).first()
    usuario.token.append(novo_token)
    servidor = session.query(Servidor).filter_by(id=1).first()
    novo_token.servidor = servidor
    session.add(novo_token)
    session.commit()

# Soh para mostrar os IDS:
#    usuarios_todos = session.query(Usuario).all()
#    for u in usuarios_todos:
#        print u.id, u.nome

#    servidores_todos = session.query(Servidor).all()
#    for u in servidores_todos:
#        print u.id, u.nome

# Efetuando a amarracao entre eles.
    usuarios_todos = session.query(Usuario).filter_by(id=3).first()
    servidores_todos = session.query(Servidor).filter_by(id=2).first()

    usuarios_todos.servidor.append(servidores_todos)
    session.commit()


