import configparser
from src.managers.core.logging_manager import logging_manager
from singleton_decorator import singleton


@singleton
class configuration_manager:
    def __init__(self, filename: str = None) -> None:
        self.filename = filename

        if filename is not None:
            self.load(self.filename)
        else:
            self.raw_config = None

        logging_manager().log.debug("Configuration manager initialized.")

    def load(self, filename: str) -> configparser.ConfigParser:
        """Loads a configuration file."""
        logging_manager().log.info(f"Loaded configuration file: {filename}")

        self.raw_config = configparser.ConfigParser()
        self.raw_config.read(filename)
        self.raw_config.sections()
        return self.raw_config

    def reload(self) -> configparser.ConfigParser:
        """Reloads the configuration file."""
        self.load(self.filename)
        return self.raw_config

    def chk_loaded(self) -> bool:
        """Checks if a configuration file is loaded."""
        return None not in [self.filename, self.raw_config]

    def get_str(self, section: str, option: str) -> str:
        """Returns a string from configuration file. Returns None if no file loaded."""
        if not self.chk_loaded():
            logging_manager().log.warning("No configuration file loaded.")
            return None
        return self.raw_config.get(section, option)

    def get_int(self, section: str, option: str) -> int:
        """Returns a int from configuration file. Returns None if no file loaded."""
        if not self.chk_loaded():
            logging_manager().log.warning("No configuration file loaded.")
            return None
        return self.raw_config.getint(section, option)

    def get_bool(self, section: str, option: str) -> bool:
        """Returns a bool from configuration file. Returns None if no file loaded."""
        if not self.chk_loaded():
            logging_manager().log.warning("No configuration file loaded.")
            return None
        return self.raw_config.getboolean(section, option)
