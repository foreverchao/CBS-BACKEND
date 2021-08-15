from flask import Flask,request,jsonify
from mongo_practice import getAllUserInfo,getOneUserInfo,delOneUser,addOneUser,getOneUserLoginInfo
from bson.json_util import dumps
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required




app = Flask(__name__)
app.secret_key = "secreatkey"
app.config['MONGO_URI'] = ""
CORS(app)
jwt = JWTManager()
app.config['JWT_SECRET_KEY'] = 'this-should-be-change'
jwt.init_app(app)
#def home():
    #return "Hello Flask health ok"

@app.route("/")
def index():
    return 'hellth ok'

@app.route('/login', methods=['POST'])
def login(): 
    email = request.json.get('email', None) 
    password = request.json.get('password', None) 
    resp = getOneUserLoginInfo(email,password)
    if resp == "null":
        return jsonify({"msg": "this account is null !"}), 401
    
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

@app.route('/userlogin', methods=['GET'])
def userlogin(): 
    _json = request.json
    _email = _json['email']
    _password = _json['password']
    resp = getOneUserLoginInfo(_email,_password)
    if resp == "null":
        return jsonify({"msg": "this account is null !"})
    return resp
    
@app.route("/add",methods=["POST"])
def add_user():
    _json = request.json
    _email = _json['email']
    _password = _json['password']
    #if _email and _password and request.method == 'POST':
    resp = addOneUser(_email,_password)
    return resp
    
@app.route("/users")
@jwt_required()
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