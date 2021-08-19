from flask_jwt_extended import jwt_required
from flask.json import jsonify,request
from bson.json_util import dumps
import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.bqv3q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.buildings
collection = db.building
roomData = client.borrow.room


def init_app(app):
    @app.route('/builds')
    #@jwt_required()
    def buildsGet():
       buildInfo = collection.find()
       resp = dumps(buildInfo)
       return resp

def init_app(app):
    @app.route('/rooms')
    #@jwt_required()
    def roomGet():
       roomInfo = roomData.find()
       resp = dumps(roomInfo)
       return resp

def init_app(app):
    @app.route('/rooms',methods=["POST"])
    #@jwt_required()
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

