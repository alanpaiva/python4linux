#!/usr/bin/python
#
# define objeto de conexao com a base
from sqlalchemy import create_engine
# importa os metodos que criam a estrutura do banco
from sqlalchemy.ext.declarative import declarative_base
# importa os metodos para definir a estrutura do banco
from sqlalchemy import Column, Integer, String
# importa o metodo para abrir uma sessao ( transaction )
from sqlalchemy.orm import sessionmaker #Abrir sessao:

# linha que conecta com o banco
engine = create_engine("sqlite:///banco.db")
# instancia do objeto para criar estrutura do banco
Base = declarative_base()
# cria objeto sessionmaker
Session = sessionmaker()
# define em qual banco deve abrir a sessao
Session.configure(bind=engine)
# abre conexao de sessao, ( define o cursor )
session = Session()

class Usuario(Base): #criando tabelas
    __tablename__ = 'usuario' #cria classe
    id = Column(Integer, primary_key=True) #id = primarykey
    nome = Column(String)
    senha = Column(String)
    servidor = relationship("Servidor",secondary=analista_servidor)

class Servidor(Base): #criando tabelas
    __tablename__ = 'servidor' #cria classe
    id = Column(Integer, primary_key=True) #id = primarykey
    nome = Column(String)
    descricao = Column(String)
    ip = Column(String)

if __name__ == '__main__':
    # cria a estrutura do banco:
    Base.metadata.create_all(engine) #uma vez criado, nao cria novamente
    # cria objeto usuario
  #  novo = Usuario()
    # seta valor das colunas:
  #  novo.nome = "Rogerio"
  #  novo.senha = "4linux"
    # faz insert, pega os valores de cima e faz insert:
  #  session.add(novo)
  #  session.commit()

    # faz o select
  #  result = session.query(Usuario).all()
    # print de resultados
  #  for r in result:
  #      print "%s|%s|%s"%(r.id,r.nome,r.senha)
    
    # faz busca de um usuario pelo id
  #  result = session.query(Usuario).filter_by(id=1).first()
  #  print result.id,result.nome,result.senha

    # atualiza dados do usuario (para o ID=1)
  #  result.nome = "Rafael"
  #  session.commit()

    # delete user:
    # busca usuario pelo id igual 3
  #  result = session.query(Usuario).filter(Usuario.id==4).first()
  #  session.delete(result)
  #  session.commit()
