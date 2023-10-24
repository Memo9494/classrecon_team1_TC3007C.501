'''
Este programa se encarga de registrar los encodings de los rostros de los alumnos que se encuentran en la carpeta "persons_data" y guardarlos en un archivo de texto llamado "encodings.txt".
Frida Cano (@FCANOF)
'''
import cv2
import os
import face_recognition
import time

print("[PROCESO] Iniciando programa...")
# Carpeta con rostros alumnos registrados
persons_path = os.path.dirname(os.path.abspath(__file__))
persons_path = persons_path + '\\persons_data'
persons_path = persons_path.replace("\\","/")

# Definir el nombre del archivo de texto en el que deseas guardar los encodings
encoding_file = "encodings.txt"

face_encodings = []
face_names = [] # Nombres de los alumnos registrados

# Crear o abrir el archivo en modo de escritura
with open(encoding_file, "w") as file:

    for image_name in os.listdir(persons_path):                                                              # Recorrer la carpeta de las personas de confianza
        image_ = cv2.imread("persons_data/"+ image_name)
        face_locations = face_recognition.face_locations(image_)[0]                                          # Obtiene las coordenadas del rostro en la imagen         
        face_encoding = face_recognition.face_encodings(image_, known_face_locations=[face_locations])[0]    # Obtenemos las características del rostro encontrado
        encoding_str = ",".join(map(str, face_encoding))
        name = image_name.split(".")[0]
    
        # Escribir el nombre y el encoding en el archivo, separados por una coma
        file.write(f"{name},{encoding_str}\n")

print(f"Los encodings se han guardado en {encoding_file}")