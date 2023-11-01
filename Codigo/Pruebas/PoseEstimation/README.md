# Pose Estimation
Estos códigos consisten en programas de detección de pose de varias personas en un frame. La implementación de esta solución requirió de múltiples iteraciones las principales son:

* Pose detection con mediapipe **_root_posedetection_mediapipe_**
* Pose detection con Yolov8 **_posedetection_yolov8_**

A continuación, se presenta una descripción detallada del código:

## [Pose Detection - Mediapipe](https://github.com/Memo9494/classrecon_team1_TC3007C.501/blob/main/Codigo/Pruebas/PoseEstimation/root_posedetection_mediapipe.py)

Este código demuestra el uso de la biblioteca **MediaPipe** para realizar la detección de poses humanas en tiempo real a través de una cámara web.

### Metadatos:

- **Basado en:** Este código se basa en un tutorial disponible en el repositorio de GitHub: [Nick Nochnack - Media Pipe Pose Tutorial](https://github.com/nicknochnack/MediaPipePoseEstimation/blob/main/Media%20Pipe%20Pose%20Tutorial.ipynb).

### Funcionalidad:

1. **Importación de Bibliotecas:**
   - `cv2`: OpenCV, se utiliza para la captura de vídeo y el procesamiento de imágenes.
   - `mediapipe as mp`: La biblioteca MediaPipe, que proporciona soluciones de visión por computadora preentrenadas.
   - `numpy as np`: Utilizado para operaciones numéricas y manipulación de matrices.

2. **Inicialización de MediaPipe:**
   - Se inicia una instancia de `mp_pose.Pose` para la detección de poses humanas.
   - Se establecen umbrales mínimos de detección y seguimiento de confianza.

3. **Conexión a la Cámara:**
   - El código se conecta a la cámara web para capturar vídeo en tiempo real.
   - Muestra un mensaje indicando que la cámara está conectada.

4. **Bucle Principal:**
   - El bucle principal se ejecuta mientras la cámara está abierta.
   - Captura continuamente fotogramas de la cámara.

5. **Procesamiento de la Imagen:**
   - Los fotogramas se convierten de BGR a RGB para el procesamiento con MediaPipe.
   - Se deshabilita la capacidad de escritura de la imagen para garantizar la eficiencia del procesamiento.
   - Se utiliza MediaPipe para detectar las poses en la imagen procesada.
   - Luego, la imagen se convierte nuevamente de RGB a BGR para visualizarla en OpenCV.

6. **Detección de Puntos Clave del Cuerpo:**
   - Se extraen los puntos clave del cuerpo humano detectados por MediaPipe.
   - El código muestra la posición de la muñeca izquierda, la muñeca derecha y el ojo izquierdo en la imagen, junto con sus coordenadas.

7. **Conteo de Participación:**
   - El código realiza un seguimiento de la participación de una persona en función de la posición de su muñeca izquierda en relación con su ojo izquierdo.
   - Si la muñeca está por debajo del ojo, se considera que está en una posición "bajada".
   - Si la muñeca está por encima del ojo y estaba en una posición "bajada", se registra como una participación.
   - El recuento de participaciones se muestra en la imagen.

8. **Visualización:**
   - Los resultados de la detección de poses se visualizan en la imagen con círculos y líneas de conexión entre los puntos clave del cuerpo.

9. **Finalización del Programa:**
   - El programa se puede detener manualmente presionando la tecla 'q'.
   - Cuando se cierra, se liberan los recursos de la cámara.

En resumen, este código utiliza la biblioteca MediaPipe para detectar y rastrear poses humanas en tiempo real a través de una cámara web. También realiza un seguimiento de la participación de una persona en función de la posición de su muñeca en relación con su ojo, lo que lo hace útil para aplicaciones como el seguimiento de la atención en un entorno educativo.

## [Pose detection - Yolov8](https://github.com/Memo9494/classrecon_team1_TC3007C.501/blob/main/Codigo/Pruebas/PoseEstimation/posedetection_yolov8.py)

Este código muestra cómo usar el modelo YOLO (You Only Look Once) para la detección de objetos, con un enfoque en la detección de poses humanas. A continuación, se proporciona una documentación detallada del código:

### Funcionalidad:

1. **Importación de Bibliotecas:**
   - `from ultralytics import YOLO`: Se importa la clase `YOLO` de la biblioteca Ultralytics, que permite realizar detección de objetos.
   - `cv2`: OpenCV, se utiliza para la captura de video y el procesamiento de imágenes.
   - `numpy as np`: Utilizado para operaciones numéricas y manipulación de matrices.
   - `from pydantic import BaseModel`: Se importa la clase `BaseModel` de la biblioteca Pydantic para definir una clase de puntos clave del cuerpo.

2. **Definición de Puntos Clave del Cuerpo:**
   - Se define una clase `GetKeypoint` que hereda de `BaseModel` para definir constantes numéricas correspondientes a puntos clave del cuerpo humano. Esto facilita el acceso a estos puntos clave más adelante.

3. **Carga del Modelo YOLO:**
   - Se carga un modelo YOLO preentrenado (`yolov8n-pose.pt`) utilizando la clase `YOLO` de Ultralytics.
   - Se muestra un mensaje indicando que el modelo se ha cargado con éxito.

4. **Conexión a la Cámara:**
   - El código se conecta a la cámara web para capturar video en tiempo real.
   - Muestra un mensaje indicando que la cámara está conectada.

5. **Bucle Principal:**
   - El bucle principal se ejecuta mientras la cámara está abierta y se encuentra disponible para capturar fotogramas.

6. **Procesamiento de la Imagen y Detección de Objetos:**
   - Se lee un fotograma de la cámara.
   - Se utiliza el modelo YOLO para realizar la detección de objetos en el fotograma con una confianza mínima de 0.5.
   - Se visualiza el resultado de la detección en el fotograma original. Los cuadros delimitadores de los objetos detectados se dibujan en el fotograma.

7. **Extracción de Puntos Clave del Cuerpo:**
   - Se extraen los puntos clave del cuerpo detectados por el modelo YOLO.
   - Estos puntos clave incluyen la muñeca izquierda, muñeca derecha, ojos, etc.
   - Los puntos clave se utilizan para calcular las coordenadas de rectángulos que rodean el rostro de la persona detectada.

8. **Visualización de Resultados:**
   - Los rectángulos que rodean el rostro de las personas detectadas se dibujan en el fotograma.
   - Las coordenadas de los rectángulos se muestran en la imagen.

9. **Participación y Conteo (Comentado):**
   - El código incluye una sección para realizar un seguimiento de la participación de una persona según la posición de su muñeca en relación con su ojo.
   - Sin embargo, esta sección se encuentra comentada y no está en uso.

10. **Finalización del Programa:**
    - El programa se puede detener manualmente presionando la tecla 'q'.
    - Cuando se cierra, se liberan los recursos de la cámara.

En resumen, este código muestra cómo cargar un modelo YOLO preentrenado y utilizarlo para detectar objetos en tiempo real desde una cámara web. También se extraen los puntos clave del cuerpo y se visualizan los rectángulos que rodean los rostros de las personas detectadas en el fotograma.

## Referencias de librerías
* `Mediapipe`: https://developers.google.com/mediapipe/solutions/vision/pose_landmarker
* `Yolov8`: https://docs.ultralytics.com/tasks/pose/
