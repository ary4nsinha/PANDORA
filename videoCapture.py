import cv2

camera = cv2.VideoCapture("car3.mp4")

while True:
    _, frame = camera.read()

    cv2.imshow("Video", frame)  # Specify a window name, e.g., "Video"

    if cv2.waitKey(5) == ord('x'):
        break

camera.release()
cv2.destroyAllWindows()
