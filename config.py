import os
from dotenv import load_dotenv
from pathlib import Path


base_dir = Path(__file__).resolve().parent
env_file = base_dir / '.env'
load_dotenv(env_file)


class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY')





