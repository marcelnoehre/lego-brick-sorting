import time
from services.logger import Logger


class Machine:
    def __init__(self):
        self._logger = Logger("Machine")
        self._is_running = False

    def start(self):
        self._is_running = True
        self._logger.info("Machine started")

    def stop(self):
        self._is_running = False
        self._logger.info("Machine stopped")
