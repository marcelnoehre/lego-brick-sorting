import RPi.GPIO as GPIO
import time
import threading
from services.logger import Logger


class LightBarrier:
    def __init__(self, id, pin, interval):
        """
        Initializes the light barrier sensor on a specified GPIO pin.

        :param pin: The GPIO pin connected to the light barrier sensor
        """
        self.id = id
        self.pin = pin
        self.interval = interval
        self._logger = Logger("Light Barrier " + str(id))
        self._is_running = False
        self._value = 1
        self._callbacks = []
        self._monitoring_thread = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    