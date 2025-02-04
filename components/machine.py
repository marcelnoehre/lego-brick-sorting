import time
import threading
from config.flags import FLAGS
from config.hardware_config import RASPBERRY_PI_CONFIG, TIME
from config.brick_colors import BRICK_COLORS
from services.logger import Logger
from components.color_box import ColorBox
from components.valve_control import ValveControl
from components.conveyor_belt import ConveyorBelt
from components.vibratory_plate import VibratoryPlate
from components.light_barrier import LightBarrier
from components.timer import Timer


class Machine:
    def __init__(self):
        """Initializes the machine component."""
        self._logger = Logger("Machine")
        self._is_running = False
        self._color_box = ColorBox()
        self._valve_control = ValveControl()
        self._conveyor_belt = ConveyorBelt()
        self._color_box_light_barrier = LightBarrier(
            "Color Box Light Barrier",
            RASPBERRY_PI_CONFIG["color_box_light_barrier_pin"],
            TIME["light_barrier_interval"],
        )
        self._valve_init_light_barrier = LightBarrier(
            "Valve Init Light Barrier",
            RASPBERRY_PI_CONFIG["valve_init_light_barrier_pin"],
            TIME["light_barrier_interval"],
        )
        self._color_box_light_barrier.subscribe(self._handle_color_box_light_barrier_event)
        self._valve_init_light_barrier.subscribe(self._handle_valve_init_light_barrier_event)
        if FLAGS["vibratory_plate"]:
            self._vibratory_plate = VibratoryPlate()
            self._vibratory_plate_light_barrier = LightBarrier(
                "Vibratory Plate Light Barrier",
                RASPBERRY_PI_CONFIG["vibratory_plate_light_barrier_pin"],
                TIME["light_barrier_interval"],
            )
            self._vibratory_plate_light_barrier.subscribe(self._handle_vibratory_plate_light_barrier_event)
        self._timer = Timer(self._toggle_valve)
        self._tick_thread = None
        self._logger.info("Machine initialized")

    def __del__(self):
        """Cleans up the machine component."""
        self._color_box_light_barrier.unsubscribe(self._handle_color_box_light_barrier_event)
        self._valve_init_light_barrier.unsubscribe(self._handle_valve_init_light_barrier_event)
        if FLAGS["vibratory_plate"]:
            self._vibratory_plate_light_barrier.unsubscribe(self._handle_vibratory_plate_light_barrier_event)

    def _tick(self):
        """Ticks the machine."""
        while True:
            if self._conveyor_belt.is_running():
                time.sleep(TIME["tick"])
                self._timer.update(TIME["tick"])

    def _handle_color_box_light_barrier_event(self, value):
        """
        Handles the color box light barrier event.

        :param value: The new sensor value (0 for interruption, 1 for light)
        """
        if value == 0:
            self._conveyor_belt.stop()
            color = self._color_box.get_color()
            self._timer.initialize(BRICK_COLORS[color]["id"], BRICK_COLORS[color]["duration"])
            self._conveyor_belt.start()

    def _handle_valve_init_light_barrier_event(self, value):
        """
        Handles the valve init light barrier event.

        :param value: The new sensor value (0 for interruption, 1 for light)
        """
        if value == 0:
            self._timer.start()

    def _handle_vibratory_plate_light_barrier_event(self, value):
        """
        Handles the vibratory plate light barrier event.

        :param value: The new sensor value (0 for interruption, 1 for light)
        """
        if value == 0:
            self._vibratory_plate.stop()

    def _toggle_valve(self, id):
        """
        Toggles the valve with the specified ID.

        :param id: The ID of the valve to toggle
        """
        self._valve_control.open_valve(id)
        time.sleep(TIME["valve_open_duration"])
        self._valve_control.close_valve(id)

    def start(self):
        """Starts the machine."""
        self._color_box_light_barrier.start()
        self._valve_init_light_barrier.start()
        self._conveyor_belt.start()
        if FLAGS["vibratory_plate"]:
            self._vibratory_plate_light_barrier.start()
            self._vibratory_plate.start()
        self._tick_thread = threading.Thread(target=self._tick, daemon=True)
        self._tick_thread.start()
        self._is_running = True
        self._logger.info("Machine started")

    def stop(self):
        """Stops the machine."""
        self._color_box_light_barrier.stop()
        self._valve_init_light_barrier.stop()
        self._valve_control.close_all_valves()
        self._conveyor_belt.stop()
        if FLAGS["vibratory_plate"]:
            self._vibratory_plate_light_barrier.stop()
            self._vibratory_plate.stop()
        self._tick_thread.join()
        self._tick_thread = None
        self._is_running = False
        self._logger.info("Machine stopped")
