import cv2

# Load OpenCV’s built-in deep learning-based face detector
face_detector = cv2.FaceDetectorYN_create(cv2.data.haarcascades + "haarcascade_frontalface_default.xml", "", (320, 320))

# Start the webcam
cap = cv2.VideoCapture(0)

# Set video frame size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

while True:
    # Read frames from webcam
    ret, frame = cap.read()
    
    if not ret:
        break  # If the camera is not available, exit

    # Detect faces
    _, faces = face_detector.detect(frame)
    
    if faces is not None:
        for face in faces:
            x, y, w, h = map(int, face[:4])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the output
    cv2.imshow("Face Scanner", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
