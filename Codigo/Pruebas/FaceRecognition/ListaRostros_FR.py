"""
Title: Reconocimiento Facial - Lib. Face Recognition OpenCV - Video un rostro por Frame
Reference: https://www.youtube.com/watch?v=51J_bYYMO2k
Author: Frida Cano Falcon
Created on Tue Sep  7 12:00:00 2021
"""
import cv2
import os
import face_recognition
from datetime import datetime
import time

# Carpeta con rostros conocidos - Circulo de personas de confianza
circuloPath = os.path.dirname(os.path.abspath(__file__))
circuloPath = circuloPath + '\\AlumnosData'
circuloPath = circuloPath.replace("\\","/")

f_circulo_encodings = []
f_circulo_names = []

# Tiempo que toma el programa
start_time = time.time() 

for image_circulo_name in os.listdir(circuloPath):                                                                      # Recorrer la carpeta de las personas de confianza
    image_circulo = cv2.imread("AlumnosData/"+ image_circulo_name)
    #image_circulo = (image_circulo, cv2.COLOR_BGR2RGB)
    f_circulo_locations = face_recognition.face_locations(image_circulo)[0]                                             # Obtiene las coordenadas del rostro en la imagen         
    f_circulo_coding = face_recognition.face_encodings(image_circulo, known_face_locations=[f_circulo_locations])[0]    # Obtenemos las características del rostro encontrado
    f_circulo_encodings.append(f_circulo_coding)
    f_circulo_names.append(image_circulo_name.split(".")[0])

print('Cargando cámara...')
cap = cv2.VideoCapture(0)

while True:
	leido, frame = cap.read()
	if not leido:break
	f_data_locations = face_recognition.face_locations(frame)
	print("f_data_locations: ", f_data_locations)
	if f_data_locations != []:
		print("Rostro detectado")
		for face_location in f_data_locations:
			f_frame_coding = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
			results = face_recognition.compare_faces(f_circulo_encodings, f_frame_coding)
			print("Result: ", results)
			#if True in results:
			#	index = results.index(True)
			#	name = f_circulo_names[index]
			#	print("Se reconocio a: ", name)
			top, right, bottom, left = face_location
			cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)

		""" f_data_locations = f_data_locations[0]
		f_data_coding = face_recognition.face_encodings(frame, known_face_locations=[f_data_locations])[0]
		result = face_recognition.compare_faces(f_circulo_encodings, f_data_coding)
		print("Result: ", result)
		if True in result:
			index = result.index(True)
			name = f_circulo_names[index]
			print("Se reconocio a: ", name)
		top, right, bottom, left = f_data_locations
		cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2) """
	else:
		print("No se detecto un rostro")
	cv2.imshow('Frame',frame)
	if cv2.waitKey(1) == ord('q'):
		break
		#cv2.imwrite('Data/rostro1.jpg', frame)
""" else:
	print("Error al acceder a la cámara") """

# Calculo del tiempo
end_time = time.time() - start_time

cap.release()
#print(f_circulo_encodings)
#print(f_circulo_names)
print("Tiempo: ",end_time)