import time
from config.log_colors import LOG_COLORS
from components.valve_control import ValveControl
from components.vibratory_plate import VibratoryPlate
from components.light_barrier import LightBarrier
from services.logger import Logger

class Test:
    def __init__(self):
        """Initializes the test component."""
        self._logger = Logger("Test")
        
    def print_commands(self):
        """Prints the available user commands."""
        print(f"""{LOG_COLORS["bold_underlined_purple"]}Test Lego Brick Sorting Machine!{LOG_COLORS["reset"]}""")
        print(f"* {LOG_COLORS['blue']}[0]{LOG_COLORS['reset']} Quit testing")
        print(f"* {LOG_COLORS['blue']}[1]{LOG_COLORS['reset']} Activate user defined valve")
        print(f"* {LOG_COLORS['blue']}[2]{LOG_COLORS['reset']} Get the color of the current brick")
        print(f"* {LOG_COLORS['blue']}[3]{LOG_COLORS['reset']} Run the vibratory plate for 5 seconds")
        print(f"* {LOG_COLORS['blue']}[4]{LOG_COLORS['reset']} Await trigger of the light barrier")
        print(f"* {LOG_COLORS['blue']}[5]{LOG_COLORS['reset']} Run vibratory plate until brick is detected")

    def user_input(self):
        """Handles the user input. The user can start, stop, or quit the program."""
        command = input("Which test should be run? ").strip().lower()
        if command == "0":
            self._logger.info("Quitting the program")
            exit()
        elif command == "1":
            self._logger.info("Activating user defined valve")
            self.activate_valve()
        elif command == "2":
            self._logger.info("Getting the color of the current brick")
            self.get_color()
        elif command == "3":
            self._logger.info("Running the vibratory plate for 5 seconds")
            self.run_vibratory_plate()
        elif command == "4":
            self._logger.info("Awaiting trigger of light barrier")
            self.start_light_barrier()
        elif command == "5":
            self._logger.info("Running vibratory plate until brick is detected")
            self.run_vibratory_plate_until_brick_detected()
        else:
            self._logger.warning("Invalid command! Please use one of the following commands:")
        self.print_commands()
        self.user_input()

    def activate_valve(self):
        """Activates the user defined valve."""
        valve_control = ValveControl()
        valve_id = int(input("Enter the valve ID: "))
        if valve_id < 1 or valve_id > 16:
            self._logger.error(f"Invalid valve ID: {valve_id}")
            return
        valve_control.open_valve(valve_id - 1)

    def get_color(self):
        """Gets the color of the current brick."""
        pass

    def run_vibratory_plate(self):
        """Runs the vibratory plate for 5 seconds."""
        vibratory_plate = VibratoryPlate()
        vibratory_plate.start()
        time.sleep(5)
        vibratory_plate.stop()

    def start_light_barrier(self):
        """Awaits trigger of the light barrier."""
        light_barrier = LightBarrier(lambda: self._logger.info("Light barrier triggered"))
        light_barrier.start()
        time.sleep(10)
        light_barrier.stop()

    def run_vibratory_plate_until_brick_detected(self):
        """Runs the vibratory plate until a brick is detected."""
        vibratory_plate = VibratoryPlate()
        light_barrier = LightBarrier(lambda: vibratory_plate.stop())
        light_barrier.start()
        vibratory_plate.start()
        light_barrier.stop()

if __name__ == "__main__":
    test = Test()
    test.print_commands()
    test.user_input()