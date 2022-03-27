import configparser


class configuration_manager:
    def __init__(self, filename: str, logging_manager) -> None:
        self.lm = logging_manager
        self.filename = filename
        self.load(self.filename)

        self.lm.log.info("Configuration manager initialized.")

    def load(self, filename: str) -> configparser.ConfigParser:
        self.lm.log.info(f"Loaded configuration file: {filename}")

        self.raw_config = configparser.ConfigParser()
        self.raw_config.read(filename)
        self.raw_config.sections()
        return self.raw_config

    def reload(self) -> configparser.ConfigParser:
        self.load(self.filename)
        return self.raw_config

    def get_str_setting(self, section: str, option: str) -> str:
        return self.raw_config.get(section, option)

    def get_int_setting(self, section: str, option: str) -> int:
        return self.raw_config.getint(section, option)

    def get_bool_setting(self, section: str, option: str) -> bool:
        return self.raw_config.getboolean(section, option)
