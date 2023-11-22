## Práctica 5. Detector de matrículas

Dentro de esta carpeta, se presenta el trabajo realizado para la quinta práctica de la asignatura de **Visión por Computador**. El objetivo principal de esta práctica es desarrollar un prototipo de sistema capaz de identificar la matrícula de un vehículo, en nuestro caso, hemos optado por detectar las matrículas a partir de imágenes.

Para facilitar la consecución de este propósito, se proporciona un modelo de detección de objetos, **YOLOv8**, que se empleará para la detección de vehículos. Además, para el reconocimiento de texto, se ha trabajado con **pytesseract**.

- **Primer Detector**: Para el primer detector, desglosaremos el proceso de detección de matrículas en tres partes. En primer lugar, nos enfocaremos en la identificación de vehículos en una imagen utilizando el modelo YOLOv8. Una vez obtenidas las detecciones de vehículos, procederemos a realizar un procesamiento en la imagen del vehículo detectado para buscar formas rectangulares, que corresponden a las matrículas. Por último, haremos uso de **pytesseract** para obtener el texto de la matrícula.
- **Segundo Detector**: En este segundo detector, entrenamos nuestro propio modelo basado en **YOLOv8** con el fin de que detecte las matrículas de las imágenes.

## Autores
[![GitHub](https://img.shields.io/badge/GitHub-Ana%20del%20Carmen%20Santana%20Ojeda-red?style=flat-square&logo=github)](https://github.com/AnaSantana016)
[![GitHub](https://img.shields.io/badge/GitHub-Pablo%20Santana-blue?style=flat-square&logo=github)](https://github.com/pablosanttanaa)

## Primer detector

- 1. **Carga del Modelo YOLO**: Se carga el modelo YOLO previamente entrenado.
- 2. **Detección de Vehículos**: Se realiza la detección de objetos en la imagen utilizando YOLO. Si se encuentra un vehículo, se resalta en la imagen original y se muestra la región de interés alrededor del vehículo.
- 3. **Detección de Matrículas (si se detecta un vehículo)**: Se convierte la región de interés (ROI) alrededor del vehículo a escala de grises y se aplica un umbral. Luego, se buscan los contornos y se filtran aquellos en la mitad inferior de la imagen. Se identifica el contorno más grande, que se asume como la matrícula del vehículo. Se muestra la matrícula y se utiliza Tesseract OCR para reconocer el texto.

## Segundo detector





## Tecnologias
  -  Python: ![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
  -  YOLOv8: ![YOLOv8](https://docs.ultralytics.com/quickstart/)
  -  Tesseract: ![Tesseract](https://github.com/tesseract-ocr/tesseract)
## Librerias 
  - OpenCV: ![OpenCV](https://img.shields.io/badge/OpenCV-Latest-brightgreen?style=flat-square&logo=opencv)
  - Pytesseract: ![Pytesseract](https://pypi.org/project/pytesseract/)
