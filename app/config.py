import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "tajna123")  # default ако нема променлива
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
        f"@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
