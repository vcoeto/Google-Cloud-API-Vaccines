import redis
from flask import Flask, jsonify, request, redirect, render_template, url_for, session, redirect
import pymongo 
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
#Hash de password
import bcrypt
import os


host_info = "redis-16819.c124.us-central1-1.gce.cloud.redislabs.com"
r = redis.Redis(host=host_info, port=16819, password='hr4OqiIokxMehjbI12BboBkQmJ36F3TW')

app = Flask(__name__)
app.config["MONGO_URI"]="mongodb+srv://Jorge:cGpoYxUlFA17JUOb@cluster0.yoqut.mongodb.net/ProyectoFinal?retryWrites=true&w=majority"

mongo = PyMongo(app)
 ## pa victor
#app.secret_key='secretivekey'

############## main.py for mongo 
##############################################################
#Front-end login

#All the routing in our app will be mentioned here 
#Proyecto final que se encuentra en el URI connect

###Gobierno###
#Default route gobierno
@app.route('/')
def index():
    if 'username' in session:
        #Lleva al usaro al url /home
        return redirect(url_for('home'))
    return render_template('index.html')

#/home url, muestra a register_reparto.html
@app.route('/home')
def home():
    return 'You are logged in as '+session['username']+render_template('register_reparto.html')

#When you press login gobierno
@app.route('/login',methods=['POST'])
def login():
    users=mongo.db.Gobierno
    login_user = users.find_one({'Username': request.form['username']})

    #If the user exists
    if login_user:
        #Compare the encripted password
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),login_user['Password'].encode('utf-8'))== login_user['Password'].encode('utf-8'):
            session['username']=request.form['username']
            r.setex("prueba", 120, request.form['username'])
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
            r.setex("prueba", 120, request.form['username'])
            return redirect(url_for('index'))
        #Existing user was not none
        return 'That username already exists!'
    
    return render_template('register.html')
###FinalGobierno###

###Hospitales###

#Ruta default del hospital, 
@app.route('/hospital')
def index_hospital():
    if 'username' in session:
        return redirect(url_for('home_hospital'))
        #return 'You are logged in as hospital ' + session['username']
    return render_template('index_hospital.html')

#/home url, muestra /home_hospital.html
@app.route('/home_hospital')
def home_hospital():
    reparto_collection=mongo.db.Reparto
    users = mongo.db.Gobierno
    hospital = mongo.db.Hospital
    reparto = mongo.db.Reparto
    existing_hospital = hospital.find_one({'Username':session['username']})
    existing_user = users.find_one({'Username':session['username']})
    reparto = reparto_collection.find({'id_Hospital':existing_hospital['_id']})
    return 'You are logged in as hospital ' + session['username']+render_template('accept_reparto.html',reparto=reparto,hospital=existing_hospital)


#When you press login
@app.route('/login_hospital',methods=['POST'])
def login_hospital():
    users=mongo.db.Hospital
    login_user = users.find_one({'Username': request.form['username']})

    #If the user exists
    if login_user:
        #Compare the encripted password
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),login_user['Password'].encode('utf-8'))== login_user['Password'].encode('utf-8'):
            session['username']=request.form['username']
            r.setex("prueba", 120, request.form['username'])
            return redirect(url_for('index_hospital'))
        return 'Invalid username/password combination for hospital'
    return 'Invalid username/password combination for hospital'


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
                users.insert({'Nombre': request.form['hospital'], 'Username':request.form['username'], 'Password': hashpass.decode('utf-8'),'Edad_minima':65,'Vacunas_disponibles':0, 'Vacunas_utilizadas':0, 'Vacunas_apartadas': 0,'id_municipal':gobierno_municipal['_id']})
                session['username_hospital']=request.form['username']
                r.setex("prueba", 120, request.form['username'])
                return redirect(url_for('index_hospital'))
            return 'No existe ese municipio'
            #return 'No existe ese gobierno municipal!'
        #Existing user was not none
        return 'That username already exists!'
    
    return render_template('register_hospital.html')

###FinHospitales###


###Users###

@app.route('/register_user', methods=['POST', 'GET'])
def register_user():
    if request.method == 'POST':
        users = mongo.db.User  
        hospital=mongo.db.Hospital
        nombhosp = hospital.find_one({'Nombre': request.form['Hospital']})
        existing_user = users.find_one({'CURP':request.form['CURP']})
        if nombhosp != None and existing_user == None:
            testedad = request.form['Edad']
            testedad = int(testedad)
            if testedad >= nombhosp["Edad_minima"] :
                if nombhosp["Vacunas_disponibles"] > 0:
                    users.insert({'CURP':request.form['CURP'], 'Edad':request.form['Edad'], 'Hospital': request.form['Hospital'], 'Vacunado':'S'})
                    nombhosp['Vacunas_apartadas']= nombhosp['Vacunas_apartadas']+1
                    nombhosp['Vacunas_disponibles']= nombhosp['Vacunas_disponibles']-1
                    hospital.save(nombhosp)
                    return 'updated hospital y created user'

                return 'Ya no quedan vacunas en este hospital'
            return 'Por el momento no estamos vacunando a las personas de su edad'
        return f'<h1>El usuario ya existe o el hospital no existe </h1>'
    return render_template('register_user.html')

