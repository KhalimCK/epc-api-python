import dotenv
from api.client import EpcClient

dotenv.load_dotenv()

# I have auth_token in my environment
client = EpcClient(version="v1")

search_resp = client.domestic.search(params={})

# Test csv accept response
client = EpcClient(version="v1", accept="application/vnd.ms-excel")
search_resp = client.domestic.search(params={})
