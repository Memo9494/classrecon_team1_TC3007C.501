

"""
Title: Reconocimiento Facial - Lib. Face Recognition OpenCV - Video varios rostros por Frame
Reference: https://www.youtube.com/watch?v=51J_bYYMO2k
Author: Frida Cano Falcon
Created on Tue Sep 19 2023
"""
import cv2
import os
import face_recognition
import time
import numpy as np

print("[PROCESO] Iniciando programa...")
# Indicadores de tiempo
start_time = round(time.time(),2)  # tiempo de incio de programa
time_limit = 120.0                 # Limite de tiempo para tomar una participacion

# Conteo de FPS
fps = 0
frame_count = 0
start_time_fps = start_time

# Nombres de los alumnos registrados
f_circulo_encodings = []
f_circulo_names = []

''' Extraer los encodings de un CSV de los alumnos registrados '''
circuloPath = os.path.dirname(os.path.abspath(__file__))
circuloPath = circuloPath + '\\encodings.txt'
circuloPath = circuloPath.replace("\\","/")
with open(circuloPath, "r") as file:
    for line in file.readlines():
        # Separar el nombre y los encodings usando la coma como delimitador
        parts = line.strip().split(",")
        name = parts[0]
        encoding_str = parts[1:]

        # Convertir los encodings de strings a flotantes
        encoding = [float(x) for x in encoding_str]

        # Agregar el nombre y los encodings a las listas correspondientes
        f_circulo_names.append(name)
        f_circulo_encodings.append(encoding)

# Elementos de asistencia
num_dt = len(f_circulo_names)
alumni_asist_cont = np.zeros(num_dt, dtype=int)
alumni_asist = np.zeros(num_dt, dtype=int)

# Cargamos la cámara
print('[PROCESO] Cargando camara...')
cap = cv2.VideoCapture(0)
while True:
    leido, frame = cap.read() # Frame leido por la camara
    if not leido:break
    
    actual_time = round(time.time(),2) - start_time
    actual_time = round(actual_time,2)
    
    elapsed_time = time.time() - start_time_fps
    frame_count += 1 # Contador de frames por segundo (FPS)
    f_data_locations = face_recognition.face_locations(frame) # Obtiene las coordenadas del rostro en la imagen
    if f_data_locations != []:                                # Si se detecta un rostro
        print("[PROCESO] Rostro detectado")
        f_frame_codings = face_recognition.face_encodings(frame,f_data_locations)        # Obtenemos las características del rostro encontrado
        for face_encoding, (top, right, bottom, left) in zip(f_frame_codings, f_data_locations): # Comparamos el rostro encontrado con los rostros conocidos
            matches = face_recognition.compare_faces(f_circulo_encodings, face_encoding) # resultados de la comparacion de rostros
            #print("Matches: ", matches) 
            if True in matches:                                                          # Si se reconoce el rostro
                index = matches.index(True)
                name = f_circulo_names[index] # Se obtiene el nombre de la persona reconocida
                alumni_asist_cont[index] += 1
            else:
                name = "Desconocido"
                
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2) # Dibujar un rectangulo en el rostro encontrado
            cv2.rectangle(frame, (left, bottom -10), (right, bottom), (0,255,0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left +3, bottom -3), font, 0.4, (255,255,255), 1)
    else:
        print("[ALERTA] No se detecto un rostro")
    # Conteo de frames por segundo (FPS)
    if elapsed_time >= 1:
            fps = frame_count / elapsed_time
            frame_count = 0
            start_time_fps = time.time()
    text = f"FPS: {fps}"
    
    # Mostrar imagen
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)    
    cv2.imshow('Frame',frame)
    
    # Toma de asistencia
    if actual_time >= time_limit:
        indices = [i for i, valor in enumerate(alumni_asist_cont) if valor >= 10]
        print("Indices: ", indices)
        for i in indices:
            alumni_asist[i] = 1
        break
    elif cv2.waitKey(1) == ord('q'):
        break
  
# Calculo del tiempo
end_time = round(time.time(),2) - start_time

cap.release()
# Resumen de asistencia
print("Numero de lecturas: ", alumni_asist_cont)
print("Nombres de alumnos: ", f_circulo_names)
print("Asistencia de alum: ", alumni_asist)
print("[PROCESO] Camara liberada")
print("[PROCESO] Tiempo de ejecucion", end_time)
print("[PROCESO] Cerrando programa...")