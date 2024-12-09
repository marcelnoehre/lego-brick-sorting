import time
from services.logger import Logger

class Machine:
    def __init__(self):
        self.is_running = False

    def start(self, *args, **kwargs):
        logger = Logger("Machine")
        self.is_running = True
        while self.is_running:
            logger.info("Sorting bricks")
            time.sleep(3)
            logger.warning("Sorting bricks")
            time.sleep(3)
            logger.error("Sorting bricks")
            time.sleep(3)

    def stop(self, *args, **kwargs):
        self.is_running = False