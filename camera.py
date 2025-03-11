import cv2
import time
import numpy as np
from config.hardware_config import CAMERA_MODULE
from picamera2 import Picamera2

# Initialize the PiCamera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={'size': (400, 400)}))
picam2.start()

def detect_colors(frame, lower_bound, upper_bound, color_name):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_objects = []
    
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Filter small objects
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), CAMERA_MODULE.color_map[color_name], 2)
            cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            detected_objects.append({"color": color_name, "size": cv2.contourArea(contour)})
    
    return frame, detected_objects

detected_color = None
badge = None
badge_color = None
timer = 0

while True:
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    detected_objects = []
    
    for color, (lower, upper) in CAMERA_MODULE.color_ranges.items():
        frame, objects = detect_colors(frame, lower, upper, color)
        detected_objects.extend(objects)
    
    detected_objects.sort(key=lambda x: x["size"], reverse=True)
    detected_objects = detected_objects if detected_objects else [{"color": None, "size": 0}]
    
    if detected_color is not None and detected_objects[0]["color"] != detected_color:
        badge = f"{detected_color} left the frame"
        badge_color = detected_color
        timer = time.time()
    
    if badge_color and badge and time.time() - timer < 1:
        cv2.rectangle(frame, (350, 0), (400, 50), CAMERA_MODULE.color_map[badge_color], -1)
    else:
        badge = None
        badge_color = None
    
    detected_color = detected_objects[0]["color"]
    
    cv2.imshow("Color Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
picam2.stop()
