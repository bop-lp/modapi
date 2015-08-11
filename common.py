from functools import wraps
from flask import abort, request

import secrets

MODAPI_SECRET_KEY = secrets.SECRET_KEY_VALUE
MODAPI_BASE_URL = secrets.BASE_URL

def secret_correct(val):
    return secrets.SECRET_KEY and secrets.SECRET_KEY_VALUE and \
        val == secrets.SECRET_KEY_VALUE

def require_secret(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if secret_correct(request.args.get(secrets.SECRET_KEY)):
            return f(*args, **kwargs)
        else:
            abort(401)
    return decorated