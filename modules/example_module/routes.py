from flask import Blueprint, request, abort

from common import require_secret
from config import config

module = Blueprint(config['module_name'], __name__)

@module.route('/')
@require_secret
def index():
    return 'hello world'