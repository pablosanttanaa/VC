## Práctica 5. Detector de matrículas

Dentro de esta carpeta, se presenta el trabajo realizado para la quinta práctica de la asignatura de **Visión por Computador**. El objetivo principal de esta práctica es desarrollar un prototipo de sistema capaz de identificar la matrícula de un vehículo, en nuestro caso, hemos optado por detectar las matrículas a partir de imágenes.

Para facilitar la consecución de este propósito, se proporciona un modelo de detección de objetos, **YOLOv8**, que se empleará para la detección de vehículos. Además, para el reconocimiento de texto, se ha trabajado con **pytesseract**.

- **Primer Detector**: Para el primer detector, desglosaremos el proceso de detección de matrículas en tres partes. En primer lugar, nos enfocaremos en la identificación de vehículos en una imagen utilizando el modelo YOLOv8. Una vez obtenidas las detecciones de vehículos, procederemos a realizar un procesamiento en la imagen del vehículo detectado para buscar formas rectangulares, que corresponden a las matrículas. Por último, haremos uso de **pytesseract** para obtener el texto de la matrícula.
- **Segundo Detector**: En este segundo detector, entrenamos nuestro propio modelo basado en **YOLOv8** con el fin de que detecte las matrículas de las imágenes.

## Autores
[![GitHub](https://img.shields.io/badge/GitHub-Ana%20del%20Carmen%20Santana%20Ojeda-red?style=flat-square&logo=github)](https://github.com/AnaSantana016)
[![GitHub](https://img.shields.io/badge/GitHub-Pablo%20Santana-blue?style=flat-square&logo=github)](https://github.com/pablosanttanaa)

## Primer detector

- **Paso 1. Carga del Modelo YOLO**: Se carga el modelo YOLO previamente entrenado.
- **Paso 2. Detección de Vehículos**: Se realiza la detección de objetos en la imagen utilizando YOLO. Si se encuentra un vehículo, se resalta en la imagen original y se muestra la región de interés alrededor del vehículo.
- **Paso 3. Detección de Matrículas (si se detecta un vehículo)**: Se convierte la región de interés (ROI) alrededor del vehículo a escala de grises y se aplica un umbral. Luego, se buscan los contornos y se filtran aquellos en la mitad inferior de la imagen. Se identifica el contorno más grande, que se asume como la matrícula del vehículo. Se muestra la matrícula y se utiliza Tesseract OCR para reconocer el texto.

A continuación se adjuntan las figuras del proceso descrito:

<p>&nbsp;</p>

<!-- Filas de dos fotos cada una -->
<div align="center">
    <!-- Fila 1 -->
    <div>
        <a href="./P5/Readme Images/1.jpg" target="_blank">
            <img src="./P5/Readme Images/1.jpg" alt="Imagen 1" width="300">
        </a>
        <a href="./P5/Readme Images/2.jpg" target="_blank">
            <img src="./P5/Readme Images/2.jpg" alt="Imagen 2" width="300">
        </a>
    </div>
</div>

<div align="center">
    <div>
        <a href="./P5/Readme Images/1.jpg" target="_blank">
            <img src="./P5/Readme Images/3.jpg" alt="Imagen 1" width="300">
        </a>
        <a href="./P5/Readme Images/2.jpg" target="_blank">
            <img src="./P5/Readme Images/4.jpg" alt="Imagen 2" width="300">
        </a>
    </div>
</div>

<div align="center">
    <div>
        <a href="./P5/Readme Images/1.jpg" target="_blank">
            <img src="./P5/Readme Images/5.jpg" alt="Imagen 1" width="300">
        </a>
        <a href="./P5/Readme Images/2.jpg" target="_blank">
            <img src="./P5/Readme Images/6.jpg" alt="Imagen 2" width="300">
        </a>
    </div>
</div>
<div align="center">
    <div>
        <a href="./P5/Readme Images/1.jpg" target="_blank">
            <img src="./P5/Readme Images/7.jpg" alt="Imagen 1" width="300">
        </a>
    </div>
</div>
<div align="center">
    <div>
        <a href="./P5/Readme Images/1.jpg" target="_blank">
            <img src="./P5/Readme Images/8.jpg" alt="Imagen 1" width="600">
        </a>
    </div>
</div>

## Segundo detector

- **Paso 1. Elegimos el Dataset**: Elegimos el dataset de [Roboflow Dataset](https://universe.roboflow.com/itrc/plate-detection-y5). Modificamos las carpetas del Dataset para tener la estructura correcta.
- **Paso 2. Creamos el archivo plates.yaml**: Creamos el archivo con el directorio de nuestro Dataset, el número de clases (en nuestro caso solo es uno, ya que es de matrículas) y, por último, el nombre de la clase.
- **Paso 3. Entrenamiento**: Para entrenar, utilizaremos el siguiente comando:

```
yolo detect train model=yolov8n.pt data=plates.yaml imgsz=640 batch=4 device=CPU epochs=40
```

<div align="center">
    <div>
        <a href="./P5/Readme Images/entrenamiento.jpg" target="_blank">
            <img src="./P5/Readme Images/entrenamiento.png" alt="Imagen 8" width="600">
        </a>
    </div>
</div>

- **Paso 4. Detectar matrículas**: Para finalizar, solo queda utilizar "matricula.pt" en nuestro segundo detector. El segundo detector obtiene la caja que representa la matrícula, marcamos la matrícula del coche y extraemos la matrícula.

<div align="center">
    <div>
        <a href="./P5/Readme Images/coche_con_matricula.jpg" target="_blank">
            <img src="./P5/Readme Images/coche_con_matricula.png" alt="Imagen 9" width="600">
        </a>
    </div>
</div>
<div align="center">
    <div>
        <a href="./P5/Readme Images/matricula.jpg" target="_blank">
            <img src="./P5/Readme Images/matricula.png" alt="Imagen 10" width="600">
        </a>
    </div>
</div>
 
## Tecnologias
  -  [Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
  -  [YOLOv8](https://docs.ultralytics.com/quickstart/)
  -  [Tesseract](https://github.com/tesseract-ocr/tesseract)
## Librerias 
  - [OpenCV](https://img.shields.io/badge/OpenCV-Latest-brightgreen?style=flat-square&logo=opencv)
  - [Pytesseract](https://pypi.org/project/pytesseract/)
