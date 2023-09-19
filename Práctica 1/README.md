# Práctica 1 - Primeros pasos con OpenCV

En esta práctica, se realizaron varios ejercicios de procesamiento de imágenes utilizando la biblioteca OpenCV en Python. No es necesario instalar ninguna biblioteca adicional para ejecutar estos ejercicios.

## Autores
[![GitHub](https://img.shields.io/badge/GitHub-Ana%20del%20Carmen%20Santana%20Ojeda-red?style=flat-square&logo=github)](https://github.com/AnaSantana016)
[![GitHub](https://img.shields.io/badge/GitHub-Pablo%20Santana-blue?style=flat-square&logo=github)](https://github.com/pablosanttanaa)

## Tecnologias
  -  Python: ![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)

## Librerias 
  - OpenCV: ![OpenCV](https://img.shields.io/badge/OpenCV-Latest-brightgreen?style=flat-square&logo=opencv)
  - Matplotlib: ![Matplotlib](https://img.shields.io/badge/Matplotlib-Latest-yellow?style=flat-square&logo=matplotlib)
  - NumPy: ![NumPy](https://img.shields.io/badge/NumPy-Latest-blueviolet?style=flat-square&logo=numpy)

## Índice

1. [Ajedrez](#ajedrez)
2. [Mondrian](#mondrian)
3. [Modificar un plano de la imagen](#modificar-un-plano-de-la-imagen)
4. [Pintar círculos en posiciones de píxeles claros y oscuros](#pintar-círculos-en-posiciones-de-píxeles-claros-y-oscuros)
5. [Crear un efecto Pop Art personalizado](#crear-un-efecto-pop-art-personalizado)
6. [Conclusión](#conclusión)

## Ajedrez

Este ejercicio genera una imagen de un tablero de ajedrez en blanco y negro. Modificamos las dimensiones del tablero, nos creamos una imagen de un único plano con niveles de grises y recorremos nuestro tablero pintando las celdas de blanco y negro.

## Mondrian

Primeramente para el apartado de Mondrian, comenzamos con una imagen en blanco y se agregan cuadrados de diferentes colores en posiciones específicas para crear la imagen. Además se dibujan líneas negras para dividir los cuadrados.

## Modificar un plano de la imagen

En este apartado utilizamos la cámara web para capturar video en tiempo real. Luego, separamos los canales de color (rojo, verde y azul) de cada fotograma y realizamos una operación de modificación en uno de los canales. Concatena los tres canales nuevamente y mostramos el video resultante con la modificación.

## Pintar círculos en posiciones de píxeles claros y oscuros

Por otra parte, en este apartado utilizamos la cámara web para buscar la zona 8x8 más clara y más oscura en cada fotograma en función de la suma de los valores de los canales de color. Se dibujan círculos rojos en la zona más clara y círculos verdes en la zona más oscura para resaltar estas áreas en el video.

## Crear un efecto Pop Art personalizado

Finalmente realizamos un Pop Art. Con la cámara web tomamos el canal de color de cada píxel (rojo, verde y azul) y aplicamos una manipulación específica en cada uno de los nueve cuadrantes de la imagen. Esto crea una composición de estilo "pop art" en tiempo real, donde los colores y las intensidades se modifican para lograr un efecto visual interesante y artístico.

## Conclusión

Estos ejercicios nos han ayudado a comprender mejor los distintos métodos de la librería OpenCV para analizar distintos aspectos de las imagenes o vídeos, como puede ser las sombras, colores, luces...


## Bibliografía

1. [W3Schools - Color Picker](https://www.w3schools.com/colors/colors_picker.asp)
2. [GeeksforGeeks - OpenCV cv2.imshow Method](https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/)
3. [GeeksforGeeks - OpenCV cv2.circle Method](https://www.geeksforgeeks.org/python-opencv-cv2-circle-method/)
4. [OpenCV Documentation - Drawing Functions](https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html)
5. [OpenCV Documentation - VideoCapture Class](https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html)