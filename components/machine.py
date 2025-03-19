from components.color_box import ColorBox
from components.valve_control import ValveControl
from components.vibratory_plate import VibratoryPlate
from components.light_barrier import LightBarrier
from services.logger import Logger
from config.flags import FLAGS

class Machine:
    def __init__(self):
        """Initializes the machine component."""
        self._logger = Logger("Machine")
        self._is_running = False
        self._valve_control = ValveControl()
        self._color_box = ColorBox(self._valve_control.open_valve)
        if FLAGS["vibratory_plate"]:
            self._vibratory_plate = VibratoryPlate()
            self._light_barrier = LightBarrier(self._vibratory_plate.stop)
        self._logger.info("Machine initialized")

    def __del__(self):
        """Cleans up the machine component."""
        self.stop()

    def start(self):
        """Starts the machine."""
        self._color_box.start()
        if FLAGS["vibratory_plate"]:
            self._light_barrier.start()
            self._vibratory_plate.start()
        self._is_running = True
        self._logger.info("Machine started")

    def stop(self):
        """Stops the machine."""
        self._color_box.stop()
        self._valve_control.close_all_valves()
        if FLAGS["vibratory_plate"]:
            self._light_barrier.stop()
            self._vibratory_plate.stop()
        self._is_running = False
        self._logger.info("Machine stopped")
