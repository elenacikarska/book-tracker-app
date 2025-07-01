# import os
#
# class Config:
#     SECRET_KEY = os.getenv("SECRET_KEY", "tajna123")  # default ако нема променлива
#     SQLALCHEMY_DATABASE_URI = (
#         f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
#         f"@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

import os

class Config:
    FLASK_ENV = os.environ.get("FLASK_ENV", "production")
    SECRET_KEY = os.environ.get("SECRET_KEY", "tajna123")

    DB_USER = os.environ.get("DATABASE_USER")
    DB_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DB_HOST = os.environ.get("DATABASE_HOST")
    DB_PORT = os.environ.get("DATABASE_PORT", 5432)
    DB_NAME = os.environ.get("DATABASE_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        if all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME])
        else None
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
