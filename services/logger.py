import datetime
from config.flags import FLAGS
from config.log_colors import LOG_COLORS


class Logger:
    def __init__(self, name):
        """
        Initialize the logger instance with a name.

        :param name: The name of the logger
        """
        self.name = name

    def _current_time(self):
        """Get the current time in the format of [YYYY-MM-DD HH:MM:SS]."""
        return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    def _log(self, msg, color, level):
        """
        Log a message with a specific color and log level.

        :param msg: The message to be logged
        :param color: The color of the log level
        :param level: The log level of the message
        """
        if FLAGS["debug"]:
            timestamp = f"{LOG_COLORS['green']}{self._current_time()}"
            seperator = f"{LOG_COLORS['white']} | "
            level = f"{LOG_COLORS[color]}{level}"
            msg = f"{LOG_COLORS['purple']}[{self.name}] {LOG_COLORS['reset']}{msg}"
            print(timestamp + seperator + level + seperator + msg)

    def info(self, msg):
        """
        Log an info message.

        :param msg: The message to be logged
        """
        self._log(msg, "cyan", " INFO  ")

    def warning(self, msg):
        """
        Log a warning message.

        :param msg: The message to be logged
        """
        self._log(msg, "yellow", "WARNING")

    def error(self, msg):
        """
        Log an error message.

        :param msg: The message to be logged
        """
        self._log(msg, "red", " ERROR ")
