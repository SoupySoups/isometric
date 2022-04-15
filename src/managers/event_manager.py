from src.utils.templates.class_starter import starter
import pygame


class event_manager(starter):
    def __init__(self, config_manager, log_manager):
        super().__init__(config_manager, log_manager)

        self.lm.log.info("Event manager initialized.")

    def get_events(self):
        events = pygame.event.get()
        unused_events = []
        for event in events:
            if event.type == pygame.QUIT:  # Quit.
                self.lm.log.info("Quitting.")
                pygame.quit()
                quit()
            else:
                unused_events.append(event)

        return unused_events
