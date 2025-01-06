import RPi.GPIO as GPIO
from config.hardware_config import RASPBERRY_PI_CONFIG
from config.flags import FLAGS
from services.logger import Logger
from components.color_sensor import ColorSensor
from components.camera_module import CameraModule


class ColorBox:
    def __init__(self):
        """Initializes the color box component."""
        self._logger = Logger("Color Box")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RASPBERRY_PI_CONFIG["led_pin"], GPIO.OUT)
        self._light_on = False
        if FLAGS["color_sensor_flag"]:
            self._color_sensor = ColorSensor()
        if FLAGS["camera_module_flag"]:
            self._camera_module = CameraModule()
        self._logger.info("Color box initialized")

    def __del__(self):
        """Cleans up the color box component."""
        if self._light_on:
            self.turn_light_off()
        GPIO.cleanup()

    def turn_light_on(self):
        """Turns the light on."""
        if self._light_on:
            self._logger.warning("Trying to turn the light on while it is already on!")
            return
        GPIO.output(RASPBERRY_PI_CONFIG["led_pin"], GPIO.HIGH)
        self._light_on = True
        self._logger.info("Light turned on")

    def turn_light_off(self):
        """Turns the light off."""
        if not self._light_on:
            self._logger.warning("Trying to turn the light off while it is already off!")
            return
        GPIO.output(RASPBERRY_PI_CONFIG["led_pin"], GPIO.LOW)
        self._light_on = False
        self._logger.info("Light turned off")

    def get_color(self):
        """Returns the color detected by the color sensor."""
        if FLAGS["color_sensor_flag"]:
            color = self._color_sensor.get_color()
        if FLAGS["camera_module_flag"]:
            color = self._camera_module.get_color()
        self._logger.info("Color detected: " + color)
        return color
