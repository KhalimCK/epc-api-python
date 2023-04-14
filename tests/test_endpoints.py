import base64
import pytest
from api.client import EpcClient
from api.exceptions import InvalidHeader


def test_recommendations_with_application_zip():

    # Currently, application/zip cannot be used with /recommendations
    test_user_email = "test@user.com"
    test_api_key = "testapikey"

    client = EpcClient(user_email=test_user_email, api_key=test_api_key, accept="application/zip")

    with pytest.raises(InvalidHeader):
        client.domestic.recommendations(lmk_key="test")