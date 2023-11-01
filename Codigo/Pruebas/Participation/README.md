# Participation
Estos códigos consisten en programas de reconocimiento facial que utilizan la biblioteca OpenCV y Face Recognition para detectar y reconocer rostros en un video en tiempo real. La implementación de esta solución requirió de múltiples iteraciones las principales son:

* Reconocimiento facial de una persona con base en una imagen: **_root_FaceRecognition_**.
* Reconocimiento facial de una persona en un video en tiempo real: **_root_FaceRecognition_**.
* Reconocimiento facial de más de una persona en un video en tiempo real: **_multipple_FR_**.
* Optimización de la obtención de los registros de los rostros de las personas en la base de datos para realizar el reconocimiento: **_multiple_FR_**.
* Implementación del algoritmo de asistencia: **_attendance_FR_**.

A continuación, se presenta una descripción detallada del código:

## attendance_FR
Este código se utiliza para llevar un registro de la asistencia de alumnos a través del reconocimiento facial en un entorno de video en tiempo real. Los datos de los alumnos se almacenan en un archivo CSV y se comparan con los rostros detectados en el video para determinar la asistencia.

### Funcionalidad:

1. **Importación de Bibliotecas:** El código importa las bibliotecas necesarias, incluyendo _OpenCV_, _os_ (para manipulación de archivos y directorios), _face_recognition_ (una librería de Python para reconocimiento facial), _time_ (para el seguimiento del tiempo) y _numpy_ para operaciones matriciales.

2. **Iniciación del Programa:** Muestra un mensaje indicando que el programa se está iniciando.

3. **Definición de Parámetros de Tiempo:**
   - `start_time`: Registra el tiempo de inicio del programa.
   - `time_limit`: Establece un límite de tiempo (en segundos) para tomar la asistencia.

4. **Conteo de FPS:** Inicializa variables para medir los cuadros por segundo (FPS) y llevar un conteo de cuadros procesados.

5. **Carga de Datos de Alumnos Registrados:**
   - Lee los datos de alumnos registrados desde un archivo CSV llamado "_encodings.txt_".
   - Convierte los encodings de rostros en números flotantes.
   - Almacena los nombres y encodings en listas separadas.

6. **Iniciación de Elementos de Asistencia:**
   - Calcula el número de alumnos registrados.
   - Inicializa matrices para llevar un registro de la asistencia.

7. **Carga de la Cámara:** Inicia la cámara web para capturar video en tiempo real.

8. **Bucle Principal del Reconocimiento Facial:**
   - Captura cada fotograma (frame) de la cámara.
   - Detecta rostros en el fotograma usando la biblioteca face_recognition.
   - Si se detecta un rostro:
     - Compara el rostro con los rostros conocidos en la base de datos.
     - Registra la asistencia si se reconoce un rostro.
     - Dibuja un rectángulo alrededor del rostro y muestra el nombre si es reconocido.
   - Muestra el FPS en el fotograma.
   - Comprueba si ha pasado el tiempo límite para tomar la asistencia y finaliza el programa si es necesario.
   - El bucle se puede detener manualmente presionando la tecla 'q'.

9. **Finalización y Resumen:**
   - Calcula el tiempo total de ejecución.
   - Libera la cámara.
   - Muestra un resumen de la asistencia, indicando cuántas veces se reconoció a cada alumno.
   - Muestra los nombres de los alumnos registrados.
   - Indica si un alumno está presente (1) o ausente (0) según el límite de reconocimientos requeridos.
   - Muestra un mensaje de cierre del programa.

## multiple_FR
Este código se utiliza para realizar el reconocimiento facial en un entorno de video en tiempo real, comparando los rostros detectados con los rostros previamente registrados. La asistencia se registra automáticamente si se reconoce un rostro registrado. La configuración del programa permite cargar los datos de los alumnos desde imágenes de rostros o desde un archivo CSV, lo que brinda flexibilidad en la fuente de datos.

### Funcionalidad:

1. **Importación de Bibliotecas:** El código importa las bibliotecas necesarias, incluyendo OpenCV (para el procesamiento de imágenes y video), os (para manipulación de archivos y directorios), face_recognition (una librería de Python para reconocimiento facial) y time (para el seguimiento del tiempo).

