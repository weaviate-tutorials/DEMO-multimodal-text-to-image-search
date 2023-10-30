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



#
#@TODO implement search_query()
#

def search_query(search_term):
    '''
    TODO: impement seach query method, return results from db
    '''
    print(f"This is running but not connected here's the query {search_term}")

    result =(
        client.query
        .get('MultiModal',['filename','image'])
        .with_additional(["certainty id"])
        .with_near_text({"concepts": [search_term]})
        .do()
    )
    print(result)
    return result

# other repo
# def search_by_text(near_text):
#     # I am fetching top 3 results for the user, we can change this by making small 
#     # altercations in this function and in upload.html file
#     # You can also analyse the result in a better way by taking a look at res.
#     # Try printing res in the terminal and see what all contents it has.
#     images = client.collection.get("ClipExample")
#     res = images.query.near_text(query=near_text, limit=3, return_properties=["text"])
#     return tuple(o.properties["text"] for o in res.objects)


#
# App.js
# # #
#   const fetch = useCallback(() => {
#     async function fetch() {
#       const res = await client.graphql
#         .get()
#         .withClassName('MultiModal')
#         .withNearText({concepts: [searchTerm]})
#         .withFields('filename image _additional{ certainty id }')
#         .do();
#       setResults(res);
#     }

#     fetch();
#   }, [searchTerm]);

#
# Site documentation: https://weaviate.io/developers/weaviate/modules/retriever-vectorizer-modules/multi2vec-clip
#