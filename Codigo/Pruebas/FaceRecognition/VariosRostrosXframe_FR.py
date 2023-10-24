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

print("[PROCESO] Iniciando programa...")
# Tiempo que toma el programa
start_time = time.time() 

# Conteo de FPS
fps = 0
frame_count = 0
start_time_fps = start_time

# Nombres de los alumnos registrados
f_circulo_encodings = []
f_circulo_names = []
alumni_asist = []

''' Extraer los encodings de las FOTOS de los alumnos registrados '''
# # Carpeta con rostros alumnos registrados
# circuloPath = os.path.dirname(os.path.abspath(__file__))
# circuloPath = circuloPath + '\\persons_data'
# circuloPath = circuloPath.replace("\\","/")
# for image_circulo_name in os.listdir(circuloPath):                                                                      # Recorrer la carpeta de las personas de confianza
#     image_circulo = cv2.imread("persons_data/"+ image_circulo_name)
#     f_circulo_locations = face_recognition.face_locations(image_circulo)[0]
#     f_circulo_coding = face_recognition.face_encodings(image_circulo, known_face_locations=[f_circulo_locations])[0]    # Obtenemos las características del rostro encontrado
#     f_circulo_encodings.append(f_circulo_coding)
#     f_circulo_names.append(image_circulo_name.split(".")[0])
# print(f_circulo_encodings)

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

# Cargamos la cámara
print('[PROCESO] Cargando camara...')
cap = cv2.VideoCapture(0)
while True:
    leido, frame = cap.read()
    if not leido:break
    
    # small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25) # Reduce el tamaño del frame para que sea más rápido el procesamiento
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    # rgb_small_frame = small_frame[:, :, ::-1]
    
    elapsed_time = time.time() - start_time_fps
    frame_count += 1
    f_data_locations = face_recognition.face_locations(frame) # Obtiene las coordenadas del rostro en la imagen
    if f_data_locations != []:                                # Si se detecta un rostro
        print("[PROCESO] Rostro detectado")
        face_names = []
        f_frame_codings = face_recognition.face_encodings(frame,f_data_locations)        # Obtenemos las características del rostro encontrado
        for face_encoding, (top, right, bottom, left) in zip(f_frame_codings, f_data_locations): # Comparamos el rostro encontrado con los rostros conocidos
            matches = face_recognition.compare_faces(f_circulo_encodings, face_encoding)
            print("Matches: ", matches)
            if True in matches:                                                          # Si se reconoce el rostro
                index = matches.index(True)
                name = f_circulo_names[index]
                face_names.append(name)
            else:
                name = "Desconocido"
            # top *= 4
            # right *= 4
            # bottom *= 4
            # left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
            cv2.rectangle(frame, (left, bottom -10), (right, bottom), (0,255,0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left +3, bottom -3), font, 0.4, (255,255,255), 1)
    else:
        print("[ALERTA] No se detecto un rostro")
    if elapsed_time >= 1:
            fps = frame_count / elapsed_time
            frame_count = 0
            start_time_fps = time.time()
    text = f"FPS: {fps}"
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)    
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break
  
# Calculo del tiempo
end_time = time.time() - start_time

cap.release()
print("[PROCESO] Camara liberada")
print("[PROCESO] Tiempo de ejecucion", end_time)
print("[PROCESO] Cerrando programa...")