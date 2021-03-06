# -*- coding: utf-8 -*-
# Copyright 2012-2013 Rooter Analysis S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
This is the default settings for an OpenMOOC Askbot project. This is not meant
to be used by the user.
"""

import os
import logging
import sys
import askbot
import site

#this line is added so that we can import pre-packaged askbot dependencies
ASKBOT_ROOT = os.path.abspath(os.path.dirname(askbot.__file__))
ROOT = os.path.dirname(askbot.__file__)

site.addsitedir(os.path.join(ASKBOT_ROOT, 'deps'))

DEBUG = False #set to True to enable debugging
TEMPLATE_DEBUG = False# keep false when debugging jinja2 templates
INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'askbot',                      # Or path to database file if using sqlite3.
        'USER': 'askbot',                      # Not used with sqlite3.
        'PASSWORD': 'askbot',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#outgoing mail server settings
SERVER_EMAIL = ''
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = ''
EMAIL_HOST=''
EMAIL_PORT=''
EMAIL_USE_TLS=False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#incoming mail settings
#after filling out these settings - please
#go to the site's live settings and enable the feature
#"Email settings" -> "allow asking by email"
#
#   WARNING: command post_emailed_questions DELETES all
#            emails from the mailbox each time
#            do not use your personal mail box here!!!
#
IMAP_HOST = ''
IMAP_HOST_USER = ''
IMAP_HOST_PASSWORD = ''
IMAP_PORT = ''
IMAP_USE_TLS = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True
USE_TZ = False

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', u'English'),
    ('es', u'Español'),
)

# Absolute path to the directory that holds uploaded media
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'askbot', 'upfiles')
MEDIA_URL = '/upfiles/'
STATIC_URL = '/m/'#this must be different from MEDIA_URL

PROJECT_ROOT = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# Make up some unique string, and don't share it with anybody.
SECRET_KEY = 'prf@a0)7jdbjm@*#$$%*ex1#3=ltvl$ojp%y+2g3t#p7sp!w3b'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'askbot.skins.loaders.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
    #'django.template.loaders.eggs.load_template_source',
)


MIDDLEWARE_CLASSES = (
    #'django.middleware.gzip.GZipMiddleware',
    # On 2013/07/01 this feature wasn't ready and gives errors. The creator encourages to comment it.
    #'askbot.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.middleware.sqlprint.SqlPrintingMiddleware',

    'askbotopenmooc.app.middlewares.Saml2SSORedirect',

    #below is askbot stuff for this tuple
    'askbot.middleware.anon_user.ConnectToSessionMessagesMiddleware',
    'askbot.middleware.forum_mode.ForumModeMiddleware',
    'askbotopenmooc.app.middlewares.ForumModeMiddleware',
    'askbot.middleware.cancel.CancelActionMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'askbot.middleware.view_log.ViewLogMiddleware',
    'askbot.middleware.spaceless.SpacelessMiddleware',
)


ROOT_URLCONF = 'askbotopenmooc.urls'


#UPLOAD SETTINGS
FILE_UPLOAD_TEMP_DIR = "/tmp"

FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)
ASKBOT_ALLOWED_UPLOAD_FILE_TYPES = (
    '.jpg',
    '.jpeg',
    '.gif',
    '.png',
    '.tiff',
    '.pdf',
    '.doc',
    '.docx',
    '.docm',
    '.xls',
    '.xlsx',
    '.xlsm',
    '.odt',
    '.ppt',
    '.pptx',
    '.pptm',
)

ASKBOT_MAX_UPLOAD_FILE_SIZE = 2 * 1024 * 1024 #result in bytes
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

#TEMPLATE_DIRS = (,) #template have no effect in askbot, use the variable below
try:
    import askbotopenmooc
    # This variable is meant to be overwritten in the instance_settings file if
    # necessary, but by default we load the default extra themes.
    ASKBOT_EXTRA_SKINS_DIR = askbotopenmooc.__path__[0] + '/themes/'
except ImportError:
    if DEBUG:
        sys.stderr.write("\033[91m\n#################################\n#\n# askbotopenmooc not found!!\n#\n#################################\n\033[0m")
#take a look here http://askbot.org/en/question/207/

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'askbot.context.application_settings',
    'askbotopenmooc.context.openmooc_settings',
    'django.core.context_processors.i18n',
    'askbot.user_messages.context_processors.user_messages',#must be before auth
    'django.contrib.auth.context_processors.auth', #this is required for the admin app
    'django.core.context_processors.csrf', #necessary for csrf protection
)


INSTALLED_APPS = (
    'longerusername',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    #all of these are needed for the askbot
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    #'debug_toolbar',
    #Optional, to enable haystack search
    #'haystack',
    'askbot',
    #'askbot.deps.django_authopenid',
    #'askbot.importers.stackexchange', #se loader
    'south',
    'askbot.deps.livesettings',
    'keyedcache',
    'robots',
    'django_countries',
    #'djcelery',
    'djkombu',
    'followit',
    'tinymce',
    'group_messaging', # manage.py runtime testing needs it
    #'avatar',#experimental use git clone git://github.com/ericflo/django-avatar.git$
    'djangosaml2',
    'askbotopenmooc.app',
)

#setup memcached for production use!
#see http://docs.djangoproject.com/en/1.1/topics/cache/ for details
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
#needed for django-keyedcache
CACHE_TIMEOUT = 6000
#sets a special timeout for livesettings if you want to make them different
LIVESETTINGS_CACHE_TIMEOUT = CACHE_TIMEOUT
CACHE_PREFIX = 'askbot' #make this unique
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#If you use memcache you may want to uncomment the following line to enable memcached based sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

AUTHENTICATION_BACKENDS = (
    'askbotopenmooc.app.backends.Saml2RestrictedForumAccess',
    'django.contrib.auth.backends.ModelBackend',
    #'askbot.deps.django_authopenid.backends.AuthBackend',
)

#logging settings
# LOG_FILENAME = 'askbot.log'
# logging.basicConfig(
#     filename=os.path.join(os.path.dirname(__file__), 'log', LOG_FILENAME),
#     level=logging.CRITICAL,
#     format='%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
# )

###########################
#
#   this will allow running your forum with url like http://site.com/forum
#
#   ASKBOT_URL = 'forum/'
#
ASKBOT_URL = '' #no leading slash, default = '' empty string
ASKBOT_TRANSLATE_URL = True #translate specific URLs
_ = lambda v:v #fake translation function for the login url
LOGIN_URL = '/%s%s%s' % (ASKBOT_URL,_('account/'),_('signin/'))
LOGIN_REDIRECT_URL = ASKBOT_URL #adjust, if needed
#note - it is important that upload dir url is NOT translated!!!
#also, this url must not have the leading slash
ALLOW_UNICODE_SLUGS = False
ASKBOT_USE_STACKEXCHANGE_URLS = False #mimic url scheme of stackexchange

#Celery Settings
BROKER_TRANSPORT = "djkombu.transport.DatabaseTransport"
CELERY_ALWAYS_EAGER = True

import djcelery
djcelery.setup_loader()
DOMAIN_NAME = ''

CSRF_COOKIE_NAME = '_csrf'
#https://docs.djangoproject.com/en/1.3/ref/contrib/csrf/
#CSRF_COOKIE_DOMAIN = DOMAIN_NAME

STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# Runtime testing forces this to be removed
# STATICFILES_DIRS = (
#     os.path.join(ASKBOT_ROOT, 'skins'),
#     os.path.join(PROJECT_ROOT, "askbot-openmooc-themes"),
#     ('default/media', os.path.join(ASKBOT_ROOT, 'media')),
# )

RECAPTCHA_USE_SSL = True

#HAYSTACK_SETTINGS
ENABLE_HAYSTACK_SEARCH = False
HAYSTACK_SITECONF = 'askbot.search.haystack'
#more information
#http://django-haystack.readthedocs.org/en/v1.2.7/settings.html
HAYSTACK_SEARCH_ENGINE = 'simple'

#delayed notifications, time in seconds, 15 mins by default
NOTIFICATION_DELAY_TIME = 60 * 15

GROUP_MESSAGING = {
    'BASE_URL_GETTER_FUNCTION': 'askbot.models.user_get_profile_url',
    'BASE_URL_PARAMS': {'section': 'messages', 'sort': 'inbox'}
}

ASKBOT_INTERNAL_IPS=('127.0.0.1',)
ASKBOT_USE_LOCAL_FONTS=True

  ######################################################
 ########################################################
##########################################################
#                                                        #
#      THIS PART IS SPECIFIC FOR OPENMOOC-ASKBOT         #
#                                                        #
# It rewrites the configuration settings to have a fully #
# automated askbot farm. Some of the askbot settings are #
# located here beacuse of the rewritten settings         #
##########################################################

# Language settings
# the default value is 'django_language' but changing this
# to 'language' makes it easier to integrate with the IdP
LANGUAGE_COOKIE_NAME = 'language'
LANGUAGE_COOKIE_DOMAIN = '.example.com'

MOOCNG_URL = 'https://moocng.org/'


FOOTER_LINKS = (
    ('%slegal' % MOOCNG_URL, {
        'en': u'Legal',
        'es': u'Condiciones legales',
    }),
    ('%scopyright' % MOOCNG_URL, {
        'en': u'Moocng Copyright 2012-2013',
        'es': u'Moocng Copyright 2012-2013',
    }),
    ('%stos' % MOOCNG_URL, {
        'en': u'Terms of Use',
        'es': u'Términos de uso',
    }),
    ('%scontact' % MOOCNG_URL, {
        'en': u'Contact',
        'es': u'Contacto',
    }),
)

# Deactivate all login providers, groups, recaptcha and change some minor
# settings.
LIVESETTINGS_OPTIONS = {
    1: {
        u'DB': True,
        u'SETTINGS': {
            u'FORUM_DATA_RULES': {
                u'ALLOW_POSTING_BEFORE_LOGGING_IN': u'False',
                u'WIKI_ON': u'False'
            },
            u'GENERAL_SKIN_SETTINGS': {
                u'ASKBOT_DEFAULT_SKIN': u'mooc',
                u'SHOW_LOGO': u'True',
                u'SITE_LOGO_URL': u'images/logo.png'
            },
            u'GROUP_SETTINGS': {
                u'GROUPS_ENABLED': u'False'
            },
            u'LOGIN_PROVIDERS': {
                u'SIGNIN_AOL_ENABLED': u'False',
                u'SIGNIN_BLOGGER_ENABLED': u'False',
                u'SIGNIN_CLAIMID_ENABLED': u'False',
                u'SIGNIN_FACEBOOK_ENABLED': u'False',
                u'SIGNIN_FLICKR_ENABLED': u'False',
                u'SIGNIN_GOOGLE_ENABLED': u'False',
                u'SIGNIN_IDENTI.CA_ENABLED': u'False',
                u'SIGNIN_LINKEDIN_ENABLED': u'False',
                u'SIGNIN_LIVEJOURNAL_ENABLED': u'False',
                u'SIGNIN_LOCAL_ENABLED': u'False',
                u'SIGNIN_OPENID_ENABLED': u'False',
                u'SIGNIN_TECHNORATI_ENABLED': u'False',
                u'SIGNIN_TWITTER_ENABLED': u'False',
                u'SIGNIN_VERISIGN_ENABLED': u'False',
                u'SIGNIN_VIDOOP_ENABLED': u'False',
                u'SIGNIN_WORDPRESS_ENABLED': u'False',
                u'SIGNIN_YAHOO_ENABLED': u'False'
            },
            u'MARKUP': {
                u'AUTO_LINK_PATTERNS': u'#course/(\\w+)/(\\d+)',
                u'AUTO_LINK_URLS': u'http://example.com/\\1/\\2',
                u'ENABLE_AUTO_LINKING': u'True',
                u'MARKUP_CODE_FRIENDLY': u'True'
            },
            u'EXTERNAL_KEYS': {
                u'USE_RECAPTCHA': u'False'
            },
            u'QA_SITE_SETTINGS': {
                u'APP_TITLE': u'Askbot OpenMooc',
                u'APP_KEYWORDS': u'Mooc,OpenMooc,forum,community',
                u'APP_SHORT_NAME': u'Askbot OpenMooc'
            },
            u'SOCIAL_SHARING': {
                'ENABLE_SHARING_LINKEDIN': u'False',
                'ENABLE_SHARING_IDENTICA': u'False',
            },
            u'ACCESS_CONTROL': {
                'ASKBOT_CLOSED_FORUM_MODE': u'False'
            },
        }
    }
}

# SAML2 specific settings to allow federation in openmooc-askbot and integration
# withe the IdP

LOGIN_URL = '/saml2/login/'
LOGIN_REDIRECT_URL = '/questions/' #aadjust, if needed
LOGOUT_URL = '/saml2/logout/'
LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SAML_CREATE_UNKNOWN_USER = True

SAML_DJANGO_USER_MAIN_ATTRIBUTE = 'email'

SAML_ATTRIBUTE_MAPPING = {
    'mail': ('email', ),
    'cn': ('first_name', ),
    'sn': ('last_name', ),
}

SAML_AUTHORIZATION_ATTRIBUTE = None
SAML_AUTHORIZATION_EXPECTED_VALUE = None

EXTERNAL_KEYS = None

SAML2_COOKIE = 'saml2_logged'

try:
    from local_settings import *
except ImportError:
    if DEBUG:
        sys.stderr.write("\033[91m\n#################################\n#\n# local_settings.py not found!!\n#\n#################################\n\033[0m")

else:
    if EXTERNAL_KEYS:
        LIVESETTINGS_OPTIONS[1][u'SETTINGS'][u'EXTERNAL_KEYS'] = EXTERNAL_KEYS
    DATABASES['default']['USER'] = ASKBOT_DATABASE_USER
    DATABASES['default']['PASSWORD'] = ASKBOT_DATABASE_PASSWORD
    DATABASES['default']['ENGINE'] = ASKBOT_DATABASE_ENGINE

try:
    sys.path.insert(0, os.getcwd())
    from instance_settings import *
    import instance_settings

    # All the askbot settings located here are beacuse of the local_settings rewriting the STATIC_ROOT setting.
    TINYMCE_COMPRESSOR = True
    TINYMCE_SPELLCHECKER = False
    TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, 'default/media/js/tinymce/')
    TINYMCE_URL = STATIC_URL + 'default/media/js/tinymce/'
    TINYMCE_DEFAULT_CONFIG = {
        'plugins': 'askbot_imageuploader,askbot_attachment',
        'convert_urls': False,
        'theme': 'advanced',
        'content_css': STATIC_URL + 'default/media/style/tinymce/content.css',
        'force_br_newlines': True,
        'force_p_newlines': False,
        'forced_root_block': '',
        'mode' : 'textareas',
        'oninit': "function(){ tinyMCE.activeEditor.setContent(askbot['data']['editorContent'] || ''); }",
        'plugins': 'askbot_imageuploader,askbot_attachment',
        'theme_advanced_toolbar_location' : 'top',
        'theme_advanced_toolbar_align': 'left',
        'theme_advanced_buttons1': 'bold,italic,underline,|,bullist,numlist,|,undo,redo,|,link,unlink,askbot_imageuploader,askbot_attachment',
        'theme_advanced_buttons2': '',
        'theme_advanced_buttons3' : '',
        'theme_advanced_path': False,
        'theme_advanced_resizing': True,
        'theme_advanced_resize_horizontal': False,
        'theme_advanced_statusbar_location': 'bottom',
        'width': '723',
        'height': '250'
    }

    STATICFILES_DIRS = (
        ASKBOT_EXTRA_SKINS_DIR,
        # os.path.join(ASKBOT_ROOT, 'skins'),
        # os.path.join(PROJECT_ROOT, "askbot-openmooc-themes"),
        ('default/media', os.path.join(ASKBOT_ROOT, 'media')),
    )

except ImportError:
    if DEBUG:
        sys.stderr.write("\033[91m\n#################################\n#\n# instance_settings.py not found!!\n#\n#################################\n\033[0m")
else:
    DATABASES = {
        'default': {
            'NAME': DATABASE_NAME,
            'HOST': DATABASE_HOST,
            'ENGINE': ASKBOT_DATABASE_ENGINE,
            'USER': ASKBOT_DATABASE_USER,
            'PASSWORD': ASKBOT_DATABASE_PASSWORD,
        },
    }

    #CACHE_PREFIX = DATABASE_NAME #make this unique
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'KEY_PREFIX': DATABASE_NAME,
        }
    }

    MEDIA_ROOT = os.path.join(INSTANCE_DIR, 'upfiles')
    MEDIA_URL = '/%s/upfiles/' % INSTANCE_NAME

    # ASKBOT_URL = ('%s/') % COURSE_NAME
    ASKBOT_URL = ''
    FULL_ASKBOT_URL = '%s%s/' % (BASE_URL, INSTANCE_NAME)

    CSRF_COOKIE_NAME = '%s_csrf' % INSTANCE_NAME
    SESSION_COOKIE_NAME = '%s_sessionid' % INSTANCE_NAME

    LIVESETTINGS_OPTIONS[1][u'SETTINGS'][u'MARKUP'] = {
        u'AUTO_LINK_URLS': u'http://%s/\\1/\\2' % (FULL_ASKBOT_URL),
    }

    LIVESETTINGS_OPTIONS[1][u'SETTINGS'][u'QA_SITE_SETTINGS'] = {
        u'APP_TITLE': INSTANCE_NAME,
        u'APP_KEYWORDS': u'Mooc,OpenMooc,forum,community',
        u'APP_SHORT_NAME': INSTANCE_NAME,
        u'ENABLE_GREETING_FOR_ANON_USER': False,
        u'FEEDBACK_SITE_URL': u"AAAAAAA",
        u'APP_URL': '%s' % FULL_ASKBOT_URL,
    }

    if 'BOOTSTRAP_MODE' in dir():
        LIVESETTINGS_OPTIONS[1][u'SETTINGS']['SITE_MODES'] = {
            'ACTIVATE_BOOTSTRAP_MODE': "%s" % BOOTSTRAP_MODE,
        }

    LOGIN_URL = '%s%s' % (FULL_ASKBOT_URL, 'saml2/login/')
    LOGIN_REDIRECT_URL = FULL_ASKBOT_URL  # adjust, if needed
    LOGOUT_URL = "%s%s" % (FULL_ASKBOT_URL, 'saml2/logout/')
    LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL

    SAML_AUTHORIZATION_EXPECTED_VALUE = INSTANCE_NAME

    SAML_CONFIG['entityid'] = '%s%s' % (FULL_ASKBOT_URL, "saml2/metadata/")
    SAML_CONFIG['service']['sp']['name'] = '%s - Askbot - OpenMOOC SP' % INSTANCE_NAME
    SAML_CONFIG['service']['sp']['endpoints']['assertion_consumer_service'] = [(
        "%s%s" % (FULL_ASKBOT_URL, 'saml2/acs/'),
        saml2.BINDING_HTTP_POST)]

    SAML_CONFIG['service']['sp']['endpoints']['single_logout_service'] = [(
                    "%s%s" % (FULL_ASKBOT_URL, 'saml2/ls/'),
                    saml2.BINDING_HTTP_REDIRECT)]
