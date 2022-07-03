from typing import Dict

gover_keycode: Dict[str, str, str, str] = {
    "encode" : r'h3%2FCptW8MZ4KfUVyw0ghR2KGSmCYLHVAP2rMLPX93EO0rJ%2Bq3wlZeLK4pubReLPflFv8uB9R5EUQ4rqmpZI6SA%3D%3D',
    "decode" : r'h3/CptW8MZ4KfUVyw0ghR2KGSmCYLHVAP2rMLPX93EO0rJ+q3wlZeLK4pubReLPflFv8uB9R5EUQ4rqmpZI6SA=='
}

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