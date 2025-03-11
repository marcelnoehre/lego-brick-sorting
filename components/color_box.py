import cv2
import time
import threading
import numpy as np
from picamera2 import Picamera2
from services.logger import Logger
from config.hardware_config import CAMERA_MODULE, VALVES

class ColorBox:
    def __init__(self, callback):
        """Initializes the camera module."""
        self._logger = Logger("Color Box")
        self._is_running = False
        self.callback = callback
        self._picam = Picamera2()
        self._picam.configure(self._picam.create_preview_configuration(main={'size': CAMERA_MODULE["resolution"]}))
        self._picam.start()
        self._thread = None
        self._stop_event = threading.Event()
        self._next_object_id = 0
        self._tracked_objects = {}
        self._initial_colors = {}
        self._recently_detected = []
        self._logger.info("Color box initialized")

    def __del__(self):
        """Cleans up the color box."""
        if self._is_running:
            self.stop()
        cv2.destroyAllWindows()
        self._picam.stop()

    def start(self):
        """Starts the color box."""
        if self._is_running:
            self._logger.warning("Trying to start the color box while it is already running!")
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_detection, daemon=True)
        self._thread.start()
        self._is_running = True
        self._logger.info("Color box started")

    def stop(self):
        """Stops the color box."""
        if not self._is_running:
            self._logger.warning("Trying to stop the color box while it is already stopped!")
            return
        self._stop_event.set()
        if self._thread:
            self._thread.join()
        self._is_running = False
        self._logger.info("Color box stopped")

    def _detect_colors(self, frame, lower_bound, upper_bound, color_name):
        """Detects objects of a specific color in the frame."""
        _roi = frame[CAMERA_MODULE["padding"]:frame.shape[0]-CAMERA_MODULE["padding"], :]
        _hsv = cv2.cvtColor(_roi, cv2.COLOR_BGR2HSV)
        _mask = cv2.inRange(_hsv, lower_bound, upper_bound)
        _contours, _ = cv2.findContours(_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        _detected_objects = []
        for _contour in _contours:
            if cv2.contourArea(_contour) > CAMERA_MODULE["threshold"]["contour"]:
                _x, _y, _w, _h = cv2.boundingRect(_contour)
                _y += CAMERA_MODULE["padding"]
                _cx, _cy = _x + _w // 2, _y + _h // 2
                cv2.rectangle(frame, (_x, _y), (_x + _w, _y + _h), CAMERA_MODULE["color_map"][color_name], 2)
                cv2.putText(frame, color_name, (_x, _y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                _detected_objects.append({
                    "color": color_name,
                    "size": cv2.contourArea(_contour),
                    "centroid": (_cx, _cy)
                })
        return frame, _detected_objects

    def _update_tracked_objects(self, detected_objects):
        """Updates the tracked objects based on the detected objects."""
        _new_tracked = {}
        for _obj_id, (_prev_centroid, _color) in self._tracked_objects.items():
            _matched = False
            for _obj in detected_objects:
                if np.linalg.norm(np.array(_prev_centroid) - np.array(_obj["centroid"])) < CAMERA_MODULE["threshold"]["tracking"]:
                    _obj_color = self._initial_colors.get(_obj_id, _obj["color"])
                    _new_tracked[_obj_id] = (_obj["centroid"], _obj_color)
                    self._initial_colors[_obj_id] = _obj_color
                    _matched = True
                    detected_objects.remove(_obj)
                    break
            if not _matched:
                if _prev_centroid[0] > CAMERA_MODULE["target_line"] - CAMERA_MODULE["threshold"]["tracking"]:
                    threading.Thread(target=self._execute_callback, args=(_color,)).start()
                    self._logger.info(f"Object {_color} (ID: {_obj_id}) reached the tracking line")
                    self._recently_detected.append((_color, time.time()))
        
        for _obj in detected_objects:
            if _obj["centroid"][0] > CAMERA_MODULE["threshold"]["tracking"]:
                continue
            _new_tracked[self._next_object_id] = (_obj["centroid"], _obj["color"])
            self._initial_colors[self._next_object_id] = _obj["color"]
            self._next_object_id += 1
        
        self._tracked_objects = _new_tracked

    def _run_detection(self):
        """Continuously captures frames and detects colors."""
        while not self._stop_event.is_set():
            _frame = self._picam.capture_array()
            _frame = cv2.cvtColor(_frame, cv2.COLOR_BGR2RGB)
            _detected_objects = []
            for _color, (_lower, _upper) in CAMERA_MODULE["color_ranges"].items():
                _frame, _objects = self._detect_colors(_frame, _lower, _upper, _color)
                _detected_objects.extend(_objects)
            self._update_tracked_objects(_detected_objects)

            _offset = 0
            self._recently_detected = [(_color, _time) for _color, _time in self._recently_detected if time.time() - _time < CAMERA_MODULE["badge"]["timer"]]
            for _i, (_color, _) in enumerate(self._recently_detected):
                cv2.rectangle(_frame, (_frame.shape[1] - CAMERA_MODULE["badge"]["width"], _offset), (_frame.shape[1], CAMERA_MODULE["badge"]["height"] + _offset), CAMERA_MODULE["color_map"][_color], -1)
                _offset += CAMERA_MODULE["badge"]["height"]

            cv2.line(_frame, (CAMERA_MODULE["target_line"], 0), (CAMERA_MODULE["target_line"], _frame.shape[0]), (255, 255, 255), 2)
            cv2.imshow("Color Detection", _frame)
            cv2.waitKey(1)

    def _execute_callback(self, color):
        """Executes the callback function."""
        for id, valve in VALVES["valves"].items():
            if valve["color"] == color:
                time.sleep(valve["duration"])
                self.callback(id)
                break
