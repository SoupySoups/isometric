from src.managers.window_manager import window_manager as window_manager
from src.managers.configuration_manager import (
    configuration_manager as configuration_manager,
)
from src.managers.logging_manager import logging_manager as logging_manager
from src.managers.screen_manager import screen_manager as screen_manager
from src.managers.data_manager import data_manager as data_manager
from src.managers.object_manager import object_manager as object_manager
from src.managers.component_manager import component_manager as component_manager

from src.elements.camera import camera as camera

import pygame


class application_manager:
    def __init__(self) -> None:
        self.lm = logging_manager("INFO")  # Set up logging manager

        # Set up managers
        # Essential managers
        self.cm = configuration_manager("config.ini", self.lm)
        self.lm.switch_log_level(
            self.cm.get_str_setting("Logging", "log_level")
        )  # Update log level based on configuration
        self.wm = window_manager(self.cm, self.lm)
        self.sm = screen_manager(self.cm, self.lm)
        self.dm = data_manager(self.cm, self.lm)
        self.om = object_manager(self.cm, self.lm)
        self.ecs = component_manager(self.cm, self.lm)
        # Common managers
        self.camera = camera(self.cm, self.lm)

        # Todo: Load custom managers

        self.sm.create_screen_handler("game_frame", self.game_frame)
        self.sm.create_screen_handler("pause_frame", self.pause_frame)

        self.lm.log.debug("Application manager initialized.")

        self.managers = {
            "logging": self.lm,
            "configuration": self.cm,
            "window": self.wm,
            "screen": self.sm,
            "level": self.dm,
            "object": self.om,
            "component": self.ecs,
            "render": self.camera,
        }

    def game_frame(self, screen: pygame.Surface, events: None) -> None:
        if not self.dm.current_level:
            self.lm.log.fatal("No level currently loaded.")

        screen.fill(self.dm.current_level.background_color)  # Clear screen.

        # print(events)
        _ = events

        self.ecs.run(
            self.om.convert_tiled_pos_to_game_world(
                self.dm.current_level.get_object_layers()
            ),
            self.managers,
        )

        self.camera.render(self.dm.current_level)  # Render.
        screen.blit(self.camera.surface, (0, 0))  # Blit to screen.

    def pause_frame(self, screen: pygame.Surface, events: None) -> None:
        screen.fill((0, 0, 0))  # Clear screen.

        # print(events)
        _ = events

        screen.blit(self.camera.surface, (0, 0))  # Blit to screen.

    def run(self) -> None:
        """Runs the main game loop."""
        while True:
            self.sm.run_screen()
            self.wm.update(self.sm.screen)  # Update screen.
