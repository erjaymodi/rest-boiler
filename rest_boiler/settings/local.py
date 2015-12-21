__author__ = 'Jay Modi'

from common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST' : 'localhost',
        'USER' : 'postgres',
        'PASSWORD' : 'root',
        'NAME': 'rest_boiler',
        'PORT' : 5432,
    }
}