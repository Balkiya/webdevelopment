"""
Django settings for pythonProject2 project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&m$i9#3&g*@*yc+jh_89mpdnjzl9csv8w54@+uo7r$=9#7!axm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'pythonProject2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'django_extensions'
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

ROOT_URLCONF = 'pythonProject2.urls'

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

WSGI_APPLICATION = 'pythonProject2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static/",
    '/var/www/static/',
]

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
  'layout': 'dot',
  'output': 'D/',
  'options': {},
  'file': None,
  'verbose_names': False,
  'exclude_models': [],
  'exclude_columns': [],
  'include_models': [],
  'include_columns': [],
  'apps': None,
  'inheritance': True,
  'output_format': 'png',
  'filename': None,
  'pygraphviz': True,
  'pydot': True,
  'verbosity': 0,
  'traceback': False,
  'rendered_filename': None,
  'title': None,
  'app': None,
  'output_file': None,
  'label': 'all',
  'rankdir': 'TB',
  'arrow_type': 'normal',
  'exclude_applications': [],
  'django_app': 'django',
  'dot': None,
  'display': False,
  'disable_fields': False,
  'show_fields': False,
  'group_sort': None,
  'ordering': None,
  'colors': {},
  'direction': 'LR',
  'app_label_color': '#ffff99',
  'related_app_label_color': '#ccffff',
  'related_name_color': '#99ccff',
  'style': None,
  'inheritance': True,
  'cluster': False,
  'group': False,
  'group_split': False,
  'group_fontname': None,
  'group_shape': 'record',
  'group_fillcolor': '#ffffcc',
  'group_label': 'GroupName',
  'group_color': '#ff9900',
  'group_style': None,
  'group_fontsize': None,
  'group_margin': None,
  'group_padding': None,
  'group_sort': None,
  'hide_edge_labels': False,
  'layout_options': None,
  'rel_limit': None,
  'node_limit': None,
  'app_ordering': [],
  'node_attributes': {},
  'edge_attributes': {},
  'no_return': False,
}
