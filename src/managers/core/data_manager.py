import pytmx
from src.utils.data_types import Point
import src.utils.sorters as sorters
from src.managers.core.logging_manager import logging_manager


class data_manager:
    def __init__(self):
        self.current_level = None

        logging_manager().log.debug("Data manager initialized.")

    def load_data(self, filename):
        logging_manager().log.info(f"Loading level: {filename}")
        self.current_level = level(filename)

    def reload_data(self):
        self.load_data(self.current_level.filename)


class level:
    def __init__(self, filename: str):
        # Load TMX file
        self.filename = filename
        self.raw_tmxdata = pytmx.load_pygame(
            self.filename, custom_property_filename="levels/propertytypes.json"
        )

        # Retive map properties
        self.background_color = self.raw_tmxdata.background_color
        if self.background_color is None:
            self.background_color = (0, 0, 0)

        self.map_width = self.raw_tmxdata.width
        self.map_height = self.raw_tmxdata.height
        self.map_tilewidth = self.raw_tmxdata.tilewidth
        self.map_tileheight = self.raw_tmxdata.tileheight

        self.version = self.raw_tmxdata.version

        self.layers = self.raw_tmxdata.layers
        self.tile_layers, _ = sorters.sort_by_instance(
            self.layers, pytmx.TiledTileLayer
        )

        logging_manager().log.info(
            f"Successfully loaded level: {self.filename}, Tiled version: {self.version}"
        )

    def get_image_at(self, point: Point):
        point.check_3d()
        return self.raw_tmxdata.get_tile_image(point.x, point.y, point.z)

    def get_object_layers(self) -> list:

        return list(self.raw_tmxdata.objectgroups)
