Repositório pt-BR/en-US

# Easy algorithm to recognize faces on images / Algoritmo fácil para reconhecimento de rosto em imagens


1. Requirements/Requisitos: 

    OpenCV;

    IDE - VScode or Pycharm;

    Python 3.10; 

2. Installing OpenCV / Instalação OpenCV (linux Ubuntu): 

    >On linux terminal write it: / No terminal Linux digite isso: 
        
            sudo pip install opencv-python


3. You can use paramethers to improve (or no) your accuracy : /Utilização de parâmetros que aumentam (ou não) a acurácia:

        scaleFactor --> Parameter specifying how much image size is reduced at each image scale/Parametro que reduz o tamanho de uma imagem que está numa escala muito grande de forma a precisar mais o resultado(ou não a depender de cada imagem);

        minNeighbors --> Parameter specifying how many neighbors each candidate rectangle should have to retain it; Parametro que pega a área do do retângulo já criado e avalia cada parte como pequenos "retângulos", de forma a ver cada um como um possível candidato a rosto;
    
        minSize --> Minimum possible object size. Objects smaller than that are ignored; Parâmetro para sinalizar qual mínima escala de tamanho de rosto deve ser dectado, o que passar da escala passada, será ignorado pelo algoritmo; Default/Padrão: 30x30;


4. Recognizement of eyes : / Reconhecimento de olhos: 


    Algorithm--> haarcascade_eye.xml. Check the code face_eyes.py
 