# import values in .env and put in os environ
#

from os import getenv, path
from dotenv import load_dotenv

APP_ROOT = path.join(path.dirname(__file__), '.')   # refers to application_top
dotenv_path = path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)



class Config:
    PINECONE_API_KEY = getenv('PINECONE_API_KEY')
    PINECONE_INDEX_NAME = getenv('PINECONE_INDEX_NAME')
    PINECONE_INDEX_DIMENSION = int(getenv('PINECONE_INDEX_DIMENSION'))
    PINECONE_INDEX_METRIC = getenv('PINECONE_INDEX_METRIC')
    PINECONE_INDEX_SPEC_CLOUD = getenv('PINECONE_INDEX_SPEC_CLOUD')
    PINECONE_INDEX_SPEC_REGION = getenv('PINECONE_INDEX_SPEC_REGION')
