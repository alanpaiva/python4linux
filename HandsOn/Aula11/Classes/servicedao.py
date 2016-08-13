#!/usr/bin/python

from Classes.product import Product as ProductClass
from Classes.service import Service as ServiceClass
from Classes.client import Client as ClientClass
from model import Service as ServiceModel, Client as ClientModel, Product as ProductModel, session

class ServiceDao:
    def __init__(self,service=""):
        self.service = service

    def get(self):
        try:
            service = session.query(ServiceModel,ClientModel,ProductModel) \
                             .join(ClientModel,ProductModel) \
                             .filter(ServiceModel.id==self.service.id) \
                             .first()
            if not service:
                return None
            else:
                client = ClientClass(service.Client.name,
                                     service.Client.cpf,
                                     service.Client.segment)
                product = ProductClass(service.Product.name,
                                     service.Product.description,
                                     service.Product.image)
                serv = ServiceClass(service.Service.id,
                                     client, 
                                     product, 
                                     service.Service.request_date,
                                     service.Service.cancel_date)
                return serv
        except Exception as e:
            print "Falhou ao buscar servico: ",e
