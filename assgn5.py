from pymongo import MongoClient
import json

#Our connection method works thus
#connect to homer
#create a db called PoGoDex
#make a collection called pokemon

#Data is already a list of dictionaries, so we can directly do insert_many with it


connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.PoGoDex
collection = db.pokemon
filename = "PoGoDex.json"
filename = open(filename)
file = filename.read()
data = json.loads(file)
filename.close()
data = data['pokemon']

collection.insert_many(data)

def find(pokemon):
    return collection.find({"name" : pokemon })

def findid(ID):
    return collection.find({ "id" : ID})

def findevo(evo):
    return collection.find({ "next_evolution.name"  :evo })


    










    
