from services.logger import Logger

class ConveyorBelt:
    def __init__(self):
        self.logger = Logger("Conveyor Belt")
        self.is_running = False

    def start(self):
        self.is_running = True
        self.logger.info("Conveyor belt started")

    def stop(self):
        self.is_running = False
        self.logger.info("Conveyor belt stopped")