#!/usr/bin/python

from Modules.MongoOps import MongoOps
from Modules.ProvisionOps import ProvisionOps

def start():
    mongo = MongoOps()
    queue = mongo.get_queue() # guarda qtdade de servicos
    print "Existem %s servicos na fila"%queue    
    for service in mongo.get_service_to_install(): #td q ainda vai ser instal
        prov = ProvisionOps(int(service.get("_id"))) #marca o id
        res = prov.install_service()#install o(s) id(s) selecionados

if __name__ == '__main__':
    start()

#eh daemon, vai ficar rodando de min em min e depois instala..
