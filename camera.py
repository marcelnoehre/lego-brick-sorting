import cv2
import numpy as np
from picamera2 import Picamera2

# Initialize the PiCamera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={'size': (800, 800)}))
picam2.start()

def detect_color(frame, lower_bound, upper_bound, color_name):
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask for the color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Bounding Boxes
    color_map = {
        "Red": (0, 0, 255),
        "Blue": (255, 0, 0),
        "Green": (0, 255, 0),
        "Yellow": (0, 255, 255),
        "Orange": (0, 165, 255),
        "Light Green": (144, 238, 144),
        "Light Blue": (173, 216, 230),
        "White": (255, 255, 255),
        "Black": (0, 0, 0),
        "Brown": (42, 42, 165),
        "Beige": (245, 245, 220),
        "Grey": (128, 128, 128)
    }
    
    offset = 0  # Labels
    
    for contour in contours:
        if cv2.contourArea(contour) > 1000: # Filter small contours
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color_map[color_name], 2)
            cv2.putText(frame, color_name, (x, y - 10 - offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            offset += 15
    
    return frame

color_ranges = {
    "Red": (np.array([0, 120, 70]), np.array([10, 255, 255])),
    "Blue": (np.array([100, 150, 70]), np.array([140, 255, 255])),
    "Green": (np.array([40, 70, 70]), np.array([80, 255, 255])),
    "Yellow": (np.array([20, 100, 100]), np.array([30, 255, 255])),
    "Orange": (np.array([10, 100, 100]), np.array([20, 255, 255])),
    "Light Green": (np.array([35, 50, 70]), np.array([55, 255, 255])),
    "Light Blue": (np.array([90, 50, 70]), np.array([110, 255, 255])),
    "White": (np.array([0, 0, 200]), np.array([180, 55, 255])),
    "Black": (np.array([0, 0, 0]), np.array([180, 255, 50])),
    "Brown": (np.array([10, 50, 20]), np.array([30, 255, 120])),
    "Beige": (np.array([15, 20, 150]), np.array([25, 80, 255])),
    "Grey": (np.array([0, 0, 70]), np.array([180, 20, 200]))
}

while True:
    # Capture frame from PiCamera
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect colors
    for color, (lower, upper) in color_ranges.items():
        frame = detect_color(frame, lower, upper, color)
    
    # Show output
    cv2.imshow("Color Detection", frame)
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
picam2.stop()