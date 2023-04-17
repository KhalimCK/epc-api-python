from epc_api.client import EpcClient

# I have auth_token in my environment
client = EpcClient(version="v1", api_key="your epc_api key", user_email="your email address")

search_resp = client.domestic.search(params={})
print(search_resp)

# Test the certificate endpoint
certificate_resp = client.domestic.certificate(lmk_key=search_resp["rows"][0]["lmk-key"])
print(certificate_resp)

# Test the recommendations endpoint
recommendation_resp = client.domestic.recommendations(lmk_key=search_resp["rows"][0]["lmk-key"])
print(recommendation_resp)
