import os
from datetime import datetime

import redis


def get_db_uri(dbinfo):
    username = dbinfo.get('user') or "root"
    password = dbinfo.get('pwd') or "123456"
    host = dbinfo.get('host') or "39.98.139.205"
    port = dbinfo.get('port') or "3306"
    database = dbinfo.get('dbname') or "flask_app"
    driver = dbinfo.get('driver') or "pymysql"
    dialect = dbinfo.get('dialect') or "mysql"
    return "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(dialect, driver, username, password, host, port, database)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploadfiles')
ADVIRED_ROOT = os.path.join(os.path.join(BASE_DIR, 'static'), 'uploadimg')


class Config(object):
    TESTING = False
    SECRET_KEY = "fVgh5dhGdfh6s8HPrt4rAeeNy"
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = str(datetime.now())+"--"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    LOG_LEVEL = "DEBUG"
    LOG_DIR = os.path.join(BASE_DIR, 'log_files')


class DevelopConfig(Config):
    DEBUG = True
    ENV = 'outline'

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_TIMEOUT = 20
    SQLALCHEMY_POOL_SIZE = 6
    SQLALCHEMY_POOL_RECYCLE = 29
    DATABASE = {
        "user": "root",
        "pwd": "123456",
        "host": "39.98.139.205",
        "port": "3306",
        "dialect": "mysql",
        "driver": "pymysql",
        "dbname": "flask_app",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
    # 用于连接redis的配置
    SESSION_REDIS = redis.Redis(host='39.98.139.205', port='6379', password='123456', db=0)


class ProductConfig(Config):
    DEBUG = False
    ENV = 'online'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_TIMEOUT = 28
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_RECYCLE = 29
    # 用于连接redis的配置
    SESSION_REDIS = redis.Redis(host='39.98.139.205', port='6379', password='123456', db=0)
    DATABASE = {
        "user": "root",
        "pwd": "123456",
        "host": "39.98.139.205",
        "port": "3306",
        "dialect": "mysql",
        "driver": "pymysql",
        "dbname": "flask_app",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


config = {
    "DevelopConfig": DevelopConfig,
    "ProductConfig": ProductConfig,
    "default": DevelopConfig,
}

