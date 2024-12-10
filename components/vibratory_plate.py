from services.logger import Logger

class VibratoryPlate:
    def __init__(self):
        self.logger = Logger("Vibratory Plate")
        self.is_running = False

    def start(self):
        if self.is_running:
            self.logger.warning("Trying to start the vibratory plate while it is already running!")
            return
        self.is_running = True
        self.logger.info("Vibratory plate started")

    def stop(self):
        if not self.is_running:
            self.logger.warning("Trying to stop the vibratory plate while it is already stopped!")
            return
        self.is_running = False
        self.logger.info("Vibratory plate stopped")