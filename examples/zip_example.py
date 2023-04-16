import dotenv
from api.client import EpcClient
import tempfile
import os

dotenv.load_dotenv()

# I have auth_token in my environment
client = EpcClient(version="v1", accept="application/zip")

response = client.domestic.search()

# Store the output
tmp = tempfile.mktemp(suffix=".zip")


with open(tmp, "wb") as f:
    f.write(response)

# That file can be unzipped and will contain csv fils of the extracted data.

# Tidy up
os.remove(tmp)


