from src.utils.isometric_calculations import isometric
from src.utils.data_types import Point
import src.utils.sorters as sorters
from src.utils.templates.manager_starter import starter
import pytmx
import pygame


class camera(starter):
    def __init__(self, config_manager, log_manager, size=None):
        super().__init__(config_manager, log_manager)

        if size:
            self.size = size
        else:
            self.size = (
                self.cm.get_int("Window", "default_width") / 3,
                self.cm.get_int("Window", "default_height") / 3,
            )

        self.surface = pygame.surface.Surface(size=self.size)

        self.object_queue = []

        self.position = (0, 0)

        self.lm.log.debug("Camera initialized.")

    def component(self, obj, fields):
        if fields.do_render:
            self.object_queue.append(obj)

    def render(self, level):
        sorted_tiles = sorters.sort_tile_distance(
            level.tile_layers,
            insert=self.object_queue,
        )
        self.object_queue = []
        for element in sorted_tiles:
            position = element["position"]

            if isinstance(element["object"], pytmx.TiledObject):
                self.render_item(element["object"].image, isometric(position))
            else:
                tile_image = level.get_image_at(position)
                if tile_image:
                    self.render_item(tile_image, isometric(position))

    def render_item(self, source: pygame.Surface, position: Point):
        position.check_2d()
        position = position.as_tuple()
        position = (
            position[0]
            - source.get_width() // 2
            + self.size[0] // 2
            + self.position[0],
            position[1] + self.size[1] // 2 + self.position[1],
        )
        self.surface.blit(source, position)
