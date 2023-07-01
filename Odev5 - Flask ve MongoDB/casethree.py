from flask import Flask,request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

#cluster = MongoClient("mongodb+srv://@flaskmongodb.puylbab.mongodb.net/")
db = cluster["flaskmongodb"]
collection = db["Users"]


@app.route("/")
def TumKullanicilar():
    users = collection.find()
    result = []
    for user in users:
        result.append({'Isim': user['Name'], 'Yas': user['Age']})
    return {'users': result}, 200
@app.route("/25")
def List():
    users = collection.find({'Age': {'$gt': 25}})
    result = []
    for user in users:
        result.append({'Isim': user['Name'], 'Yas': user['Age']})
    return {'users': result}, 200

@app.route("/adduser", methods=["POST"])
def KullaniciEkle():
    name=request.form['Name']
    age=request.form['Age']
    job=request.form['Job']
    description=request.form['Description']

    user={
        "Name":name,
        "Age":age,
        "Job":job,
        "Description":description
    }
    collection.insert_one(user)

    return "Başarılı bir şekilde kullanıcı eklenmiştir"
@app.route("/deleteuser",methods=["POST","DELETE"])
def KullaniciSil():
    id=request.form['id']
    db['Users'].delete_one({'_id': ObjectId(id)})
    return "Silme İşlemi Başarılı"


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)