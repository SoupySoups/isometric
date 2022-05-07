from src.utils.templates.manager_starter import starter
from src.utils.common_routines import quit
import pygame


class event_manager(starter):
    def __init__(self, config_manager, log_manager):
        super().__init__(config_manager, log_manager)

        self.lm.log.debug("Event manager initialized.")

    def get_events(self):
        events = pygame.event.get()
        unused_events = []
        for event in events:
            if event.type == pygame.QUIT:  # Quit.
                quit(self.lm)
            else:
                unused_events.append(event)

        return unused_events
