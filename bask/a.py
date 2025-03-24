import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera 0 not accessible, trying another index...")
    cap = cv2.VideoCapture(1)

if cap.isOpened():
    print("Camera is working!")
    cap.release()
else:
    print("No available camera found.")
