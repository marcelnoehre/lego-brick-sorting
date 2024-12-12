from config.flags import FLAGS
from services.logger import Logger
from components.color_box import ColorBox
from components.valve_control import ValveControl
from components.conveyor_belt import ConveyorBelt
from components.vibratory_plate import VibratoryPlate


class Machine:
    def __init__(self):
        """Initializes the machine component."""
        self._logger = Logger("Machine")
        self._is_running = False
        self._color_box = ColorBox()
        self._valve_control = ValveControl()
        self._conveyor_belt = ConveyorBelt()
        if FLAGS["vibratory_plate"]:
            self._vibratory_plate = VibratoryPlate()
        self._logger.info("Machine initialized")

    def start(self):
        """Starts the machine."""
        self._conveyor_belt.start()
        if FLAGS["vibratory_plate"]:
            self._vibratory_plate.start()
        self._is_running = True
        self._logger.info("Machine started")

    def stop(self):
        """Stops the machine."""
        self._color_box.turnLightOff()
        self._valve_control.closeAllValves()
        self._conveyor_belt.stop()
        if FLAGS["vibratory_plate"]:
            self._vibratory_plate.stop()
        self._is_running = False
        self._logger.info("Machine stopped")