2. **Iniciación del Programa:** Muestra un mensaje indicando que el programa se está iniciando.

3. **Definición de Parámetros de Tiempo:**
   - `start_time`: Registra el tiempo de inicio del programa.

4. **Conteo de FPS:** Inicializa variables para medir los cuadros por segundo (FPS) y llevar un conteo de cuadros procesados.

5. **Nombres de Alumnos Registrados:** Inicializa listas para almacenar los nombres y encodings de los alumnos registrados y una lista vacía para llevar un registro de la asistencia.

6. **Carga de Datos de Alumnos Registrados:**
   - El código permite cargar los encodings de los alumnos registrados desde dos fuentes diferentes:
     - Desde imágenes de rostros en una carpeta llamada "persons_data". Sin embargo, esta sección está actualmente comentada (bloqueado), lo que significa que no se utiliza en la ejecución del programa.
     - Desde un archivo CSV llamado "encodings.txt". En este caso, se lee el archivo, se separan los nombres y encodings, y se almacenan en listas.

7. **Iniciación de la Cámara:** Inicia la cámara web (dispositivo de captura de video) para capturar video en tiempo real.

8. **Bucle Principal del Reconocimiento Facial:**
   - Captura cada fotograma (frame) de la cámara.
   - Detecta rostros en el fotograma utilizando la biblioteca face_recognition.
   - Si se detecta un rostro:
     - Compara el rostro con los rostros conocidos en la base de datos.
     - Registra el nombre del alumno si el rostro es reconocido.
     - Dibuja un rectángulo alrededor del rostro y muestra el nombre si es reconocido.
   - Muestra el FPS en el fotograma.
   - El bucle se puede detener manualmente presionando la tecla 'q'.

9. **Finalización y Resumen:**
   - Calcula el tiempo total de ejecución.
   - Libera la cámara.
   - Muestra un mensaje de cierre del programa, junto con el tiempo de ejecución y la liberación de la cámara.

## Root
Este código permite detectar y comparar rostros en un video en tiempo real con un rostro de referencia en una imagen estática. Puede ser útil para tareas de reconocimiento facial y autenticación.

### Funcionalidad:

1. **Importación de Bibliotecas:** El código importa las bibliotecas necesarias, incluyendo OpenCV (para el procesamiento de imágenes y video) y face_recognition (una librería de Python para reconocimiento facial).

2. **Carga de una Imagen Fija:** Carga una imagen estática llamada 'Frida.jpg' en la que se desea reconocer un rostro. Luego, detecta la ubicación del rostro en la imagen y calcula su codificación (encoding) para su posterior comparación con rostros en un video en tiempo real.

3. **Detección de Rostro en Imagen Fija:** Se incluye un bloque de código que está actualmente comentado, el cual dibuja un rectángulo alrededor del rostro detectado en la imagen estática y muestra la imagen con el rectángulo. Esta parte se utiliza para visualizar el proceso de detección en una imagen estática.

4. **Detección de Rostro en Video y Comparación con una Imagen:** El código inicia la cámara (o dispositivo de captura de video) y comienza a capturar fotogramas en tiempo real. Luego, detecta rostros en cada fotograma y compara cada rostro detectado con el rostro previamente codificado en la imagen estática.

   - Si se detecta un rostro en el video, se calcula su codificación.
   - Luego, se compara esta codificación con la codificación del rostro en la imagen estática.
   - Los resultados de la comparación se almacenan en la variable "results".
   - Si la comparación devuelve "True", significa que el rostro en el video coincide con el de la imagen estática; de lo contrario, devuelve "False".

5. **Visualización en Tiempo Real:** Muestra el video en tiempo real con rectángulos verdes alrededor de los rostros detectados. Además, imprime en la consola los resultados de comparación ("True" o "False") para cada rostro detectado en el video.

6. **Finalización del Programa:** El programa se puede detener manualmente presionando la tecla 'q'. Cuando se cierra, se liberan los recursos de la cámara y se termina la ejecución del programa.


## Referencias de librerías
* `face_recognition`: https://pypi.org/project/face-recognition/
* `opencv`: https://opencv.org/
