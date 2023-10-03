"""
Title: Reconocimiento Facial - Lib. Face Recognition OpenCV - Video varios rostros por Frame
Reference: https://www.youtube.com/watch?v=51J_bYYMO2k
Author: Frida Cano Falcon
Created on Tue Sep 19 2023
"""
import cv2
import os
import face_recognition
import time

print("[PROCESO] Iniciando programa...")
# Tiempo que toma el programa
global start_time, start_time_fps
start_time = round(time.time(),2)
start_time_fps = time.time()
# Carpeta con rostros alumnos registrados
regis_path = os.path.dirname(os.path.abspath(__file__))
regis_path = regis_path + '\\persons_data'
regis_path = regis_path.replace("\\","/")

print('[PROCESO] Cargando base de datos...')
# Nombres de los alumnos registrados
regis_encodings = []
regis_names = []
for regis_name in os.listdir(regis_path):                                                                      # Recorrer la carpeta de las personas de confianza
    regis_img = cv2.imread("persons_data/"+ regis_name)
    regis_locations = face_recognition.face_locations(regis_img)[0]
    regis_coding = face_recognition.face_encodings(regis_img, known_face_locations=[regis_locations])[0]    # Obtenemos las características del rostro encontrado
    regis_encodings.append(regis_coding)
    regis_names.append(regis_name.split(".")[0])

# Cargamos la cámara
print('[PROCESO] Cargando video streaming...')
global cap
cap = cv2.VideoCapture(0)

global num_alumni_new, num_profs_new, fps, frame_count
num_alumni_new = 0
num_profs_new = 0
fps = 0
frame_count = 0

def main():
    while True:
        faceRecognition()
        if cv2.waitKey(1) == ord('q'):
            break
        elif cv2.waitKey(1) == ord('a'):
            print("a listener")
            registroPersona('a')
        elif cv2.waitKey(1) == ord('p'):
            print("p listener")
            registroPersona('p')
    # Calculo del tiempo
    end_time = time.time() - start_time
    cap.release()
    cv2.destroyAllWindows()
    print("[PROCESO] Camara liberada")
    print("[PROCESO] Cerrando programa...")
    print("[PROCESO] Tiempo de ejecucion", end_time)
    

def faceRecognition():
    global start_time_fps, fps, frame_count
    leido, frame = cap.read()
    if leido:
        #small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25) # Reduce el tamaño del frame para que sea más rápido el procesamiento
        elapsed_time = time.time() - start_time_fps
        frame_count += 1
        face_locations = face_recognition.face_locations(frame) # Obtiene las coordenadas del rostro en la imagen
        if face_locations != []:                                # Si se detecta un rostro
            print("[PROCESO] Rostro detectado")
            face_names = []
            face_codings = face_recognition.face_encodings(frame,face_locations)        # Obtenemos las características del rostro encontrado
            for face_encoding, (top, right, bottom, left) in zip(face_codings, face_locations):                                            # Comparamos el rostro encontrado con los rostros conocidos
                matches = face_recognition.compare_faces(regis_encodings, face_encoding)
                if True in matches:                                                          # Si se reconoce el rostro
                    index = matches.index(True)
                    name = regis_names[index]
                    face_names.append(name)
                else:
                    name = "Desconocido"
                cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
                cv2.rectangle(frame, (left, bottom -10), (right, bottom), (0,255,0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left +3, bottom -3), font, 0.4, (255,255,255), 1)
        else:
            print("[ALERTA] No se detecto un rostro")
        if elapsed_time >= 1:
            fps = frame_count / elapsed_time
            frame_count = 0
            start_time_fps = time.time()
        text = f"FPS: {fps}"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Frame',frame)
    else:
        print("[ALERTA] No se detecto un frame")
        cap.release()
        cv2.destroyAllWindows()
        main()
def registroPersona(persona):
    print('[CAMARA] Se tomará una foto dentro de 10 segundos: preparese para la captura.')
    time.sleep(10)
    leido, frame = cap.read()
    if leido:
        cv2.imwrite('temp/temp_new.jpg', frame)
        temp = cv2.imread('temp/temp_new.jpg')
        if face_recognition.face_locations(temp) != []: 
            new_locations = face_recognition.face_locations(temp)[0]                                       # Obtiene las coordenadas del rostro en la imagen         
            new_coding = face_recognition.face_encodings(temp, known_face_locations=[new_locations])[0]    # Obtenemos las características del rostro encontrado
            if persona == 'a':
                num_alumnos_new += 1
                nombre = "Alumno" + str(num_alumnos_new)
            elif persona == 'p':
                num_profesores_new += 1
                nombre = "Profesor" + str(num_profesores_new)
    
            cv2.imwrite('persons_data/{}.jpg'.format(nombre), temp)
            regis_encodings.append(new_coding)
            regis_names.append(persona)
            return True
        else:
            print('NO SE DETECTÓ EL ROSTRO')
            return False
    else:
        print("[ERROR] Error al acceder a la CAMARA")
        return False
    
if __name__ == '__main__':
    main()