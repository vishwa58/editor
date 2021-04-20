"""
For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uz34lc79a3bhzy@r$la%fg@q^tcc4j!3hmz-7a$tw5wsbb(y4f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'accounts',
    'editor',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'django.contrib.humanize',
    'sanitizer',
    'notifications',
    'analytical',
    'reversion',
    'registration',
    'django_tables2',
    'taggit',
    'el_pagination',
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

ROOT_URLCONF = 'numbas.urls'

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
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "editor.context_processors.global_settings",
                "editor.context_processors.site_root",
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = 'static/'

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join('static'), )

SITE_TITLE = 'Numbas'
SITE_ID = 1

MATHJAX_URL = 'https://cdn.jsdelivr.net/npm/mathjax@2'

MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

GLOBAL_SETTINGS = {
    'NUMBAS_PATH': '../numbas_runtime',
    'PREVIEW_PATH': 'static/previews/',
    'PREVIEW_URL': '/static/previews/',    # a URL which serves files from PREVIEW_PATH
    'HELP_URL': 'https://docs.numbas.org.uk/en/latest/',        # the URL of the Numbas webdocs
    'PYTHON_EXEC': 'python3',
    'NUMBAS_THEMES': [('Standard', 'default'), ('Printable worksheet', 'worksheet'), ('School', 'school')],
    'NUMBAS_LOCALES': [
        ('English', 'en-GB'),
        ('Bahasa Indonesia (52% complete)', 'in-ID'),
        ('Deutsch', 'de-DE'),
        ('Español (94% complete)', 'es-ES'),
        ('Français (75% complete)', 'fr-FR'),
        ('Italiano (64% complete)', 'it-IT'),
        ('Nederlands (74% complete)', 'nl-NL'),
        ('Norsk bokmål (68% complete)', 'nb-NO'),
        ('Polski (22% complete)', 'pl-PL'),
        ('Português brasileiro (74% complete)', 'pt-BR'),
        ('Shqip (51% complete)', 'sq-AL'),
        ('Svenska (74% complete)', 'sv-SE'),
        ('Tiếng Việt (90% complete)', 'vi-VN'),
        ('Türkçe (16% complete)', 'tr-TR'),
        ('עִבְרִית (24% complete)', 'he-IL'),
        ('中文 (90% complete)', 'zh-CN'),
        ('日本語 (45% complete)', 'ja-JP'),
        ('ﺎﻠﻋﺮﺒﻳﺓ (97% complete)', 'ar-SA'),
    ],
    #Uncomment the line below and provide a path to a minification tool to minify javascript files
    #'MINIFIER_PATH': 'uglifyjs',
}

EVERYTHING_VISIBLE = False  # Set this to True to allow every user to see all content, regardless of access settings

ALLOW_REGISTRATION = True
ACCOUNT_ACTIVATION_DAYS = 10

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
CAN_LOGOUT = True
CAN_CHANGE_PASSWORD = True
LOGOUT_REDIRECT_URL = '/'

sys.path.append(os.path.join(GLOBAL_SETTINGS['NUMBAS_PATH'],'bin'))

SANITIZER_ALLOWED_TAGS = ['a', 'p', 'img','br','strong','em','div','code','i','b', 'ul', 'ol', 'li', 'table','thead','tbody','td','th','tr']
SANITIZER_ALLOWED_ATTRIBUTES = ['href','title']

DEFAULT_FROM_EMAIL = 'vishwan56@icloud.com'

# Must users be able to view all the questions in an exam in order to view the exam?
EXAM_ACCESS_REQUIRES_QUESTION_ACCESS = False
