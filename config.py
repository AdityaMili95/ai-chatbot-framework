import os


class Config(object):
    DEBUG = False
    DB_NAME = "am-wallte-mongodb"
    DB_HOST = "mongodb://haha:123@ds163826.mlab.com:63826/am-wallte-mongodb"
    DB_USERNAME = ""
    DB_PASSWORD = ""
    # Web Server details
    WEB_SERVER_PORT = 8001

    # Intent Classifier model detials
    MODELS_DIR = "model_files"
    INTENT_MODEL_NAME = "intent.model"
    DEFAULT_FALLBACK_INTENT_NAME = "fallback"
    DEFAULT_WELCOME_INTENT_NAME = "init_conversation"


class Development(Config):
    DEBUG = True


class Production(Config):
    # MongoDB Database Details
    DB_HOST = "mongodb://haha:123@ds163826.mlab.com:63826/am-wallte-mongodb"
    DB_USERNAME = ""
    DB_PASSWORD = ""

    # Web Server details
    WEB_SERVER_PORT = 8001
