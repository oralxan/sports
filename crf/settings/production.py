from .base import *

DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'sportapi$default',
        'USER': 'sportapi',
        'PASSWORD': 'B_LbH@NMtmxce95',
        'HOST': 'sportapi.mysql.pythonanywhere-services.com'

    }
}


