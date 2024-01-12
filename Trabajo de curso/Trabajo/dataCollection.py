import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

# Inicializar la cámara y el detector de manos
camara = cv2.VideoCapture(0)
detector_mano = HandDetector(maxHands=1)  # Definimos el número máximo de manos

# Configuración de parámetros
margen_recorte = 20  # Margen alrededor de la mano al recortar la imagen
new_size = 300  # Tamaño deseado para la imagen recortada y redimensionada

directorio_guardado = "C:/Direccion/Para/Guardar/Fotos/Dataset"
contador = 0

while True:
    # Capturar el fotograma actual de la cámara
    success, imagen = camara.read()

    # Detectar manos en la imagen
    manos, imagen = detector_mano.findHands(imagen)
    
    # Visualizar la imagen original
    cv2.imshow("Imagen", imagen)

    if manos:
        # Tomar la información de la primera mano detectada
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

        # Visualizar la imagen recortada y la imagen blanca
        cv2.imshow("ImagenRecortada", region_mano_recortada)
        cv2.imshow("ImagenBlanca", imagen_blanca)
        
    key = cv2.waitKey(1)
    
    # Se espera a que se pulse la tecla "S" para sacar una captura de la posición de la mano
    if key == ord("s"):
        contador += 1
        cv2.imwrite(f'{directorio_guardado}/Imagen_{time.time()}.jpg', imagen_blanca)
        print(contador)

    # Espera la tecla 'q' para cerrar la cámara
    if key == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
camara.release()
cv2.destroyAllWindows()
