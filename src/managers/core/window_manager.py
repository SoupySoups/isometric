from src.utils.quiet_print import QuietPrint
from src.managers.core.logging_manager import logging_manager
from src.managers.core.configuration_manager import configuration_manager

with QuietPrint():
    import pygame


class window_manager:
    def __init__(self):
        self.window_name = configuration_manager().get_str("Window", "window_name")
        self.window_icon = pygame.image.load(
            configuration_manager().get_str("Window", "window_icon")
        )

        pygame_init_stats = pygame.init()
        if pygame_init_stats[1] != 0:
            logging_manager().log.fatal(
                f"Pygame failed to initialize {pygame_init_stats[1]} module(s)."
            )
        logging_manager().log.debug(
            f"Successfully initialized {pygame_init_stats[0]} pygame modules, {pygame_init_stats[1]} failed."
        )  # Initialize pygame modules

        self.fps = 0
        self.max_fps = configuration_manager().get_int(
            "Window", "maximum_fps"
        )  # Get maximum FPS from configuration

        # Create windows and surfaces
        self.size = (
            configuration_manager().get_int("Window", "default_width"),
            configuration_manager().get_int("Window", "default_height"),
        )  # Get default window size from configuration

        logging_manager().log.info(
            f'Creating window "{self.window_name}" with size: {self.size[0]}x{self.size[1]}'
        )
        pygame.display.set_caption(self.window_name)  # Set window name
        pygame.display.set_icon(self.window_icon)  # Set window icon

        # Set window properties based on configuration
        self.window_flags = 0
        self.window_flags_list = []
        if configuration_manager().get_bool("Window", "resizeable"):
            self.window_flags_list.append(pygame.RESIZABLE | pygame.SCALED)
        if configuration_manager().get_bool("Window", "borderless"):
            self.window_flags_list.append(pygame.NOFRAME)

        self.calculateFlags()  # Calculate window flags

        self.screen = pygame.display.set_mode(
            self.size, self.window_flags, vsync=1
        )  # Create window

        self.clock = pygame.time.Clock()  # Create clock

        self.delta_time = 0

    def enable_fullscreen(self):
        if pygame.FULLSCREEN not in self.window_flags_list:
            self.window_flags_list.append(pygame.FULLSCREEN)
            self.calculateFlags()

            self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN, vsync=1)
        return self.screen

    def disable_fullscreen(self):
        if pygame.FULLSCREEN in self.window_flags_list:
            self.window_flags_list.pop(pygame.FULLSCREEN)
            self.calculateFlags()

            self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN, vsync=1)
        return self.screen

    def calculateFlags(self):
        for flag in self.window_flags_list:
            self.window_flags |= flag

        return self.window_flags

    def change_name(self, name):
        self.window_name = name
        pygame.display.set_caption(self.window_name)  # Set window name

    def resize(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(self.size, self.window_flags, vsync=1)
        return self.screen

    def update(self, content: pygame.Surface):
        self.screen.blit(pygame.transform.scale(content, self.size), (0, 0))

        self.fps = int(self.clock.get_fps())

        pygame.display.update()
        self.delta_time = self.clock.tick(self.max_fps) / 1000

    def get_delta_time(self):
        return self.delta_time
