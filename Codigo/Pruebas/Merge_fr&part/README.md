# Face Recognition

El código proporciona un sistema de registro de participación en un entorno de aula utilizando la detección facial y de cuerpos humanos. A continuación, se presenta una documentación detallada del código:

## Funcionalidad:

1. **Importación de Bibliotecas:** El código importa varias bibliotecas necesarias para su funcionamiento, incluyendo:
   - `os`: Para operaciones relacionadas con archivos y directorios.
   - `numpy`: Para operaciones matriciales y cálculos numéricos.
   - `time`: Para el seguimiento del tiempo.
   - `cv2` (OpenCV): Para el procesamiento de imágenes y vídeo.
   - `face_recognition`: Para el reconocimiento facial.
   - `ultralytics.YOLO`: Para la detección de objetos y seguimiento de cuerpos en imágenes y vídeo.
   - `pydantic.BaseModel`: Para definir una clase que enumera los puntos clave del cuerpo humano.
   - `collections.defaultdict`: Para almacenar datos de seguimiento.

2. **Carga de Datos de Alumnos Registrados:** El código carga los datos de los alumnos registrados desde un archivo de texto llamado "encodings.txt". En este archivo, se almacenan los nombres y las codificaciones faciales de los alumnos.

3. **Inicialización de Listas y Diccionarios:** Se inicializan listas para almacenar las codificaciones faciales y un diccionario que almacena información sobre los alumnos registrados, como el nombre, la asistencia, la demora y las participaciones.

4. **Carga del Modelo de Pose:** Se carga un modelo YOLOv8 específico para la detección y seguimiento de cuerpos en el video. El modelo se inicializa con una instancia de la clase `GetKeypoint` que enumera los puntos clave del cuerpo humano.

5. **Conexión a la Cámara:** El código establece una conexión a la cámara, que se utiliza para capturar vídeo en tiempo real.

6. **Indicadores de Tiempo:** Se definen varios indicadores de tiempo para rastrear el tiempo de inicio y fin de la clase, el tiempo límite para tomar la asistencia y el estado de si la asistencia ya ha sido tomada.

7. **Bucle Principal de Detección y Registro:**
   - El bucle captura continuamente fotogramas de vídeo desde la cámara.
   - Realiza la detección facial en los fotogramas utilizando la biblioteca `face_recognition`.
   - Lleva un registro de la asistencia de los alumnos en función de la detección facial.
   - Una vez que se alcanza el tiempo límite para tomar la asistencia, el código verifica si un estudiante ha aparecido más de 10 veces en ese tiempo y, si es así, marca su asistencia.
   - Luego, el código utiliza YOLOv8 para detectar y realizar un seguimiento de los cuerpos en el vídeo, destacando las muñecas y la posición del rostro.
   - Se registra la participación de los estudiantes si levantan la muñeca por encima de la altura del ojo.
   - El vídeo en tiempo real se muestra con rectángulos verdes alrededor de los rostros detectados y la posición de las muñecas.

8. **Cálculo de la Velocidad de Fotogramas (FPS):** El código calcula la velocidad de fotogramas (FPS) y la muestra en la esquina superior izquierda del vídeo.

9. **Finalización del Programa:** El programa se puede detener manualmente presionando la tecla 'q'. Cuando se cierra, se liberan los recursos de la cámara y se muestra un resumen que incluye información sobre la asistencia de los alumnos.

Este código se utiliza para llevar un registro de la asistencia y la participación de los alumnos en un aula mediante la detección facial y de cuerpos. Es especialmente útil en un entorno educativo para realizar un seguimiento de la asistencia y la participación de los estudiantes de manera eficiente y automática.
