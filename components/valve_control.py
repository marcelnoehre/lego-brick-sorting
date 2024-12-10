from services.logger import Logger


class ValveControl:
    def __init__(self):
        self._logger = Logger("Valve Control")
        self._valves = [False] * 16

    def openValve(self, valve_id):
        if valve_id < 0 or valve_id > len(self._valves) - 1:
            self._logger.error(f"Invalid valve ID: {valve_id}")
            return
        if self.valves[valve_id]:
            self._logger.warning(f"Trying to open valve {valve_id} while it is already open!")
            return
        self._valves[valve_id] = True
        self._logger.info(f"Valve {valve_id} opened")

    def closeValve(self, valve_id):
        if valve_id < 0 or valve_id > len(self._valves) - 1:
            self._logger.error(f"Invalid valve ID: {valve_id}")
            return
        if not self._valves[valve_id]:
            self._logger.warning(f"Trying to close valve {valve_id} while it is already closed!")
            return
        self._valves[valve_id] = False
        self._logger.info(f"Valve {valve_id} closed")
