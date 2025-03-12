from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mw#9l(-2v+fz(k8amzjl0qm#ukc60ajm(=#zk#827d97a)p=m9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['wine-fermentation.onrender.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wine_app', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wine_backend.urls'

# ✅ **Templates სექცია - შეცვლილი**
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # აქ გამოვასწორე, ახლა ორივე ვერსიას უყურებს:
        'DIRS': [
            BASE_DIR / "templates",  # თუ templates საერთო ფოლდერშია
   #         BASE_DIR / "wine_app" / "templates",  # თუ templates აპლიკაციის შიგნით არის
        ],
        'APP_DIRS': True,  # ეს აუცილებელია, რომ app-ის შიგნით არსებული templates იმუშაოს
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

WSGI_APPLICATION = 'wine_backend.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'ka'  # ქართული ენა
TIME_ZONE = 'Asia/Tbilisi'  # თბილისის დროის ზონა
USE_I18N = True
USE_TZ = True

# ✅ **Static ფაილების პარამეტრები - შეცვლილი**
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # თუ შენი სტატიკური ფაილები პროექტის ფოლდერშია
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # Render-სთვის აუცილებელია

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
