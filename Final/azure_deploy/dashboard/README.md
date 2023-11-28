
# Dashboard

## Funcionalidad de los archivos


- **views**: En este archivo se generan las vistas al utilizar los htmls de la carpeta de template, este es el verdadero "backend" dado que aqui se le pasan los argumentos al fron-end para que los visualize e interactue el usuario.

En este archivo de views se encuentran diferentes classes que sirven al momento de realizar las vistas, especificamente las siguientes:

- HomeView nos puestra los cursos a los que esta inscrito nuestro usuario

- DetailView manda contexto de ciertos datos que se obtienen de los objetos que buscamos en la vista especifica, por ejemplo queremos que se muestren los datos del curso que estamos viendo, asi como los maestros y alumnos asignados a ese curso.

- la funcion videofeed es aquella que se encarga de tomar asistencia, esta llama a la funcion gen, que a su vez utiliza un objeto que es la clase utilziada en cuestion, esta se diide en tres funciones __init__, get_frame y __del__ que se encargan de cargar los modelos, y utilizarlos iterativamente con el proceso descrito en la documentacion de Face_recognition y participacion, todo esto se pasa por bytes al front donde se reconstruye la imagen cuadro por cuadro.