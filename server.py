import imp
import os

from flask import Flask

import config

app = Flask(__name__)

def get_modules():
    return [x[0] for x in os.walk(config.MODULES_DIR)][1:]

if __name__ == "__main__":
    app.run(debug=True)