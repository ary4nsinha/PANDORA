import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pytesseract
# PATH TO TESSERACT FILE
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"


#video capture

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

def ocr_with_preprocessing(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use adaptive thresholding to convert the grayscale image to binary
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Pass the processed image to tesseract
    text = pytesseract.image_to_string(binary)
    
    return text

# IMAGE PATH
image_path = "SAMPLE/ss.png"
extracted_text = ocr_with_preprocessing(image_path)
print(extracted_text)

# IMAGE DISPLAY
img = cv2.imread('SAMPLE/ss.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

