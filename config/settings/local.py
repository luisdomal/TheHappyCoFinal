"""Development Settings"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rv1e!&p418ssmu2&1l02+r@!co6c7opcqdqvqttp_hftw7hs&0'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#Google Cloud Settings.
from google.oauth2 import service_account

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'happyco'
#STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_PROJECT_ID = 'jovial-light-323900'
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    "jovial-light-323900-29d597db8c7e.json"
)

INSTALLED_APPS.append("django_extensions")
