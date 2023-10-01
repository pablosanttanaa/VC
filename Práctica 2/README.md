# Práctica 2 - Funciones básicas de OpenCV

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

1. [Cuenta de píxeles blancos por filas](#cuenta-de-píxeles-blancos-por-filas)
2. [Imagen resultado de Sobel](#imagen-resultado-de-sobel)
3. [Imagen resultante de Sobel 8 bits](#imagen-resultado-de-sobel-8-bits)
4. [Función de un Umbral](#función-de-un-umbral)
5. [Reinterpretación del procesamiento de imágenes](#reinterpretación-del-procesamiento-de-imágenes)
6. [Conclusión](#conclusión)

## Cuenta de píxeles blancos por filas

Este código procesa la imagen 'mandril.jpg' para contar píxeles blancos en cada fila y columna después de aplicar el operador Canny para detectar bordes. Luego, normaliza los resultados y muestra gráficos de estas cuentas. La cuarta subtrama muestra ambas cuentas. El eje x de los gráficos está limitado al ancho de la imagen.

## Imagen resultado de Sobel

Para esta tarea decidimos utilizar una imagen de un gatito y le añadimos un filtro Gaussiano para quitar el ruido. Calculamos los gradientes horizontal y vertical para detectar bordes. Para finalizar muestramos tres imágenes: gradientes verticales, gradientes horizontales y la combinación de ambos para resaltar los bordes en la imagen.

## Imagen resultante de Sobel 8 bits

En el siguiente apartado procesamos la imagen del gatito, suaviza, detecta bordes y analiza la distribución de píxeles blancos en la imagen. Las gráficas resultantes muestran cómo los bordes están distribuidos en la imagen.

## Función de un Umbral

Utilizamos la webcam en tiempo real y aplicamos un efecto espejo a la imagen. Luego, realizamos una umbralización en el fotograma y mostramos el resultado en una ventana.

## Reinterpretación del procesamiento de imágenes

Finalmente realizamos una especie de filtro. Con la cámara web detectamos el rostro y le añadimos una imagen cada vez que detecte el rostro de una persona.

## Conclusión

Estos ejercicios demuestran una variedad de técnicas de procesamiento de imágenes. Desde el análisis de bordes en imágenes estáticas utilizando el operador Canny y el filtro Sobel, hasta la aplicación de efectos en tiempo real a través de una cámara web, cada parte muestra cómo se pueden manipular y analizar imágenes para diferentes propósitos. 

## Bibliografía

1. [W3Schools - Color Picker](https://www.w3schools.com/colors/colors_picker.asp)
2. [GeeksforGeeks - OpenCV cv2.imshow Method](https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/)
3. [GeeksforGeeks - OpenCV cv2.circle Method](https://www.geeksforgeeks.org/python-opencv-cv2-circle-method/)
4. [OpenCV Documentation - Drawing Functions](https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html)
5. [OpenCV Documentation - VideoCapture Class](https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html)