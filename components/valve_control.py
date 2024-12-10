from services.logger import Logger

class ValveControl:
    def __init__(self):
        self.logger = Logger("Valve Control")
        self.valves = [False] * 16

    def openValve(self, valve_id):
        if valve_id < 0 or valve_id > len(self.valves) - 1:
            self.logger.error(f"Invalid valve ID: {valve_id}")
            return
        if self.valves[valve_id]:
            self.logger.warning(f"Trying to open valve {valve_id} while it is already open!")
            return
        self.valves[valve_id] = True
        self.logger.info(f"Valve {valve_id} opened")

    def closeValve(self, valve_id):
        if valve_id < 0 or valve_id > len(self.valves) - 1:
            self.logger.error(f"Invalid valve ID: {valve_id}")
            return
        if not self.valves[valve_id]:
            self.logger.warning(f"Trying to close valve {valve_id} while it is already closed!")
            return
        self.valves[valve_id] = False
        self.logger.info(f"Valve {valve_id} closed")