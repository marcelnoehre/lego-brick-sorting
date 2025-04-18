import RPi.GPIO as GPIO
import time
import threading
from services.logger import Logger
from config.hardware_config import VIBRATORY_PLATE

class VibratoryPlate:
    def __init__(self):
        """Initializes the vibratory plate component."""
        self._logger = Logger("Vibratory Plate")
        self._is_running = False
        GPIO.setmode(GPIO.BCM)
        for pin in VIBRATORY_PLATE["motor"].values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        self._logger.info("Vibratory plate initialized")

    def __del__(self):
        """Cleans up the vibratory plate component."""
        if self._is_running:
            self.stop(False)
        GPIO.cleanup()

    def _restart_after_delay(self):
        """Restarts the vibratory plate after a delay."""
        time.sleep(VIBRATORY_PLATE["timeout"])
        self.start()

    def start(self):
        """Starts the vibratory plate."""
        if self._is_running:
            self._logger.warning("Trying to start the vibratory plate while it is already running!")
            return
        GPIO.output(VIBRATORY_PLATE["motor"]["in_1"], GPIO.HIGH)
        GPIO.output(VIBRATORY_PLATE["motor"]["in_3"], GPIO.HIGH)
        self._is_running = True
        self._logger.info("Vibratory plate started")

    def stop(self, restart = True):
        """Stops the vibratory plate."""
        if not self._is_running:
            self._logger.warning("Trying to stop the vibratory plate while it is already stopped!")
            return
        GPIO.output(VIBRATORY_PLATE["motor"]["in_1"], GPIO.LOW)
        GPIO.output(VIBRATORY_PLATE["motor"]["in_3"], GPIO.LOW)
        self._is_running = False
        if restart:
            threading.Thread(target=self._restart_after_delay).start()
        self._logger.info("Vibratory plate stopped")
