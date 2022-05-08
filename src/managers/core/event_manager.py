from src.utils.templates.manager_starter import starter
from src.utils.common_routines import quit
import pygame


class event_manager(starter):
    def __init__(self, config_manager, log_manager):
        super().__init__(config_manager, log_manager)

        self.callbacks = {}

        self.lm.log.debug("Event manager initialized.")

    def get_events(self):
        events = pygame.event.get()
        unused_events = []
        for event in events:
            if event.type == pygame.QUIT:  # Quit.
                quit(self.lm)
            else:
                for handler in self.callbacks.keys():
                    if event.type == handler:
                        self.callbacks[handler](event)
                unused_events.append(event)

        return unused_events

    def register_event_handler(self, event_type, event_handler):
        self.callbacks[event_type] = event_handler
