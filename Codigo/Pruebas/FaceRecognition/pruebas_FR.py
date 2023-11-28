"""
Title: Pruebas de reconocimiento facial obteniendo métricas
Description: Reconocimiento Facial - Lib. Face Recognition OpenCV
Author: Frida Cano Falcon
Created on 25/11/2023
"""
import cv2
import os
import face_recognition

# Nombres de los alumnos registrados
sujetos_encodings = []
sujetos_names = []
alumni_asist = []

''' Extraer los encodings de un CSV de los alumnos registrados '''
sujetos_path = os.path.dirname(os.path.abspath(__file__))
sujetos_path = sujetos_path + '\\encodings.txt'
sujetos_path = sujetos_path.replace("\\","/")

with open(sujetos_path, "r") as file:
    for line in file.readlines():
        # Separar el nombre y los encodings usando la coma como delimitador
        parts = line.strip().split(",")
        name = parts[0]
        encoding_str = parts[1:]

        # Convertir los encodings de strings a flotantes
        encoding = [float(x) for x in encoding_str]

        # Agregar el nombre y los encodings a las listas correspondientes
        sujetos_names.append(name)
        sujetos_encodings.append(encoding)

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