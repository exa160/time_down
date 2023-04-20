import copy
import os
import tempfile
import appdirs

from units.config import ConfigAttrDict


class Config(ConfigAttrDict):
    def __init__(self, _config_path):
        super().__init__(_config_path)
        new_config = copy.deepcopy(self._get_config())
        self.debug = False
        self.pos_x = 0
        self.pos_y = 0
        self.font_type = '楷体'
        self.font_size = 8
        self.foreground = 'black'
        self.background = 'red'
        self.alpha = 1
        self.qt_pos_x = 0
        self.qt_pos_y = 0
        self.qt_show_alpha = 0.9
        self.qt_hide_alpha = 0.05

        self.qt_text = dict(LABEL_1='距摸鱼结束',
                            LABEL_2='还剩',
                            LABEL_3='分',
                            LABEL_NUM=' {text} ',
                            LABEL_4='THE TOUCHING FISH FINISH\nIN {text} {unit}')
        self.dict_init(new_config)
        self.save()


data_path = appdirs.user_data_dir()
os.makedirs(os.path.join(data_path, 'Timer'), exist_ok=True)
config_path = os.path.join(data_path, 'Timer', 'data.cfg')
config = Config(config_path)

if __name__ == '__main__':
    print(tempfile.gettempdir())
    print(appdirs.user_data_dir())
    print(config.read_config())
