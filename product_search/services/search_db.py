import sys
import os
from config import Config
from pinecone import Pinecone

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../utils')))
from setup_pinecone import generate_embeddings

pc = Pinecone(api_key=Config.PINECONE_API_KEY)
index_name = Config.PINECONE_INDEX_NAME

index = pc.Index(index_name)

def search_products(query):
    print('Searching for:', query)
    vector = generate_embeddings([query])[0]
    
    # Ensure the vector is a list of floats
    vector_list = [float(x) for x in vector.tolist()]

    results = index.query(queries=[vector_list], top_k=5)
    return results.ids