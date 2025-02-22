import RPi.GPIO as GPIO
from services.logger import Logger
from config.hardware_config import LIGHT_BARRIER

class LightBarrier:
    def __init__(self, callback):
        """Initializes the light barrier sensor."""
        self._logger = Logger("Light Barrier")
        self._is_running = False
        self.callback = callback
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LIGHT_BARRIER["pin"], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self._logger.info("Light barrier initialized")

    def __del__(self):
        """Cleans up the light barrier sensor."""
        if self._is_running:
            self.stop()
        GPIO.cleanup()

    def start(self):
        """Starts monitoring the light barrier sensor."""
        if self._is_running:
            self._logger.warning("Trying to start the light barrier sensor while it is already running!")
            return
        GPIO.add_event_detect(LIGHT_BARRIER["pin"], GPIO.BOTH, callback=self.handle_event, bouncetime=LIGHT_BARRIER["bounce_time"])
        self._is_running = True
        self._logger.info("Light barrier monitoring started")

    def stop(self):
        """Stops monitoring the light barrier sensor."""
        if not self._is_running:
            self._logger.warning("Trying to stop the light barrier sensor while it is already stopped!")
            return
        GPIO.remove_event_detect(LIGHT_BARRIER["pin"])
        self._is_running = False
        self._logger.info("Light barrier monitoring stopped")

    def handle_event(self, channel):
        """Callback function to handle the event when an object is detected."""
        if GPIO.input(channel) == GPIO.LOW:
            self.callback()
            self._logger.info("Object detected!")
        else:
            self._logger.info("Object removed.")
