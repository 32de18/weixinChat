import configparser
import os.path



class ConfigUtils(object):
    CFG_PATH = '../config.ini'

    CONFIG = None
    KEY_APP_ID = 'appid'
    KEY_APP_SECRET = 'appsecret'
    KEY_TOKEN = 'token'

    KEY_SESS_WX = 'wechat'

    @classmethod
    def get_config(cls, cfg_path=CFG_PATH):
        if not os.path.exists(cfg_path):
            return None

        config = configparser.ConfigParser()
        config.read(cfg_path)
        cls.CONFIG = {
            cls.KEY_APP_ID: config.get(cls.KEY_SESS_WX, cls.KEY_APP_ID),
            cls.KEY_APP_SECRET: config.get(cls.KEY_SESS_WX, cls.KEY_APP_SECRET),
            cls.KEY_TOKEN: config.get(cls.KEY_SESS_WX, cls.KEY_TOKEN)
        }
        return cls.CONFIG


if __name__ == '__main__':
    a = ConfigUtils.get_config()
    print(a)
