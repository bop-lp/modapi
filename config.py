import secrets

MODULES_DIR = 'modules'

# Server configuration
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8888

# Module configuration
MOD_CONFIG_ROUTES_MOD_KEY = 'routes_mod'
MOD_CONFIG_ROUTES_MOD_DEFAULT = 'routes'

MOD_CONFIG_MOD_VAR_KEY = 'module_var'
MOD_CONFIG_MOD_VAR_DEFAULT = 'module'

MOD_CONFIG_URL_PREFIX_KEY = 'url_prefix'

MOD_CONFIG_MOD_NAME_KEY = 'module_name'

# Injection
MOD_CONFIG_INJECT_KEY = 'inject'


### Maps module config keys to values to be injected
INJECTABLE = {
    'secret_key': secrets.SECRET_KEY,
    'secret_key_value': secrets.SECRET_KEY_VALUE
}