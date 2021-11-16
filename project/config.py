class Config(object):
    DEBUG = False
    TESTING = False
    DB = 'data/database.db'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev'


class TestingConfig(Config):
    TESTING = True
