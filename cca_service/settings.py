"""
Django settings for cca_service project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# Read in .env file
ENV = environ.Env()
environ.Env.read_env()

# Application configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# https://docs.djangoproject.com/en/3.0/ref/settings/
# https://docs.djangoproject.com/en/3.0/ref/middleware/#django.middleware.security.SecurityMiddleware
DEBUG = ENV('DEBUG', cast=bool, default=False)

if DEBUG:
    ALLOWED_HOSTS = [] if not ENV('ALLOWED_HOSTS', default=[]) else ENV('ALLOWED_HOSTS').split(',')
    CSRF_COOKIE_SECURE = False
    SECRET_KEY = ENV('SECRET_KEY', default="FakeDevKey")
    SESSION_COOKIE_SECURE = False
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
    SECURE_HSTS_SECONDS = 0
    SECURE_REFERRER_POLICY = 'strict-origin'
    SECURE_SSL_REDIRECT = False
else:
    ALLOWED_HOSTS = ['.cca.gg'] if not ENV('ALLOWED_HOSTS', default=[]) else ENV('ALLOWED_HOSTS').split(',')
    CSRF_COOKIE_SECURE = True
    SECRET_KEY = ENV('SECRET_KEY', default="FakeProdKey")
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_SECONDS = ENV('SECURE_HSTS_SECONDS', cast=int, default=60)
    SECURE_REFERRER_POLICY = 'strict-origin'
    SECURE_SSL_REDIRECT = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'cca_service.cca_registry',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cca_service.urls'

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

WSGI_APPLICATION = 'cca_service.wsgi.application'

# Rest Framework settings
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': ENV.db('DATABASE_URL', default='sqlite://:memory:')
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = './static/'
STATIC_URL = '/static/'


# WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
