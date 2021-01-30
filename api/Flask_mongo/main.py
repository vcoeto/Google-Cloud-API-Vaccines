from flask import Flask
import pymongo 
from pymongo import MongoClient
import json
from bson import json_util

cluster = MongoClient("mongodb+srv://Jorge:cGpoYxUlFA17JUOb@cluster0.yoqut.mongodb.net/ProyectoFinal?retryWrites=true&w=majority")
db = cluster["ProyectoFinal"]
collection = db["Gobierno"]
Hospital = db["Hospital"]

app = Flask(__name__)

@app.route("/gobierno",methods = ["GET"])
def get_gobiernos():
    all_gobiernos = list(collection.find({}))
    return json.dumps(all_gobiernos, default=json_util.default)

from flask import Flask, jsonify
from pymongo import MongoClient
import json
from bson import json_util



@app.route('/gobiernos',methods = ['GET'])
def get_gobiernos():
    filt = {'_id': 1}
    users = collection.find(filt)
    output = [{'_id': user['_id'],
    'Municipio': user['Municipio'],
    'Username' : user['Username'],
    'Password': user['Password'],
    'Vacunas-Disp': user['Vacunas-Disp'],
    'Vacunas-utl': user['Vacunas-utl']
    }
    for user in users
    ]


    return jsonify(output)
@app.route("/addvacunas",methods=["POST","GET"])
def update_vacunas():
    filt = {'Municipio': 'Cuajimalpa'} #pedir el municicpio
    add = 2009 #pedir la cantidad de vacunas que se van a agregar 
    updated_data = {"$inc": {'Vacunas_Disp':add}}
    response = collection.update_one(filt, updated_data)
    output = "Updated"
    return output

@app.route("/remvacunas",methods=["POST","GET"])
def rem_vacunas():
    filt = {'Municipio': 'Cuajimalpa'} #pedir el municicpio
    add = 2009 #pedir la cantidad de vacunas que se van a restar
    updated_data = {"$min": {'Vacunas_Disp':add}}
    response = collection.update_one(filt, updated_data)
    output = "Updated vacunas restadas"
    return output