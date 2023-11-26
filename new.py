import cv2

def process_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Define the region of interest (ROI) for the number plate
    # This is just an example; you may need to adjust the coordinates based on your specific case
    roi = gray[100:300, 200:400]

    # Apply thresholding to the ROI
    _, thresholded = cv2.threshold(roi, 127, 255, cv2.THRESH_BINARY)

    # Add a green border around the ROI
    frame_with_border = frame.copy()
    cv2.rectangle(frame_with_border, (200, 100), (400, 300), (0, 255, 0), 2)

    return frame_with_border, thresholded

def main():
    # Open a video capture object (0 for default camera)
    cap = cv2.VideoCapture("car3.mp4")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if the frame is successfully captured
        if not ret:
            print("Failed to capture frame")
            break

        # Process the frame
        processed_frame, thresholded = process_frame(frame)

        # Display the original frame with green border around ROI
        cv2.imshow('Original Frame with ROI', processed_frame)

        # Display the thresholded frame
        cv2.imshow('Thresholded Frame', thresholded)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
