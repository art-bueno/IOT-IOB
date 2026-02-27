import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_blue = np.array([100, 50, 50])
upper_blue = np.array([150, 255, 255])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, lower_blue, upper_blue)


    cv2.imshow("Video Original", frame)
    cv2.imshow("Mascara Azul", mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

