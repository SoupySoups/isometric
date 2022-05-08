from src.managers.core.window_manager import window_manager
from src.managers.core.configuration_manager import configuration_manager
from src.managers.core.logging_manager import logging_manager
from src.managers.core.screen_manager import screen_manager
from src.managers.core.data_manager import data_manager
from src.managers.core.object_manager import object_manager
from src.managers.core.component_manager import component_manager
from src.managers.core.event_manager import event_manager

from src.elements.camera import camera as camera

import pygame


class application_manager:
    def __init__(self) -> None:

        # Set up managers
        # Core Managers
        self.lm = logging_manager("INFO")  # Set up logging manager
        self.cm = configuration_manager("config.ini", self.lm)
        self.lm.switch_log_level(self.cm.get_str("Logging", "log_level"))
        self.wm = window_manager(self.cm, self.lm)
        self.sm = screen_manager(self.cm, self.lm)
        self.dm = data_manager(self.cm, self.lm)
        self.om = object_manager(self.cm, self.lm)
        self.ecs = component_manager(self.cm, self.lm)

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
        self.create_singleton_manager("render", camera(self.cm, self.lm))

        # Regester screens
        self.sm.register_screen_handler("game_frame", self.game_frame)
        self.sm.register_screen_handler("pause_frame", self.pause_frame)

        self.lm.log.info(f"Successfully created {len(self.managers.keys())}")
        self.lm.log.debug("Application manager initialized.")

    def create_singleton_manager(self, name: str, manager: any) -> any:
        """Creates a manager."""
        if name in self.managers.keys():
            self.lm.log.warning(f"Manager {name} already exists.")
            return self.managers[name]
        else:
            self.lm.log.debug(f"Creating the {name} manager.")
            self.managers[name] = manager

    def get_manager(self, name: str) -> any:
        try:
            return self.managers[name]
        except KeyError:
            self.lm.log.fatal(f"Manager {name} does not exist.")

    def game_frame(self, screen: pygame.Surface, event_manager: event_manager) -> None:
        if not self.dm.current_level:
            self.lm.log.fatal("No level currently loaded.")

        screen.fill(self.dm.current_level.background_color)  # Clear screen.

        # print(event_manager.get_events())
        _ = event_manager

        self.ecs.run(
            self.om.convert_tiled_pos_to_game_world(
                self.dm.current_level.get_object_layers()
            ),
            self.managers,
        )

        camera_manager = self.get_manager("render")
        camera_manager.render(self.dm.current_level)  # Render.
        screen.blit(camera_manager.surface, (0, 0))  # Blit to screen.

    def pause_frame(self, screen: pygame.Surface, event_manager: event_manager) -> None:
        screen.fill((0, 0, 0))  # Clear screen.

        # print(event_manager.get_events())
        _ = event_manager

        screen.blit(self.camera.surface, (0, 0))  # Blit to screen.

    def run(self) -> None:
        """Runs the main game loop."""
        while True:
            self.sm.run_screen()
            self.wm.update(self.sm.screen)  # Update screen.


def main() -> None:
    # Set up the application manager
    am = application_manager.application_manager()

    am.lm.log.warning("Application manager running as main, use main.py.")

    am.dm.load_data("levels/test_level.tmx")
    am.run()


if __name__ == "__main__":
    main()
