import RPi.GPIO as GPIO
from services.logger import Logger
from config.hardware_config import VALVES


class ValveControl:
    def __init__(self):
        """Initializes the valve control component."""
        self._logger = Logger("Valve Control")
        self._valves = [False] * 16
        GPIO.setmode(GPIO.BCM)
        for i in range(16):
            GPIO.setup(VALVES[i + 1]["pin"], GPIO.OUT)
            GPIO.output(VALVES[i + 1]["pin"], GPIO.LOW)
            self._logger.info(f"Valve {i + 1} initialized")
        self._logger.info("Valve control initialized")

    def __del__(self):
        """Cleans up the valve control component."""
        self.close_all_valves()
        GPIO.cleanup()

    def open_valve(self, valve_id):
        """
        Opens the specified valve.

        :param valve_id: The ID of the valve to open
        """
        if valve_id < 0 or valve_id > len(self._valves) - 1:
            self._logger.error(f"Invalid valve ID: {valve_id + 1}")
            return
        if self._valves[valve_id]:
            self._logger.warning(f"Trying to open valve {valve_id + 1} while it is already open!")
            return
        GPIO.output(VALVES[valve_id + 1]["pin"], GPIO.HIGH)
        self._valves[valve_id] = True
        self._logger.info(f"Valve {valve_id + 1} opened")

    def close_valve(self, valve_id):
        """
        Closes the specified valve.

        :param valve_id: The ID of the valve to close
        """
        if valve_id < 0 or valve_id > len(self._valves) - 1:
            self._logger.error(f"Invalid valve ID: {valve_id + 1}")
            return
        if not self._valves[valve_id]:
            self._logger.warning(f"Trying to close valve {valve_id + 1} while it is already closed!")
            return
        GPIO.output(VALVES[valve_id + 1]["pin"], GPIO.LOW)
        self._valves[valve_id] = False
        self._logger.info(f"Valve {valve_id + 1} closed")

    def close_all_valves(self):
        """Closes all valves."""
        for i in range(len(self._valves)):
            if self._valves[i]:
                self.close_valve(i)
