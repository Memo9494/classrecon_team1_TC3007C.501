# Participation
Estos códigos consisten en programas de reconocimiento facial que utilizan la biblioteca OpenCV y Face Recognition para detectar y reconocer rostros en un video en tiempo real. La implementación de esta solución requirió de múltiples iteraciones.

A continuación, se presenta una descripción detallada del código:

## [Participación con Reconocimiento Facial](https://github.com/Memo9494/classrecon_team1_TC3007C.501/blob/main/Codigo/Pruebas/Participation/participation.py)

Este código es un sistema de registro de participación que utiliza la detección de cuerpos y el reconocimiento facial en tiempo real. El programa identifica a los estudiantes presentes en un aula y registra sus participaciones mediante el análisis de la posición de las manos y la detección de rostros. A continuación, se presenta una descripción detallada del código:

### Funcionalidad:

1. **Importación de Bibliotecas:** El código importa las bibliotecas necesarias para su funcionamiento, incluyendo:
   - `ultralytics.YOLO`: Para la detección de objetos en imágenes y video.
   - `cv2` (OpenCV): Para el procesamiento de imágenes y video.
   - `os`: Para manipulación de archivos y directorios.
   - `face_recognition`: Para el reconocimiento facial.
   - `time`: Para el seguimiento del tiempo.
   - `numpy`: Para operaciones matriciales.
   - `pydantic.BaseModel`: Para definir una clase que enumera los puntos clave del cuerpo humano.

2. **Definición de la Clase `GetKeypoint`:** Se define una clase llamada `GetKeypoint` que hereda de `BaseModel` (de Pydantic) y enumera los puntos clave del cuerpo humano, como la nariz, los ojos, los oídos, los hombros, los codos, las muñecas, las caderas, las rodillas y los tobillos.

3. **Carga de Rostros Conocidos:** El código carga los datos de los rostros conocidos de los alumnos desde un archivo de texto llamado "encodings.txt". En este archivo, se almacenan los nombres y las codificaciones faciales de los alumnos.

4. **Carga del Modelo YOLO:** El código carga un modelo YOLO (You Only Look Once) entrenado para la detección de objetos en imágenes y video. En este caso, se carga un modelo llamado 'yolov8n-pose.pt'.

5. **Variables de Participación:** Se inicializan variables para llevar un registro de las participaciones de los alumnos. Estas variables incluyen el número de alumnos registrados, un contador de participaciones por alumno, y variables para rastrear el estado de detección y el nombre del alumno que participa.

6. **Conexión a la Cámara:** El código establece una conexión a la cámara, que se utilizará para capturar video en tiempo real.

7. **Bucle Principal de Detección y Registro de Participación:**
   - El bucle captura continuamente fotogramas de video desde la cámara.
   - Utiliza el modelo YOLO para detectar objetos en el fotograma, en este caso, la posición de las manos.
   - Calcula la posición de la muñeca derecha, la nariz, el oído izquierdo y derecho, el ojo izquierdo y el ojo derecho en relación con el cuerpo.
   - Luego, se determina si una mano está en posición arriba o abajo, lo que indica una participación.
   - Si se detecta una participación, se extrae el área del rostro de la persona y se realiza el reconocimiento facial utilizando la biblioteca `face_recognition`.
   - Si el rostro se reconoce como el de un estudiante registrado, se incrementa el contador de participaciones para ese estudiante.
   - Se muestra el número de participaciones de ese estudiante en el fotograma.
   - El video en tiempo real se muestra con rectángulos verdes alrededor de los rostros detectados y el contador de participaciones.

8. **Finalización del Programa:** El programa se puede detener manualmente presionando la tecla 'q'. Cuando se cierra, se liberan los recursos de la cámara y se muestra un resumen que incluye los nombres de los alumnos registrados y la cantidad de participaciones registradas para cada uno.

Este código se utiliza para llevar un registro de la participación de los alumnos en un aula utilizando la detección de manos y el reconocimiento facial. Es especialmente útil en un entorno educativo para realizar un seguimiento de la asistencia y la participación de los estudiantes.
