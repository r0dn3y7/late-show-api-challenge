import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "postgresql://your_user:your_password@localhost:5432/late_show_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "supersecret")
