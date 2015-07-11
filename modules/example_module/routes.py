from flask import Blueprint, jsonify, abort
from config import config

module = Blueprint(config['module_name'], __name__)

counter = 0

@module.route('/')
def index():
    try:
        counter += 1
        return jsonify({'counter': counter})
    except:
        abort(404)