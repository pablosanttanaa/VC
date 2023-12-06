## Práctica 6. Análisis facial

Dentro de esta carpeta, se presenta el trabajo realizado para la sexta práctica de la asignatura de **Visión por Computador**. El objetivo principal de esta práctica es  la detección y el reconocimiento facial.

- **Primer reconocimiento facial**: En el primer reconocimiento facial, se utiliza la herramienta DeepFace para detectar, a través de la webcam, el género, la edad, la raza y las emociones de una persona.
- **Segundo reconocimiento facial**: En este segundo reconocimiento facial, empleamos la herramienta DeepFace para determinar la similitud de una persona con celebridades. Para llevar a cabo este proceso, utilizamos un conjunto de datos denominado [Celebrity Faces Dataset](https://www.kaggle.com/datasets/vishesh1412/celebrity-face-image-dataset/)

## Autores
[![GitHub](https://img.shields.io/badge/GitHub-Ana%20del%20Carmen%20Santana%20Ojeda-red?style=flat-square&logo=github)](https://github.com/AnaSantana016)
[![GitHub](https://img.shields.io/badge/GitHub-Pablo%20Santana-blue?style=flat-square&logo=github)](https://github.com/pablosanttanaa)

## Primer reconocimiento facial

- **Paso 1. Añadimos una imagen**: Para que las letras que nos permiten identificar se vean más claras, hemos decidido añadir una imagen de fondo que contiene emoticonos asociados a cada una de las características que vamos a analizar de la persona. Esto facilitará la identificación de cada elemento.
- **Paso 2. Analizamos a la persona**: Utilizamos DeepFace para analizar la edad, el género, la raza y las emociones de la persona.
- **Paso 3. Mostramos los datos**: Presentamos los resultados sobre la imagen incorporada para mejorar la legibilidad.

A continuación, se adjunta un gif del detector de rasgos de una persona:

<!-- Gif de detector de rasgos de una persona -->
<div align="center">
    <div>
        <a href="./P6/readme/detector.gif" target="_blank">
            <img src="./P6/readme/detector.gif" alt="Dectetor de rasgos" width="300">
        </a>
    </div>
</div>

## Segundo reconocimiento facial

- **Paso 1. Cargamos los recursos necesarios**: Cargamos nuestro conjunto de datos y la imagen que usaremos para la comparación. Verificamos la existencia de la imagen y recorremos el conjunto de datos hasta encontrar una imagen.
- **Paso 2. Analizamos el parecido**: Utilizando la herramienta DeepFace, comparamos la imagen con el conjunto de datos. Si existe una similitud notable, concluimos que se trata de la persona famosa. En caso contrario, proporcionamos información sobre a quién se asemeja y el grado de similitud.

 
## Tecnologias
  -  [Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)

## Librerias 
  - [OpenCV](https://img.shields.io/badge/OpenCV-Latest-brightgreen?style=flat-square&logo=opencv)
  - [DeepFace](https://github.com/serengil/deepface)
  - [os](https://docs.python.org/3/library/os.html)