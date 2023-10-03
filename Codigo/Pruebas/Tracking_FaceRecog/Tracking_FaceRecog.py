"""
Title: Reconocimiento Facial - Lib. Face Recognition OpenCV - Video varios rostros por Frame
Reference: https://www.youtube.com/watch?v=51J_bYYMO2k
Author: Frida Cano Falcon
Created on Tue Sep 19 2023
"""
import cv2
import os
import face_recognition
from ultralytics import YOLO
from sort import Sort
import time
import numpy as np

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
    f_circulo_locations = face_recognition.face_locations(image_circulo)[0]
    #f_circulo_locations = face_recognition.face_locations(image_circulo, model="cnn")[0]                                # Obtiene las coordenadas del rostro en la imagen         
    f_circulo_coding = face_recognition.face_encodings(image_circulo, known_face_locations=[f_circulo_locations])[0]    # Obtenemos las características del rostro encontrado
    f_circulo_encodings.append(f_circulo_coding)
    f_circulo_names.append(image_circulo_name.split(".")[0])

# Cargamos la cámara
print('[PROCESO] Cargando video...')
cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("videos/people.mp4")

print('[PROCESO] Cargando modelo...')
model = YOLO("yolov8n.pt")
tracker = Sort()
tracks = []

while True:
    leido, frame = cap.read()
    if not leido:break
    #small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25) # Reduce el tamaño del frame para que sea más rápido el procesamiento
    cut_frame = frame.copy() # Se crea una copia del frame para que no se modifique el original
    results = model(frame, stream=True)
    
    for res in results:
        person_indices = np.where((res.boxes.cls.cpu().numpy() == 0) & (res.boxes.conf.cpu().numpy() > 0.5))[0]
        # filtered_indices = np.where(res.boxes.conf.cpu().numpy() > 0.5)[0]
        print(person_indices)
        boxes = res.boxes.xyxy.cpu().numpy()[person_indices].astype(int)
        tracks = tracker.update(boxes)
        tracks = tracks.astype(int)
        
        for xmin, ymin, xmax, ymax, track_id in tracks:
            # cut_frame = cut_frame[ymin:ymax, xmin:xmax]
            f_data_locations = face_recognition.face_locations(frame)                                    # Obtiene las coordenadas del rostro en la imagen
            print(f_data_locations)
            if f_data_locations != []:                                                                   # Si se detecta un rostro
                print("[PROCESO] Rostros detectados")
                f_frame_codings = face_recognition.face_encodings(frame,f_data_locations)                # Obtenemos las características del rostro encontrado
                face_encoding = f_frame_codings[0]
                top, right, bottom, left = f_data_locations[0] 
                matches = face_recognition.compare_faces(f_circulo_encodings, face_encoding)
                if True in matches:                                                                      # Si se reconoce el rostro
                    index = matches.index(True)
                    name = f_circulo_names[index]
                else:
                    name = "Desconocido"
                
                cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
                cv2.rectangle(frame, (left, bottom -10), (right, bottom), (0,255,0), cv2.FILLED)
                cv2.putText(frame, name, (left +3, bottom -3), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255,255,255), 1)
            else:
                print("[ALERTA] No se detecto un rostro")
            # cv2.putText(img=frame, text=f"Id: {track_id}", org=(xmin, ymin-10), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0,255,0), thickness=2)
            # cv2.rectangle(img=frame, pt1=(xmin, ymin), pt2=(xmax, ymax), color=(0, 255, 0), thickness=2)
            
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
  
# Calculo del tiempo
end_time = time.time() - start_time

cap.release()
print("[PROCESO] Camara liberada")
print("[PROCESO] Tiempo de ejecucion", end_time)
print("[PROCESO] Cerrando programa...")