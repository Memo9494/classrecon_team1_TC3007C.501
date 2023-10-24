from ultralytics import YOLO
import cv2
from pydantic import BaseModel
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
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
count = 0
stage = None

img_counter = 0
while cap.isOpened():
    ret , frame = cap.read()
    if not ret: break
    results = model.predict(frame, conf=0.5)
    #frame = results[0].plot(boxes=False)
    
    if results[0]:
        for r in results[0]:
            result_box = r.boxes.xyxy.cpu().numpy()[0]
            start_pt = (int(result_box[0]), int(result_box[1]))
            end_pt = (int(result_box[2]), int(result_box[3]))
            image = frame[start_pt[1]:end_pt[1], start_pt[0]:end_pt[0]]
            # cv2.rectangle(frame, start_pt, end_pt, (0, 255, 0), 2)
            # Recolor image to RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
        
            # Make detection
            results = pose.process(image)
        
            # Recolor back to BGR
            image.flags.writeable = True
            
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )               

            # result_keypoints = r.keypoints.xy.cpu().numpy()[0]
            # right_wrist_x, right_wrist_y = result_keypoints[get_keypoint.RIGHT_WRIST] 
            # left_eye_x, left_eye_y = result_keypoints[get_keypoint.LEFT_EYE]
            
            # # Participation Counter
            # if right_wrist_y < left_eye_y :
            #     stage = "down"
            # if right_wrist_y > left_eye_y and stage =='down':
            #     stage="up"
            #     count +=1

            # cv2.putText(frame, str(int(right_wrist_y)),
            #             [int(right_wrist_x), int(right_wrist_y)],
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            # cv2.putText(frame, str(count),
            #             (10, 30),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
    
    cv2.imshow('frame', image)
    
    if cv2.waitKey(1) == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()