from services.logger import Logger

class ConveyorBelt:
    def __init__(self):
        self.logger = Logger("Conveyor Belt")
        self.is_running = False

    def start(self):
        if self.is_running:
            self.logger.warning("Trying to start the conveyor belt while it is already running!")
            return
        self.is_running = True
        self.logger.info("Conveyor belt started")

    def stop(self):
        if not self.is_running:
            self.logger.warning("Trying to stop the conveyor belt while it is already stopped!")
            return
        self.is_running = False
        self.logger.info("Conveyor belt stopped")