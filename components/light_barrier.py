import RPi.GPIO as GPIO
import time
import threading
from services.logger import Logger


class LightBarrier:
    def __init__(self, id, pin, interval):
        """
        Initializes the light barrier sensor on a specified GPIO pin.

        :param id: The ID of the light barrier sensor
        :param pin: The GPIO pin connected to the light barrier sensor
        :param interval: The interval in seconds in which the sensor state is checked
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
        """Checks the current state of the sensor and emits an event if the state has changed."""
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
        """Starts monitoring the sensor and checks for changes in a separate thread."""
        try:
            while self._monitoring_thread is not None:
                self._check_sensor_state()
                time.sleep(self.interval)
        finally:
            GPIO.cleanup()

    def subscribe(self, callback):
        """
        Subscribes to the event that is triggered when the light barrier is interrupted or completed.

        :param callback: The callback function to be called when the barrier is interrupted or completed.
        """
        if callback not in self._callbacks:
            self._callbacks.append(callback)

    def unsubscribe(self, callback):
        """
        Unsubscribes from the event.

        :param callback: The callback function to be removed from the subscription list.
        """
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    def start(self):
        """Starts monitoring the light barrier sensor."""
        if self.is_running:
            self._logger.warning("Trying to start monitoring while it is already running!")
            return
        if self.monitoring_thread is not None:
            self._logger.error("Monitoring thread already exists!")
            return
        self.monitoring_thread = threading.Thread(target=self._monitor)
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()
        self._is_running = True
        self._logger.info("Monitoring started")

    def stop(self):
        """Stops monitoring the light barrier sensor."""
        if not self.is_running:
            self._logger.warning("Trying to stop monitoring while it is already stopped!")
            return
        if not self.monitoring_thread:
            self._logger.error("Monitoring thread does not exist!")
            return
        self._monitoring_thread.join()
        self._monitoring_thread = None
        self._is_running = False
        self._logger.info("Monitoring stopped")
