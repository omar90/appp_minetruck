import dj_database_url
from mysite.settings import *
DEBUG = False

TEMPLATE_DEBUG=False

DATABASES['default']= dj_database_url.config()

MIDDLEWARE+=[  'whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['truck-mine.herokuapp.com']
