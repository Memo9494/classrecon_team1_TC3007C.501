import cv2
import os
import time
import face_recognition
import firebase_admin as fa
from firebase_admin import db

''' Conexión con la base de datos en tiempo real - Firebase'''
# Cargar el certificado de mi proyecto Firebase
firebase_sdk = fa.credentials.Certificate('classrecognition-563f7-firebase-adminsdk-jqkoi-bb0e1f5297.json')
# Hacemos referencia a la base de datos en tiempo real de firebase
fa.initialize_app(firebase_sdk, {'databaseURL':'https://classrecognition-563f7-default-rtdb.firebaseio.com/'})

# ------------------- ALUMNOS REGISTRADOS -----------------
print("INFORMACIÓN DE USUARIOS REGISRADOS EN LA BASE DE DATOS")
global database_UsersID, database_circleID, database_circleNames
database_UsersID = []
database_alumnosID = []
database_alumnosNames = []
users = db.reference('/User')
users_childs = users.order_by_key().get()
for key,val in users_childs.items():
    database_UsersID.append(key)
print('Usuarios regstrados: ',database_UsersID)