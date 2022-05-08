from typing import Any
import pygame
from src.managers.core.logging_manager import logging_manager
import src.managers.core.event_manager as event_manager
from src.managers.core.configuration_manager import configuration_manager


class screen_manager:
    def __init__(self) -> None:
        self.em = event_manager.event_manager()

        self.screen = self.surface = pygame.Surface(
            (
                configuration_manager().get_int("Window", "default_width") / 3,
                configuration_manager().get_int("Window", "default_height") / 3,
            )
        )

        self.callbacks = {}

        self.current_state = ""

        logging_manager().log.debug("Screen manager initialized.")

    def register_screen_handler(self, name, func: str) -> callable:
        """Registers a screen handler"""
        if len(self.callbacks.keys()) == 0:
            self.current_state = name
        self.callbacks[name] = func
        return func

    def set_screen(self, name: str) -> None:
        if name in self.callbacks.keys():
            self.current_state = name
        else:
            logging_manager().log.fatal(
                f"Screen attempted to switch to a non-existent screen: {name}"
            )

    def run_screen(self) -> Any:
        return self.callbacks[self.current_state](self.screen, event_manager=self.em)
