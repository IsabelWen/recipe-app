from .base import *
import environ
import dj_database_url
import os

# add new config for production
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(str(BASE_DIR / ".env"))

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = ["127.0.0.1", "recipe-app-hedk.onrender.com"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default=env.str('DATABASE_URL'),
        conn_max_age=500
    )
}


MEDIA_URL = '/media/'
MEDIA_ROOT= BASE_DIR / 'media'

# Static files (CSS, JavaScript, Images)
#STATIC_URL = '/static/'
#STATICFILES_DIRS=[
#    BASE_DIR / "static",
#]

#STATIC_ROOT = BASE_DIR / 'staticfiles'