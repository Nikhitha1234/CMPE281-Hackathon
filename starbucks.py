# mongo.py
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import pymongo
from pymongo.errors import (AutoReconnect,
                            ConfigurationError,
                            ConnectionFailure,
                            InvalidOperation,
                            InvalidURI,
                            NetworkTimeout,
                            NotMasterError,
                            OperationFailure)
from random import randint
from pymongo import MongoClient
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Starbucks'
uri = 'mongodb://localhost:27017/Starbucks'
mongo = MongoClient(uri)
  
    
@app.route('/api/PaloAlto/orders', methods=['POST'])
def post_order():
  try:
    starbucks = mongo.db.orders1
    order_id = randint(10000,99999)
    location = request.json['location']
    items = []
    items = request.json['items']
    object_id = starbucks.insert({'order_id':order_id,'location': location, 'items': items})
    return("Successfully inserted") 
  except:
    return "Insert Failed" 
  
@app.route('/api/PaloAlto/orders', methods=['GET'])
def get_all_orders():
  try:
    starbucks = mongo.db.orders1
    output = []
    if starbucks.find().count() != 0:
      for s in starbucks.find():
        output.append({'order_id':s['order_id'],'location': s['location'], 'items': s['items']})
      return jsonify({'result' : output})
    else:
      return "No orders found"
  except:
    result = {}
    result['success'] = False
    result['error'] = "Db connection Failed"
    return "Server error"

@app.route('/api/PaloAlto/order/<int:order_id>', methods=['GET'])
def get_one_order(order_id):
  try:
    starbucks = mongo.db.orders1
    output = []
    if starbucks.find({"order_id":order_id}).count() != 0:
      for s in starbucks.find({"order_id":order_id}):
        output.append({'order_id':s['order_id'],'location': s['location'], 'items': s['items']})
        return jsonify({'result' : output})
    else:
      return "Order ID not found"
  except:
    result = {}
    result['success'] = False
    result['error'] = "Db connection Failed"
    return "Server Error"
@app.route('/api/PaloAlto/order/<int:order_id>', methods=['PUT'])
def put_star(order_id):
  try: 
    starbucks = mongo.db.orders1
    output = []
    location = request.json['location']
    items = []
    items = request.json['items']
    if starbucks.find({"order_id":order_id}).count() != 0:
      star_id = starbucks.update({'order_id':order_id},{"order_id":order_id,"location":request.json['location'],"items":request.json['items']})
      return "success"
    else:
      return "Order ID not found"
  except:
    return "Server Error"
@app.route('/api/PaloAlto/order/<int:order_id>', methods=['DELETE'])
def delete_star(order_id):
  try:
    starbucks = mongo.db.orders1
    starbucks.remove({"order_id":order_id})
    return "success"
  except:
    return "Server Error"

if __name__ == '__main__':
    app.run(debug=True)
