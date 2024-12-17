import time
import cv2
from picamera2 import Picamera2
import numpy as np
from config.hardware_config import CAMERA_MODULE, TIME
from services.logger import Logger

class CameraModule:
    def __init__(self):
        """Initializes the camera module."""
        self._logger = Logger("Color Box")
        self._pi_cam = Picamera2()
        self._pi_cam.configure(self._pi_cam.create_preview_configuration(main={"size": CAMERA_MODULE["resolution"]}))
        self._pi_cam.start()
        self._logger.info("Camera module initialized")

    def __del__(self):
        """Cleans up the camera module."""
        self._pi_cam.stop()
        cv2.destroyAllWindows()
        self._logger.info("Camera module stopped")

    def get_color(self):
        """Returns the color detected by the camera."""
        frame = self._pi_cam.capture_array()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        detected_colors = {}
        for color, (lower, upper) in CAMERA_MODULE["color_ranges"].items():
            lower = np.array(lower, dtype=np.uint8)
            upper = np.array(upper, dtype=np.uint8)
            mask = cv2.inRange(hsv, lower, upper)
            count = cv2.countNonZero(mask)
            if count > 0:
                detected_colors[color] = count
        result = max(detected_colors, key=detected_colors.get)
        self._logger.info("Color detected: " + result)
        return result
        
if __name__ == "__main__":
    try:
        camera_module = CameraModule()
        while True:
            color = camera_module.get_color()
            print(f"Color detected: {color}")
            time.sleep(TIME["tick"] * 2)
    except KeyboardInterrupt:
        print("Exiting...")
