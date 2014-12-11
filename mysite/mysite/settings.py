"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a9-w+&x*+2*3d$7i@0cu3s3)aj!h%vdr7+9$^@71#2ve-5l(%v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
  #= {
    #'default': {
       # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
       # 'NAME':'test',
        #'USER': 'postgres',                      # Not used with sqlite3.
        #'PASSWORD': '123',                  # Not used with sqlite3.
        #'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
#'PORT': '8000',      
    #}
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
DEFAULT_FROM_EMAIL = 'mhtkmrarticles@gmail.com'
SERVER_EMAIL = 'mhtkmrarticles@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mhtkmrarticles@gmail.com'
EMAIL_HOST_PASSWORD = '17291729@'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT=''
STATIC_URL = '/static/'
STATICFILES_DIRS = ('assets',
    os.path.join(os.path.dirname(BASE_DIR), "static","CSS"),
    
)
if DEBUG:
   
    MEDIA_URL=''
    MEDIA_ROOT= 'C:/Downloads/risk/ecommerce1/static/'
#templATE LOCATION
TEMPLATE_DIRS =(
    os.path.join(os.path.dirname(BASE_DIR), "templates"),
  os.path.join(os.path.dirname(BASE_DIR),"mysite","books", "templates"),
  )