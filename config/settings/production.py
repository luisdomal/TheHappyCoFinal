"""Production Settings"""

import os
import dj_database_url
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

#Google Cloud Settings.
from google.oauth2 import service_account

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'happyco'
#STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_PROJECT_ID = 'jovial-light-323900'
GS_CREDENTIALS = os.getenv("GCS_SECRET_KEY")

#Apartado de seguridad

SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True