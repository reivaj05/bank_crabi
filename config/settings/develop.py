from .base import *

DEBUG = True

# INSTALLED_APPS += (
#    'django_extensions',
# )


DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get('DATABASE_NAME', 'crabi'),
    'USER': os.environ.get('DATABASE_USER', 'postgres'),
    'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'postgres'),
    'HOST': os.environ.get('DATABASE_HOST', 'localhost')
}
