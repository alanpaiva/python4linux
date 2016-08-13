#!/usr/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

engine = create_engine("sqlite:///banco.db")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class Client(Base):
    __tablename__ = "client"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    cpf = Column(String)
    segment = Column(String)
    service = relationship("Service")

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)

class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer,primary_key=True)
    client_id = Column(Integer,ForeignKey("client.id"))
    product_id = Column(Integer,ForeignKey("product.id"))
    request_date = Column(DateTime,default=datetime.now())
    cancel_date = Column(DateTime)
    client = relationship("Client")
    product = relationship("Product")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    c = Client()
    c.name = "Alan"
    c.cpf = "111.111.111-11"
    c.segment = "Tecnologia"
    p = Product()
    p.name = "Hospedagem"
    p.description = "Hospedagem Compartilhada"
    p.image = "Ubuntu_Hosting"
    session.add(c) #gera ids p. relacionar com service
    session.add(p) #gera ids p. relacionar com service
    s = Service()
    c.service.append(s) #add servico ao cliente
    s.product = p 
    session.add(s)
    session.commit()









