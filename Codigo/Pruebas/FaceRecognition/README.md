# Face Recognition
Este código es un programa de reconocimiento facial que utiliza la biblioteca OpenCV y Face Recognition para detectar y reconocer rostros en un video en tiempo real. A continuación, se presenta una descripción detallada del código:

## Asistencia_FR
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

## Varios Rostros Xframe_FR
Este código se utiliza para realizar el reconocimiento facial en un entorno de video en tiempo real, comparando los rostros detectados con los rostros previamente registrados. La asistencia se registra automáticamente si se reconoce un rostro registrado. La configuración del programa permite cargar los datos de los alumnos desde imágenes de rostros o desde un archivo CSV, lo que brinda flexibilidad en la fuente de datos.

# Funcionalidad:

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

## 3. Documentación
En esta etapa, se busca presentar los avances en cuanto a la documentación del proceso realizado en función de la metodología.

* `MR3_Documentacion`

## 4. Modelo y refinamiento
En esta etapa, se investigan y evalúan diferentes modelos o enfoques para abordar el problema en cuestión. Se analizan las características de los datos y se selecciona el modelo que mejor se adapte a los requisitos del proyecto. Esto podría incluir la exploración de modelos de aprendizaje automático, algoritmos de análisis estadístico u otras técnicas pertinentes.

* `MR4_ModeloRefinamiento`

## 5. Evaluación
En esta etapa, se analizan los requerimientos y los datos disponibles y se determinan los tipo de pruebas y métricas que permitirán saber si realmente están cumpliendo con su objetivo y generar diagnósticos del modelo.

* `MR5_Evaluacion`
