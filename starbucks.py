# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from random import randint

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Starbucks'

mongo = PyMongo(app)

@app.route('/api/PaloAlto/orders', methods=['POST'])
def post_order():
  starbucks = mongo.db.orders1
  order_id = randint(10000,99999)
  location = request.json['location']
  items = []
  items = request.json['items']
  star_id = starbucks.insert({'order_id':order_id,'location': location, 'items': items})
 
  return ("success")


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
    app.run(debug=True)
