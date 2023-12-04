from .base import *


DEBUG = True

# SECRET_KEY = 'django-insecure-mes(hm(67b$q(yav%fz6a-s(=8r1eyq-u$68-q2h4)krx(%#cj'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Security srttings
SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False


# These are used in django-hosts resolvers(reverse and reverse_lazy)
MAIN_PORT = 8000

MAIN_SCHEME = 'http'

PARENT_HOST = 'localhost'
