#!/usr/bin/python

#daemon sempre chama o provisionOps para execucao de funcoes

from Classes.service import Service as ServiceClass
from Classes.servicedao import ServiceDao
from Modules.DockerOps import DockerOps

class ProvisionOps:

    def __init__(self,id):
        self.id = id

    def install_service(self):
        service = ServiceClass() #instanciar a classe service
        service.id = self.id 
        servicedao = ServiceDao(service) #instacia servicedao
        service = servicedao.get() #vai no banco e popula o service
#        print service.__dict__ # para debugar os valores..
#        print service.product__dict__ # para debugar os valores..
#        return
        print "Produto %s contratado"%service.product.name
        print "Client: ",service.client.name
        print "Data de Contratacao: %s"%service.request_date
        docker = DockerOps()
        res = docker.create_container(service.id,service.product.image)
        # criar container com id do servico com imagem p. instalacao
