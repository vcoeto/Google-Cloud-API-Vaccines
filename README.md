# TC3041 Proyecto Final Invierno 2021

# *[Vacunando a México]*
---

##### Integrantes:
1. *[Antonio Junco de Haas]* - *[A01339695]* - *[CSF]*
2. *[Victor Coeto]* - *[A01654866]* - *[CSF]*
3. *[Jorge Damian Palacios Hristova]* - *[A01654203]* - *[CSF]*

---
## 1. Aspectos generales

Las orientaciones del proyecto se encuentran disponibles en la plataforma **Canvas**.

Este documento es una guía sobre qué información debe entregar como parte del proyecto, qué requerimientos técnicos debe cumplir y la estructura que debe seguir para organizar su entrega.

### 1.1 Requerimientos técnicos

A continuación se mencionan los requerimientos técnicos mínimos del proyecto, favor de tenerlos presente para que cumpla con todos.

* El equipo tiene la libertad de elegir las tecnologías de desarrollo a utilizar en el proyecto.
* El proyecto debe utilizar al menos dos modelos de bases de datos diferentes, de los estudiados en el curso.
* La arquitectura debe ser modular, escalable, con redundancia y alta disponibilidad.
* La arquitectura deberá estar separada claramente por capas (*frontend*, *backend*, *API RESTful*, datos y almacenamiento).
* Los diferentes componentes del proyecto (*frontend*, *backend*, *API RESTful*, bases de datos, entre otros) deberán ejecutarse sobre contenedores [Docker](https://www.docker.com/) o desplegarse en un servicio en la nube.
* Todo el código, *datasets* y la documentación del proyecto debe alojarse en este repositorio de GitHub siguiendo la estructura que aparece a continuación.

### 1.2 Estructura del repositorio
El proyecto debe seguir la siguiente estructura de carpetas:
```
- / 			        # Raíz de todo el proyecto
    - README.md			# Archivo con los datos del proyecto (este archivo)
    - frontend			# Carpeta con la solución del frontend (Web app)
    - api			# Carpeta con la solución de la API o el backend
    - dbs			# Carpeta con los modelos, catálogos y scripts necesarios para generar las bases de datos
    - docs			# Carpeta con la documentación del proyecto
```

### 1.3 Documentación  del proyecto

Como parte de la entrega final del proyecto, se debe incluir la siguiente información:

* Justificación de los modelo de *bases de datos* que seleccionaron.
* Descripción del o los *datasets* y las fuentes de información utilizadas.
* Guía de configuración, instalación y despliegue de la solución.
* Documentación de la API (si aplica). Puede ver un ejemplo en [Swagger](https://swagger.io/). 
* El código debe estar documentado siguiendo los estándares definidos para el lenguaje de programación seleccionado.

## 2. Descripción del proyecto

* El proyecto vacunanado a México consiste en una aplicación en dónde permite llevar acabo un inventario de las vacunas que se usan por municpio y por hospital en la ciudad de México cada municipio cuenta con un número de vacunas que se 
  distribuyen en los hospitales del mismo através de un reparto que se hacen los hospitales, estos cuenta de la misma manera con un inventario de vacunas que se han utilizado, las vacunas disponibles y las vacunas que han sido apartadas 
  para el grupo de edad que se está vacunando, al igual cómo usuario se presenta la opción de registrarse para apartar la vacuna en el hospital que escoja de su municipio, usando su CURP el usuario solo podrá apartar una vacuna 
  si el hospital esta vacunando a las personas de su edad si no tendrá que esperar a que eso cambie. 

### 2.1 Casos de negocio 
    Para este proyecto se tomaron en cuenta los siguientes casos de negocio:

        * El inicio de sesión de Hospital y Gobierno al igual que el registro de cada uno 
        * El reparto de vacunas por parte del Gobierno hacia los Hospitales de su localidad 
        * Los hospitales tienen un inventario con sus vacunas utilizadas, disponiples ya apartadas y pueden acepatar el reparto que hace el gobierno sumandolas a las vacunas disponibles.
        * Los usuarios tienen la opción de llenar una forma para apartar una vacuna 

## 3. Solución

A continuación aparecen descritos los diferentes elementos que forman parte de la solución del proyecto.


### 3.1 Modelos de *bases de datos* utilizados

* Para la solución de este proyecto se utilizo mongodb para almacenar los gobiernos, hospitales, el reparto que se hace de las vacunas y un registro de los usuarios que hacen un aparatdo de la vacuna, el modelo se presenta a continuación de 
cómo está estructurada la base de datos en la parte de Mongodb :

![(https://github.com/tec-csf/tc3041-pf-invierno-2021-eq2/blob/master/dbs/SchemaMongoDb.jpgs)]

* Se escogió esta base de datos debido  a que es una base de datos NoSQL que es de las más usadas y permite la integración con otras bases de datos, de igual manera permite manejar grandes cantidades de datos y este tipo de base de datos no
  necesita un modelo entidad relación lo cual hace más sencillo a la hora de inserta información en las diferentes colecciones y permite hacer relaciones de mejor forma con las diferentes colecciones y de la misma manera permite hacer consultas optimizadas
  al igual que tiene una gran capacidad de escalabilidad. 
  
* La segunda base de datos que se escogió fue Redis la principal función es mantener la sesión del usuario iniciada durante un tiempo específico, se escogió redis debido a dos facotres lo sencillo que es ingresar una llave valor y crearle un tiempo
  para que expire la sesión y la cierre automáticamente despues de que esa llave expire.  

### 3.2 Arquitectura de la solución

*[Incluya aquí un diagrama donde se aprecie la arquitectura de la solución propuesta, así como la interacción entre los diferentes componentes de la misma.]*

### 3.3 Frontend

*[Incluya aquí una explicación de la solución utilizada para el frontend del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.3.1 Lenguaje de programación
#### 3.3.2 Framework
#### 3.3.3 Librerías de funciones o dependencias

### 3.4 API o backend

*[Incluya aquí una explicación de la solución utilizada para implementar la API del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.4.1 Lenguaje de programación
El lenguaje que se utilizo para la arquitectura se uso Python. 

#### 3.4.2 Framework
El framework que se usa es Flask 

#### 3.4.3 Librerías de funciones o dependencias

* Flask.- el framework de donde vienen las dependecias para hacer la parte web de la aplicación
* jsonify
* request
* redirect
* render_template 
* url_for 
* session 
* MongoClient.-  Conexión con mongodb
* pymongo .- Conexión con mognodb y sus operaciones dentro de él 
* ObjectId
* bycript. - Hash de passwords 
* os 

*[Incluya aquí una explicación de cada uno de los endpoints que forman parte de la API. Cada endpoint debe estar correctamente documentado.]*

## 3.5 Pasos a seguir para utilizar el proyecto

*[Incluya aquí una guía paso a paso para poder utilizar el proyecto, desde la clonación del repositorio hasta el despliegue de la solución en una plataforma en la nube.]*

## 4. Referencias

* Algunos sitios que fueron usados para este proyecto fueron los siguientes: 

* https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/ 

* https://www.youtube.com/watch?v=vVx1737auSE

* https://flask-pymongo.readthedocs.io/en/latest/

* https://dev.to/paurakhsharma/flask-rest-api-part-1-using-mongodb-with-flask-3g7d 



