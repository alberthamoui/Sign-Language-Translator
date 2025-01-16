import os
import cv2
import time

data_dir = './data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

numClasses = 3
datasetSize = 100
restTime = 3

cap = cv2.VideoCapture(0)
cv2.namedWindow("Coletando imagens", cv2.WINDOW_AUTOSIZE)

for classId in range(numClasses):
    classDir = os.path.join(data_dir, f"{classId}")
    if not os.path.exists(classDir):
        os.makedirs(classDir)

    print(f"Coletando imagens para classe {classId}...")
    count = 0
    while count < datasetSize:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao acessar a câmera.")
            break

        # Espelhar a imagem
        frame = cv2.flip(frame, 1)
        text = f"Classe {classId}, Imagem {count + 1}/{datasetSize}"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Coletando imagens", frame)

        # Capture a imagem quando a barra de espaço for pressionada
        key = cv2.waitKey(1)
        if key == 32:  # Spacebar
            nomeImg = os.path.join(classDir, f"{count:04d}.jpg")
            cv2.imwrite(nomeImg, frame)
            print(f"Imagem {count + 1}/{datasetSize} salva: {nomeImg}")
            count += 1
        elif key == 27:  # ESC to exit
            print("Interrompido pelo usuário.")
            break

    # Descanso entre classes
    if classId < numClasses - 1:
        print(f"Descanso de {restTime} segundos antes da próxima classe...")
        for remaining in range(restTime, 0, -1):
            print(f"Próxima classe em {remaining} segundos...", end="\r")
            time.sleep(1)
        print("\n")

            
cap.release()
cv2.destroyAllWindows()
