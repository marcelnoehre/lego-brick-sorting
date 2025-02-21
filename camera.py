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
        "Brown": (42, 42, 165),
        "Beige": (245, 245, 220),
        "Grey": (128, 128, 128),
        "Purple": (128, 0, 128),
        "Pink": (255, 105, 180)
    }

    offset = 0  # Labels

    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    if cv2.contourArea(contours[:1]) > 1000: # Filter small contour
        x, y, w, h = cv2.boundingRect(contours[:1])
        cv2.rectangle(frame, (x, y), (x + w, y + h), color_map[color_name], 2)
        cv2.putText(frame, color_name, (x, y - 10 - offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        offset += 15
        return frame, color_name
    else:
        return frame, None

color_ranges = {
    "Red": (np.array([0, 120, 70]), np.array([10, 255, 255])),
    "Blue": (np.array([100, 150, 70]), np.array([130, 255, 255])),
    "Green": (np.array([40, 70, 70]), np.array([80, 255, 255])),
    "Yellow": (np.array([22, 150, 100]), np.array([30, 255, 255])),
    "Orange": (np.array([10, 150, 100]), np.array([20, 255, 255])),
    "Light Green": (np.array([35, 50, 70]), np.array([50, 255, 255])),
    "Light Blue": (np.array([90, 100, 100]), np.array([100, 255, 255])),
    "White": (np.array([0, 0, 200]), np.array([180, 50, 255])),
    "Brown": (np.array([10, 50, 20]), np.array([18, 255, 100])),
    "Beige": (np.array([12, 40, 150]), np.array([20, 100, 255])),
    "Grey": (np.array([0, 0, 50]), np.array([180, 10, 180])),
    "Purple": (np.array([140, 100, 50]), np.array([160, 255, 255])),
    "Pink": (np.array([160, 100, 100]), np.array([175, 255, 255]))
}

detected_colors = []

while True:
    # Capture frame from PiCamera
    frame = picam2.capture_array()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect colors
    current_colors = []
    for color, (lower, upper) in color_ranges.items():
        frame, color_name = detect_color(frame, lower, upper, color)
        if color_name:
            current_colors.append(color_name)
    
    for color in detected_colors:
        if color not in current_colors:
            print(f"{color} left the frame")
    detected_colors = current_colors
    
    # Show output
    cv2.imshow("Color Detection", frame)
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
picam2.stop()