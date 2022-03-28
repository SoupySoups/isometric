import src.managers.window_manager as window_manager
import src.managers.configuration_manager as configuration_manager
import src.managers.logging_manager as logging_manager
import src.managers.screen_manager as screen_manager
import src.managers.data_manager as data_manager
import pygame


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

        self.sm = screen_manager.screen_manager(self.cm, self.lm)  # Set up screen manager

        self.dm = data_manager.data_manager(self.cm, self.lm)  # Set up data manager

        self.lm.log.info("Application manager initialized.")

        self.events = []
    

    def run(self) -> None:
        while True:
            if not self.dm.current_level:
                raise AttributeError("No currently loaded.")

            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT: # Quit.
                    pygame.quit()
                    quit()

            self.sm.current.surface.fill(self.dm.current_level.background_color)
            
            
            self.wm.update(self.sm.get_current().surface) # Update screen.
