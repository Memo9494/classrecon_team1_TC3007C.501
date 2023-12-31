# Modelo y refinamiento

En esta etapa, se investigan y evalúan diferentes modelos o enfoques para abordar el problema en cuestión. Se analizan las características de los datos y se selecciona el modelo que mejor se adapte a los requisitos del proyecto. Esto podría incluir la exploración de modelos de aprendizaje automático, algoritmos de análisis estadístico u otras técnicas pertinentes.

En lo que concierne al reto, el socio formador nos indicó que por la aplicación que se le daráa mos modelos requerimos de modelos de redes preentrenados. En el caso del reconocimiento facial, es necesario un data set robusto de rostros y que su entrenamiento requiere procesamiento con el que no se cuenta en este momento. Sabiendo esto, se investigaron distintos modelos preentrenados, se obtuvo uno de Dlib C++, el cual tiene una 99% de taza de precisión utilizando el benchmarck de Labeled Faces in the Wild, para el desarrollo de nuestro algoritmo integramos este modelo a través de la librería face_recognition. 

En lo que concierne a la detección de participación decidimos utilizar un modelo que nos permitiera obtener los keypoints de las articulaciones de una persona. Yolo (You only look once) tiene modelos preentremados que brindan como información, los bounding boxes de una persona, sus keypoints y contiene una función de trackeo en donde se le asigna IDs a las personas. Para el contexto del aula de clases no es necesario un entrenamiento ya que los movimientos que se ejercen ahí son lentos y accesibles de rastrear.

En el siguiente video se explica más afondo nuestra implementación: https://youtu.be/WVavTEa8yoE
En el documento presente, se busca solución a los requerimientos de la rúbrica.
