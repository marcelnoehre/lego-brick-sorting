import cv2
from picamera2 import Picamera2
import numpy as np
from config.hardware_config import CAMERA_MODULE
from services.logger import Logger

logger = Logger("Background Filter")
pi_cam = Picamera2()
pi_cam.configure(pi_cam.create_preview_configuration(main={"size": CAMERA_MODULE["resolution"]}))
pi_cam.start()
frame = pi_cam.capture_array()
bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
min_hsv = tuple(np.min(hsv.reshape(-1, 3), axis=0))
max_hsv = tuple(np.max(hsv.reshape(-1, 3), axis=0))
logger.info(f"Background HSV range: Lower: {min_hsv}, Upper: {max_hsv}")
logger.info(f"Formatted for config: [{min_hsv}, {max_hsv}]")