from services.logger import Logger

class ValveControl:
    def __init__(self):
        self.logger = Logger("Valve Control")
        self.valves = [False] * 16

    def openValve(self, valve_id):
        self.valves[valve_id] = True
        self.logger.info(f"Valve {valve_id} opened")

    def closeValve(self, valve_id):
        self.valves[valve_id] = False
        self.logger.info(f"Valve {valve_id} closed")