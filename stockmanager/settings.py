"""
Django settings for stockmanager project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import re

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'test')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost',
                 '127.0.0.1',
                 'radiant-earth-99799.herokuapp.com']

# Application definition

POSTGRES_URL_REGEX = re.compile(
    r'^postgres:\/\/(?P<username>.*?):(?P<password>.*?)@(?P<host>.*?):(?P<port>\d+)/(?P<db>.*?)$')


def get_postgres_settings(url):
    matches = POSTGRES_URL_REGEX.match(url)
    return {
        'name': matches.group('db'),
        'username': matches.group('username'),
        'password': matches.group('password'),
        'host': matches.group('host'),
        'port': matches.group('port')
    }


# USERNAME and PASSWORD
DB_USERNAME = os.getenv('USERNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_PORT = os.getenv('PORT', '3306')

INSTALLED_APPS = [
    'dashboard.apps.DashboardConfig',
    'stockData.apps.StockDataConfig',
    'django_mysql',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'stockmanager.urls'

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

WSGI_APPLICATION = 'stockmanager.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

db_type = os.getenv('DB_TYPE', 'mysql')

DATABASES = {}

if db_type == 'mysql':
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stock',
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': DB_PORT,
    }
elif db_type == 'postgres':
    postgres_settings = get_postgres_settings(os.getenv('DATABASE_URL'))
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': postgres_settings['name'],
        'USER': postgres_settings['username'],
        'PASSWORD': postgres_settings['password'],
        'HOST': postgres_settings['host'],
        'PORT': postgres_settings['port'],
    }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
