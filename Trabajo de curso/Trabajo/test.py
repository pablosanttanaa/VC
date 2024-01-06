import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
from cvzone.ClassificationModule import Classifier


# Inicializar la cámara y el detector de manos
camera = cv2.VideoCapture(0)
hand_detector = HandDetector(maxHands=1)  # Definimos el número máximo de manos
classifier = Classifier("Trabajo de curso/Model/keras_model.h5", 
                        "Trabajo de curso/Model/labels.txt")


# Configuración de parámetros
offset = 20  # Margen alrededor de la mano al recortar la imagen
imgSize = 300  # Tamaño deseado para la imagen recortada y redimensionada

# Posibles clases dentro del Modelo
label = ["A", "B", "C", "D", "E", "F",
        "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X",
        "Y"]

while True:
    # Capturar el fotograma actual de la cámara
    success, img = camera.read()
    
    imgOutput = img.copy()

    # Detectar manos en la imagen
    hands, img = hand_detector.findHands(img)
    
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
            prediction, index = classifier.getPrediction(imgWhite)
            print(prediction, index)
                 
        else:
            # Si la posición de la mano es más ancha que alta 
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = int(math.ceil((imgSize - hCal) / 2))
            
            # Convertir a enteros y asignar la región redimensionada a la imagen blanca
            imgWhite[hGap:hCal + hGap, :] = imgResize
            
            prediction, index = classifier.getPrediction(imgWhite)

        cv2.putText(imgOutput, label[index], (x,y-20), cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)
        cv2.rectangle(imgOutput,(x,y),(x+w, y+h), (255,0,255), 4)
        
    # Visualizar la imagen original
    cv2.imshow("Image", imgOutput)
    
    # Espera la tecla 'q' para cerrar la cámara
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
camera.release()
cv2.destroyAllWindows()
