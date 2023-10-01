#importando cv2 para uso de algoritmos
import cv2

#carregamento do algoritmo pretendido

carregaAlgoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

#acesso a imagem da minha pasta

imagem = cv2.imread('imagens/equipe.jpg')

#imagem cinza para maior acuracia

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#descobrir faces em imagem e listar as coordenadas em uma matriz

face = carregaAlgoritmo.detectMultiScale(imagemCinza)

print(face)

#criar retangulo sobre rosto detectado

for(x, y, l, a) in face:
    cv2.rectangle(imagem, (x,y), (x+l, y+a), (0,255,0) , 2)


cv2.imshow("Faces", imagem)
cv2.waitKey()