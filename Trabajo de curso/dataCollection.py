import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1) # Definimos el número máximo de manos

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    # Visualizar la imagen original
    cv2.imshow("Image", img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgCrop = img[y:y + h, x:x + w]
        
        # Verificar si las dimensiones de imgCrop son válidas antes de mostrar
        if w > 0 and h > 0:
            cv2.imshow("ImageCrop", imgCrop)
        else:
            print("Dimensiones no válidas para la imagen recortada.")

    # Espera la tecla 'q' para cerrar la cámara
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()
