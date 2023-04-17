import os

import tempfile
from epc_api_python.client import EpcClient

# I have auth_token in my environment
client = EpcClient(api_key="your epc_api_python key", user_email="your email address", version="v1", accept="text/csv")

response = client.domestic.search()

tmp = tempfile.mktemp(suffix=".csv")

with open(tmp, "wb") as f:
    f.write(response)

# This csv file may now be used as desired

# Tidy up
os.remove(tmp)
