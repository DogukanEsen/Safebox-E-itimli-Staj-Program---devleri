import pymongo
from pymongo import MongoClient
import random


#cluster = MongoClient("mongodb+srv://@flaskmongodb.puylbab.mongodb.net/")

db = cluster["flaskmongodb"]
collection = db["Users"]
# Users collectionında tüm verileri getiren sorgu
for i in collection.find():
     print(i)
# Users collectionında belirlediğiniz isimdeki kişiyi getiren (İsmi Ahmet olanları getir) sorgu
for i in collection.find({"Name": "Ad1"}):
     print(i)
# Users collectionında yaşı 20'den fazla olanları getiren sorgu
for i in collection.find({"Age": {"$gt": 20}}):
    print(i)
# Users collectionında yaşı 25'den fazla olanların description'ı 0 olacak.
collection.update_many(
    {"Age": {"$gt": 25}},
    {"$set": {"Description": 0}}
)
for i in collection.find({"Age": {"$gt": 25}}):
    print(i)
# Users collectionında yaşı 45-48 yaş aralığında olan kişileri silen sorgu
for i in collection.find({"Age": {"$gte": 45, "$lte": 48}}):
    print(i)
collection.delete_many({"Age": {"$gte": 45, "$lte": 48}})
print("-------------------")
for i in collection.find({"Age": {"$gte": 45, "$lte": 48}}):
    print(i)

