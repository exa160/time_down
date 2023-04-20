import inspect
import json
import os.path
import traceback

from units.logger import *

if getattr(sys, 'frozen', False):  # 打包静态资源问题
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")
    # base_path = os.path.dirname(os.path.realpath(sys.argv[0]))

cur_path = os.path.dirname(os.path.realpath(sys.argv[0]))


class AttrDict:

    def __init__(self):
        self.__attr_dict = {}

    def __getattr__(self, *args, **kwargs):
        if '__' in args[0]:
            return super().__getattr__(*args, **kwargs)
        return self.__attr_dict.__getitem__(*args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        if '__' in args[0]:
            return super().__setattr__(*args, **kwargs)
        f_locals = inspect.currentframe().f_back.f_locals
        if f_locals.get('self', None) is not self and args[0] not in self.__attr_dict:
            raise AttributeError("don't change constant data")
        self.__attr_dict.__setitem__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        self.__attr_dict.__setitem__(*args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        f_locals = inspect.currentframe().f_back.f_locals
        if f_locals and f_locals.get('self', None) is not self:
            raise AttributeError("don't change constant data")
        self.__attr_dict.__getitem__(*args, **kwargs)

    def __delattr__(self, key):
        del self[key]

    def _pop(self, *args, **kwargs):
        return self.__attr_dict.pop(*args, **kwargs)

    def _get_config(self):
        return self.__attr_dict


class ConfigAttrDict(AttrDict):
    def __init__(self, config_file=r'config.json', _config=None):
        super().__init__()
        _config_path = os.path.join(cur_path, config_file)
        self.config_path = _config_path
        if os.path.exists(_config_path):
            local_config = self.read_config()
            if local_config.get('debug', False):
                _config = {}
            else:
                _config = local_config
        elif _config is None:
            _config = {}
        self.dict_init(_config)
        self.config_init(config_file, _config)

    def dict_init(self, dict_data):
        for key, values in dict_data.items():
            self[key] = values

    # @staticmethod
    def config_init(self, config_file, _config=None):
        """
        初始化配置文件
        :param config_file:配置文件名
        :param _config:dict
        :return:
        """
        if _config is None:
            _config = {}
        with open(config_file, 'w') as c:
            json.dump(_config, c, indent=4, ensure_ascii=False)
        self.config_path = config_file

    def read_config(self):
        """
        获取配置信息
        :return: _config: AttrDict
        """
        with open(self.config_path, 'r') as c:
            try:
                _config = json.load(c)
            except json.decoder.JSONDecodeError:
                _config = {}
        return _config

    def save(self, config_file=None, _config=None):
        """
        保存配置文件
        :param config_file:
        :param _config:
        :return:
        """
        if config_file is None:
            config_file = self._pop('config_path')
        if _config is None:
            _config = self._get_config()
        try:
            self.config_init(config_file, _config)
        except Exception as e:
            print(traceback.format_exc())


if __name__ == '__main__':
    config_path = os.path.join(base_path, 'data.cfg')
    config = ConfigAttrDict(config_path)
    print(config.read_config())
