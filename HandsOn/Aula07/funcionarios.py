#!/usr/bin/python
#
# define objeto de conexao com a base
from sqlalchemy import create_engine
# importa os metodos que criam a estrutura do banco
from sqlalchemy.ext.declarative import declarative_base
# importa os metodos para definir a estrutura do banco
from sqlalchemy import Column, Integer, String, ForeignKey #chave estrangeira sempre vai ser o ID de outra tabela.
# importa o metodo para abrir uma sessao ( transaction )
from sqlalchemy.orm import sessionmaker, relationship #Abrir sessao:

engine = create_engine("sqlite:///banco.db")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class Funcionario(Base): 
    __tablename__ = 'funcionario' #tabela pai 1)
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    dependente = relationship("Dependente") 
    #nao eh um campo da tabela, somente para mapear.

class Dependente(Base): #nome da classe sempre inicia com maiuscula
    __tablename__ = 'dependente' #tabela filha N)
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    funcionario_id = Column(Integer,ForeignKey("funcionario.id"))
    # padrao sqlalchemy nome da tabela_id
    # sempre recebe a chave estrangeira (FK)

if __name__ == '__main__':
    Base.metadata.create_all(engine) #cria as tabelas no banco

# PARTE 1
#    # criando funcionario
#    antonio = Funcionario()
#    antonio.nome = "Antonio"
#    # criando dependende
#    haroldo = Dependente()
#    haroldo.nome = "Haroldo"
#    # adiciona dependente
#    antonio.dependente.append(haroldo)
#    session.add(antonio)
#    session.add(haroldo)
#    session.commit()

# PARTE 2
#    # Buscando funcionario
#    funcionario = session.query(Funcionario).filter_by(id=1).first()
#    # Criando dependente
#    dependente = Dependente()
#    dependente.nome = "Maria"
#    # adiciona dependente
#    funcionario.dependente.append(dependente)
#    session.add(dependente)
#    session.commit()

    # Buscando funcionario
    result = session.query(Funcionario,Dependente) \
                         .join(Dependente) \
                         .filter(Funcionario.id==1).first()
                        # .first nao traz como lista
    print "Funcionario: ",result.Funcionario.nome
    for d in result.Funcionario.dependente:
        print "Dependente: ",d.nome

    # Remover dependente (listar e remover como qualquer outro dado:
    # removeu o dependente: Haroldo
#    dependente = session.query(Dependente).filter_by(id=1).first()
#    session.delete(dependente)
#    session.commit()
