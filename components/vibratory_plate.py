from services.logger import Logger


class VibratoryPlate:
    def __init__(self):
        """Initializes the vibratory plate component."""
        self._logger = Logger("Vibratory Plate")
        self._is_running = False
        self._logger.info("Vibratory plate initialized")

    def __del__(self):
        """Cleans up the vibratory plate component."""
        if self._is_running:
            self.stop()

    def start(self):
        """Starts the vibratory plate."""
        if self._is_running:
            self._logger.warning("Trying to start the vibratory plate while it is already running!")
            return
        # TODO: Start the vibratory plate
        self._is_running = True
        self._logger.info("Vibratory plate started")

    def stop(self):
        """Stops the vibratory plate."""
        if not self._is_running:
            self._logger.warning("Trying to stop the vibratory plate while it is already stopped!")
            return
        # TODO: Stop the vibratory plate
        self._is_running = False
        self._logger.info("Vibratory plate stopped")
