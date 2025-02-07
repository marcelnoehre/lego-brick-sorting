import time
from config.log_colors import LOG_COLORS
from config.hardware_config import RASPBERRY_PI_CONFIG, TIME
from services.logger import Logger
from components.valve_control import ValveControl
from components.conveyor_belt import ConveyorBelt
from components.vibratory_plate import VibratoryPlate
from components.light_barrier import LightBarrier
from components.timer import Timer


def print_commands():
    """Prints the available user commands."""
    print(f"""{LOG_COLORS["bold_underlined_purple"]}Test Lego Brick Sorting Machine!{LOG_COLORS["reset"]}""")
    print(f"* {LOG_COLORS['blue']}[0]{LOG_COLORS['reset']} Quit testing")
    print(f"* {LOG_COLORS['blue']}[1]{LOG_COLORS['reset']} Run the vibratory plate for 5 seconds")
    print(f"* {LOG_COLORS['blue']}[2]{LOG_COLORS['reset']} Run the conveyor belt for 5 seconds")
    print(f"* {LOG_COLORS['blue']}[3]{LOG_COLORS['reset']} Activate user defined valve")
    print(f"* {LOG_COLORS['blue']}[4]{LOG_COLORS['reset']} Get the color of the current brick")
    print(f"* {LOG_COLORS['blue']}[5]{LOG_COLORS['reset']} Await trigger of user defined light barrier")
    print(f"* {LOG_COLORS['blue']}[6]{LOG_COLORS['reset']} Run vibratory plate until brick is detected")
    print(f"* {LOG_COLORS['blue']}[7]{LOG_COLORS['reset']} Run conveyor belt until brick is sorted")


def user_input():
    """Handles the user input. The user can start, stop, or quit the program."""
    logger = Logger("Test")
    command = input("Which test should be run? ").strip().lower()
    if command == "0":
        logger.info("Quitting the program")
        exit()
    elif command == "1":
        logger.info("Running the vibratory plate for 5 seconds")
        run_vibratory_plate()
    elif command == "2":
        logger.info("Running the conveyor belt for 5 seconds")
        run_conveyor_belt()
    elif command == "3":
        logger.info("Activating user defined valve")
        activate_valve(logger)
    elif command == "4":
        logger.info("Getting the color of the current brick")
        get_color(logger)
    elif command == "5":
        logger.info("Awaiting trigger of light barrier")
        start_light_barrier(logger)
    elif command == "6":
        logger.info("Running vibratory plate until brick is detected")
        run_vibratory_plate_until_brick_detected()
    elif command == "7":
        logger.info("Sort a brick")
        sort_brick(logger)
    else:
        logger.warning("Invalid command! Please use one of the following commands:")
    print_commands()
    user_input()


def run_vibratory_plate():
    """Runs the vibratory plate for 5 seconds."""
    vibratory_plate = VibratoryPlate()
    vibratory_plate.start()
    time.sleep(5)
    vibratory_plate.stop()


def run_conveyor_belt():
    """Runs the conveyor belt for 5 seconds."""
    conveyor_belt = ConveyorBelt()
    conveyor_belt.start()
    time.sleep(5)
    conveyor_belt.stop()


def activate_valve(logger):
    """Activates the user defined valve."""
    valve_control = ValveControl()
    valve_id = int(input("Enter the valve ID: "))
    if valve_id < 1 or valve_id > 16:
        logger.error(f"Invalid valve ID: {valve_id}")
        return
    valve_control.open_valve(valve_id - 1)
    time.sleep(TIME["valve_open_duration"])
    valve_control.close_valve(valve_id - 1)


def get_color(logger):
    """Gets the color of the current brick."""
    pass


def start_light_barrier(logger):
    """Awaits trigger of the light barrier."""
    light_barrier = LightBarrier("Light Barrier", RASPBERRY_PI_CONFIG["light_barrier_pin"], TIME["light_barrier_interval"])
    
    def handle_light_barrier_event(value):
        logger.info("Light barrier triggered", value)
        light_barrier.unsubscribe(handle_light_barrier_event)
    
    light_barrier.subscribe(handle_light_barrier_event)


def run_vibratory_plate_until_brick_detected():
    """Runs the vibratory plate until a brick is detected."""
    vibratory_plate = VibratoryPlate()
    light_barrier = LightBarrier("Light Barrier", RASPBERRY_PI_CONFIG["light_barrier_pin"], TIME["light_barrier_interval"])
    light_barrier.subscribe(lambda value: vibratory_plate.stop())
    vibratory_plate.start()


def sort_brick(logger):
    """Runs the conveyor belt until a brick is sorted."""
    pass


if __name__ == "__main__":
    print_commands()
    user_input()