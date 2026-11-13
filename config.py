import os

class DevelopmentConfig:
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get(
        "DEV_SERVICE_SECRET_KEY",
        "local-development-only-secret"
    )


class TestingConfig:
    DEBUG = False
    TESTING = True
    SECRET_KEY = os.environ.get(
        "TEST_SERVICE_SECRET_KEY",
        "test-only-secret"
    )


class ProductionConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("PROD_SERVICE_SECRET_KEY")

configurations = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}