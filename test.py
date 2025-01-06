import time
from config.flags import FLAGS
from config.log_colors import LOG_COLORS
from config.hardware_config import RASPBERRY_PI_CONFIG, TIME
from config.brick_colors import BRICK_COLORS
from services.logger import Logger
from components.color_box import ColorBox
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
    print(f"* {LOG_COLORS['blue']}[2]{LOG_COLORS['reset']} Turn the light on for 5 seconds")
    print(f"* {LOG_COLORS['blue']}[3]{LOG_COLORS['reset']} Run the conveyor belt for 5 seconds")
    print(f"* {LOG_COLORS['blue']}[4]{LOG_COLORS['reset']} Activate user defined valve")
    print(f"* {LOG_COLORS['blue']}[5]{LOG_COLORS['reset']} Get the color of the current brick")
    print(f"* {LOG_COLORS['blue']}[6]{LOG_COLORS['reset']} Await trigger of user defined light barrier")
    print(f"* {LOG_COLORS['blue']}[7]{LOG_COLORS['reset']} Run vibratory plate until brick is detected")
    print(f"* {LOG_COLORS['blue']}[8]{LOG_COLORS['reset']} Run conveyor belt until brick is in color box")
    print(f"* {LOG_COLORS['blue']}[9]{LOG_COLORS['reset']} Run conveyor belt until brick is sorted")


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
        logger.info("Turning the light on for 5 seconds")
        turn_light_on()
    elif command == "3":
        logger.info("Running the conveyor belt for 5 seconds")
        run_conveyor_belt()
    elif command == "4":
        logger.info("Activating user defined valve")
        activate_valve(logger)
    elif command == "5":
        logger.info("Getting the color of the current brick")
        get_color(logger)
    elif command == "6":
        logger.info("Awaiting trigger of user defined light barrier")
        user_defined_light_barrier(logger)
    elif command == "7":
        logger.info("Running vibratory plate until brick is detected")
        run_vibratory_plate_until_brick_detected()
    elif command == "8":
        logger.info("Running conveyor belt until brick is in color box")
        run_conveyor_belt_until_brick_in_color_box()
    elif command == "9":
        logger.info("Sort a user defined brick color")
        sort_brick(logger)
    else:
        logger.warning("Invalid command! Please use one of the following commands:")
    print_commands()
    user_input()


def run_vibratory_plate():
    """Runs the vibratory plate for 5 seconds."""
    vibratory_plate = VibratoryPlate()
    vibratory_plate.run()
    time.sleep(5)
    vibratory_plate.stop()


def turn_light_on():
    """Turns the light on for 5 seconds."""
    color_box = ColorBox()
    color_box.turn_light_on()
    time.sleep(5)
    color_box.turn_light_off()


def run_conveyor_belt():
    """Runs the conveyor belt for 5 seconds."""
    conveyor_belt = ConveyorBelt()
    conveyor_belt.run()
    time.sleep(5)
    conveyor_belt.stop()


def activate_valve(logger):
    """Activates the user defined valve."""
    valve_control = ValveControl()
    valve_id = int(input("Enter the valve ID: "))
    if valve_id < 0 or valve_id > 15:
        logger.error(f"Invalid valve ID: {valve_id}")
        return
    valve_control.open_valve(valve_id)
    time.sleep(TIME["valve_open_duration"])
    valve_control.close_valve(valve_id)


def get_color(logger):
    """Gets the color of the current brick."""
    color_box = ColorBox()
    color_box.turn_light_on()
    color = color_box.get_color()
    color_box.turn_light_off()
    logger.info(f"The color of the current brick is {color}")


def user_defined_light_barrier(logger):
    """Awaits the trigger of the user defined light barrier."""
    barrier = input("Enter the barrier ID (color_box, valve_init, vibratory_plate): ")
    if barrier not in ["color_box", "valve_init", "vibratory_plate"]:
        logger.error(f"Invalid barrier ID: {barrier}")
        return

    if barrier == "color_box":
        light_barrier = LightBarrier("Color Box Light Barrier", RASPBERRY_PI_CONFIG["color_box_light_barrier_pin"], TIME["light_barrier_interval"])
    elif barrier == "valve_init":
        light_barrier = LightBarrier("Valve Init Light Barrier", RASPBERRY_PI_CONFIG["valve_init_light_barrier_pin"], TIME["light_barrier_interval"])
    elif barrier == "vibratory_plate":
        light_barrier = LightBarrier("Vibratory Plate Light Barrier", RASPBERRY_PI_CONFIG["vibratory_plate_light_barrier_pin"], TIME["light_barrier_interval"])
    
    def handle_light_barrier_event(value):
        logger.info("{Light barrier triggered")
        light_barrier.unsubscribe(handle_light_barrier_event)
    
    light_barrier.subscribe(handle_light_barrier_event)


def run_vibratory_plate_until_brick_detected():
    """Runs the vibratory plate until a brick is detected."""
    vibratory_plate = VibratoryPlate()
    light_barrier = LightBarrier("Vibratory Plate Light Barrier", RASPBERRY_PI_CONFIG["vibratory_plate_light_barrier_pin"], TIME["light_barrier_interval"])
    light_barrier.subscribe(lambda value: vibratory_plate.stop())
    vibratory_plate.run()


def run_conveyor_belt_until_brick_in_color_box():
    """Runs the conveyor belt until a brick is in the color box."""
    conveyor_belt = ConveyorBelt()
    light_barrier = LightBarrier("Color Box Light Barrier", RASPBERRY_PI_CONFIG["color_box_light_barrier_pin"], TIME["light_barrier_interval"])
    light_barrier.subscribe(lambda value: conveyor_belt.stop())
    conveyor_belt.run()


def sort_brick(logger):
    """Runs the conveyor belt until a brick is sorted."""
    color = input("Enter the color of the brick: ")
    if color not in BRICK_COLORS:
        logger.error(f"Invalid brick color: {color}")
        return
    valve_id = BRICK_COLORS[color]["id"]
    valve_control = ValveControl()
    light_barrier = LightBarrier("Valve Init Light Barrier", RASPBERRY_PI_CONFIG["valve_init_light_barrier_pin"], TIME["light_barrier_interval"])
    conveyor_belt = ConveyorBelt()
    
    def toggle_valve(id):
        valve_control.open_valve(id)
        time.sleep(TIME["valve_open_duration"])
        valve_control.close_valve(id)

    timer = Timer(lambda: toggle_valve(valve_id))
    timer.initialize(valve_id, BRICK_COLORS[color]["duration"])

    light_barrier.subscribe(lambda value: timer.start())
    conveyor_belt.start()

    while len(timer._instances) > 0:
        time.sleep(TIME["tick"])
        timer.update(TIME["tick"])


if __name__ == "__main__":
    print_commands()
    user_input()