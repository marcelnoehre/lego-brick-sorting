import time
from services.logger import Logger


class Machine:
    def __init__(self):
        self.logger = Logger("Machine")
        self.is_running = False

    def start(self):
        self.is_running = True
        self.logger.info("Machine started")

    def stop(self):
        self.is_running = False
        self.logger.info("Machine stopped")
