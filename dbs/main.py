import pymongo 
import datetime
myclient = pymongo.MongoClient("mongodb+srv://Jorge:cGpoYxUlFA17JUOb@cluster0.yoqut.mongodb.net/ProyectoFinal?retryWrites=true&w=majority")
#myclient = pymongo.MongoClient("mongodb+srv://Victor:ElCacas@cluster0.yoqut.mongodb.net/ProyectoFinal?retryWrites=true&w=majority")
db = myclient.test
mydb = myclient["ProyectoFinal"]
Hospital = mydb["Hospital"]
Gobierno = mydb["Gobierno"]
Reparto = mydb["Reparto"]
Usuario = mydb["Usuario"]

print(myclient.list_database_names())

Hospital_insert = Hospital.insert_many ([
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
    },
    { "_id": 3, "Nombre": "Hospital3", "Username": "Hospital3", "Contraseña":"Hospital3Pass", 
    "Grupo_vacunacion_1a": {"_id": 1, "Mes_inicio": 1, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_1b": {"_id": 2, "Mes_inicio": 4, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2a": {"_id": 3, "Mes_inicio": 7, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2b": {"_id": 4, "Mes_inicio": 10, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0}
    },
    { "_id": 4, "Nombre": "Hospital4", "Username": "Hospital4", "Contraseña":"Hospital4Pass", 
    "Grupo_vacunacion_1a": {"_id": 1, "Mes_inicio": 1, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_1b": {"_id": 2, "Mes_inicio": 4, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2a": {"_id": 3, "Mes_inicio": 7, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2b": {"_id": 4, "Mes_inicio": 10, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0}
    },
    { "_id": 5, "Nombre": "Hospital5", "Username": "Hospital5", "Contraseña":"Hospital5Pass", 
    "Grupo_vacunacion_1a": {"_id": 1, "Mes_inicio": 1, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_1b": {"_id": 2, "Mes_inicio": 4, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2a": {"_id": 3, "Mes_inicio": 7, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2b": {"_id": 4, "Mes_inicio": 10, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0}
    },
    { "_id": 6, "Nombre": "Hospital6", "Username": "Hospital6", "Contraseña":"Hospital6Pass", 
    "Grupo_vacunacion_1a": {"_id": 1, "Mes_inicio": 1, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_1b": {"_id": 2, "Mes_inicio": 4, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2a": {"_id": 3, "Mes_inicio": 7, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2b": {"_id": 4, "Mes_inicio": 10, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0}
    },
    { "_id": 7, "Nombre": "Hospital7", "Username": "Hospital7", "Contraseña":"Hospital7Pass", 
    "Grupo_vacunacion_1a": {"_id": 1, "Mes_inicio": 1, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_1b": {"_id": 2, "Mes_inicio": 4, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2a": {"_id": 3, "Mes_inicio": 7, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2b": {"_id": 4, "Mes_inicio": 10, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0}
    },
    { "_id": 8, "Nombre": "Hospital8", "Username": "Hospital8", "Contraseña":"Hospital8Pass", 
    "Grupo_vacunacion_1a": {"_id": 1, "Mes_inicio": 1, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_1b": {"_id": 2, "Mes_inicio": 4, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2a": {"_id": 3, "Mes_inicio": 7, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2b": {"_id": 4, "Mes_inicio": 10, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0}
    },
    { "_id": 9, "Nombre": "Hospital9", "Username": "Hospital9", "Contraseña":"Hospital9Pass", 
    "Grupo_vacunacion_1a": {"_id": 1, "Mes_inicio": 1, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_1b": {"_id": 2, "Mes_inicio": 4, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2a": {"_id": 3, "Mes_inicio": 7, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2b": {"_id": 4, "Mes_inicio": 10, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0}
    },
    { "_id": 10, "Nombre": "Hospital10", "Username": "Hospital10", "Contraseña":"Hospital10Pass", 
    "Grupo_vacunacion_1a": {"_id": 1, "Mes_inicio": 1, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_1b": {"_id": 2, "Mes_inicio": 4, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2a": {"_id": 3, "Mes_inicio": 7, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0},
    "Grupo_vacunacion_2b": {"_id": 4, "Mes_inicio": 10, "Vacunas_disponibles": 0, "Vacunas_utilizadas": 0, "Vacunas_apartadas":0}
    }
    ])

Gobierno_insert = Gobierno.insert_many ([
        {
         "_id": 1,
         "Municipio": "Benito juárez",
         "Username":"El beno",
         "Password":"Elcacas",
         "Vacunas-Disp":0,
         "Vacunas-utl":0
    
     },

     {
        "_id": 2,
        "Municipio": "Cuajimalpa",
        "Username":"Cuajim",
        "Password":"Elansioso",
        "Vacunas-Disp":0,
        "Vacunas-utl":0
   
    },

    {
        "_id": 3,
        "Municipio": "Álvaro Obregón",
        "Username":"Obre",
        "Password":"ElcacasTu",
        "Vacunas-Disp":0,
        "Vacunas-utl":0
   
    },

    {
        "_id": 4,
        "Municipio": "Magdalena Contreras",
        "Username":"Mag",
        "Password":"ElcacasTu",
        "Vacunas-Disp":0,
        "Vacunas-utl":0
   
    }
])



#for x in result: print (x)
print(Gobierno_insert.inserted_ids)
myclient.close()