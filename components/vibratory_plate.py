from services.logger import Logger


class VibratoryPlate:
    def __init__(self):
        self._logger = Logger("Vibratory Plate")
        self._is_running = False

    def start(self):
        if self._is_running:
            self._logger.warning("Trying to start the vibratory plate while it is already running!")
            return
        self._is_running = True
        self._logger.info("Vibratory plate started")

    def stop(self):
        if not self._is_running:
            self._logger.warning("Trying to stop the vibratory plate while it is already stopped!")
            return
        self._is_running = False
        self._logger.info("Vibratory plate stopped")
