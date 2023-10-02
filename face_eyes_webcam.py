import cv2
#criando variavel webcam que receberá a cpatura de video
# o zero representa a camera selecionada, como não tenho nenhuma USB conectada, usara a camera mais interna, a do computador que estou usando

webcam = cv2.VideoCapture(0)

#algoritmos para deteccao de rosto e de olhos
classificadorVideoFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregaOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

#estrtura de repeticao que vai regir o funcionamento da camera e a criacao dos retangulos para face e olhos

while True:
    camera, frame = webcam.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detecta = classificadorVideoFace.detectMultiScale(cinza)
    #criacao do retangulo sob a face
    for(x, y, l, a) in detecta:
       frame = cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 2)
       localOlho = frame[y: y + a, x: x + l]
       # utilizando o face para dentro da mesma area delimitada pela face, reconhecer olhos
       local_olhocinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
       detectado = (carregaOlho.detectMultiScale(local_olhocinza))

       # desenhar o retangulo na area detectada
    for (ox, oy, ol, oa) in detectado:
        cv2.rectangle(localOlho, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2)


    cv2.imshow("video webcamera", frame)
    #Quando a tecla Q for apertada, quit da webcam
    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()


