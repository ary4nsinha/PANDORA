import cv2
import pytesseract

# Provide the absolute path to the image
image_path = r'C:\Users\worka\Downloads\pandora-version-1\PANDORA\test\example\number1.jpg'

try:
    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Unable to load the image.")
    else:
        # Apply Gaussian blur with parameters (3, 3)
        blurred_image = cv2.GaussianBlur(image, (3, 3), 0)
        
        # Convert the blurred image to grayscale
        gray_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)
        
        # Use Tesseract to perform OCR on the grayscale image
        plate_text = pytesseract.image_to_string(gray_image)
        
        # Print the detected text (number plate)
        print("Detected Number Plate:", plate_text.strip())
        
except Exception as e:
    print("An error occurred:", e)
