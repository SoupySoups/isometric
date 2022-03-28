import pygame


class screen_manager:
    def __init__(self, configuration_manager, logging_manager) -> None:
        self.cm = configuration_manager
        self.lm = logging_manager

        self.current = screen(
            "intro",
            "cutscene",
            x=self.cm.get_int_setting("Window", "default_width") / 3,
            y=self.cm.get_int_setting("Window", "default_height") / 3,
        )

        self.lm.log.info("Screen manager initialized.")

    def set_current(self, screen):
        self.current = screen

    def get_current(self):
        return self.current


class screen:
    def __init__(self, name, screen_type=None, surface=None, x=None, y=None):
        self.name = name
        self.type = screen_type
        if surface is not None:
            self.surface = surface
        else:
            self.surface = pygame.Surface(
                (300 if x is None else x, 300 if y is None else y)
            )
