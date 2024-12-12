import RPi.GPIO as GPIO
from config.hardware_config import RASPBERRY_PI_CONFIG
from services.logger import Logger


class ColorBox:
    def __init__(self):
        """Initializes the color box component."""
        self._logger = Logger("Color Box")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RASPBERRY_PI_CONFIG["led_pin"], GPIO.OUT)
        self._light_on = False
        self._logger.info("Color box initialized")

    def __del__(self):
        """Cleans up the color box component."""
        if self._light_on:
            self.turnLightOff()
        GPIO.cleanup()

    def turnLightOn(self):
        """Turns the light on."""
        if self._light_on:
            self._logger.warning("Trying to turn the light on while it is already on!")
            return
        GPIO.output(RASPBERRY_PI_CONFIG["led_pin"], GPIO.HIGH)
        self._light_on = True
        self._logger.info("Light turned on")

    def turnLightOff(self):
        """Turns the light off."""
        if not self._light_on:
            self._logger.warning("Trying to turn the light off while it is already off!")
            return
        GPIO.output(RASPBERRY_PI_CONFIG["led_pin"], GPIO.LOW)
        self._light_on = False
        self._logger.info("Light turned off")

    def getColor(self):
        """Returns the color detected by the color sensor."""
        color = "unrecognized"
        self._logger.info("Color detected: " + color)
        return color
