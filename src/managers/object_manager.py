from src.utils.data_types import Point
from src.utils.templates.manager_starter import starter


class object_manager(starter):
    def __init__(self, config_manager, log_manager):
        super().__init__(config_manager, log_manager)

        self.lm.log.debug("Object manager initialized.")

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
