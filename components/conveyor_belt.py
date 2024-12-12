from services.logger import Logger


class ConveyorBelt:
    def __init__(self):
        """Initializes the conveyor belt component."""
        self._logger = Logger("Conveyor Belt")
        self._is_running = False
        self._logger.info("Conveyor belt initialized")

    def start(self):
        """Starts the conveyor belt."""
        if self._is_running:
            self._logger.warning("Trying to start the conveyor belt while it is already running!")
            return
        self._is_running = True
        self._logger.info("Conveyor belt started")

    def stop(self):
        """Stops the conveyor belt."""
        if not self._is_running:
            self._logger.warning("Trying to stop the conveyor belt while it is already stopped!")
            return
        self._is_running = False
        self._logger.info("Conveyor belt stopped")
