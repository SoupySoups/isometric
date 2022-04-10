from src.utils.isometric_calculations import isometric
from src.utils.data_types import Point
import pygame


class render_manager:
    def __init__(self, config_manager, log_manager):
        self.cm = config_manager
        self.lm = log_manager

        self.lm.log.info("Render manager initialized.")

    def render(self, level, surface):
        for tile in level.sorted_tiles:
            tile_image = level.get_image_at(tile)
            if tile_image:
                self.render_item(surface, tile_image, isometric(tile))

    def render_item(
        self, target: pygame.Surface, source: pygame.Surface, position: Point
    ):
        position.check_2d()
        position = position.as_tuple()
        position = (position[0] - source.get_width() // 2, position[1])
        target.blit(source, position)
