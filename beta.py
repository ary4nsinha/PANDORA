import cv2
import pytesseract

# Function to perform OCR with preprocessing
def ocr_with_preprocessing(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the colors to get a black and white view
    inverted = cv2.bitwise_not(gray)
    
    # Use Tesseract OCR to read the numbers on the plate
    text = pytesseract.image_to_string(inverted, config='--psm 6')
    
    return text

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Create a Tesseract OCR object
pytesseract.pytesseract.tesseract_cmd = 'path_to_your_tesseract_executable'

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Perform number plate detection (you may need to fine-tune this for your specific use case)
    # This example uses simple thresholding for demonstration purposes
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through the detected contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Check if the detected region is a reasonable size for a number plate
        if 100 < w < 300 and 50 < h < 150:
            # Crop the region of interest (ROI)
            roi = frame[y:y + h, x:x + w]

            # Use the ocr_with_preprocessing function to read the numbers on the plate
            plate_text = ocr_with_preprocessing(roi)

            # Display the number plate and its read text
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, plate_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Number Plate Detection", frame)

    # Press 'q' to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
