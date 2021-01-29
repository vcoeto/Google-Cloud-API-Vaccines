from flask import Flask
import pymongo 
from pymongo import MongoClient
import json
from bson import json_util

cluster = MongoClient("mongodb+srv://Jorge:cGpoYxUlFA17JUOb@cluster0.yoqut.mongodb.net/ProyectoFinal?retryWrites=true&w=majority")
db = cluster["ProyectoFinal"]
collection = db["Gobierno"]

app = Flask(__name__)

@app.route("/gobierno",methods = ["GET"])
def get_gobiernos():
    all_gobiernos = list(collection.find({}))
    return json.dumps(all_gobiernos, default=json_util.default)