# ALL IMPORTSimport cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# ALGORITHM FOR FACE DETECTION
face_cascade = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_frontalface_default.xml')


# DRAWING RECTANGLE ON DETECTED FACE
def detect_face(img):
    
    face_rects = face_cascade.detectMultiScale(img)
    
    for(x, y, w, h) in face_rects:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 10)
        
    return img   


# VIDEO CAPTURE USING DEFAULT CAMERA
cap = cv2.VideoCapture(0)

# VIDEO DIMENSIONS
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20


# LOOP TO BREAK OUT OF THE VIDEO RECORDING WHEN 'q' BUTTON IS PRESSED
while True:
    ret, frame = cap.read()
    

    frame = detect_face(frame)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# RELASING CAPTURE AND CLOSING ALL WINDOWS
cap.release()     
cv2.destroyAllWindows()   