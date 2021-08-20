import pymongo
from flask import request
from bson.json_util import dumps
from flask_jwt_extended import jwt_required
client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.bqv3q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
buildData = client.buildings.building
roomData = client.borrow.room

def init_app(app):
    @app.route('/builds')
    @jwt_required()
    def buildsGet():
       buildInfo = buildData.find()
       resp = dumps(buildInfo)
       return resp


    @app.route('/rooms')
    @jwt_required()
    def roomGet():
       roomInfo = roomData.find()
       resp = dumps(roomInfo)
       return resp

    @app.route('/rooms',methods=["POST"])
    @jwt_required()
    def roomPost():
       _json = request.json

       _building = _json['building']
       _room = _json['room']
       _date = _json['date']
       _time = _json['time']
      

       roomInfo = roomData.insert_one({
           'building': _building,
           'room': _room,
           'date': _date,
           'time':_time
           
       })
        
       return "insert room ok"
