import os

import dotenv
import tempfile
from api.client import EpcClient

dotenv.load_dotenv()

# I have auth_token in my environment
client = EpcClient(version="v1", accept="text/csv")

response = client.domestic.search()

tmp = tempfile.mktemp(suffix=".csv")

with open(tmp, "wb") as f:
    f.write(response)

# This csv file may now be used as desired

# Tidy up
os.remove(tmp)
