import pytesseract
import PIL.Image
import cv2
import matplotlib.pyplot as plt

myconfig = r"--psm 6 --oem 3"
img_path = "assets/numberPlate4.jpg"
img = plt.imread(img_path)  # Use plt.imread() to read image data
text = pytesseract.image_to_string(PIL.Image.open(img_path), config=myconfig)
print(text)
