from picamera2 import Picamera2
import numpy as np
import cv2
from config.hardware_config import CAMERA_MODULE

picam = Picamera2()
picam.configure(picam.create_preview_configuration(main={'size': CAMERA_MODULE["resolution"]}))
picam.start()
frame = picam.capture_array()
cv2.imshow("Captured Image", frame)

def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        pixel = hsv_image[y, x]
        print(f"HSV: {pixel}")

cv2.setMouseCallback('Captured Image', pick_color)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
picam.stop()
