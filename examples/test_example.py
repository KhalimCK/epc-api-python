import dotenv
from api.client import EpcClient

dotenv.load_dotenv()

# I have auth_token in my environment
client = EpcClient(version="v1")

search_resp = client.domestic.search(params={})

address_search_resp = client.domestic.search(params={"postcode": "w6 9bf"})