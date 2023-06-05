import pymongo
from pymongo import MongoClient
import random


#cluster = MongoClient("mongodb+srv://@flaskmongodb.puylbab.mongodb.net/")

db = cluster["flaskmongodb"]
collection = db["Users"]

data1 = []

for i in range(50):
    name = "Ad" + str(i+1)
    age = random.randint(0, 50)
    job = "Is" + str(i+1)
    description = 1

    temp = {
        'Name':name,
        'Age': age,
        'Job': job,
        'Description': description
    }
    data1.append(temp)

collection.insert_many(data1)