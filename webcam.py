import cv2

#criando variavel webcam que receberá a cpatura de video
# o zero representa a camera selecionada, como não tenho nenhuma USB conectada, usara a camera mais interna, a do computador que estou usando


webcam = cv2.VideoCapture(0)

#estrtura de repeticao que vai regir o funcionamento da camera
while True:
    camera, frame = webcam.read()
    cv2.imshow("webcam", frame)





    if cv2.waitKey(1) == ord('z'):
        break

webcam.release()
cv2.destroyAllWindows()

