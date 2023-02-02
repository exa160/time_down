import os

from units.config import ConfigAttrDict, base_path


class Config(ConfigAttrDict):
    def __init__(self, _config_path):
        self.debug = False
        self.pos_x = 0
        self.pos_y = 0
        self.font_type = '楷体'
        self.font_size = 8
        self.foreground = 'black'
        self.background = 'red'
        self.alpha = 1
        super().__init__(_config_path)
        self.save()


config_path = os.path.join(base_path, 'data.cfg')
config = Config(config_path)
