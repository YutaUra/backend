from .common import *
import django_heroku
import dj_database_url

DEBUG = True

ALLOWED_HOSTS += [
    '.herokuapp.com',
    '127.0.0.1',
]

FRONTEND_POINT = {
    'PROTOCOL': 'https',
    'DOMAIN': 'tutorportal-web.herokuapp.com/',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': '',
        'HOST': 'host',
        'PORT': '',
    }
}

FRONTEND_URL = '%s://%s' % (FRONTEND_POINT['PROTOCOL'], FRONTEND_POINT['DOMAIN'])
db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)

django_heroku.settings(locals())
