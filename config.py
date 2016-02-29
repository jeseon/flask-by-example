class Config(object):
    DEBUG = False
	TESTING = False
	DEVELOPMENT = False
	CSRF_ENABLED = True
	SECRET_KEY = 'secret'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEBUG = True
	DEVELOPMENT = True


class DevelopmentConfig(Config):
    DEBUG = True
	DEVELOPMENT = True


class TestingConfig(Config):
    TESTING = True