#End of frontend login
##############################################################################

###Creacion de repartos###
@app.route('/register_reparto',methods=['POST','GET'])
def register_reparto():
    if request.method=='POST':
        #Check if it is registered already
        users = mongo.db.Gobierno
        hospital = mongo.db.Hospital
        reparto = mongo.db.Reparto
        existing_hospital = hospital.find_one({'Nombre':request.form['hospital']})
        existing_user = users.find_one({'Username':session['username']})
        vacunas_string =request.form['vacunas']
        #DELETE reparto.insert({'id_Hospital': 0, 'Vacunas':request.form['vacunas'], 'id_Municipal': 0,'estado': 'enviado'})
        #Check if the user does not exist and register it
        if existing_hospital:
            lol = r.get("prueba")
            if lol == None:
                return "sesion timeout" + render_template("index.html")
            reparto.insert({'id_Hospital': existing_hospital['_id'], 'Vacunas':request.form['vacunas'], 'id_Municipal': existing_user['_id'],'estado': 'enviado'})

            #reparto.insert({'id_Hospital': existing_hospital['_id'], 'Vacunas':request.form['vacunas'], 'id_Municipal': session['id'],'estado': 'enviado'})
            #DELETE session['username']=request.form['username']
            return redirect(url_for('index'))
        return 'NO EXISTE HOSPITAL'
    return render_template('register_reparto.html')
###Fin creacion de repartos###

@app.route('/accept_reparto/<oid>',methods=['POST','GET'])
def accept_reparto(oid):
    lol = r.get("prueba")
    if lol == None:
        return "sesion timeout" + render_template("index_hospital.html")
    reparto_collection = mongo.db.Reparto
    hospital_collection = mongo.db.Hospital
    reparto=reparto_collection.find_one({'_id':ObjectId(oid)})
    current_hospital = hospital_collection.find_one({'Username':session['username']})
    reparto['estado']="aceptado"
    current_hospital['Vacunas_disponibles']= current_hospital['Vacunas_disponibles']+int(reparto['Vacunas'])
    reparto_collection.save(reparto)
    hospital_collection.save(current_hospital)
    return redirect(url_for('home_hospital'))


#TO DO
@app.route('/main_vacunados')
def main_vacunados():
    lol = r.get("prueba")
    if lol == None:
        return "sesion timeout" + render_template("index_hospital.html")
    users = mongo.db.User
    hospital = mongo.db.Hospital
    current_hospital = hospital.find_one({'Username':session['username']})
    user = users.find({'Hospital':current_hospital['Nombre']})
    return 'You are logged in as hospital ' + session['username']+render_template('main_vacunados.html',user=user,hospital=current_hospital)


#TO DO
@app.route('/accept_vacunados/<oid>',methods=['POST','GET'])
def accept_vacunados(oid):
    lol = r.get("prueba")
    if lol == None:
        return "sesion timeout" + render_template("index_hospital.html")
    user_collection = mongo.db.User
    hospital_collection = mongo.db.Hospital
    user=user_collection.find_one({'_id':ObjectId(oid)})
    current_hospital = hospital_collection.find_one({'Username':session['username']})
    user['Vacunado']='V'
    current_hospital['Vacunas_apartadas']= current_hospital['Vacunas_apartadas']-1
    current_hospital['Vacunas_utilizadas']= current_hospital['Vacunas_utilizadas']+1
    user_collection.save(user)
    hospital_collection.save(current_hospital)
    return redirect(url_for('main_vacunados'))


@app.route('/delete_vacunados/<oid>',methods=['POST','GET'])
def delete_vacunados(oid):
    lol = r.get("prueba")
    if lol == None:
        return "sesion timeout" + render_template("index_hospital.html")
    user_collection = mongo.db.User
    hospital_collection = mongo.db.Hospital
    user=user_collection.find_one({'_id':ObjectId(oid)})
    current_hospital = hospital_collection.find_one({'Username':session['username']})
    current_hospital['Vacunas_apartadas']= current_hospital['Vacunas_apartadas']-1
    current_hospital['Vacunas_disponibles']= current_hospital['Vacunas_disponibles']+1
    user_collection.delete_one(user)
    hospital_collection.save(current_hospital)
    return redirect(url_for('main_vacunados'))

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

if __name__=='__main__':
    app.secret_key='secretivekey'
    app.run(debug=True)
