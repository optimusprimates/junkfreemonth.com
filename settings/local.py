from __future__ import absolute_import
from .base import *

# Configure these however you like for local development.
# Don't forget to configure a database!

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os
_BASE_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir,
))
_DB_PATH = os.path.join(
    _BASE_PATH,
    os.pardir,
    'jfm-local-dev.db',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': _DB_PATH,                # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'junkfreemonth-dev',
    },
}

FIXTURE_DIRS = (
    os.path.join(_BASE_PATH, 'fixtures'),
)
