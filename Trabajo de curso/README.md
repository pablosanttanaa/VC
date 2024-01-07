## Práctica 7. Trabajo de curso

Este repositorio contiene código en Python para el reconocimiento de gestos manuales utilizando la biblioteca OpenCV y el módulo cvzone. El sistema está diseñado para detectar gestos manuales en tiempo real a través de una cámara web y capturar imágenes de posturas específicas de las manos para entrenar un modelo de clasificación de gestos. 

## Motivación

Este proyecto surge con la idea de hacer algo útil para la sociedad. Queríamos echar una mano a quienes más lo necesitan, facilitar la vida de aquellos que enfrentan desafíos, como, por ejemplo, comunicarse.

La idea es que, a raíz de nuestro trabajo, se pueda utilizar o brindar ideas para desarrollar aplicaciones que faciliten la comunicación o el entendimiento de las personas con discapacidad auditiva o sordas que necesitan comunicarse con lenguaje de signos.

En resumen, la motivación que tuvimos es la necesidad de que todo el mundo pueda utilizar fácilmente las tecnologías y comunicarse entre sí, sin marginar a nadie.

## Objetivo

El objetivo de este trabajo consiste en diseñar un sistema de detección de gestos manuales en tiempo real mediante una cámara web y capturar imágenes de posturas específicas de las manos para entrenar un modelo de clasificación de gestos.
 
 ## Contenido

 - **dataCollection.py**: Este script captura posturas de manos en tiempo real utilizando la cámara web, recorta y redimensiona la región de la mano, y guarda las imágenes para entrenar un modelo.

- **test.py**: Este script utiliza el modelo entrenado para realizar el reconocimiento de gestos manuales en tiempo real. Captura posturas de manos, preprocesa las imágenes y predice los gestos correspondientes utilizando un modelo de clasificación preentrenado.

## Autores
[![GitHub](https://img.shields.io/badge/GitHub-Ana%20del%20Carmen%20Santana%20Ojeda-red?style=flat-square&logo=github)](https://github.com/AnaSantana016)
[![GitHub](https://img.shields.io/badge/GitHub-Pablo%20Santana-blue?style=flat-square&logo=github)](https://github.com/pablosanttanaa)

 ## Estructura de archivos:
 - **/Trabajo de curso/Model/keras_model.h5:** Modelo preentrenado de Keras para la clasificación de gestos manuales.

- **/Trabajo de curso/Model/labels.txt:** Archivo de texto que contiene las etiquetas correspondientes a los gestos manuales.

- **/C:/Users/Lenovo/Desktop/Data/Y:** Carpeta predeterminada para guardar las imágenes de posturas de manos capturadas. Puedes modificar la variable 'folder' en ambos scripts para cambiar la ubicación de almacenamiento.

 ## Uso
 - **1. dataCollection.py:**
    - Ejecuta el script para abrir la transmisión de la cámara web.
    - Coloca tu mano dentro del encuadre de la cámara y presiona la tecla 'S' para capturar y guardar una imagen de la postura de tu mano.
    - Repite el proceso para diferentes posturas de mano para recopilar un conjunto de datos diverso.
    - Presiona 'Q' para salir de la aplicación.

<div align="center">
    <!-- Fila 1 -->
    <div>
        <a href="./Imagenes/gesto1.jpg" target="_blank">
            <img src="./Imagenes/gesto1.jpg" alt="Imagen 1" width="300">
        </a>
        <a href="./Imagenes/gesto2.jpg" target="_blank">
            <img src="./Imagenes/gesto2.jpg" alt="Imagen 2" width="280">
        </a>
    </div>
</div>
<p>&nbsp;</p>


 - **2. test.py:**
    - Ejecuta el script para abrir la transmisión de la cámara web y realizar el reconocimiento de gestos manuales en tiempo real.
    - El gesto predicho se mostrará en la pantalla, junto con un cuadro delimitador alrededor de la mano detectada.
    - Presiona 'Q' para salir de la aplicación.

<div align="center">
    <!-- Fila 1 -->
    <div>
        <a href="./Imagenes/1.jpg" target="_blank">
            <img src="./Imagenes/1.jpg" alt="Imagen 1" width="300">
        </a>
        <a href="./Imagenes/2.jpg" target="_blank">
            <img src="./Imagenes/2.jpg" alt="Imagen 2" width="342">
        </a>
    </div>
</div>

<div align="center">
    <div>
        <a href="./Imagenes/3.jpg" target="_blank">
            <img src="./Imagenes/3.jpg" alt="Imagen 1" width="300">
        </a>
        <a href="./Imagenes/2.jpg" target="_blank">
            <img src="./Imagenes/4.jpg" alt="Imagen 2" width="350">
        </a>
    </div>
</div>
    

 ## Entrenamiento del modelo
 Para entrenar el modelo que se encuentran dentro de este repositorio, se ha hecho utilizando [Teachable Machine](https://teachablemachine.withgoogle.com/)

<div align="center">
    <div>
        <a href="./Imagenes/Entrenamiento.jpg" target="_blank">
            <img src="./Imagenes/Entrenamiento.jpg" alt="Imagen 8" width="600">
        </a>
    </div>
</div>

## Conclusión

Conclusión:

En resumen, hemos desarrollado una herramienta que no solo identifica movimientos de manos, sino que también busca promover la inclusión y accesibilidad tecnológica.

La motivación que impulsó este proyecto fue clara: queríamos crear algo beneficioso para la sociedad, especialmente para aquellos que enfrentan desafíos en su comunicación diaria. La idea de contribuir a la creación de aplicaciones que mejoren la calidad de vida de personas con discapacidad auditiva o sordas, facilitándoles la comunicación a través del lenguaje de signos, fue el motor detrás de nuestro esfuerzo.

Creemos que la accesibilidad a la tecnología debería ser un derecho universal, y este proyecto representa un modesto avance hacia ese ideal.

## Propuestas Adicionales

1. Interfaz de Modificación de Letras

Podríamos desarrollar una interfaz interactiva que permita al usuario no solo visualizar las letras detectadas, sino también editarlas según sea necesario, además de mostrar la frase completa. Esto ofrecería una forma más flexible y precisa de comunicarse utilizando gestos.

2. Integración en redes sociales

Integración de la herramienta en redes sociales para facilitar la comunicación en tiempo real. Esto podría incluir traducción automática de gestos a texto o incluso la posibilidad de enviar mensajes de video basados en los gestos capturados.

3. Entrenamiento Personalizado

Implementar un sistema de entrenamiento personalizado que permita a los usuarios adaptar la herramienta a sus gestos individuales, mejorando la precisión y la personalización de la experiencia.


## Tecnologias
  -  [Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
  - [TensorFlow](https://www.tensorflow.org/?hl=es-419)

## Librerias 
- [cvzone](https://pypi.org/project/cvzone/)
- [NumPy](https://numpy.org/)
- [Math](https://docs.python.org/3/library/math.html)
- [Time](https://docs.python.org/es/3/library/time.html)