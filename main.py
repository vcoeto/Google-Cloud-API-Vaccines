import pymongo 
import datetime
myclient = pymongo.MongoClient("mongodb+srv://Victor:ElCacas@cluster0.yoqut.mongodb.net/ProyectoFinal?retryWrites=true&w=majority")
db = myclient.test
mydb = myclient["ProyectoFinal"]
Hospital = mydb["Hospital"]
Gobierno = mydb["Gobierno"]
Reparto = mydb["Reparto"]
Usuario = mydb["Usuario"]

print(myclient.list_database_names())

Hospital_insert = Hospital.insert_many([
    { "_id": 1, "Nombre": "Hospital1", "Username": "Hospital1", "Contraseña":"Hospital1Pass", 
    "Grupo_vacunacion_1a": {"_id": 1, "Mes_inicio": 1, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_1b": {"_id": 2, "Mes_inicio": 4, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2a": {"_id": 3, "Mes_inicio": 7, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2b": {"_id": 4, "Mes_inicio": 10, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0}
    },
    { "_id": 2, "Nombre": "Hospital2", "Username": "Hospital2", "Contraseña":"Hospital2Pass", 
    "Grupo_vacunacion_1a": {"_id": 1, "Mes_inicio": 1, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_1b": {"_id": 2, "Mes_inicio": 4, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2a": {"_id": 3, "Mes_inicio": 7, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2b": {"_id": 4, "Mes_inicio": 10, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0}
    }
    ])


#for x in result: print (x)
print(Hospital_insert.inserted_ids)
myclient.close()