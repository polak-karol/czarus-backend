import os
from datetime import timedelta

DEBUG = True
SQLALCHEMY_DATABASE_URI = "postgresql://czarus:czarus@localhost:5432/czarus"
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_SECRET_KEY = os.getenv("APP_SECRET_KEY")
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)
