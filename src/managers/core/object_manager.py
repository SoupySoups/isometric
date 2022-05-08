from src.utils.data_types import Point
from src.managers.core.logging_manager import logging_manager


class object_manager:
    def __init__(self):
        self.objects = []

        logging_manager().log.debug("Object manager initialized.")

    def convert_tiled_pos_to_game_world(self, object_groups: list) -> list:
        out = []
        for group in object_groups:
            for object in group:
                object.threeD_point = Point(
                    (object.x - group.offsetx) / 10 - 1,
                    (object.y - group.offsety) / 10,
                    group.offsety * -1 / 14,
                )
                out.append(object)

        return out

    def load_objects(self, object_layers: list) -> list:
        self.objects = self.convert_tiled_pos_to_game_world(object_layers)
