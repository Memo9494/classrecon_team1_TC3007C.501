import os
import numpy as np
import time
import cv2
import face_recognition
from ultralytics import YOLO
from pydantic import BaseModel
from collections import defaultdict

print("[PROCESO] Iniciando programa...")
# Indicadores de tiempo
start_time_class = round(time.time(),2)  # tiempo de incio de clase
end_time_class= 60.0    # tiempo de fin de clase
time_lim_attendance = 30.0         # Limite de tiempo para tomar una asistencia
attendance_taken = False           # Indicador de asistencia tomada
# Conteo de FPS
fps = 0
frame_count = 0
start_time_fps = start_time_class

print("[PROCESO] Cargando datos...")
''' Extraer los encodings de un CSV de los alumnos registrados '''
# Directorio de los encodings
data_path = os.path.dirname(os.path.abspath(__file__))
data_path = data_path + '\\encodings.txt'
data_path = data_path.replace("\\","/")
# Inicializar listas de encodings y nombres
f_circulo_encodings = []
data_encodings = []
alumni_list = {}
num_alumni = 0
with open(data_path, "r") as file:
    for line in file.readlines():
        # Separar el nombre y los encodings usando la coma como delimitador
        parts = line.strip().split(",")
        name = parts[0]
        encoding_str = parts[1:]

        # Convertir los encodings de strings a flotantes
        encoding = [float(x) for x in encoding_str]

        # Agregar el nombre y los encodings a las listas correspondientes
        data_encodings.append(encoding)
        alumni_list[num_alumni] = {"name":name, "attendance": 0, "delay":0, "participations":0} # Dicicionario por alumno -> Nombre:[asistencia, conteo]
        num_alumni += 1
print(data_encodings)
alumni_asist_cont = np.zeros(num_alumni, dtype=int)# Conteo de asistencia
print("[PROCESO] Datos cargados")
print("[PROCESO] Cargando modelo de pose...")
'''Mapa de keypoints de la pose'''
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
model = YOLO('yolov8_models/yolov8n-pose.pt') # usar modelo de pose













get_keypoint = GetKeypoint()
stages = [None] * num_alumni
# Store the track history
track_history = defaultdict(lambda: [])
print("[PROCESO] Modelo cargado")
print('[PROCESO] Cargando camara...')
cap = cv2.VideoCapture(0)
print('[PROCESO] Camara conectada')



