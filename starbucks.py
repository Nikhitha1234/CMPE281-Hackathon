from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify
from flask import request
from pymongo import MongoClient
from random import randint
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Welcome to Starbucks'
class mongo:
  #Connects to Mongo DB
  app.config['MONGO_DBNAME'] = 'restdb'
  app.config['MONGO_URI'] = 'mongodb://54.183.242.172:27017/restdb'
  uri = 'mongodb://54.183.242.172:27017/Starbucks'
  mongo = MongoClient(uri)

#Route for POST request
@app.route('/api/PaloAlto/order/', methods=['POST'])
def post_order():
for s in starbucks.find():
  id = s['order_id']
    if id > maxi_id:
      maxi_id = id
  order_id = maxi_id + 1
  location = request.json['location']
  qty = request.json['qty']
  name = request.json['name']
  milk = request.json['milk']
  size = request.json['size']
  object_id = starbucks.insert({'order_id':order_id,'location': location, 'qty': qty,'name':name,'milk':milk,'size':size})
  return str(order_id)

#Route for GET request for all orders
@app.route('/api/PaloAlto/order/', methods=['GET'])
def get_all_orders():
  starbucks = mongo.db.testt
  output = []
  for s in starbucks.find():
    output.append({'order_id':s['order_id'],'location': s['location'],'qty': s['qty'],'name':s['name'],'milk':s['milk'],'size':s['size']})
  return jsonify(output)

#Route for GET request based on order ID
@app.route('/api/PaloAlto/order/<int:order_id>/', methods=['GET'])
def get_one_order(order_id):
  starbucks = mongo.db.testt
  output = []
  for s in starbucks.find({"order_id":order_id}):
    return jsonify({'order_id':s['order_id'],'location': s['location'],'qty': s['qty'],'name':s['name'],'milk':s['milk'],'size':s['size']})

#Route for PUT request based on order ID
@app.route('/api/PaloAlto/order/<int:order_id>/', methods=['PUT'])
def put_order(order_id):
  starbucks = mongo.db.testt
  output = []
  location = request.json['location']
  qty = request.json['qty']
  name = request.json['name']
  milk = request.json['milk']
  size = request.json['size']
  star_id = starbucks.update({'order_id':order_id},{'order_id':order_id,'location': location,'qty': qty,'name':name,'milk':milk,'size':size})
  for s in starbucks.find({"order_id":order_id}):
    return jsonify({'order_id':s['order_id'],'location': s['location'],'qty': s['qty'],'name':s['name'],'milk':s['milk'],'size':s['size']})

#Route for DELETE request based on order ID
@app.route('/api/PaloAlto/order/<int:order_id>/', methods=['DELETE'])
def delete_order(order_id):
  starbucks = mongo.db.testt
  starbucks.remove({"order_id":order_id})
  return "success"

if __name__ == '__main__':
   app.run('0.0.0.0')
