import RPi.GPIO as GPIO
import time
import threading
from services.logger import Logger
from config.hardware_config import VALVES


class ValveControl:
    def __init__(self):
        """Initializes the valve control component."""
        self._logger = Logger("Valve Control")
        self._valves = [False] * VALVES["amount"]
        GPIO.setmode(GPIO.BCM)
        for i in range(1, VALVES["amount"] + 1):
            GPIO.setup(VALVES["valves"][i]["pin"], GPIO.OUT)
            GPIO.output(VALVES["valves"][i]["pin"], GPIO.HIGH)
            self._logger.info(f"Valve {i} initialized")
        self._logger.info("Valve control initialized")

    def __del__(self):
        """Cleans up the valve control component."""
        self.close_all_valves()
        GPIO.cleanup()

    def _close_valve_after_delay(self, valve_id):
        """Closes the valve after a delay."""
        time.sleep(VALVES["open_duration"])
        self.close_valve(valve_id)

    def open_valve(self, valve_id):
        """
        Opens the specified valve.

        :param valve_id: The ID of the valve to open
        """
        if valve_id < 1 or valve_id > VALVES["amount"]:
            self._logger.error(f"Invalid valve ID: {valve_id}")
            return
        if self._valves[valve_id - 1]:
            self._logger.warning(f"Trying to open valve {valve_id} while it is already open!")
            return
        GPIO.output(VALVES["valves"][valve_id]["pin"], GPIO.LOW)
        self._valves[valve_id - 1] = True
        threading.Thread(target=self._close_valve_after_delay, args=(valve_id,)).start()
        self._logger.info(f"Valve {valve_id} opened")

    def close_valve(self, valve_id):
        """
        Closes the specified valve.

        :param valve_id: The ID of the valve to close
        """
        if valve_id < 1 or valve_id > VALVES["amount"]:
            self._logger.error(f"Invalid valve ID: {valve_id}")
            return
        if not self._valves[valve_id - 1]:
            self._logger.warning(f"Trying to close valve {valve_id} while it is already closed!")
            return
        GPIO.output(VALVES["valves"][valve_id]["pin"], GPIO.HIGH)
        self._valves[valve_id - 1] = False
        self._logger.info(f"Valve {valve_id} closed")

    def close_all_valves(self):
        """Closes all valves."""
        for i in range(1, VALVES["amount"] + 1):
            if self._valves[i - 1]:
                self.close_valve(i)
        self._logger.info("All valves closed")
