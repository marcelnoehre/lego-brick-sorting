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

    def _check_sensor_state(self):
        """
        Checks the current state of the sensor and emits an event if the state has changed.
        """
        value = GPIO.input(self.pin)
        if value != self._value:
            self._value = value
            self._emit_event(value)

    def _emit_event(self, value):
        """
        Emits an event and triggers all subscribed callbacks.

        :param value: The new sensor value (0 for interruption, 1 for light)
        """
        for callback in self._callbacks:
            callback(value)

    def _monitor(self):
        """
        Starts monitoring the sensor and checks for changes in a separate thread.
        """
        try:
            while self._monitoring_thread is not None:
                self._check_sensor_state()
                time.sleep(self.interval)
        finally:
            GPIO.cleanup()
