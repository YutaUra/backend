from .common import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS += [
    '.herokuapp.com',
    '127.0.0.1',
]

FRONTEND_POINT = {
    # 'PROTOCOL': 'http',
    # 'DOMAIN': 'localhost:8080',
}

# FRONTEND_URL = '%s://%s' % (FRONTEND_POINT['PROTOCOL'], FRONTEND_POINT['DOMAIN'])

django_heroku.settings(locals())
