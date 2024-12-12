from services.logger import Logger

class Timer:
    def __init__(self, function):
        """Initializes the timer component."""
        self.function = function
        self._logger = Logger("Timer")
        self._instances = []

    def __del__(self):
        """Cleans up the timer component."""
        self._instances.clear()
        self._logger.info("Timer cleaned up")

    def _emit_event(self, id):
        """
        Emits an event for a timer that has completed its countdown.

        :param id: The ID of the valve to open
        """
        self._logger.info(f"Timer for valve {id} completed")
        self.function(id)

    def initialize(self, id, duration):
        """
        Initializes a new timer instance.

        :param id: The ID of the valve to open
        :param duration: The duration of the timer instance in ms
        """
        self._instances.append({"id": id, "duration": duration, "initialized": False})  
        self._logger.info(f"Timer instance for valve {id} initialized with a duration of {duration} ms")

    def start(self):
        """Starts the most recently initialized timer instance."""
        for timer in self._instances:
            if not timer["initialized"]:
                if timer["duration"] <= 0:
                    self._instances.remove(timer)
                    self._logger.info("Timer of unrecognized piece removed")
                else:
                    timer["initialized"] = True
                    self._logger.info(f"Timer for valve {timer['id']} started")
                break

    def update(self, delta_time):
        """
        Updates all timers by decrementing their remaining time if they are running.

        :param delta_time: The elapsed time since the last update in milliseconds
        """
        for timer in self._instances:
            if timer["initialized"]:
                timer["duration"] -= delta_time
                if timer["duration"] <= 0:
                    self._emit_event(timer["id"])
                    self._instances.remove(timer)
        self._logger.info("Timers updated")