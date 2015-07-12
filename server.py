from importlib import import_module
import os

from flask import Flask

import config

def get_modules():
    dirs = []
    for f in os.listdir(config.MODULES_DIR):
        path = os.path.join(config.MODULES_DIR, f)
        if os.path.isdir(path):
            dirs.append(path.replace('/', '.'))
    return dirs

def inject(module, mod_conf):
    inject_secret(module, mod_conf)

def inject_secret(module, mod_conf):
    if config.MOD_CONFIG_INJECT_KEY in mod_conf:
        inject_config = mod_conf[config.MOD_CONFIG_INJECT_KEY]
        if config.MOD_CONFIG_INJECT_SECRET_KEY in inject_config and config.MOD_CONFIG_INJECT_SECRET_KEY_VALUE in inject_config:
            x = inject_config[config.MOD_CONFIG_INJECT_SECRET_KEY]
            setattr(module, x, config.SECRET_KEY)
            x = inject_config[config.MOD_CONFIG_INJECT_SECRET_KEY_VALUE]
            setattr(module, x, config.SECRET_KEY_VALUE)

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
            inject(m, c.config)
            k = config.MOD_CONFIG_URL_PREFIX_KEY
            pre = c.config[k] if k in c.config else None
            self.app.register_blueprint(mod, url_prefix=pre)

if __name__ == "__main__":
    api = ModApi()
    api.app.run(host=config.SERVER_HOST, port=config.SERVER_PORT)