from importlib import import_module
import os

from flask import Flask

import config

def get_modules():
    return [x[0].replace('/', '.') for x in os.walk(config.MODULES_DIR)][1:]

class ModApi:
    def __init__(self):
        self.app = Flask(__name__)
        self.load_modules()

    def load_modules(self):
        for p in get_modules():
            c = import_module(p + '.config')
            k = config.MOD_CONFIG_ROUTES_MOD_KEY
            rmod = c.config[k] if k in c.config else config.MOD_CONFIG_ROUTES_MOD_DEFAULT
            m = import_module(p + '.' + rmod)
            k = config.MOD_CONFIG_MOD_VAR_KEY
            mvar = c.config[k] if k in c.config else config.MOD_CONFIG_MOD_VAR_DEFAULT
            mod = getattr(m, mvar)
            k = config.MOD_CONFIG_URL_PREFIX_KEY
            pre = c.config[k] if k in c.config else None
            self.app.register_blueprint(mod, url_prefix=pre)

if __name__ == "__main__":
    api = ModApi()
    api.app.run(debug=True)