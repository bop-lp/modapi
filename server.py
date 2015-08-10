import argparse
from importlib import import_module
import os

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException, HTTP_STATUS_CODES

import notify
import config

def get_modules():
    dirs = []
    for f in os.listdir(config.MODULES_DIR):
        path = os.path.join(config.MODULES_DIR, f)
        if os.path.isdir(path):
            dirs.append(path.replace('/', '.'))
    return dirs

def inject(module, mod_conf):
    if config.MOD_CONFIG_INJECT_KEY in mod_conf:
        inject_config = mod_conf[config.MOD_CONFIG_INJECT_KEY]
        for k, v in config.INJECTABLE.iteritems():
            single_inject(k, v, module, inject_config)

def single_inject(key, value, module, inject_config):
    if key in inject_config:
        x = inject_config[key]
        setattr(module, x, value)

def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    notifier = notify.boxcar.BoxcarNotifier()
    notifier.quick_send('Error: %s' % e)
    return jsonify(error=str(e)), code

class ModApi:
    def __init__(self):
        self.app = Flask(__name__)
        self.load_modules()

        for code in HTTP_STATUS_CODES:
            self.app.register_error_handler(code, handle_error)

        @self.app.route('/favicon.ico')
        def favicon():
            return send_from_directory(app.root_path, 'favicon.ico',
                    mimetype='image/vnd.microsoft.icon')

        @self.app.route('/')
        def index():
            notifier = notify.boxcar.BoxcarNotifier()
            notifier.quick_send('Modapi running.')
            return jsonify({'status': 'ok'})

    def load_modules(self):
        for p in get_modules():
            c = import_module(p + '.config')
            mc = c.config
            k = config.MOD_CONFIG_ROUTES_MOD_KEY
            rmod = mc[k] if k in mc else config.MOD_CONFIG_ROUTES_MOD_DEFAULT
            m = import_module(p + '.' + rmod)
            k = config.MOD_CONFIG_MOD_VAR_KEY
            mvar = mc[k] if k in mc else config.MOD_CONFIG_MOD_VAR_DEFAULT
            mod = getattr(m, mvar)
            inject(m, mc)
            k = config.MOD_CONFIG_URL_PREFIX_KEY
            pre = mc[k] if k in mc else None
            self.app.register_blueprint(mod, url_prefix=pre)

api = ModApi()
app = api.app

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="enable debug", action="store_true")
    args = parser.parse_args()

    api = ModApi()
    api.app.run(debug=args.debug, host=config.SERVER_HOST, port=config.SERVER_PORT)