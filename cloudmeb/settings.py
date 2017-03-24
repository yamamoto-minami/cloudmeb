# Settings for cloudmeb project.

import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_ID = 1

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#1m_luvq5#c46s8wz49$lmx-44do6n=%*n@n^k==*s^%z*(9)+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

TASTYPIE_DEFAULT_FORMATS = ['json']

API_LIMIT_PER_PAGE = 0

# Application definition

HTML_MINIFY = True

INSTALLED_APPS = (
    # 'bootstrap3',
    # 'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'cloudmeb.websites',
    'cloudmeb.users',
    'cloudmeb.pages',
    'cloudmeb.seos',
    'cloudmeb.categories',
    'cloudmeb.benefits',
    'cloudmeb.inputs',
    'cloudmeb.values',
    'cloudmeb.prices',
    'cloudmeb.solutions',
    'cloudmeb.products',
    'cloudmeb.partners',
    'cloudmeb.services',
    'cloudmeb.partner_services',
    'cloudmeb.testimonials',
    'cloudmeb.experiences',
    'cloudmeb.whytabs',
    'cloudmeb.why_cloudmeb_txts',
    'cloudmeb.solution_page_txts',
    'cloudmeb.become_partner_txts',
    'cloudmeb.pricing_txts',
    'cloudmeb.shared_txts',
    'tastypie',
)

DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'cloudmeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'cloudmeb', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.i18n',
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

WSGI_APPLICATION = 'cloudmeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'cloudmeb.db'),
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': '',
        # 'USER': '',
        # 'PASSWORD': '',
        # 'HOST': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

LANGUAGES = (
    ('fr', _('French')),
    ('en', _('English')),
)

LANGUAGE_COOKIE_NAME = 'i18n'

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'),)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_URL = '/static/'

