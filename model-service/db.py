import weaviate
from weaviate.classes.init import Auth
from config import WEAVIATE_URL, WEAVIATE_API_KEY

def init_weaviate():
    
    return weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_URL,
        auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
        skip_init_checks=True,
    )
