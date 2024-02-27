from .base import *

DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'footsports$default',
        'USER': 'footsports',
        'PASSWORD': 'B_LbH@NMtmxce95',
        'HOST': 'sportapi.mysql.pythonanywhere-services.com'

    }
}


