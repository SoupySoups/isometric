from typing import Any
import pygame
from src.utils.templates.class_starter import starter


class screen_manager(starter):
    def __init__(self, config_manager, log_manager) -> None:
        super().__init__(config_manager, log_manager)

        self.screen = self.surface = pygame.Surface(
            (
                self.cm.get_int_setting("Window", "default_width") / 3,
                self.cm.get_int_setting("Window", "default_height") / 3,
            )
        )

        self.callbacks = {}

        self.current_state = ""

        self.lm.log.info("Screen manager initialized.")

    def create_callback(self, name: str, callback: callable) -> None:
        if len(self.callbacks.keys()) == 0:
            self.current_state = name
        self.callbacks[name] = callback

    def run_callback(self) -> Any:
        return self.callbacks[self.current_state](self.screen)
