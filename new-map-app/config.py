
import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                '\xfb\x13\xdf\xa1@i\xd6>V\xc0\xbf\x3fp'
                                '\x16#Z\x0b\x81\xeb\x16')
    PROPAGATE_EXCEPTIONS = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
