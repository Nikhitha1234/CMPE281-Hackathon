from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify
from flask import request
from pymongo import MongoClient
from pymongo.errors import (AutoReconnect,
                            ConfigurationError,
                            ConnectionFailure,
                            InvalidOperation,
                            InvalidURI,
                            NetworkTimeout,
                            NotMasterError,
                            OperationFailure)
from random import randint
from flask.globals import request
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Welcome to Starbucks'
class Status:
    def __init__(self,status,message):
        self.status = status
        self.message = message
try:
  app.config['MONGO_DBNAME'] = 'restdb'
  app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
  uri = 'mongodb://localhost:27017/Starbucks'
  mongo = MongoClient(uri)
except pymongo.errors.ConnectionFailure as e:
    result = {}
    result['success'] = False
    result['error'] = "Db connection Failed"
    print(e)
  
@app.route('/api/PaloAlto/order', methods=['POST'])
def post_order():
  try:
    starbucks = mongo.db.orders1
    maxi_id = 0
    for s in starbucks.find():
        id = s['order_id']
        if id > maxi_id:
            maxi_id = id
    order_id = maxi_id + 1
    location = request.json['location']
    items = []
    items = request.json['items']
    object_id = starbucks.insert({'order_id':order_id,'location': location, 'items': items})
    text = 'Your Order Id is ' + str(order_id)
    return(text)  
  except pymongo.errors.ConnectionFailure as e:
    result = {}
    result['success'] = False
    result['error'] = "Db connection Failed"
    print(e)
    
    
@app.route('/api/PaloAlto/orders', methods=['GET'])
def get_all_stars():
  starbucks = mongo.db.orders1
  output = []
  for s in starbucks.find():
    output.append({'order_id':s['order_id'],'location': s['location'], 'items': s['items']})
  return jsonify({'result' : output})

@app.route('/api/PaloAlto/order/<int:order_id>', methods=['GET'])
def get_one_star(order_id):
  starbucks = mongo.db.orders1
  output = []
  for s in starbucks.find({"order_id":order_id}):
    output.append({'order_id':s['order_id'],'location': s['location'], 'items': s['items']})
  return jsonify({'result' : output})

@app.route('/api/PaloAlto/order/<int:order_id>', methods=['PUT'])
def put_star(order_id):
  starbucks = mongo.db.orders1
  output = []
  location = request.json['location']
  items = []
  items = request.json['items']
  star_id = starbucks.update({'order_id':order_id},{"order_id":order_id,"location":request.json['location'],"items":request.json['items']})
  return "success"

@app.route('/api/PaloAlto/order/<int:order_id>', methods=['DELETE'])
def delete_star(order_id):
  starbucks = mongo.db.orders1
  starbucks.remove({"order_id":order_id})
  return "success"
if __name__ == '__main__':
   app.run()
