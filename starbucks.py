from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pymongo

from random import randint
from flask.globals import request
app = Flask(__name__)
print('out')
@app.route('/')
def hello_world():
   return 'Welcome to Starbucks'
class Status:
    def __init__(self,status,message):
        self.status = status
        self.message = message
        
def db_conn():
    print('db conn')
    try:
        #app.config['MONGO_DBNAME'] = 'restdb'
        #app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
        #uri = 'mongodb://localhost:27017/Starbucks'
        mongo = MongoClient(host='localhost', port=27017)
        result = mongo.admin.command("ismaster")
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to DB server")
        result = {}
        result['success'] = False
        result['error'] = "Db connection Failed"
        mongo = None
    except pymongo.errors.ServerSelectionTimeoutError as e:
        print("DB server timeout")
        mongo = None
    return mongo

mongo = db_conn()
def checkDbConnection():
    if mongo is None:
        return(False)
    return(True)
  
@app.route('/api/PaloAlto/orders', methods=['POST'])
def post_order():
    conn = checkDbConnection()
    print('post')
    if conn == True:
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
    else:
        result = {}
        result['success'] = False
        result['error'] = "Db connection Failed"
        return "DB is down"
    
    
@app.route('/api/PaloAlto/orders', methods=['GET'])
def get_all_stars():
  print('get all')
  starbucks = mongo.db.orders1
  output = []
  for s in starbucks.find():
    output.append({'order_id':s['order_id'],'location': s['location'], 'items': s['items']})
  return jsonify({'result' : output})

@app.route('/api/PaloAlto/order/<int:order_id>', methods=['GET'])
def get_one_star(order_id):
    conn = checkDbConnection()
    print('get one')
    if conn == True:
        starbucks = mongo.db.orders1
        output = []
        s = None
        for s in starbucks.find({"order_id":order_id}):            
            output.append({'order_id':s['order_id'],'location': s['location'], 'items': s['items']})
            print(s)
        print(s)
        if s == None:
            return 'Order Id doesnt exist'
        else:
            return jsonify({'result' : output})
    else:
        return 'DB is down'

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
