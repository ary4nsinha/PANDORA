import cv2
import matplotlib.pyplot as plt

img_path = "test/numberPlate4.jpg"
img = cv2.imread(img_path)

if img is None:
    print(f"Error: Unable to load the image at '{img_path}'. Make sure the file exists.")
else:
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_resized = cv2.resize(img, (560, 900))
    _, result = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

    # Create a subplot with 1 row and 2 columns
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(result, cmap='gray')
    plt.title('Thresholded Result')

    plt.show()
