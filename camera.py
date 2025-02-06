import cv2
import numpy as np

COLOR_RANGES = {
    "red": [(0, 120, 70), (10, 255, 255)],
    "yellow": [(20, 100, 100), (30, 255, 255)],
    "green": [(40, 40, 40), (80, 255, 255)],
    "blue": [(90, 50, 50), (130, 255, 255)]
}

inside_img = False

def detect_lego_brick(frame):
    global inside_img

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])
    mask_black = cv2.inRange(hsv, lower_black, upper_black)
    mask_black = cv2.bitwise_not(mask_black)

    contours, _ = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        if not inside_img:
            print("Brick recognized!")
            inside_img = True

        largest_contour = max(contours, key=cv2.contourArea)
        
        x, y, w, h = cv2.boundingRect(largest_contour)
        roi = hsv[y:y+h, x:x+w]

        avg_color = np.mean(roi.reshape(-1, 3), axis=0)

        detected_color = "none"
        for color, (lower, upper) in COLOR_RANGES.items():
            if all(lower[i] <= avg_color[i] <= upper[i] for i in range(3)):
                detected_color = color
                break

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, detected_color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        return frame, detected_color

    else:
        if inside_img:
            print("brick left the frame")
            inside_img = False
    
    return frame, None

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame, color = detect_lego_brick(frame)

    cv2.imshow("Lego Color Cam", processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
