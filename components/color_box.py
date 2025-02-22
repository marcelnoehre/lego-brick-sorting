import cv2
import time
import numpy as np
import threading
from picamera2 import Picamera2
from services.logger import Logger
from config.hardware_config import CAMERA_MODULE, VALVES

class ColorBox:
    def __init__(self, callback):
        """Initializes the camera module."""
        self._logger = Logger("Color Box")
        self._is_running = False
        self.callback = callback
        self._picam = None
        self._thread = None
        self._stop_event = threading.Event()
        self.detected_color = None
        self.badge_text = None
        self.badge_color = None
        self.badge_timer = 0
        self._logger.info("Color box initialized")

    def __del__(self):
        """Cleans up the camera module."""
        if self._is_running:
            self.stop()

    def start(self):
        """Starts the camera module."""
        if self._is_running:
            self._logger.warning("Trying to start the camera while it is already running!")
            return
        self._picam = Picamera2()
        self._picam.configure(self._picam.create_preview_configuration(main={'size': CAMERA_MODULE["resolution"]}))
        self._picam.start()
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_detection, daemon=True)
        self._thread.start()
        self._is_running = True
        self._logger.info("Color box started")

    def stop(self):
        """Stops the camera module."""
        if not self._is_running:
            self._logger.warning("Trying to stop the camera while it is already stopped!")
            return
        self._stop_event.set()
        if self._thread:
            self._thread.join()
        if self._picam:
            self._picam.stop()
            self._picam = None
        cv2.destroyAllWindows()
        self._is_running = False
        self._logger.info("Color box stopped")

    def _detect_color(self, frame, lower_bound, upper_bound, color_name):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)

        if len (contours) > 0 and cv2.contourArea(contours[0]) > 1000:
            x, y, w, h = cv2.boundingRect(contours[0])
            cv2.rectangle(frame, (x, y), (x + w, y + h), CAMERA_MODULE["color_map"][color_name], 2)
            cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            return frame, color_name, cv2.contourArea(contours[0])
        else:
            return frame, None, 0

    def _run_detection(self):
        """Continuously captures frames and detects colors."""
        while not self._stop_event.is_set():
            frame = self._picam.capture_array()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            current_colors = []
            for color, (lower, upper) in CAMERA_MODULE["color_ranges"].items():
                frame, color_name, size = self._detect_color(frame, lower, upper, color)
                if color_name:
                    current_colors.append({"color": color_name, "size": size})

            current_colors = sorted(current_colors, key=lambda x: x["size"], reverse=True)
            current_colors = current_colors if len(current_colors) > 0 else [{"color": None, "size": 0}]

            if self.detected_color is not None and current_colors[0]["color"] != self.detected_color:
                self.callback(self._get_valve_id(self.detected_color))
                self.badge_text = f"{self.detected_color} left the frame"
                self.badge_color = self.detected_color
                self.badge_timer = time.time()

            if self.badge_color and self.badge_text and time.time() - self.badge_timer < 1:
                cv2.rectangle(frame, CAMERA_MODULE["badge"]["top_left"], CAMERA_MODULE["badge"]["bottom_right"], CAMERA_MODULE["color_map"][self.badge_color], -1)
            else:
                self.badge_text = None
                self.badge_color = None

            self.detected_color = current_colors[0]["color"]
            cv2.imshow("Color Box", frame)
            cv2.waitKey(1)

    def _get_valve_id(self, color):
        for id, valve in VALVES["valves"].items():
            if valve["color"] == color:
                return id
        return None
