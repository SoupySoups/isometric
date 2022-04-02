from src.utils.data_types import Point
from src.utils.isometric_calculations import isometric


class render_manager:
    def __init__(self, config_manager, log_manager):
        self.cm = config_manager
        self.lm = log_manager

        self.lm.log.info("Render manager initialized.")

    def render(self, level, surface):
        for z, layer in enumerate(level.tile_layers):
            if layer in level.tile_layers:
                for y in range(layer.height):
                    for x in range(layer.width):
                        tile = level.get_image_at(Point(x, y, z))
                        if tile:
                            surface.blit(tile, isometric(x, y, z))