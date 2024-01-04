import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
from cvzone.ClassificationModule import Classifier


# Inicializar la cámara y el detector de manos
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)  # Definimos el número máximo de manos
classifier = Classifier("Trabajo de curso/Model/keras_model.h5", 
                        "Trabajo de curso/Model/labels.txt")


# Configuración de parámetros
offset = 20  # Margen alrededor de la mano al recortar la imagen
imgSize = 300  # Tamaño deseado para la imagen recortada y redimensionada

folder = "C:/Users/Lenovo/Desktop/Data/Y"
counter = 0

label = [
    "A", "B", "C", "D", "E", "F"
    "G", "H", "I", "J", "K", "L"
    "M", "N", "O", "P", "Q", "R"
    "S", "T", "U", "V", "W", "X"
    "Y", "Z"
    ]

while True:
    # Capturar el fotograma actual de la cámara
    success, img = cap.read()

    # Detectar manos en la imagen
    hands, img = detector.findHands(img)
    
    # Visualizar la imagen original
    cv2.imshow("Image", img)

    if hands:
        # Tomar la información de la primera mano detectadas
        hand = hands[0]
        x, y, w, h = hand['bbox']
        
        # Crear una imagen blanca del tamaño deseado
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        # Recortar la región de la mano de la imagen original
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        
        # Obtener la forma de la región recortada
        imgCropShape = imgCrop.shape
        
        # Calcular la relación de aspecto de la mano
        aspectRatio = h / w
        
        if aspectRatio > 1:
            # Si la posición de la mano es más alta que ancha
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = int(math.ceil((imgSize - wCal) / 2))
            
            # Convertir a enteros y asignar la región redimensionada a la imagen blanca
            wGap = int(wGap)
            wCal = int(wCal)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(img)
            print(prediction, index)
            
        else:
            # Si la mposición de la mano es más ancha que alta 
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = int(math.ceil((imgSize - hCal) / 2))
            
            # Convertir a enteros y asignar la región redimensionada a la imagen blanca
            #hGap = int(hGap)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        # Visualizar la imagen recortada y la imagen blanca
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    # Espera la tecla 'q' para cerrar la cámara
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
