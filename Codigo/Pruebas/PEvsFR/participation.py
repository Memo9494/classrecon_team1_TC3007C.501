print("Iniciando programa...")
from ultralytics import YOLO
import cv2
import os
import face_recognition
import time
import numpy as np
from pydantic import BaseModel

class GetKeypoint(BaseModel):
    NOSE:           int = 0
    LEFT_EYE:       int = 1
    RIGHT_EYE:      int = 2
    LEFT_EAR:       int = 3
    RIGHT_EAR:      int = 4
    LEFT_SHOULDER:  int = 5
    RIGHT_SHOULDER: int = 6
    LEFT_ELBOW:     int = 7
    RIGHT_ELBOW:    int = 8
    LEFT_WRIST:     int = 9
    RIGHT_WRIST:    int = 10
    LEFT_HIP:       int = 11
    RIGHT_HIP:      int = 12
    LEFT_KNEE:      int = 13
    RIGHT_KNEE:     int = 14
    LEFT_ANKLE:     int = 15
    RIGHT_ANKLE:    int = 16

print("Cargando rostros conocidos...")
# Nombres de los alumnos registrados
f_circulo_encodings = []
f_circulo_names = []
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
print("Rostros conocidos cargados")

print("Cargando el modelo...")
model = YOLO('yolov8n-pose.pt')
get_keypoint = GetKeypoint()
print("Modelo cargado")

# Varibles de participaciones
num_dt = len(f_circulo_names) # Numero de alumnos
part_count = np.zeros(num_dt, dtype=int) # Contador de participaciones por alumno
stage = None                  # Estado de Deteccion de participacion
name = ""                     # Texto a desplegar en el frame sobre quien participo

print("Conexion a la camara...")
cap = cv2.VideoCapture(0)
print("Conexion establecida")
while cap.isOpened():
    ret , org_frame = cap.read()
    if not ret: break
    results = model.predict(org_frame, conf=0.5)
    frame = results[0].plot(boxes =False)
    if results[0]:
        for r in results[0]:
            result_keypoints = r.keypoints.xy.cpu().numpy()[0]
            right_wrist_x, right_wrist_y = result_keypoints[get_keypoint.RIGHT_WRIST]
            nose_x, nose_y = result_keypoints[get_keypoint.NOSE]
            left_ear_x, left_ear_y = result_keypoints[get_keypoint.LEFT_EAR]
            right_ear_x, right_ear_y = result_keypoints[get_keypoint.RIGHT_EAR]
            left_eye_x, left_eye_y = result_keypoints[get_keypoint.LEFT_EYE]
            rect_len = left_ear_x - right_ear_x
            nosey_len = nose_y - left_eye_y
            # Rectangulos que indican el rostro
            st = (int(right_ear_x - (rect_len*0.2)), int(nose_y - rect_len))
            st_str = str(st[0]) + "," + str(st[1])
            ed = (int(left_ear_x + (rect_len*0.2)), int(nose_y + (nosey_len * 4)))
            ed_str = str(ed[0]) + "," + str(ed[1])
            cv2.rectangle(frame, st, ed, (0, 255, 0), 2)
            # Participation Counter
            if right_wrist_y < left_eye_y :
                stage = "down"
            if right_wrist_y > left_eye_y and stage =='down':
                stage="up"
                print("PARTICIPACION")
                face_frame = org_frame[st[1]:ed[1], st[0]:ed[0]]
                f_data_locations = face_recognition.face_locations(face_frame) # Obtiene las coordenadas del rostro en la imagen
                if f_data_locations != []:
                    print("[PROCESO] Rostro detectado")
                    f_frame_codings = face_recognition.face_encodings(face_frame,f_data_locations)        # Obtenemos las características del rostro encontrado
                    for face_encoding, (top, right, bottom, left) in zip(f_frame_codings, f_data_locations): # Comparamos el rostro encontrado con los rostros conocidos
                        matches = face_recognition.compare_faces(f_circulo_encodings, face_encoding)
                        if True in matches:                                                          # Si se reconoce el rostro
                            index = matches.index(True)   # Indx persona reconocida
                            # Suma de participacion al respectivo estudiante
                            part_count[index] += 1
                            name = f_circulo_names[index] + " participo " + str(part_count[index]) + " veces."
                        else:
                            name = "Desconocido"
                else:
                    print("[ALERTA] No se detecto un rostro")
                    
            cv2.putText(frame, str(int(right_wrist_y)),
                        [int(right_wrist_x), int(right_wrist_y)],
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, str(name),
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("\n-----------------------RESUMEN-------------------------")
print("Nombres de alumnos:         ", f_circulo_names)
print("Participaciones por alumno: ", part_count)