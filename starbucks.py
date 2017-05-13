from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify
from flask import request
from pymongo import MongoClient
from random import randint
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def welcome():
   return 'Welcome to Starbucks'
#Coapp.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://54.175.140.152:27017/'
uri = 'mongodb://54.175.140.152:27017/StarBucksOrders'
mongo = MongoClient(uri)

#Route for POST request
@app.route('/api/PaloAlto/order/', methods=['POST'])
def post_order():
  starbucks = mongo.db.StarBucksOrders
  maxi_id = 0
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
  starbucks = mongo.db.StarBucksOrders
  output = []
  for s in starbucks.find():
    output.append({'order_id':s['order_id'],'location': s['location'],'qty': s['qty'],'name':s['name'],'milk':s['milk'],'size':s['size']})
  return jsonify(output)

#Route for GET request based on order ID
@app.route('/api/PaloAlto/order/<int:order_id>', methods=['GET'])
def get_one_order(order_id):
  starbucks = mongo.db.StarBucksOrders
  output = []
  for s in starbucks.find({"order_id":order_id}):
    return jsonify({'order_id':s['order_id'],'location': s['location'],'qty': s['qty'],'name':s['name'],'milk':s['milk'],'size':s['size']})

#Route for PUT request based on order ID
@app.route('/api/PaloAlto/order/<int:order_id>', methods=['PUT'])
def put_order(order_id):
  starbucks = mongo.db.StarBucksOrders
  output = []
  location = request.json['location']
  qty = request.json['qty']
  name = request.json['name']
  milk = request.json['milk']
  size = request.json['size']
  object_id = starbucks.update({'order_id':order_id},{'order_id':order_id,'location': location,'qty': qty,'name':name,'milk':milk,'size':size})
  for s in starbucks.find({"order_id":order_id}):
    print("a")
    return jsonify({'order_id':s['order_id'],'location': s['location'],'qty': s['qty'],'name':s['name'],'milk':s['milk'],'size':s['size']})

#Route for DELETE request based on order ID
@app.route('/api/PaloAlto/order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
  starbucks = mongo.db.StarBucksOrders
  starbucks.remove({"order_id":order_id})
  return "success"

if __name__ == '__main__':
   app.run('0.0.0.0')
                       
