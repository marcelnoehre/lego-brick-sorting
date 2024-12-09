import datetime
from config.log_colors import LOG_COLORS

class Logger:
    def __init__(self, name):
        self.name = name

    def _current_time(self):
        return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

    def _log(self, msg, color, level):
        print(f"{LOG_COLORS['green']}{self._current_time()}{LOG_COLORS['white']} | {LOG_COLORS[color]}{level}{LOG_COLORS['white']} | {LOG_COLORS['purple']}[{self.name}] {LOG_COLORS['reset']}{msg}")

    def info(self, msg):
        self._log(msg, "cyan", "INFO   ")

    def warning(self, msg):
        self._log(msg, "yellow", "WARNING")

    def error(self, msg):
        self._log(msg, "red", "ERROR  ")