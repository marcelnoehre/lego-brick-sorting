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
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_objects = []
    
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Filter small objects
            x, y, w, h = cv2.boundingRect(contour)
            cx, cy = x + w // 2, y + h // 2  # Compute centroid
            cv2.rectangle(frame, (x, y), (x + w, y + h), CAMERA_MODULE["color_map"][color_name], 2)
            cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            detected_objects.append({"color": color_name, "size": cv2.contourArea(contour), "centroid": (cx, cy)})
    
    return frame, detected_objects

tracked_objects = {}
next_object_id = 0
badge = None
badge_color = None
timer = 0

def update_tracked_objects(detected_objects):
    global next_object_id, tracked_objects
    current_centroids = [obj["centroid"] for obj in detected_objects]
    new_tracked = {}
    
    for obj_id, (prev_centroid, color) in tracked_objects.items():
        # Check if previous centroid is close to any current centroids
        matched = False
        for obj in detected_objects:
            if np.linalg.norm(np.array(prev_centroid) - np.array(obj["centroid"])) < 50:  # Threshold for tracking
                new_tracked[obj_id] = (obj["centroid"], obj["color"])
                matched = True
                detected_objects.remove(obj)
                break
        
        if not matched:
            print(f"Object {color} (ID: {obj_id}) left the frame")
    
    # Assign new IDs to unmatched objects
    for obj in detected_objects:
        new_tracked[next_object_id] = (obj["centroid"], obj["color"])
        next_object_id += 1
    
    tracked_objects = new_tracked

while True:
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    detected_objects = []
    
    for color, (lower, upper) in CAMERA_MODULE["color_ranges"].items():
        frame, objects = detect_colors(frame, lower, upper, color)
        detected_objects.extend(objects)
    
    update_tracked_objects(detected_objects)
    
    if badge_color and badge and time.time() - timer < 1:
        cv2.rectangle(frame, (350, 0), (400, 50), CAMERA_MODULE["color_map"][badge_color], -1)
    else:
        badge = None
        badge_color = None
    
    cv2.imshow("Color Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
picam2.stop()