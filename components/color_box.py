from services.logger import Logger


class ColorBox:
    def __init__(self):
        self.logger = Logger("Color Box")
        self.light_on = False

    def turnLightOn(self):
        if self.light_on:
            self.logger.warning("Trying to turn the light on while it is already on!")
            return
        self.light_on = True
        self.logger.info("Light turned on")

    def turnLightOff(self):
        if not self.light_on:
            self.logger.warning("Trying to turn the light off while it is already off!")
            return
        self.light_on = False
        self.logger.info("Light turned off")
