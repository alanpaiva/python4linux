#!/usr/bin/python

from pymongo import MongoClient

client = MongoClient("127.0.0.1")
db = client["curso_python"]

# PARTE 3 - insert
#db.aulas.insert({"curso":"mongoDB","assunto":"replicacao","aula":5})
#aulas = db.aulas.find()

# PARTE 1 - 
#aulas = db.aulas.find()
#for a in aulas:
#    print a

# PARTE 2 - filtrar
#aulas = db.aulas.find()
#for a in aulas:
#    print a.get("curso"),a.get("assunto")

# PARTE 4 - update
#db.aulas.insert({"curso":"cassandra","assunto":"replicacao","aula":5})
#db.aulas.update({"curso":"mongoDB"},{"$set":{"assunto":"backup"}})
#aulas = db.aulas.find()
#for a in aulas:
#    print a.get("curso"),a.get("assunto")

# PARTE 5 - remover
#db.aulas.insert({"curso":"cassandra","assunto":"replicacao","aula":5})
#db.aulas.update({"curso":"mongoDB"},{"$set":{"assunto":"backup"}})
#db.aulas.remove({"cassandra":""}) ???????
#aulas = db.aulas.find()
#for a in aulas:
#    print a.get("curso"),a.get("assunto")

# PARTE 6 - 
#cursos = {"nome":"python","aulas":[
#                                   {"aula":"basico"},
#                                   {"aula":"estruturas de decisao"},
#                                   {"aula":"funcoes"}
#                                  ]
#         
#         }
#db.aulas.insert(cursos)

# PARTE 7 - add nova aula no dicionario acima

#aula = {"aula":"sqlalchemy"}
#db.aulas.update({"nome":"python"},
#                {"$addToSet":{"aulas":aula}})

# PARTE 8 - remover item da lista
db.aulas.update({"nome":"python"},
                {"@pull":{"aulas":{"aulas":"basico"}}})

