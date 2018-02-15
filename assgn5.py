import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")
pokedex = connection.PoGoDex
filename = "PoGoDex.json"
filename = open(filename,'r')

for x in filename:
    print x
    break

filename.close()
    
