import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection["test"]
collection = db.restaurants

def lookupBorough(borough):
    restList = collection.find({"borough":borough})
    l = []
    for each in restList:
        l.append(each["name"])          
    return l
    return restList

def lookupZip(zipcode):
    zipList= collection.find({"address.zipcode" :zipcode})
    l = []
    for each in zipList:
        l.append(each["name"])
    return l

def lookupZipGrade(zipcode, grade):
    zipList = collection.find({"address.zipcode" : zipcode, "grades.grade": grade})
    l = []
    for each in zipList:
        l.append(each["name"])
    return l

def lookupZipBelowScore(zipcode, score):
    zipList = collection.find({"address.zipcode" : zipcode, "grades.score": {"$lt": score}})
    l = []
    for each in zipList:
        l.append(each["name"])
    return l

def lookupSubstringOfName(name):
    restList = collection.find({"name": {"$regex": name, "$options": "i"}})
    l = []
    for each in restList:
        l.append(each["name"])
    return l

print lookupBorough("Bronx")[:4]
print lookupZip("11375")[:4]        
print lookupZipGrade("11375", "A")[:4]       
print lookupZipBelowScore("11375", 10)[:4]       
print lookupSubstringOfName("diner")[:4]       
    
