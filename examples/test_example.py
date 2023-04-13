import dotenv
import requests
from api.client import EpcClient

dotenv.load_dotenv()

# I have auth_token in my environment
client = EpcClient()

VERSION = "v1"

host = "https://epc.opendatacommunities.org/api/{version}/domestic".format(version=VERSION)

url = "/".join([host, "search"])

resp = requests.get(
    url=url,
    headers=client.headers,
)

search_resp = client.domestic.search(params={})
