from config.flags import FLAGS
from services.logger import Logger
from components.color_sensor import ColorSensor
from components.camera_module import CameraModule


class ColorBox:
    def __init__(self):
        """Initializes the color box component."""
        self._logger = Logger("Color Box")
        if FLAGS["color_sensor_flag"]:
            self._color_sensor = ColorSensor()
        if FLAGS["camera_module_flag"]:
            self._camera_module = CameraModule()
        self._logger.info("Color box initialized")

    def get_color(self):
        """Returns the color detected by the color sensor."""
        if FLAGS["color_sensor_flag"]:
            color = self._color_sensor.get_color()
        if FLAGS["camera_module_flag"]:
            color = self._camera_module.get_color()
        self._logger.info("Color detected: " + color)
        return color
