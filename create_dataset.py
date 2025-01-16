import os
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt


mpHands = mp.solutions.hands
mpDrawing = mp.solutions.drawing_utils
mpDrawingStyles = mp.solutions.drawing_styles

hands = mpHands.Hands(static_image_mode=True, min_detection_confidence=0.3)


dataDir = './data'

for dir in os.listdir(dataDir):
    for img in os.listdir(os.path.join(dataDir, dir))[:1]:
        imgPath = os.path.join(dataDir, dir, img)
        img = cv2.imread(imgPath)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        result = hands.process(imgRGB)
        if result.multi_hand_landmarks:
            for handLandmarks in result.multi_hand_landmarks:
                mpDrawing.draw_landmarks(
                    imgRGB, 
                    handLandmarks, 
                    mpHands.HAND_CONNECTIONS, 
                    mpDrawingStyles.get_default_hand_landmarks_style(),
                    mpDrawingStyles.get_default_hand_connections_style()
                )

        plt.figure()
        plt.imshow(imgRGB)
plt.show()

