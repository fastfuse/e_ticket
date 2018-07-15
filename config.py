import os


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY',
                                'sO\xc6\xec=\xae\xd0\x0b\xf3\x01\xb0,\x12\x11&/\xf4\x14\xccyv\xfd\xea\x13')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             "postgresql://pt_tickets:admin@localhost/pt_eticket_db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    FLASK_ENV = 'development'


class TestConfig(Config):
    pass


class StagingConfig(Config):
    pass


class ProductionConfig(Config):
    pass
