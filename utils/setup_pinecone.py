from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
import pandas as pd
from uuid import uuid4
import numpy as np
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from config import Config

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def generate_embeddings(texts):
    return model.encode(texts)

pc = Pinecone(api_key=Config.PINECONE_API_KEY)

index_name = Config.PINECONE_INDEX_NAME

if index_name in pc.list_indexes():
    pc.delete_index(index_name)
pc.create_index(name=Config.PINECONE_INDEX_NAME, dimension=Config.PINECONE_INDEX_DIMENSION, metric=Config.PINECONE_INDEX_METRIC, spec=ServerlessSpec(cloud=Config.PINECONE_INDEX_SPEC_CLOUD, region=Config.PINECONE_INDEX_SPEC_REGION))

index = pc.Index(index_name)

products = pd.read_csv('/home/jaggu/misc/RAG/project/data/amazon-products-preprocessed.csv').to_dict('records')

for product in products:
    try:
        vector = generate_embeddings([product['title'] + '.' + product['description']])[0]
        index.upsert(ids=[product['uuid']], vectors=[vector])
    except Exception as e:
        print(e)
        print(product)

print(pc.list_indexes())