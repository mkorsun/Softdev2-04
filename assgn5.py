from pymongo import MongoClient
import json

#Our connection method works thus
#connect to homer
#create a db called PoGoDex
#make a collection called pokemon

#Dataset is already a list of dictionaries, so we can directly do insert_many with it
#Downloaded from https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
#Contains stats and info of all Pokemon

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


    










    
