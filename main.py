import threading
from config.log_colors import LOG_COLORS
from services.logger import Logger
from components.machine import Machine


def print_commands():
    """Prints the available user commands."""
    print(f"""{LOG_COLORS["bold_underlined_purple"]}Lego Brick Sorting Machine!{LOG_COLORS["reset"]}""")
    print(f"* {LOG_COLORS['blue']}start{LOG_COLORS['reset']} - Starts the sorting machine")
    print(f"* {LOG_COLORS['blue']}stop{LOG_COLORS['reset']} - Stops the sorting machine")
    print(f"* {LOG_COLORS['blue']}quit{LOG_COLORS['reset']} - Quits the program")


def user_input():
    """Handles the user input. The user can start, stop, or quit the program."""
    global machine_thread
    global is_running
    is_running = False
    logger = Logger("System")

    while True:
        command = input("").strip().lower()
        if command == "start":
            if not is_running:
                logger.info("Starting the sorting machine")
                machine = Machine()
                machine_thread = threading.Thread(target=machine.start, daemon=True)
                machine_thread.start()
                is_running = True
            else:
                logger.warning("The sorting machine is already running!")

        elif command == "stop":
            if is_running:
                logger.info("Stopping the sorting machine")
                machine.stop()
                is_running = False
            else:
                logger.warning("The sorting machine is not running!")

        elif command == "quit":
            if is_running:
                logger.warning("The sorting machine is still running! Please stop it before quitting.")
                return
            logger.info("Quitting the program")
            exit()

        else:
            logger.warning("Invalid command! Please use one of the following commands:")
            print_commands()


if __name__ == "__main__":
    print_commands()
    user_input()
