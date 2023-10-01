import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_img(img):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img)

plate_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')

def detect_plate(img):
    plate_img = img.copy()
    plate_rects = plate_cascade.detectMultiScale(plate_img) 
    
    for (x,y,w,h) in plate_rects: 
        cv2.rectangle(plate_img, (x,y), (x+w,y+h), (0,255,0), 15)
        cropped_number_plate = plate_img[y:y+h, x:x+w]  # Crop the detected license plate
        
    return cropped_number_plate

plate = cv2.imread('SAMPLE_IMAGES/img1.jpg')
plate = cv2.cvtColor(plate, cv2.COLOR_BGR2RGB) 
display_img(plate)

blurred = cv2.blur(plate, (40,40)) 
display_img(blurred)

cropped_number_plate = detect_plate(blurred)  # Store the cropped license plate
display_img(cropped_number_plate)  # Display the cropped license plate

plt.show()  # Show the Matplotlib plot
