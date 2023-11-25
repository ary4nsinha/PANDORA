import cv2 
import time

vid_path = "car3.mp4"
videoCapture = cv2.VideoCapture(vid_path)

# Set the video capture to 3 seconds (3000 milliseconds)
target_time_ms = 6000
videoCapture.set(cv2.CAP_PROP_POS_MSEC, target_time_ms)

# Read the frame at 3 seconds
ret, frame = videoCapture.read()

if ret:
    cv2.imwrite("frame_after_3_seconds.png", frame)
    print("Frame captured 3 seconds after the video starts.")
else:
    print("Failed to capture the frame.")

videoCapture.release()
cv2.destroyAllWindows()
