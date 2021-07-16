from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'toy',
        'USER': 'toy',
        'PASSWORD': 'toypassword',
        'HOST': 'db',
        'PORT': 5432,
    }
}
