from src.utils.isometric_calculations import isometric
from src.managers.object_manager import add_world_point_to_object_layer_objects
from src.utils.data_types import Point
import src.utils.sorters as sorters
from src.managers.manager import manager
import pytmx
import pygame


class render_manager(manager):
    def __init__(self, config_manager, log_manager):
        super().__init__(config_manager, log_manager)

        self.lm.log.info("Render manager initialized.")

    def render(self, level, surface):
        sorted_tiles = sorters.sort_tile_distance(
            level.tile_layers,
            insert=add_world_point_to_object_layer_objects(level.get_object_layers()),
        )
        for element in sorted_tiles:
            position = element["position"]

            if isinstance(element["object"], pytmx.TiledObject):
                self.render_item(surface, element["object"].image, isometric(position))
            else:
                tile_image = level.get_image_at(position)
                if tile_image:
                    self.render_item(surface, tile_image, isometric(position))

    def render_item(
        self, target: pygame.Surface, source: pygame.Surface, position: Point
    ):
        position.check_2d()
        position = position.as_tuple()
        position = (position[0] - source.get_width() // 2, position[1])
        target.blit(source, position)
