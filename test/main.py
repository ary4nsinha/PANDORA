import cv2
import matplotlib.pyplot as plt
import numpy as np 

img = cv2.imread(r'C:\Users\worka\Downloads\pandora-version-1\PANDORA\test\number-pl8-1.jpg', cv2.IMREAD_GRAYSCALE)

img_array = np.array(img)
plt.imshow(img, cmap='gray')  
plt.show()
print(img_array)


#capture image from video frames 
#read image 
#convert image to grayscale 
#turn the image into an array 
#identify where the number plate is 
#draw a rectangle border along the number plate 
#crop the number plate part inside the rectangle 
#use thresholding to sharpen the image 
#tessaract ocr for making out the array -> text 
#reading the number 