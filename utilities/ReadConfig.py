import configparser
import os

class ReadConfig:
    @staticmethod
    def get_config(section, key):
        """Read string value from config.ini"""
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Configurations', 'config.ini'))
        config = configparser.ConfigParser()
        config.read(config_path)
        return config.get(section, key)

    @staticmethod
    def get_bool(section, key):
        """Read boolean value from config.ini"""
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Configurations', 'config.ini'))
        config = configparser.ConfigParser()
        config.read(config_path)
        return config.getboolean(section, key)
