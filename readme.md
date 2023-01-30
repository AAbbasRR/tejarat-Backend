## Tejarat Backend

env variables:

    # ___Project Setup___ #
    SECRET_KEY = string
    DEBUG = bollean
    # __Redis Setup__ #
    REDIS_HOST = url[localhost]
    REDIS_PORT = int
    REDIS_DB = int
    # ___DataBase___ #
    MYSQL_NAME = string(if USE_MYSQL is true, need to set this variable.)
    MYSQL_USER = string(if USE_MYSQL is true, need to set this variable.)
    MYSQL_PASS = string(if USE_MYSQL is true, need to set this variable.)
    MYSQL_HOST = url[localhost](if USE_MYSQL is true, need to set this variable.)
    MYSQL_PORT = int(if USE_MYSQL is true, need to set this variable.)


How To Run:

    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
