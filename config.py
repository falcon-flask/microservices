import os
from dotenv import load_dotenv
import dotenv

dotenv_file_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.isfile(dotenv_file_path):
    load_dotenv(dotenv_file_path)


class Config:
    SQLACHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = 'development'
    SQLACHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/dog"

class ProductionConfig(Config):
    pass