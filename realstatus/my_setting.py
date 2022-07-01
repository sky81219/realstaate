from typing import Dict

SECRET_KEY: Dict[str, str] = {
    "SECRET_KEY": 'django-insecure-e=mn@h$*c12e4exw%fd^fd-3*z5pp%2za-+o@igqa=bw525$oe'
}

MY_DATABASES: Dict[str, str] = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'realstatus',
        'USER': 'root',
        'PASSWORD': '123456789',
        'HOST': 'sql',
        'PORT': '3306'
    }
}