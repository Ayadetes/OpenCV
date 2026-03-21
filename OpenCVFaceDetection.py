import cv2
from cv2 import *
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
while True:
    if cv2.waitKey(1) and 0xFF == ord('q'):
        print("Exiting...")
        break
    net, frame = cap.read()
    if not net:
        print("Error: Could not read footage from webcam.")
        break
    grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayscaled, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Face Detection', frame)
cv2.destroyAllWindows()
cap.release()