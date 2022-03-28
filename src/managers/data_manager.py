import pytmx
from src.utils.data_types import Point

class data_manager:
    def __init__(self, config_manager, log_manager):
        self.cm = config_manager
        self.lm = log_manager

        self.current_level = None

        self.lm.log.info("Data manager initialized.")

    def load_data(self, filename):
        self.lm.log.info(f"Loading level: {filename}")
        self.current_level = level(filename, self.cm, self.lm)

    def reload_data(self):
        self.load_data(self.current_level.filename, self.cm, self.lm)

class level:
    def __init__(self, filename, config_manager, log_manager):
        self.cm = config_manager
        self.lm = log_manager

        # Load TMX file
        self.filename = filename
        self.raw_tmxdata = pytmx.load_pygame(self.filename)

        # Retive map properties
        self.background_color = self.raw_tmxdata.background_color

        self.map_width = self.raw_tmxdata.width
        self.map_height = self.raw_tmxdata.height
        self.map_tilewidth = self.raw_tmxdata.tilewidth
        self.map_tileheight = self.raw_tmxdata.tileheight

        self.version = self.raw_tmxdata.version

        self.lm.log.info(f"Successfully loaded level: {self.filename} z{self.version}")

    def get_image_at(self, point: Point):
        point.check_3d()
        return self.raw_tmxdata.get_tile_image(point.x, point.y, point.z)