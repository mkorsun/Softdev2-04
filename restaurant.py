import pymongo


def lookupBorough(borough):
    connection = pymongo.MongoClient("homer.stuy.edu")
    db = connection["test"]
    collection = db.restaurants
    restList = collection.find({"borough":borough})
    list = []
    for each in restList:
        list.append(each["name"])          
    return list

def lookupZip(zipcode):
    connection = pymongo.MongoClient("homer.stuy.edu")
    db = connection["test"]
    collection = db.restaurants
    zipList= collection.find({"address.zipcode" :zipcode})
    list = []
    for each in zipList:
        list.append(each["name"])
    return list
    


#print lookupBorough("Bronx")
print lookupZip("11375")        
        
    
