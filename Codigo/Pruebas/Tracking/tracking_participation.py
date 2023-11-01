'''
Programa base: https://docs.ultralytics.com/modes/track/#persisting-tracks-loop
'''
from collections import defaultdict
import cv2
import os
import numpy as np
import face_recognition
from ultralytics import YOLO
from pydantic import BaseModel

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

''' Extraer los encodings de un CSV de los alumnos registrados '''
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
    
# Load the YOLOv8 model
model = YOLO('yolov8_models/yolov8n-pose.pt') # usar modelo de pose
get_keypoint = GetKeypoint()


# Id Tracking
n = len(f_circulo_names)
aux = [[0,] * 2 for _ in range(n)]
ids_names = {}
stage =  [None] * n
for i in range(n):
    nombre = f_circulo_names[i]
    ids_names[nombre] = aux[i]
# Store the track history
track_history = defaultdict(lambda: [])

# Open the video file
# video_path = "Tracking/videos/ClaseNinos.mp4"
cap = cv2.VideoCapture(0)
count = 0
name = ""
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if not success: break
    # Run YOLOv8 tracking on the frame, persisting tracks between frames
    results = model.track(frame, persist=True)
    if results[0]: 
        # Get the boxes and track IDs
        boxes = results[0].boxes.xywh.cpu()
        track_ids = results[0].boxes.id.cpu().tolist()
        # keypoints = results[0].boxes.keypoints.xy.cpu().numpy()
        keypoints = results[0].keypoints.xy.cpu().numpy()

        # Visualize the results on the frame
        annotated_frame = results[0].plot(boxes=False)

        # Plot the tracks
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
                stage[int(track_id)] = 0
            if rW_y > rEy_y and stage[int(track_id)] == 0:
                stage[int(track_id)]= 1
                print("PARTICIPACION")
                face_frame = frame[st_pt[1]:ed_pt[1], st_pt[0]:ed_pt[0]]
                f_data_locations = face_recognition.face_locations(face_frame)
                if f_data_locations != []:
                    print("[PROCESO] Rostro detectado")
                    f_frame_encoding = face_recognition.face_encodings(face_frame,f_data_locations)[0]        # Obtenemos las características del rostro encontrado
                    matches = face_recognition.compare_faces(f_circulo_encodings, f_frame_encoding)
                    if True in matches:                                                          # Si se reconoce el rostro
                        index = matches.index(True)   # Indx persona reconocida
                        name = f_circulo_names[index] # Se obtiene el nombre de la persona reconocida
                        # Suma de participacion al respectivo estudiante
                        ids_names[name][1] += 1
                        ids_names[name][0] = track_id
                        cv2.imwrite(f"Participacion_{name}_{ids_names[name][1]}.jpg", face_frame)    
                    else:
                        name = "Desconocido"
                    print("Nombre: ", name)
                else:
                    print("[ALERTA] No se detecto un rostro")
                # Wrists coordinates
            rW_x, rW_y = None, None
            lW_x, lW_y = None, None
            # Nose coordinates
            n_x, n_y = None, None
            # Ears coordinates
            rE_x, rE_y = None, None
            lE_x, lE_y = None, None
            # Eyes coordinates
            rEy_x, rEy_y = None, None
            
    # print(count)
    # count += 1
    # Display the annotated frame
    cv2.imshow("YOLOv8 Tracking", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()


print("\n-----------------------RESUMEN-------------------------")
print(ids_names)
