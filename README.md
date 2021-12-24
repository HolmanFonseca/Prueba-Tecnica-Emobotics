# Prueba-Tecnica-Emobotics
En este repositorio reponderé las preguntas para la prueba tecnica de la empresa Emobotics.
### 1.

Pre requisitos:
-python 
-Django
-Navicat(opcional)

-Para correr el proyecto hacer un clon del repositorio y correr en la terminal el siguiente comando dentro de la carpeta prueba:

python manage.py runserver

Con este comando el proyecto estara funcionando con normalidad.

si desea agregar un usuario nuevo:

ingrese en su navegador localhost:8000/usuario/registrar y digite los datos del nuevo usuario. Siga las intrucciones y a continuacion darle guardar.

si desea consultar un usuario:

ingrese en su navegador localhost:8000/consulta/usuario luego digite el username del usuario a consultar y se mostrara en pantalla los datos del usuario registrado.



### 2.
Se desea desarrollar una funcionalidad para una app móvil que permita obtener de los usuarios las respuestas a una secuencia de preguntas predeterminadas. Las preguntas deben hacerse una a la vez y la pregunta siguiente puede depender de la respuesta a la pregunta anterior. Describa brevemente que funciones implementaría en el backend para atender dicha funcionalidad de la app (No es necesario hacer código).
La secuencia de preguntas es la misma para todos los usuarios y debe almacenarse en el backend de la app ¿Que tipo de almacenamiento usaría para estas?

-R/ Se podria solucionar con un chatbot, el cual se desarrollaria de la misma manera que en el primer punto, con una api web en el backend, o alguna libreria de python debido a que alguno de los fuertes de este legunaje es la cantidad de librerias que pueden ser de gran utilidad, al tener el chatbot se predeterminaria las preguntas debido a que son las mismas para cada usuario, y agregarles ciertas condicionales teniendo en cuenta que algunas preguntas depende de otras, para finalizar almacenaria los datos de cada usuario en una base de datos como SQLite que viene por defecto en Django y utlizaria navicat para una mejor visualizacion de este.

Las funciones que implementaria:
 -Una funcion para pedir los datos al usuario.
 -Una funcion donde tenga todas las respuestas y sus respectivas condiciones.
 -Una ultima funcion para almacenar los datos en la base de datos.
 
 

### 3.
Se desea utilizar Inteligencia Artificial para generar voz humana a partir de oraciones escritas. ¿Qué tipo de modelo de AI utilizaría para esta tarea? ¿Qué tipo de dataset se necesita para entrenar el modelo a utilizar?

-R/ El modelo se entrenaria de la misma manera que se entrena un modelo de speech to text, con un dataset de audiolibros y libros digitales ya que nuestra red si o si tendria que aprender como se pronuncia la palabra y como se escribe, y para el modelo, utilizaria redes neuronales que se pueden implementar por medio de tensorflow, teniendo los audios sincronizados con los libros digitales, se dejaria un porcentaje para entrenar el cual seria el mayor porcentaje del dataset y un porcentaje de testeo. sin embargo como ya hay modelos entrenados como el de google o el de azure, reentrenaria estos modelos.


### 4.
Se desea desplegar el modelo anterior en Google Cloud Platform (GCP) para que pueda ser consultado desde el backend de la app. Explique brevemente qué servicio de GCP usaría para el despliegue y por qué.

-R/En primer lugar crearia el proyecto, habilitaria la api de google, de igual manera Se podria desarrollar creando una instancia con google cloud TPU, el cual seria una maquina virtual y se instalaria una libreria de tensorflow y asi poder desplegar el modelo. Una TPU es la unidad de procesamiento de google para tareas como machine learning y deep learning.Para las pruebas unitarias desde el backend utilizaria Django o fastAPI.

