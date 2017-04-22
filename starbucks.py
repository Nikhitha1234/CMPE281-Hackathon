from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
import pymongo

from random import randint
from flask.globals import request


import logging
try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS

except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS


app = Flask('FlaskCorsAppBasedExample')
logging.basicConfig(level=logging.INFO)
# To enable logging for flask-cors,
logging.getLogger('flask_cors').level = logging.DEBUG
#app = Flask(__name__)
CORS(app)
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
        mongo = MongoClient(host='54.183.242.172', port=27017)
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
        print(mongo)
        return(False)
    return(True)
  
@app.route('/api/PaloAlto/order', methods=['POST'])
def post_order():
    conn = checkDbConnection()

    print('post')
    if conn == True:
            starbucks = mongo.db.orders
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
  starbucks = mongo.db.orders
  output = []
  for s in starbucks.find():
    output.append({'order_id':s['order_id'],'location': s['location'],'qty': s['qty'],'name':s['name'],'milk':s['milk'],'size':s['size']})
  return jsonify({'result' : output})

@app.route('/api/PaloAlto/order/<int:order_id>', methods=['GET'])
def get_one_star(order_id):
    conn = checkDbConnection()
    print('get one')
    if conn == True:
        starbucks = mongo.db.orders
        output = []
        s = None
        for s in starbucks.find({"order_id":order_id}):            
            output.append({'order_id':s['order_id'],'location': s['location'], 'qty': s['qty'],'name':s['name'],'milk':s['milk'],'size':s['size']})
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
  starbucks = mongo.db.orders
  output = []
  location = request.json['location']
  qty = request.json['qty']
  name = request.json['name']
  milk = request.json['milk']
  size = request.json['size']
  star_id = starbucks.update({'order_id':order_id},{"order_id":order_id,"location":request.json['location'],"qty":request.json['qty'],"name":request.json['name'],"milk":request.json['milk'],"size":request.json['size']})
  return "success"

@app.route('/api/PaloAlto/order/<int:order_id>', methods=['DELETE'])
def delete_star(order_id):
  starbucks = mongo.db.orders
  starbucks.remove({"order_id":order_id})
  return "success"
#if __name__ == '__main__':
#   app.run('0.0.0.0')

if __name__ == '__main__':
    BaseHTTPServer.test(CORSRequestHandler, BaseHTTPServer.HTTPServer)
