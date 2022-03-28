import src.managers.window_manager as window_manager
import src.managers.configuration_manager as configuration_manager
import src.managers.logging_manager as logging_manager
import src.managers.screen_manager as screen_manager
import src.managers.data_manager as data_manager
import src.managers.render_manager as render_manager
import pygame


class application_manager:
    def __init__(self) -> None:
        self.lm = logging_manager.logging_manager("INFO")  # Set up logging manager

        # Set up managers
        self.cm = configuration_manager.configuration_manager("config.ini", self.lm)
        self.lm.switch_log_level(
            self.cm.get_str_setting("Logging", "log_level")
        )  # Update log level based on configuration
        self.cm.lm = self.lm  # Update configuration manager's logging manager
        self.wm = window_manager.window_manager(self.cm, self.lm)
        self.sm = screen_manager.screen_manager(self.cm, self.lm)
        self.dm = data_manager.data_manager(self.cm, self.lm)
        self.rm = render_manager.render_manager(self.cm, self.lm)

        self.lm.log.info("Application manager initialized.")

        self.events = []

    def run(self) -> None:
        while True:
            if not self.dm.current_level:
                raise AttributeError("No currently loaded.")

            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:  # Quit.
                    pygame.quit()
                    quit()

            self.sm.current.surface.fill(self.dm.current_level.background_color)

            self.wm.update(self.sm.get_current().surface)  # Update screen.
