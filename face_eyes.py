#importando cv2 para uso de algoritmos

import cv2

#carregamento do algoritmo pretendido para checar uma face

carregaAlgoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

#carregamento de algoritmo pretendido para checar olhos

carregaOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

#acesso a imagem da minha pasta

imagem = cv2.imread('imagens/pessoa1.jpeg')

#imagem cinza para maior acuracia

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#descobrir faces em imagem e listar as coordenadas em uma matriz

face = carregaAlgoritmo.detectMultiScale(imagemCinza)

print(face)
#criar retangulo sobre rosto detectado

for(x, y, l, a) in face:
    imagem = cv2.rectangle(imagem, (x,y), (x+l, y+a), (0,255,0) , 2)
    localOlho = imagem [y: y + a, x: x + l]
    #utilizando o face para dentro da mesma area delimitada pela face, reconhecer olhos
    local_olhocinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
    detectado = (carregaOlho.detectMultiScale(local_olhocinza))

 #desenhar o retangulo na area detectada
    for(ox, oy, ol, oa) in detectado:
        cv2.rectangle(localOlho, (ox, oy), (ox + ol, oy + oa), (0, 0, 255) , 2)

cv2.imshow("Faces e olho", imagem)
cv2.waitKey()