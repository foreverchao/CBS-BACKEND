from flask.json import jsonify
import pymongo
from bson.objectid import ObjectId
from pymongo import collection
from bson.json_util import dumps

client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.bqv3q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.website
collection = db.members

def getOneUserLoginInfo(email,password):
    user = collection.find_one({'email' :email,'password' : password})
    resp = dumps(user)
    return resp


def addOneUser(_email,_password):
    user = collection.insert_one({
        'email':_email,
        'password':_password
    })
    resp = jsonify("user add success")
    return resp

def getAllUserInfo():
    users = collection.find()
    resp = dumps(users)
    #print (doc)
        #print (userdata[0])
    return resp

def getOneUserInfo(id):
    user = collection.find_one({'_id' :ObjectId(id)})
    resp = dumps(user)
    return resp

def delOneUser(id):
    collection.delete_one({'_id' :ObjectId(id)})
    resp = jsonify("user delete success")
    return resp