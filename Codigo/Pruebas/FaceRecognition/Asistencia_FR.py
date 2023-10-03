'''
Programa para determinar la asistencia con base a la detección de rostros
Frida Cano (@FCANOF)
'''
import cv2
import os
import face_recognition
import time

print("[PROCESO] Iniciando programa...")
# Nombres de los alumnos registrados
face_encodings = []
face_names = []

# Nombre del archivo TXT
txt_file = 'encodings.txt'

# Abrir el archivo y leer cada línea
with open(txt_file, 'r') as file:
    lines = file.readlines()

# Procesar cada línea del archivo
for line in lines:
    # Dividir la línea en elementos utilizando la coma como separador
    elementos = line.strip().split(',')
    
    # El primer elemento se agrega al arreglo de primeros_elementos
    face_names.append(elementos[0])
    
    # Los últimos 128 elementos se agregan al arreglo de ultimos_128_elementos
    face_encodings.append(elementos[-128:])

# Imprimir los arreglos (opcional)
print("Primeros elementos:")
print(face_names)

print("\nÚltimos 128 elementos:")
print(face_encodings)
