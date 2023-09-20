"""
Title: Reconocimiento Facial - Lib. Face Recognition OpenCV - Video varios rostros por Frame
Reference: https://www.youtube.com/watch?v=51J_bYYMO2k
Author: Frida Cano Falcon
Created on Tue Sep 19 2023
"""
import cv2
import os
import face_recognition
from datetime import datetime
import time

print("[PROCESO] Iniciando programa...")
# Tiempo que toma el programa
start_time = time.time() 
# Carpeta con rostros alumnos registrados
circuloPath = os.path.dirname(os.path.abspath(__file__))
circuloPath = circuloPath + '\\AlumnosData'
circuloPath = circuloPath.replace("\\","/")

# Nombres de los alumnos registrados
f_circulo_encodings = []
f_circulo_names = []
for image_circulo_name in os.listdir(circuloPath):                                                                      # Recorrer la carpeta de las personas de confianza
    image_circulo = cv2.imread("AlumnosData/"+ image_circulo_name)
    #image_circulo = (image_circulo, cv2.COLOR_BGR2RGB)
    f_circulo_locations = face_recognition.face_locations(image_circulo)[0]                                             # Obtiene las coordenadas del rostro en la imagen         
    f_circulo_coding = face_recognition.face_encodings(image_circulo, known_face_locations=[f_circulo_locations])[0]    # Obtenemos las características del rostro encontrado
    f_circulo_encodings.append(f_circulo_coding)
    f_circulo_names.append(image_circulo_name.split(".")[0])

# Cargamos la cámara
print('[PROCESO] Cargando camara...')
cap = cv2.VideoCapture(0)

while True:
    leido, frame = cap.read()
    if not leido:break
    #small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25) # Reduce el tamaño del frame para que sea más rápido el procesamiento
    f_data_locations = face_recognition.face_locations(frame) # Obtiene las coordenadas del rostro en la imagen
    if f_data_locations != []:                                # Si se detecta un rostro
        print("[PROCESO] Rostro detectado")
        face_names = []
        f_frame_codings = face_recognition.face_encodings(frame,f_data_locations)        # Obtenemos las características del rostro encontrado
        for face_encoding in f_frame_codings:                                            # Comparamos el rostro encontrado con los rostros conocidos
            matches = face_recognition.compare_faces(f_circulo_encodings, face_encoding)
            if True in matches:                                                          # Si se reconoce el rostro
                index = matches.index(True)
                name = f_circulo_names[index]
                face_names.append(name)
        for (top, right, bottom, left), name in zip(f_data_locations, face_names):       # Dibujamos un rectángulo alrededor del rostro
            # top *= 4 # Multiplica por 4 el tamaño del frame
            # right *= 4
            # bottom *= 4
            # left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
            cv2.rectangle(frame, (left, bottom -10), (right, bottom), (0,255,0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left +3, bottom -3), font, 0.25, (255,255,255), 1)
    else:
        print("[ALERTA] No se detecto un rostro")
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break
  
# Calculo del tiempo
end_time = time.time() - start_time

cap.release()
print("[PROCESO] Camara liberada")
print("[PROCESO] Tiempo de ejecucion",end_time)
print("[PROCESO] Cerrando programa...")