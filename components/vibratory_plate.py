from services.logger import Logger
from components.light_barrier import LightBarrier
from config.hardware_config import RASPBERRY_PI_CONFIG


class VibratoryPlate:
    def __init__(self):
        self._logger = Logger("Vibratory Plate")
        self._is_running = False
        self._light_barrier = LightBarrier(
            "Light Barrier (Vibratory Plate)", RASPBERRY_PI_CONFIG["vibratory_plate_light_barrier_pin"], 0.1
        )
        self._light_barrier.subscribe(self._handle_light_barrier_event)
        self._light_barrier.start()
        self.start()

    def __del__(self):
        self._light_barrier.unsubscribe(self._handle_light_barrier_event)
        self._light_barrier.stop()

    def _handle_light_barrier_event(self, value):
        if value == 0 and self._is_running:
            self.stop()

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
