"""
Django settings for Backend project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'User',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',

    # Django-user-sessions
    'user_sessions',

    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Django-Password-validators
    'django_password_validators',
    'django_password_validators.password_history',

    # Django-zxcvbn-password
    'zxcvbn_password',

    # Django-admin-honeypot
    'admin_honeypot',

    # Django-honeypot
    'honeypot',

    # Custom Google ReCaptcha
    'G_Recaptcha',

    # Django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',

    # Django-user-sessions
    'user_sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # Django-Restrict-Sessions
    'restrictedsessions.middleware.RestrictedSessionsMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Custom User Middleware
    'User.middleware.PreventConcurrentStaffLogin',

    # django-xforwardedfor-middleware
    # https://github.com/allo-/django-xforwardedfor-middleware
    'x_forwarded_for.middleware.XForwardedForMiddleware',

    # Django-honeypot
    # https://pypi.org/project/django-honeypot/
    'honeypot.middleware.HoneypotMiddleware',

    # Custom Google ReCaptcha
    'G_Recaptcha.middleware.RecaptchaMiddleware',
]

ROOT_URLCONF = 'Backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath('templates'),
        ],
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

WSGI_APPLICATION = 'Backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Custom User Model
AUTH_USER_MODEL = 'User.User'


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # Django-allauth
    # `allauth` specific authentication methods, such as login by e-mail
    # https://django-allauth.readthedocs.io/en/latest/installation.html
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },

    # Django-Password-validators
    {
        'NAME': 'django_password_validators.password_history.password_validation.UniquePasswordsValidator',  # noqa
        'OPTIONS': {
            'last_passwords': 10
        }
    },
    {
        'NAME': 'django_password_validators.password_character_requirements.password_validation.PasswordCharacterValidator',  # noqa
        'OPTIONS': {
            'min_length_digit': 1,
            'min_length_alpha': 1,
            'min_length_special': 1,
            'min_length_lower': 1,
            'min_length_upper': 1,
            'special_characters': "~!@#$%^&*()_+{}\":;'[]-"
        }
    },
    {
        'NAME': 'zxcvbn_password.ZXCVBNValidator',
        'OPTIONS': {
            'min_score': 3,
            'user_attributes': ('username', 'email', 'first_name', 'last_name')
        }
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kuala_Lumpur'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = BASE_DIR.joinpath('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.joinpath("static_files"),
]

# Public media files

MEDIA_ROOT = BASE_DIR.joinpath('media')
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django-password-validator settings
# https://github.com/fizista/django-password-validators
DPV_DEFAULT_HISTORY_HASHER = 'django_password_validators.password_history.hashers.HistoryHasher'  # noqa

# GeoIP2 settings
# https://docs.djangoproject.com/en/3.2/ref/contrib/gis/geoip2/
GEOIP_PATH = BASE_DIR.joinpath("GeoIP")

# Django-user-sessions
# https://django-user-sessions.readthedocs.io/en/stable/installation.html
SESSION_ENGINE = 'user_sessions.backends.db'


# Common Django Settings
LOGIN_URL = "account/login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SILENCED_SYSTEM_CHECKS = ['admin.E410']

# Django-honeypot
# https://pypi.org/project/django-honeypot/
HONEYPOT_FIELD_NAME = "secret_key"

# Custom Google Recaptcha
RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_REQUIRED_SCORE = config('RECAPTCHA_REQUIRED_SCORE', cast=float)

# Django-allauth
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True


# Django Email Backend
# https://docs.djangoproject.com/en/3.2/topics/email/#obtaining-an-instance-of-an-email-backend
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR.joinpath('test').joinpath('email')