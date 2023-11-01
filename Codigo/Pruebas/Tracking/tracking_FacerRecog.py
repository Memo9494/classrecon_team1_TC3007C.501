'''
Programa base: https://docs.ultralytics.com/modes/track/#persisting-tracks-loop
'''
from collections import defaultdict
import cv2
import os
import numpy as np
import face_recognition
from ultralytics import YOLO

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
# Id Tracking
n = len(f_circulo_names)
aux = [[0,] * 2 for _ in range(n)]
ids_names = {}
for i in range(n):
    nombre = f_circulo_names[i]
    ids_names[nombre] = aux[i]
    
# Load the YOLOv8 model
model = YOLO('yolov8_models/yolov8n-pose.pt') # usar modelo de pose

# Open the video file
# video_path = "Tracking/videos/ClaseNinos.mp4"
cap = cv2.VideoCapture(0)

# Store the track history
track_history = defaultdict(lambda: [])

count = 0
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

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Plot the tracks
        for box, track_id in zip(boxes, track_ids):
            x, y, w, h = box
            print("Track ID: ", track_id)
            track = track_history[track_id]
            track.append((float(x), float(y)))  # x, y center point
            # cv2.rectangle(annotated_frame, (int(x-(w/2)), int(y-(h/2))), (int(x + (w/2)), int(y + (h/2))), (0, 255, 0), 2)
            if count > 20 and count < 30:
                face_frame = frame[int(y-(h/2)):int(y+(h/2)), int(x-(w/2)):int(x+(w/2))]   
                f_data_locations = face_recognition.face_locations(face_frame) # Obtiene las coordenadas del rostro en la imagen
                if f_data_locations != []:                                # Si se detecta un rostro
                    print("[PROCESO] Rostro detectado")
                    f_frame_codings = face_recognition.face_encodings(face_frame,f_data_locations)        # Obtenemos las características del rostro encontrado
                    for face_encoding, (top, right, bottom, left) in zip(f_frame_codings, f_data_locations): # Comparamos el rostro encontrado con los rostros conocidos
                        matches = face_recognition.compare_faces(f_circulo_encodings, face_encoding) # resultados de la comparacion de rostros
                        #print("Matches: ", matches) 
                        if True in matches:                                                          # Si se reconoce el rostro
                            index = matches.index(True)
                            name = f_circulo_names[index] # Se obtiene el nombre de la persona reconocida
                            ids_names[name][0] = track_id
                        else:
                            name = "Desconocido"
                        print("Nombre: ", name)
                else:
                    print("[ALERTA] No se detecto un rostro")
            elif count > 30:
                count = 0
                
            if len(track) > 30:  # retain 90 tracks for 90 frames
                track.pop(0)

            # Draw the tracking lines
            points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
            cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 230, 230), thickness=5)

    # Display the annotated frame
    print(count)
    count += 1
    cv2.imshow("YOLOv8 Tracking", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()


print("\n-----------------------RESUMEN-------------------------")
print(ids_names)
