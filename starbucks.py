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

@app.route('/api/PaloAlto/order/<order_id>', methods=['GET'])

def get_one_star(order_id):
  
  starbucks = mongo.db.orders1
  s = starbucks.find_one({'order_id' : order_id})
  print('_____________________________________________')
  
  output = {'order_id':s['order_id'],'location': s['location'], 'items': s['items']}
  if s:
    return jsonify({'result':output})
  else:
    output = "No such name"
  return jsonify({'result' : output})



if __name__ == '__main__':
    app.run(debug=True)
