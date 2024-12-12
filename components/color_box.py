from services.logger import Logger


class ColorBox:
    def __init__(self):
        """Initializes the color box component."""
        self._logger = Logger("Color Box")
        self._light_on = False

    def turnLightOn(self):
        """Turns the light on."""
        if self._light_on:
            self._logger.warning("Trying to turn the light on while it is already on!")
            return
        self._light_on = True
        self._logger.info("Light turned on")

    def turnLightOff(self):
        """Turns the light off."""
        if not self._light_on:
            self._logger.warning("Trying to turn the light off while it is already off!")
            return
        self._light_on = False
        self._logger.info("Light turned off")
