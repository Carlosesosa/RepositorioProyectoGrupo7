from .base import *
from .local import *

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'carlossosa$default',
        'USER': 'carlossosa',
        'PASSWORD': 'macarebe',
        'HOST': 'carlossosa.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}