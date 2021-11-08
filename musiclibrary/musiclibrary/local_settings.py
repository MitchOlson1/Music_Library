from pathlib import Path

SECRET_KEY = 'django-insecure-*!k6ptcrld#qet%k4n2$a%hu0@i6jmsd@#y7xgmy+rups6w2n5'

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    'default':{
        'ENGINE': 'mysql.connector.django',
        'NAME': 'Music_library_database',
        'USER': 'root',
        'PASSWORD': 'Bucksinsix6',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}