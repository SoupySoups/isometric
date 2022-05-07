from typing import Any
import pygame
from src.utils.templates.manager_starter import starter
import src.managers.event_manager as event_manager


class screen_manager(starter):
    def __init__(self, config_manager, log_manager) -> None:
        super().__init__(config_manager, log_manager)

        self.em = event_manager.event_manager(self.cm, self.lm)

        self.screen = self.surface = pygame.Surface(
            (
                self.cm.get_int_setting("Window", "default_width") / 3,
                self.cm.get_int_setting("Window", "default_height") / 3,
            )
        )

        self.callbacks = {}

        self.current_state = ""

        self.lm.log.debug("Screen manager initialized.")

    def create_screen_handler(self, name: str, callback: callable) -> None:
        if len(self.callbacks.keys()) == 0:
            self.current_state = name
        self.callbacks[name] = callback

    def set_screen(self, name: str) -> None:
        if name in self.callbacks.keys():
            self.current_state = name
        else:
            self.lm.log.fatal(
                f"Screen attempted to switch to a non-existent screen: {name}"
            )

    def run_screen(self) -> Any:
        return self.callbacks[self.current_state](
            self.screen, events=self.em.get_events()
        )
