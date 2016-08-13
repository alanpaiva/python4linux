#!/usr/bin/python

from pymongo import MongoClient

class MongoOps:
    def __init__(self):
        self.client = MongoClient("127.0.0.1")
        self.db = self.client["dexterops"]

    def get_queue(self):
        return self.db.queue.find({"status":0}).count()

    def get_service_to_install(self):
        # status = 0 (pendente a instalacao)
        # status = 1 (instalacao em andamento)
        # status = 2 (pendente a remocao)
        return self.db.queue.find({"status":0})
