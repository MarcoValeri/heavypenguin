from .base import *

DEBUG = False

ALLOWED_HOSTS = ['devmarcovaleri.eu.pythonanywhere.com']

ROOT_URLCONF = 'heavypenguin.urls'

SECRET_KEY = 'u%k+9u+(scbg!0rdq!f0ejdcyh+ap#7(j3e-b13fepp+2(n_8n'

try:
    from .local import *
except ImportError:
    pass
