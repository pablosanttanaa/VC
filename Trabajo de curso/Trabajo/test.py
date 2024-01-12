import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
from cvzone.ClassificationModule import Classifier


# Inicializar la cámara y el detector de manos
camera = cv2.VideoCapture(0)
detector_mano = HandDetector(maxHands=1)  # Definimos el número máximo de manos
classifier = Classifier("Trabajo de curso/Model/keras_model.h5", 
                        "Trabajo de curso/Model/labels.txt")


# Configuración de parámetros
margen_recorte = 20  # Margen alrededor de la mano al recortar la imagen
new_size = 300  # Tamaño deseado para la imagen recortada y redimensionada

# Posibles clases dentro del Modelo
label = ["A", "B", "C", "D", "E", "F",
        "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X",
        "Y"]

while True:
    # Capturar el fotograma actual de la cámara
    success, imagen = camera.read()
    
    imgOutput = img.copy()

    # Detectar manos en la imagen
    manos, img = detector_mano.findHands(img)
    
    if manos:
        # Tomar la información de la primera mano detectadas
        mano = manos[0]
        x, y, w, h = mano['bbox']
        
        # Crear una imagen blanca del tamaño deseado
        imagen_blanca = np.ones((new_size, new_size, 3), np.uint8) * 255

        # Recortar la región de la mano de la imagen original
        region_mano_recortada = imagen[y - margen_recorte:y + h + margen_recorte, x - margen_recorte:x + w + margen_recorte]
        
        # Obtener la forma de la región recortada
        forma_region_recortada = region_mano_recortada.shape
        
        # Calcular la relación de aspecto de la mano
        relacion_aspecto = h / w
        
        if relacion_aspecto > 1:
            # Si la posición de la mano es más alta que ancha
            factor_redimension = new_size / h
            ancho_calculado = math.ceil(factor_redimension * w)
            region_redimensionada = cv2.resize(region_mano_recortada, (ancho_calculado, new_size))
            forma_redimensionada = region_redimensionada.shape
            brecha_ancho = int(math.ceil((new_size - ancho_calculado) / 2))
            
            # Convertir a enteros y asignar la región redimensionada a la imagen blanca
            brecha_ancho = int(brecha_ancho)
            ancho_calculado = int(ancho_calculado)
            imagen_blanca[:, brecha_ancho:ancho_calculado + brecha_ancho] = region_redimensionada
            
        else:
            # Si la posición de la mano es más ancha que alta 
            factor_redimension = new_size / w
            alto_calculado = math.ceil(factor_redimension * h)
            region_redimensionada = cv2.resize(region_mano_recortada, (new_size, alto_calculado))
            forma_redimensionada = region_redimensionada.shape
            brecha_alto = int(math.ceil((new_size - alto_calculado) / 2))
            
            # Convertir a enteros y asignar la región redimensionada a la imagen blanca
            imagen_blanca[brecha_alto:alto_calculado + brecha_alto, :] = region_redimensionada
            
            prediction, index = classifier.getPrediction(imagen_blanca)

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


