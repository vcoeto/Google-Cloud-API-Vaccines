from flask import Flask, jsonify, request, redirect, render_template, url_for, session, redirect
import pymongo 
from pymongo import MongoClient
import json
from bson import json_util
from flask_pymongo import PyMongo
#Hash de password
import bcrypt
import os
cluster = MongoClient("mongodb+srv://Jorge:cGpoYxUlFA17JUOb@cluster0.yoqut.mongodb.net/ProyectoFinal?retryWrites=true&w=majority")
db = cluster["ProyectoFinal"]
collection = db["Gobierno"]
Hospital = db["Hospital"]
repartos = db["Reparto"]


#template_dir = os.path.abspath('../templates')
app = Flask(__name__)
app.config["MONGO_URI"]="mongodb+srv://Jorge:cGpoYxUlFA17JUOb@cluster0.yoqut.mongodb.net/ProyectoFinal?retryWrites=true&w=majority"

mongo = PyMongo(app)
##############################################################33
#Front-end login

#All the routing in our app will be mentioned here 
#Proyecto final que se encuentra en el URI connect

###Gobierno###
#Default route gobierno
@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    return render_template('index.html')
#db_operations = mongo.db.<Collection_name>
#do_operations = mongo.db.User


#When you press login gobierno
@app.route('/login',methods=['POST'])
def login():
    users=mongo.db.Gobierno
    login_user = users.find_one({'Username': request.form['username']})

    #I the user exists
    if login_user:
        #Compare the encripted password
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),login_user['Password'].encode('utf-8'))== login_user['Password'].encode('utf-8'):
            session['username']=request.form['username']
            return redirect(url_for('index'))
        return 'Er'
    return 'Invalid username/password combination'
#Register
#When you press register gobierno
@app.route('/register', methods=['POST','GET'])
def register():
    if request.method=='POST':
        #Check if it is registered already
        users = mongo.db.Gobierno
        #The 'username appears in the register.html. Pass username and look in database for name
        #'Username' referse to the name column in databae, may need to change that
        existing_user = users.find_one({'Username':request.form['username']})
        #Check if the user does not exist and register it
        if existing_user is None:
            #Hash the password
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            
            #Insert in name username, and password the hash password
            #Since the password is hashed, it becomes a byte object, we need to transform it to string, therefore we decode it
            users.insert({'Municipio': request.form['municipio'], 'Username':request.form['username'], 'Password': hashpass.decode('utf-8'),'Vacunas_Disp': 0, 'Vacunas_utl': 0})
            session['username']=request.form['username']
            return redirect(url_for('index'))
        #Existing user was not none
        return 'That username already exists!'
    
    return render_template('register.html')
###FinalGobierno

###Hospitales###

#Ruta default del hospital, 
@app.route('/hospital')
def index_hospital():
    if 'username' in session:
        return 'You are logged in as hospital ' + session['username']
    return render_template('index_hospital.html')
#db_operations = mongo.db.<Collection_name>
#do_operations = mongo.db.User



#When you press login
@app.route('/login_hospital',methods=['POST'])
def login_hospital():
    users=mongo.db.Hospital
    login_user = users.find_one({'Username': request.form['username']})

    #I the user exists
    if login_user:
        #Compare the encripted password
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),login_user['Password'].encode('utf-8'))== login_user['Password'].encode('utf-8'):
            session['username']=request.form['username']
            return redirect(url_for('index_hospital'))
        return 'Er'
    return 'Invalid username/password combination'


@app.route('/register_hospital', methods=['POST','GET'])
def register_hospital():
    if request.method=='POST':
        #Check if it is registered already
        users = mongo.db.Hospital

        #The 'username appears in the register.html. Pass username and look in database for name
        #'Username' referse to the name column in databae, may need to change that
        existing_user = users.find_one({'Username':request.form['username']})

        #Check if the user does not exist and register it
        if existing_user is None:
            #Hash the password
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())

            #Encuentra al gobierno correspondiente al hospital basado en en nombre del municipio
            gobierno=mongo.db.Gobierno
            gobierno_municipal = gobierno.find_one({'Municipio': request.form['municipio']})

            if gobierno_municipal:
                hosptial = mongo.db.Hospital
                #Insert in name username, and password the hash password
                #Since the password is hashed, it becomes a byte object, we need to transform it to string, therefore we decode it
                Hospital.insert({'Nombre': request.form['hospital'], 'Username':request.form['username'], 'Password': hashpass.decode('utf-8'),'Edad_minima':65,'Vacunas_disponibles':0, 'Vacunas_utilizadas':0,'id_municipal':gobierno_municipal['_id']})
                session['username_hospital']=request.form['username']
                return redirect(url_for('index_hospital'))
            return 'No existe ese municipio'
            #return 'No existe ese gobierno municipal!'
        #Existing user was not none
        return 'That username already exists!'
    
    return render_template('register_hospital.html')

###FinHospitales###


if __name__=='__main__':
    app.secret_key='secretivekey'
    app.run(debug=True)

#End of frontend login
##############################################################################



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
    munc = 'Cuajimalpa' #pedir el municicpio
    filt = {'Municipio': munc}
    add = 2009 #pedir la cantidad de vacunas que se van a restar
    updated_data = {"$min": {'Vacunas_Disp':add}}
    response = collection.update_one(filt, updated_data)
    output = "Updated vacunas restadas"
    return output

#esto debe de pedir a que hospital va y cuantas vacunas recibe y que municicpio las manda
@app.route("/repartir", methods=["POST","GET"])
def reparto():
    hosp = 2
    vac = 123
    repartos.insert_one({'id_Hospital': hosp, 'Vacunas':vac, 'id_Municipal':3, 'estado':'Enviado'}) 
    output = "Repartos funciona"
    return output


@app.route('/register_user', methods=['POST','GET'])
def register_user():
    if request.method=='POST':
        #Check if it is registered already
        users = mongo.db.User

        #The 'username appears in the register.html. Pass username and look in database for name
        #'Username' referse to the name column in databae, may need to change that
        existing_user = users.find_one({'RFC':request.form['rfc']})

        #Check if the user does not exist and register it
        if existing_user is None:
            #Encuentra al gobierno correspondiente al hospital basado en en nombre del municipio
            hospital=mongo.db.Hospital
            nombhosp = hospital.find_one({'Hospital': request.form['Hospital'],'Edad_minima ': request.form['edad']})
        
            if nombhosp:
                add =1
                users.insert({'RFC':request.form['rfc'], 'Edad':request.form['edad'], 'Hospital': request.form['hospital'], 'Vacunado':'S'})
                Hospital.update({"$inc": {'Vacunas apartadas':add}})
                return redirect(url_for('index_hospital'))
            return 'por el momento no estamos vacunando a las personas de su edad'
        #Existing user was not none
        return 'Este usuario ya registro una vacuna'
    
    return render_template('uservacuna.html')

###Fin usuarios registros y aparatado de vacunas ###