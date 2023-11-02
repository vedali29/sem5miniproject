"""
Django settings for childVacc project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import firebase_admin
from firebase_admin import credentials
import os
import pyrebase


BASE_DIR = Path(__file__).resolve().parent.parent
# Use the path to the JSON file containing your Firebase Admin SDK credentials
# cred = credentials.Certificate('credential.json')
config = {
  "type": "service_account",
  "apiKey": "AIzaSyAbCSVC8yDxih3j7aIf__dFKQ64YlCwz3A",
  "authDomain": "childvacc-614df.firebaseapp.com",
  "project_id": "childvacc-614df",
  "storageBucket": "childvacc-614df.appspot.com",
  "private_key_id": "ac34efb84d799ebee1452dbf130f022297f57354",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDWRWHpvuTEK0K2\nB4EHKMma1EXs4C7sDzasoxQ835QXeqzMt/mGUBkTJ1Gju7vYU/T7dIBftn4BybNk\nTQ5QOUfNKuUjckBtTfUIJ+Ne0ugnln0x7VvmymoEfqJtFpgYhO3o2kq3CXwuhIkV\nBv47QjrxUVXl9APnSsrYRl2aTUgi2fBO9fSVTNC3wjiX0i2RpoX1clcdRrGAtVeI\ngShYmRr6sQer/87DbJsHnzxbV7hwBbaoMcPxg/xrQwVjHxQdNhoSArQWyeaKDo7/\n1nzRfb2h2/m++wi/sdKl7d4O8crXLQEAsE0s9KUR5TKkk4Kg2q9wdgf+ojAcB5QR\nW9H4OhkZAgMBAAECggEAEXjW4xiNzvE4H1+9RbgtuFJW4VnmeZlD/A/QNqaEjOWT\n8Z2O20TsxoMORSupxZoS/+4gCa332G16E1O1NxV0pWY6CQnn9wHEWUXnZHQOOiwr\nSUbxl4Ap5PPuiras8FLmk3Y5YXOEjMaB5xUK5goghEz9lCKxrsqKf9g9CbgDidPV\nWkXnNw1c7xIvG71JmfUVYPn6GDfV0jvhIaOtQ10z+Fi6NIAA4jZGq1IUsGJ26J/R\nrw9t2AYsko1jL3hM94pe8bpUV481sB7qdnkLNYPvedxDCkIiJIXaA8mwg+pvjhij\n7MazY0+SCXQvMzin7pBFgRQBrkcLFEOR7XLAWFYNgQKBgQD7Qbh5fqKrkgyWVeud\nn2LOccoY9eOL0C2Gh/rp+w3Ar6QYMX+Mw3Jx6/0rKwfr4YYJGpyvx8czwMVdsVmp\nuC/JHqt0Jw77MLZRs5OuGyAIdRFctXFJtB0KPbnRIwKbiwqRyyOwCMVf0OKL/Lgt\ns9Jp0lB3gCOJjk/NQ7TPTo/29wKBgQDaUOqhjsfYq+ItFmJ5Xyp0ipYVbQsY8ZlI\nsJTb65sY4Kt4zxb+cdZ6RucMeMiNLNXLf7uM6GUvuJOblNyUjtQvabLvXe5njHo5\nNRlWcjEDdc9cV3hKOS+t4qkdIdQxMCYrgCdurHlclQYRmzeKO5XfnOy2tUMvNaON\nRP9Cg80cbwKBgQCHovPmSpGgU0iOQ7XdMnTRg6YZEWyURn69GF1AwLGs6mSIVvhH\nUh9PFplmG2W8VdPYyE/7qLqF2rPxH1OLBo5tYSwnmQpCWgqiUnIP1D7XsfL8fEq7\nAguHQskz+FVpCIddKy+J0UJTtl0GOxhmO6QEUm/0Au2sTXIRGlLacsvPAwKBgFOK\nHx6POl3o9/V02V3EUsShu2ibf2GeIZ+1ImE9OO4+Gp9x70SSXxYPR554IZYUEAN8\n71GuI/os0R75yaZ3OS6jbbs24GFzWdnGPdncfHDshdq6BeexFlOdpkTliwL/f7up\noG0zRoVs6ROXp5sXzfPxYotPtVO9XMZUHrFfKf+1AoGALeUXPQe/8wXDiVqkQCw1\nr9rzjhjddAVeYBBqrFeiOhDDrVCYn6cuK/RQih/HC4SYDOsYoP70cK7qRBDE9Ey0\nNiISH2VjcC94ABRmziW6gM8ZOxzbdWzYLZjS2XXO3SSdvi0QD1fh8qluAcFAoRtF\nEoOkKm9UkuWV+jmrc32ViNE=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-c2ygy@childvacc-614df.iam.gserviceaccount.com",
  "client_id": "112796066415265309626",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-c2ygy%40childvacc-614df.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com",
  "databaseURL": "https://childvacc-614df-default-rtdb.firebaseio.com/"
}
# cred = credentials.Certificate(os.path.join(BASE_DIR, 'credential.json'))
# firebase_admin.initialize_app(cred,options={'databaseURL': 'https://childvacc-614df-default-rtdb.firebaseio.com/'})

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

# Build paths inside the project like this: BASE_DIR / 'subdir'.



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--it3oh@@w%)q1=sfp%f=pu*h2&)*b=s^30(c!o-f@doqxi4y4c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vacc',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'childVacc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'childVacc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
