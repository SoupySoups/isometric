from src.utils.isometric_calculations import isometric


class render_manager:
    def __init__(self, config_manager, log_manager):
        self.cm = config_manager
        self.lm = log_manager

        self.lm.log.info("Render manager initialized.")

    def render(self, level, surface):
        for tile in level.sorted_tiles:
            tile_image = level.get_image_at(tile)
            if tile_image:
                surface.blit(tile_image, isometric(tile).as_tuple())
