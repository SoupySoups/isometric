import src.managers.window_manager as window_manager
import src.managers.configuration_manager as configuration_manager
import src.managers.logging_manager as logging_manager
import src.managers.screen_manager as screen_manager
import src.managers.data_manager as data_manager
import src.elements.camera as camera
import src.managers.object_manager as object_manager
import src.managers.event_manager as event_manager
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
        self.om = object_manager.object_manager(self.cm, self.lm)
        self.em = event_manager.event_manager(self.cm, self.lm)
        self.camera = camera.camera(self.cm, self.lm)

        self.sm.create_callback("game_frame", self.game_frame)

        self.lm.log.info("Application manager initialized.")

        self.events = []

    def game_frame(self, screen: pygame.Surface) -> None:
        if not self.dm.current_level:
            raise AttributeError("No level currently loaded.")

        screen.fill(self.dm.current_level.background_color)  # Clear screen.

        # events = self.em.get_events()
        self.em.get_events()

        x, y = pygame.mouse.get_pos()
        self.camera.position = ((x - 800) // 3, (y - 450) // 3)

        self.camera.render(self.dm.current_level)  # Render.
        screen.blit(self.camera.surface, (0, 0))  # Blit to screen.

    def run(self) -> None:
        while True:
            self.sm.run_callback()
            self.wm.update(self.sm.screen)  # Update screen.
