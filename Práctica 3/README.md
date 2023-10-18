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

En el siguiente ejercicio, se trataba de sacar una foto que incluyera monedas no solapadas y otro objeto, teníamos que contar la cantidad de monedas que había en la imagen. En nuestro caso, optamos por crear una imagen que tuviera tanto monedas como un billete. A continuación, realizamos las siguientes operaciones:

-Convertimos la imagen a formato RGB y la transformamos a escala de grises.

-Utilizamos el algoritmo HoughCircles de OpenCV para detectar los círculos en la imagen, ajustando parámetros como el valor del gradiente y los radios mínimo y máximo.

-Una vez que el algoritmo reconoce las monedas en la imagen, procedemos a contarlas y devolver el número total de monedas presentes.

A continuación, se muestra el resultado de la detección de monedas en la imagen:

![Resultado de la Detección de Monedas](total_de_monedas.png)

## Cantidad de dinero

Para el siguiente apartado cogemos dos imagenes, una que es 'dinero.jpg' que la utilizamos en el anterior ejercicio y otra que es 'Solapadas.jpg' que contiene monedas solapadas y consiste en detectar la moneda de 1€ y una vez clickes, te cuente la cantidad de dinero que hay en la imagen. 

Lo primero que hacemos es convertir la imagen en formato RGB para asegurarnos de que se muestre correctamente y a su vez la convertimos a escala de grises. Detectamos los círculos en la imagen como en el anterior ejercicio. 

Verificamos si se han detectado círculos en la imagen, y si es así, iteramos a través de ellos. Para cada círculo detectado, definimos una Región de Interés (ROI) alrededor del círculo. Calculamos la relación de aspecto del ROI para determinar si se trata de una moneda. Dependiendo del tamaño del radio del círculo, sumamos un valor correspondiente al "total". Las monedas se reconocen según su diámetro aproximado.

Finalmente, redimensionamos la imagen resultante y la mostramos en una ventana de visualización. También hemos implementado una función para manejar clics en la imagen resultante. Al hacer clic en la imagen, se muestra la cantidad total de monedas detectadas en la imagen.

Tenemos que destacar que con la imagen solapada no funciono debido a que el algoritmo HoughCircles no es capaz de dectectar media circuferencias o circuferencias que esten inclinadas.

![Resultado de la Detección de la Moneda de 1€](cantidad_de_dinero.png)

## Microplásticos

En este último ejercicio, consiste en crear una matriz de confusión a raiz de las imagenes de microplásticos. Lo que hacemos es cargar, procesar y mostrar tres imágenes de microplásticos en escala de grises, con el propósito de eliminar las sombras y aplicar un filtro de suavizado a las imágenes.

![Microplásticos](microplasticos.png)

Luego lo que hacemos es segmentar las regiones de interés en las imágenes y resaltar las áreas de mayor interés. Los valores de umbral se han ajustado para lograr la segmentación deseada. 

![Segmentación](segmentacion.png)

Para finalizar el ejercicio, lo que hacemos es contarmos las imagenes y clasificamos elementos en imágenes en tres categorías distintas y visualiza los resultados a través de una matriz de confusión.

![Matriz de Confusión](matriz.png)

## Conclusión



## Bibliografía

1. []()
2. []()
3. []()
4. []()