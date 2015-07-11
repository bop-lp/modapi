from flask import Blueprint
from config import config

module = Blueprint(config['module_name'], __name__)

@module.route('/')
def index():
    return 'hello world'