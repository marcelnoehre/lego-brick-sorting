import time
from services.logger import Logger

class Machine:
    def __init__(self):
        self.logger = Logger("Machine")
        self.is_running = False

    def start(self, *args, **kwargs):
        self.is_running = True
        self.logger.info("Machine started")
        while self.is_running:
            self.logger.info("Sorting bricks")
            time.sleep(3)
            self.logger.warning("Sorting bricks")
            time.sleep(3)
            self.logger.error("Sorting bricks")
            time.sleep(3)

    def stop(self, *args, **kwargs):
        self.is_running = False
        self.logger.info("Machine stopped")