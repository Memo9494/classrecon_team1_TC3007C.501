"""
Title: Reconocimiento Facial - Lib. Face Recognition OpenCV
Reference: https://www.youtube.com/watch?v=51J_bYYMO2k
Author: Frida Cano Falcon
Created on Tue Sep  7 12:00:00 2021
"""
# Librerías
import cv2
import face_recognition


image = cv2.imread('Images/Frida.jpg')
face_location = face_recognition.face_locations(image)[0]
# print("face_loc:",face_location) # face_loc: (top, right, bottom, left)
face_image_encoding = face_recognition.face_encodings(image, known_face_locations=[face_location])[0]
#print("face_image_encoding:",face_image_encoding) # face_image_encoding: [-0.062...] 128-dimension face encoding

# Detectar rostro en imágen fija
""" cv2.rectangle(image, (face_location[3], face_location[0]), (face_location[1], face_location[2]), (0,255,0), 2) # (x1,y1), (x2,y2), (B,G,R), grosor
cv2.imshow('Frida',image)
cv2.waitKey(0)
cv2.destroyAllWindows() """

# Detectar rostro en video y compararlo con una imagen.
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:break
    frame =cv2.flip(frame,1)

    face_locations = face_recognition.face_locations(frame)
    if face_locations != []:
        for face_location in face_locations:
            face_frame_encoding = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
            
            # Comparar con la imagen fija
            results = face_recognition.compare_faces([face_image_encoding], face_frame_encoding)
            print("results:",results) # results: [True] or [False]
            
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break