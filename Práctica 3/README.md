## Práctica 3. Detección de formas

En esta práctica, se llevaron a cabo tres ejercicios con el objetivo de extraer información geométrica de los objetos presentes en una imagen. Para el último ejercicio, tuvimos que instalar dos librerías. Una de ellas es "seaborn", la cual se utiliza para la visualización de datos y está construida sobre Matplotlib. La segunda es "scikit-learn", también conocida como "sklearn", cuyo propósito es proporcionar una amplia gama de algoritmos y herramientas para llevar a cabo tareas comunes en el campo del aprendizaje automático.

## Autores
[![GitHub](https://img.shields.io/badge/GitHub-Ana%20del%20Carmen%20Santana%20Ojeda-red?style=flat-square&logo=github)](https://github.com/AnaSantana016)
[![GitHub](https://img.shields.io/badge/GitHub-Pablo%20Santana-blue?style=flat-square&logo=github)](https://github.com/pablosanttanaa)

## Tecnologias
  -  Python: ![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)

## Librerias 
  - OpenCV: ![OpenCV](https://img.shields.io/badge/OpenCV-Latest-brightgreen?style=flat-square&logo=opencv)
  - Matplotlib: ![Matplotlib](https://img.shields.io/badge/Matplotlib-Latest-yellow?style=flat-square&logo=matplotlib)
  - NumPy: ![NumPy](https://img.shields.io/badge/NumPy-Latest-blueviolet?style=flat-square&logo=numpy)
  - Seaborn: ![Seaborn](https://img.shields.io/badge/Seaborn-Latest-orange?style=flat-square&logo=seaborn)
  - scikit-learn (sklearn): ![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-blue?style=flat-square&logo=scikit-learn)


## Índice

1. [Total de monedas](#total-de-monedas)
2. [Cantidad de dinero](#cantidad-de-dinero)
3. [Microplásticos](#microplásticos)
4. [Conclusión](#conclusión)

## Total de monedas

En el siguiente ejercicio, se trataba de sacar una foto que incluyera monedas no solapadas y otro objeto, teníamos que contar la cantidad de monedas que había en la imagen. En nuestro caso, optamos por crear una imagen que contuviera tanto monedas como un billete. A continuación, realizamos las siguientes operaciones:

-Convertimos la imagen a formato RGB y la transformamos a escala de grises.

-Utilizamos el algoritmo HoughCircles de OpenCV para detectar los círculos en la imagen, ajustando parámetros como el valor del gradiente y los radios mínimo y máximo.

-Una vez que el algoritmo reconoce las monedas en la imagen, procedemos a contarlas y devolver el número total de monedas presentes.

A continuación, se muestra el resultado de la detección de monedas en la imagen:

![Resultado de la Detección de Monedas](total_de_monedas.png)

## Cantidad de dinero



## Microplásticos



## Conclusión



## Bibliografía

1. []()
2. []()
3. []()
4. []()