## Práctica 4. Detección de caras

En esta cuarta práctica se plantean hacer un filtro detectando nuestra cara. Tenemos dos filtros en el primero superponemos una imagen a nuestro rostro y en el segundo filtro detectamos los ojos y le añadimos un filtro de desenfoque a nuestro ojos.

## Autores
[![GitHub](https://img.shields.io/badge/GitHub-Ana%20del%20Carmen%20Santana%20Ojeda-red?style=flat-square&logo=github)](https://github.com/AnaSantana016)
[![GitHub](https://img.shields.io/badge/GitHub-Pablo%20Santana-blue?style=flat-square&logo=github)](https://github.com/pablosanttanaa)

## Tecnologias
  -  Python: ![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)

## Librerias 
  - OpenCV (cv2): [![OpenCV (cv2)](https://img.shields.io/badge/OpenCV (cv2)-Latest-brightgreen?style=flat-square&logo=opencv)](https://opencv.org/)
  - FaceNormalizationUtils: [![FaceNormalizationUtils](https://img.shields.io/badge/FaceNormalizationUtils-Latest-blue?style=flat-square)](https://github.com/tu_usuario/FaceNormalizationUtils)
  - time: [![time](https://img.shields.io/badge/time-Latest-blue?style=flat-square)](https://github.com/tu_usuario/time)
  - FaceDetectors: [![FaceDetectors](https://img.shields.io/badge/FaceDetectors-Latest-blue?style=flat-square)](https://github.com/tu_usuario/FaceDetectors)


## Índice

1. [Primer filtro](#primer-filtro)
2. [Segundo filtro](#segundo-filtro)
3. [Conclusión](#conclusión)

## Primer filtro



## Segundo filtro

El segundo filtro se encuentra en el archivo "VC_P4_deepface.ipynb". Este filtro utiliza la clase "FaceDetector", que incluye un método denominado "DetectLargestFaceEyesDNN" diseñado para la detección de caras y ojos. Una vez que se ha detectado una cara y los ojos, se procede a dibujar un rectángulo alrededor de la cara, creando también una región correspondiente a los ojos. A continuación, aplicamos un efecto de desenfoque gaussiano a la región de los ojos con el fin de lograr un efecto de desenfoque atractivo. Finalmente, reemplazamos la región de los ojos previamente difuminada en la imagen original.

![Segundo Filtro](segundo-filtro.gif)

## Conclusión



## Bibliografía

