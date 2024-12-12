from services.logger import Logger


class ValveControl:
    def __init__(self):
        """Initializes the valve control component."""
        self._logger = Logger("Valve Control")
        self._valves = [False] * 16
        self._logger.info("Valve control initialized")

    def openValve(self, valve_id):
        """
        Opens the specified valve.

        :param valve_id: The ID of the valve to open
        """
        if valve_id < 0 or valve_id > len(self._valves) - 1:
            self._logger.error(f"Invalid valve ID: {valve_id}")
            return
        if self._valves[valve_id]:
            self._logger.warning(f"Trying to open valve {valve_id} while it is already open!")
            return
        self._valves[valve_id] = True
        self._logger.info(f"Valve {valve_id} opened")

    def closeValve(self, valve_id):
        """
        Closes the specified valve.

        :param valve_id: The ID of the valve to close
        """
        if valve_id < 0 or valve_id > len(self._valves) - 1:
            self._logger.error(f"Invalid valve ID: {valve_id}")
            return
        if not self._valves[valve_id]:
            self._logger.warning(f"Trying to close valve {valve_id} while it is already closed!")
            return
        self._valves[valve_id] = False
        self._logger.info(f"Valve {valve_id} closed")

    def closeAllValves(self):
        """Closes all valves."""
        for i in range(len(self._valves)):
            self._valves[i] = False
        self._logger.info("All valves closed")
