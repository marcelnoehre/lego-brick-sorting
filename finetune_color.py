import cv2
from picamera2 import Picamera2
import numpy as np
from config.hardware_config import CAMERA_MODULE
from services.logger import Logger

logger = Logger("Finetune Color")
pi_cam = Picamera2()
pi_cam.configure(pi_cam.create_preview_configuration(main={"size": CAMERA_MODULE["resolution"]}))
pi_cam.start()
frame = pi_cam.capture_array()
bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

filter_lower, filter_upper = CAMERA_MODULE["color_ranges"]["filter"]
filter_mask = cv2.inRange(hsv, np.array(filter_lower), np.array(filter_upper))
brick_mask = cv2.bitwise_not(filter_mask)
pixels = hsv[np.where(brick_mask > 0)]

if len(pixels) > 0:
    min_hsv = np.min(pixels, axis=0)
    max_hsv = np.max(pixels, axis=0)
    logger.info(f"Detected Color Range: Lower={tuple(min_hsv)}, Upper={tuple(max_hsv)}")
    logger.info(f"Formatted for config: [{tuple(min_hsv)}, {tuple(max_hsv)}]")
else:
    logger.error("No Lego brick detected.")