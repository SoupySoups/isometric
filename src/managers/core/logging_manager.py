import logging
from sys import stdout
from typing import Union
from src.utils.common_routines import quit
from singleton_decorator import singleton



@singleton
class logging_manager:
    """Manages logging needs."""

    def __init__(self) -> None:
        self.log_level = self.log_level_name_to_value('INFO')
        logging.basicConfig(
            format="%(asctime)s - [%(name)s | %(filename)s:%(lineno)d] - %(levelname)s - %(message)s",
            filename="game.log",
            filemode="w",
            level=self.log_level,
        )
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.StreamHandler(stdout))

        self.log.addHandler(self.log_type_hander())

        self.log.debug("Logging manager initialized.")

    def log_level_name_to_value(self, log_level_name: str) -> int:
        """Returns the log level value for a log level name."""
        if type(log_level_name) == str:
            return logging.getLevelName(log_level_name)
        else:
            self.log.error("Log level name must be a string.")

    def log_level_value_to_name(self, log_level_value: int) -> str:
        """Returns the log level name for a log level value."""
        if type(log_level_value) == int:
            return logging.getLevelName(log_level_value)
        else:
            self.log.error("Log level value must be an integer.")

    def switch_log_level(self, log_level: Union[int, str]) -> bool:
        """Switches the log level."""
        old = self.log_level
        if type(log_level) == int:
            self.log_level = log_level
        elif type(log_level) == str:
            self.log_level = self.log_level_name_to_value(log_level)
        else:
            self.log.error("Log level must be a string or an integer.")
            return False

        self.log.setLevel(self.log_level)
        if old != self.log_level:
            self.log.info(
                "Log level switched to %s.", self.log_level_value_to_name(self.log_level)
            )
        return True
    
    @singleton
    class log_type_hander(logging.StreamHandler):
        """Responds to logging events."""

        def emit(self, record):
            if record.levelno >= logging.CRITICAL:
                quit()
            elif record.levelno >= logging.FATAL:
                quit()
            elif record.levelno >= logging.ERROR:
                quit()
            else:
                pass