#######################################################
while cap.isOpened():
    read, frame = cap.read() # Frame leido por la camara
    if not read:break
    actual_time = round(time.time(),2) - start_time_class
    actual_time = round(actual_time,2)
    
    elapsed_time = time.time() - start_time_fps
    frame_count += 1 # Contador de frames por segundo (FPS)
    if actual_time < time_lim_attendance :
        
        data_face_locations = face_recognition.face_locations(frame) # Obtiene las coordenadas del rostro en la imagen
        if data_face_locations != []:                                # Si se detecta un rostro
            data_face_encodings = face_recognition.face_encodings(frame, data_face_locations) # Obtiene los encodings de los rostros del frame
            for face_encoding, (top, right, bottom, left) in zip(data_face_encodings, data_face_locations):
                matches = face_recognition.compare_faces(data_encodings, face_encoding) # resultados de la comparacion de rostros
                if True in matches:
                    index = matches.index(True)
                    alumni_asist_cont[index] += 1
                    name = alumni_list[index]["name"]
                else:
                    name = "Desconocido"
                cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)  # Dibuja un rectangulo en el rostro
                cv2.rectangle(frame, (left, bottom -10), (right, bottom), (0,255,0), cv2.FILLED)
                cv2.putText(frame, name, (left +3, bottom - 5), cv2.FONT_HERSHEY_DUPLEX, 0.4, (255,255,255), 1)
        else:
            print("[PROCESO] Rostros no detectados")
    else:
        if attendance_taken == False:
            attendance_taken = True
            print("[PROCESO] Tiempo de asistencia a tiempo terminado")
            indices = [i for i, valor in enumerate(alumni_asist_cont) if valor >= 10] # Verificar si aparece mas de 10 veces en ese tiempo
            for i in indices:
                alumni_list[i]["attendance"] = 1
            print("[PROCESO] Asistencia tomada")
        else:
            # Run YOLOv8 tracking on the frame, persisting tracks between frames
            results = model.track(frame, persist=True)
            if results[0] and results[0].boxes:
                # Get the boxes and track IDs
                boxes = results[0].boxes.xywh.cpu()
                track_ids = results[0].boxes.id.cpu().tolist()
                # keypoints = results[0].boxes.keypoints.xy.cpu().numpy()
                keypoints = results[0].keypoints.xy.cpu().numpy()
                # Visualize the results on the frame
                annotated_frame = results[0].plot(boxes=False)
                for box, track_id, kpts in zip(boxes, track_ids, keypoints):
                    print("TRACK ID : ", track_id)
                    # Wrists coordinates
                    rW_x, rW_y = kpts[get_keypoint.RIGHT_WRIST]
                    lW_x, lW_y = kpts[get_keypoint.LEFT_WRIST]
                    # Nose coordinates
                    n_x, n_y = kpts[get_keypoint.NOSE]
                    # Ears coordinates
                    rE_x, rE_y = kpts[get_keypoint.RIGHT_EAR]
                    lE_x, lE_y = kpts[get_keypoint.LEFT_EAR]
                    # Eyes coordinates
                    rEy_x, rEy_y = kpts[get_keypoint.RIGHT_EYE]
                    # Face distances
                    ears_dist = lE_x - rE_x
                    noseye_dist = n_y - rEy_y
                    st_pt = (int(rE_x - (ears_dist*0.2)), int(n_y - ears_dist))
                    st_pt_str = str(st_pt[0]) + "," + str(st_pt[1])
                    ed_pt = (int(lE_x + (ears_dist*0.2)), int(n_y + (noseye_dist * 4)))
                    ed_pt_str = str(ed_pt[0]) + "," + str(ed_pt[1])
                    cv2.rectangle(annotated_frame, st_pt, ed_pt, (0, 255, 0), 2)
                    
                    # Participation Counter
                    if rW_y < rEy_y :
                        stages[int(track_id)] = 0
                    if rW_y > rEy_y and stages[int(track_id)] == 0:
                        stages[int(track_id)]= 1
                        print("PARTICIPACION")
                        face_frame = frame[st_pt[1]:ed_pt[1], st_pt[0]:ed_pt[0]]
                        face_frame = np.ascontiguousarray(face_frame)
                        face_locations = face_recognition.face_locations(face_frame)
                        if face_locations != []:
                            print("[PROCESO] Rostro detectado")
                            frame_encodings = face_recognition.face_encodings(face_frame,face_locations)[0]        # Obtenemos las características del rostro encontrado
                            matches = face_recognition.compare_faces(data_encodings, frame_encodings)
                            if True in matches:                                                          # Si se reconoce el rostro
                                index = matches.index(True)   # Indx persona reconocida
                                if alumni_list[index]["attendance"] == 0:
                                    alumni_list[index]["delay"] = 1
                                    alumni_list[index]["attendance"] = 1
                                name = alumni_list[index]["name"]
                                alumni_list[index]["participations"] += 1
                                cv2.imwrite(f"Participacion_{name}_{alumni_list[index]['participations']}.jpg", face_frame)    
                            else:
                                name = "Desconocido"
                            print("[PROCESO] Participacion registrada")
                            print("Nombre: ", name)
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
    if cv2.waitKey(1) == ord('q'):
        break

# Calculo del tiempo
end_time = round(time.time(),2) - start_time_class
cap.release()
cv2.destroyAllWindows()
print("\n-----------------------RESUMEN-------------------------")
print("[PROCESO] Camara liberada")
print(alumni_list)
print("[PROCESO] Cerrando programa...")
print("[PROCESO] Tiempo de ejecucion", end_time)