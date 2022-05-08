from src.managers.core.logging_manager import logging_manager
from src.utils.common_routines import quit
import pygame


class event_manager:
    def __init__(self):
        self.callbacks = {}

        logging_manager().log.debug("Event manager initialized.")

    def get_events(self):
        events = pygame.event.get()
        unused_events = []
        for event in events:
            if event.type == pygame.QUIT:  # Quit.
                quit()
            else:
                unused_events.append(event)

        return unused_events

    def register_event_handler(self, event_type, event_handler):
        self.callbacks[event_type] = event_handler
