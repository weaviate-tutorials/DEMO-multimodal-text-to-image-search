import base64
import os

import weaviate
from weaviate import Config


WEAVIATE_URL = os.getenv('WEAVIATE_URL')
if not WEAVIATE_URL:
    WEAVIATE_URL = 'http://localhost:8080'
print(WEAVIATE_URL, flush=True)

client = weaviate.Client(WEAVIATE_URL)
print(f"Client is ready {client.is_ready()} (python/This is utils.py)")




def search_query(search_term):
    result =(
        client.query
        .get('MultiModal',['filename','image'])
        .with_additional(["certainty id"])
        .with_near_text({"concepts": [search_term]})
        .do()
    )
    print(result)
    return result

