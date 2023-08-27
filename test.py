import cv2

def detect_faces():
    # face detection model that has already been trained 
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    #for opening the web cam on your device
    cap = cv2.VideoCapture(0)

    while True:
        # capture a frame from the web cam video stream 
        ret, frame = cap.read()

        if not ret:
            break

        # converts the frame to grayscale (face detection works on grayscale images)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detects faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # show the exact frame
        cv2.imshow('Face Detection', frame)

        # exit loop with q key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_faces()
