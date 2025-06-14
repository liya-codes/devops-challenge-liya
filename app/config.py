import os
from dotenv import load_dotenv

#load local .env
load_dotenv()

#all the env are loaded 
AWS_REGION = os.getenv('AWS_REGION')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
CODE_NAME = os.getenv('CODE_NAME')
DOCKERHUB_URL = os.getenv('DOCKERHUB_URL')
GITHUB_PROJECT = os.getenv('GITHUB_PROJECT')
