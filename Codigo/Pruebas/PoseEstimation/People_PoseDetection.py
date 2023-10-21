from ultralytics import YOLO
import cv2
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

print("Cargando modelo...")
model = YOLO('yolov8n-pose.pt')
print("Modelo cargado!")
print("Conectando con la camara...")
cap = cv2.VideoCapture(0)
print("Camara conectada!")
get_keypoint = GetKeypoint()
count =0
stage = None
while cap.isOpened():
    ret , frame = cap.read()
    if ret:
        results = model.predict(frame, conf=0.5)
        frame = results[0].plot(boxes=False)
        if results[0]: # Verificar si hay detecciones
            for r in results[0]: # Recorrer la lista de objetos (Personas) detectados
                # result_keypoints = r.keypoints.xyn.cpu().numpy()[0]
                result_keypoints = r.keypoints.xy.cpu().numpy()[0]
                nose_x, nose_y = result_keypoints[get_keypoint.NOSE]
                left_ear_x, left_ear_y = result_keypoints[get_keypoint.LEFT_EAR]
                right_ear_x, right_ear_y = result_keypoints[get_keypoint.RIGHT_EAR]
                left_eye_x, left_eye_y = result_keypoints[get_keypoint.LEFT_EYE]
                rect_len = left_ear_x - right_ear_x
                nosey_len = nose_y - left_eye_y
                print(rect_len)
                # Rectangulos que indican el rostro
                st = (int(right_ear_x - (rect_len*0.2)), int(nose_y - rect_len))
                st_str = str(st[0]) + "," + str(st[1])
                ed = (int(left_ear_x + (rect_len*0.2)), int(nose_y + (nosey_len * 4)))
                ed_str = str(ed[0]) + "," + str(ed[1])
                cv2.rectangle(frame, st, ed, (0, 255, 0), 2)
                
                # right_wrist_x, right_wrist_y = result_keypoints[get_keypoint.RIGHT_WRIST] 
                # left_eye_x, left_eye_y = result_keypoints[get_keypoint.LEFT_EYE]
                
                # Participation Counter
                # if right_wrist_y < left_eye_y :
                #     stage = "down"
                # if right_wrist_y > left_eye_y and stage =='down':
                #     stage="up"
                #     count +=1
                
                cv2.putText(frame, st_str,
                            st,
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
                cv2.putText(frame, ed_str,
                            ed,
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
                
                # cv2.putText(frame, str(count),
                #             (10, 30),
                #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()