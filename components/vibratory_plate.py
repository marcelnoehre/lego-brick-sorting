from services.logger import Logger

class VibratoryPlate:
    def __init__(self):
        self.logger = Logger("Vibratory Plate")
        self.is_running = False

    def start(self):
        self.is_running = True
        self.logger.info("Vibratory plate started")

    def stop(self):
        self.is_running = False
        self.logger.info("Vibratory plate stopped")