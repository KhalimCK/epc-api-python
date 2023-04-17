epc-api-python
========================

Simple python client to interface with the EPC data API.

API docs for the domestic api can be found [here](https://epc.opendatacommunities.org/docs/api/domestic)

API docs for the non-domestic api can be found [here](https://epc.opendatacommunities.org/docs/api/non-domestic)

You need to sign up with the EPC api which will provide you with an api key. You need to use
the api key in conjunction with your sign up email address, or with the authorisation
token that you are provided with to access the api

# Installation

This package can be installed by running
```
pip install epc-api-python
```

# Usage
Some usage examples can be found in the `/examples` folder

To set up the api import the `EpcClient` class an initialise the client by tunning

```commandline
import dotenv
from epc_api.client import EpcClient

your_email = "email you signed up with"
api_key = "api you were emailed after sign up"


# I have auth_token in my environment
client = EpcClient(
    user_email=your_email, api_key=your_email_key, version="v1"
)

client.domestic  # interfaces with the domestic url https://epc.opendatacommunities.org/api/<version>/domestic/
client.non_domestic  # interfaces with the non-domestic url https://epc.opendatacommunities.org/api/<version>/non-domestic/
```

There are three main functions that you should use. They are used identically
for both the domestic and non-domestic urls. These are `search`, `certificate` and `recommendations`, which 
access the `/search`, `/certificate` and `/recommendations` urls respectively. Detailed description of these urls
can be found in the api documentation however each of these functions can be used immediately, 
for example

```commandline
search_resp = client.domestic.search()
print(search_resp)

# Test the certificate endpoint
# Use the first lmk_key which is provided as a response from /search
lmk_key = search_resp["rows"][0]["lmk-key"]

certificate_resp = client.domestic.certificate(lmk_key=lmk_key)
print(certificate_resp)

# Test the recommendations endpoint with the same lmk_key
recommendation_resp = client.domestic.recommendations(lmk_key=lmk_key)
print(recommendation_resp)
```

The client can be set up with multiple mime types, with the default value being
`application/json`. If this value is supplied, the json data is parsed and returned in a 
list/dictionary format, however for other mime types, the user is presented the 
content back and it's up to the user to parse the response in a suitable
fashion. Some examples of handling different mime types of have provided in `/examples`.
