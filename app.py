from flask import Flask,jsonify,request
from mongo_practice import getAllUserInfo,getOneUserInfo,delOneUser,addOneUser
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from werkzeug.security import generate_password_hash,check_password_hash
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = "secreatkey"
app.config['MONGO_URI'] = ""
CORS(app)
#def home():
    #return "Hello Flask health ok"

@app.route("/")
def index():
    return 'hellth ok'
    
@app.route("/add",methods=["POST"])
def add_user():
    _json = request.json
    _email = _json['email']
    _password = _json['password']
    #if _email and _password and request.method == 'POST':
    resp = addOneUser(_email,_password)
    return resp
    
@app.route("/users")
def users():
    users = getAllUserInfo()
    #print(data)
    return users


@app.route("/user/<id>")
def user(id):
    user = getOneUserInfo(id)
    return user

@app.route("/delete/<id>",methods=['DELETE'])
def delete_user(id):
    userDelete = delOneUser(id)
    return userDelete

if __name__ == "__main__":
    app.run(debug=False)