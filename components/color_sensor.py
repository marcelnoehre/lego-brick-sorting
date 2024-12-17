import smbus
import time
from services.logger import Logger
from config.hardware_config import COLOR_SENSOR, TIME

class ColorSensor:
    def __init__(self):
        """Initializes the color sensor component."""
        self._logger = Logger("Color Sensor")
        self._bus = smbus.SMBus(COLOR_SENSOR["i2c_bus"])
        self._enable_sensor()
        self._logger.info("Color sensor initialized")

    def _enable_sensor(self):
        """Enables the color sensor."""
        self._bus.write_byte_data(COLOR_SENSOR["i2c_address"], COLOR_SENSOR["integration_time"], COLOR_SENSOR["ensure_power"])
        self._logger.info("Color sensor enabled")
    
    def get_color(self):
        """Returns the color from the color sensor."""
        red = self._bus.read_byte_data(COLOR_SENSOR["i2c_address"], COLOR_SENSOR["red_channel"])
        green = self._bus.read_byte_data(COLOR_SENSOR["i2c_address"], COLOR_SENSOR["green_channel"])
        blue = self._bus.read_byte_data(COLOR_SENSOR["i2c_address"], COLOR_SENSOR["blue_channel"])
        return red, green, blue
    

if __name__ == "__main__":
    try:
        color_sensor = ColorSensor()
        while True:
            red, green, blue = color_sensor.read_color()
            print(f"Red: {red}, Green: {green}, Blue: {blue}")
            time.sleep(TIME["tick"] * 2)
    except KeyboardInterrupt:
        print("Exiting...")