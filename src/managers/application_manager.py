import src.managers.window_manager as window_manager
import src.managers.configuration_manager as configuration_manager
import src.managers.logging_manager as logging_manager


class application_manager:
    def __init__(self) -> None:
        self.lm = logging_manager.logging_manager("INFO")  # Set up logging manager

        self.cm = configuration_manager.configuration_manager(
            "config.ini", self.lm
        )  # Set up configuration manager
        self.lm.switch_log_level(
            self.cm.get_str_setting("Logging", "log_level")
        )  # Update log level based on configuration
        self.cm.lm = self.lm  # Update configuration manager's logging manager

        self.wm = window_manager.window_manager(
            self.cm, self.lm
        )  # Set up window manager

        self.lm.log.info("Application manager initialized.")
        pass
