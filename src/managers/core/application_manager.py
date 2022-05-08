from src.managers.core.window_manager import window_manager
from src.managers.core.configuration_manager import configuration_manager
from src.managers.core.logging_manager import logging_manager
from src.managers.core.screen_manager import screen_manager
from src.managers.core.data_manager import data_manager
from src.managers.core.object_manager import object_manager
from src.managers.core.component_manager import component_manager
from src.managers.core.event_manager import event_manager

from src.elements.camera import camera
from src.elements.movement import movement

import pygame


class application_manager:
    def __init__(self) -> None:

        # Set up managers
        # Core Managers
        self.lm = logging_manager()
        self.cm = configuration_manager(filename="config.ini")
        logging_manager().switch_log_level(
            configuration_manager().get_str("Logging", "log_level")
        )
        self.wm = window_manager()
        self.sm = screen_manager()
        self.dm = data_manager()
        self.om = object_manager()
        self.ecs = component_manager()

        self.managers = {
            "logging": self.lm,
            "configuration": self.cm,
            "window": self.wm,
            "screen": self.sm,
            "level": self.dm,
            "object": self.om,
            "component": self.ecs,
        }

        # Common component managers
        self.create_manager("render", camera())
        self.create_manager("movement", movement())

        # Regester screens
        self.sm.register_screen_handler("game_frame", self.game_frame)
        self.sm.register_screen_handler("pause_frame", self.pause_frame)

        logging_manager().log.info(
            f"Successfully created {len(self.managers.keys())} manager(s)."
        )
        logging_manager().log.debug("Application manager initialized.")

    # @component_manager().register_component("render")
    def load_level(self, level_name: str) -> None:
        self.dm.load_data(level_name)
        self.om.load_objects(self.dm.current_level.get_object_layers())

    def create_manager(self, name: str, manager: any) -> any:
        """Creates a manager."""
        if name in self.managers.keys():
            logging_manager().log.warning(f"Manager {name} already exists.")
            return self.managers[name]
        else:
            logging_manager().log.debug(f"Creating the {name} manager.")
            self.managers[name] = manager

    def get_manager(self, name: str) -> any:
        try:
            return self.managers[name]
        except KeyError:
            logging_manager().log.fatal(f"Manager {name} does not exist.")

    def game_frame(self, screen: pygame.Surface, event_manager: event_manager) -> None:
        if not self.dm.current_level:
            logging_manager().log.fatal("No level currently loaded.")

        screen.fill(self.dm.current_level.background_color)  # Clear screen.

        # print(event_manager.get_events())
        _ = event_manager.get_events()

        self.ecs.run(self.om.objects, self.managers)

        camera_manager = self.get_manager("render")
        camera_manager.render(self.dm.current_level)  # Render.
        screen.blit(camera_manager.surface, (0, 0))  # Blit to screen.

    def pause_frame(self, screen: pygame.Surface, event_manager: event_manager) -> None:
        screen.fill((0, 0, 0))  # Clear screen.

        # print(event_manager.get_events())
        _ = event_manager.get_events()

        screen.blit(self.camera.surface, (0, 0))  # Blit to screen.

    def run(self) -> None:
        """Runs the main game loop."""
        while True:
            self.sm.run_screen()
            self.wm.update(self.sm.screen)  # Update screen.
