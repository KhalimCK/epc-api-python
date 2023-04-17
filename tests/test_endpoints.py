import pytest
from epc_api.client import EpcClient
from epc_api.exceptions import InvalidHeader, Unauthorized, InvalidApiParameter


def test_recommendations_with_application_zip():

    # Currently, application/zip cannot be used with /recommendations
    test_user_email = "test@user.com"
    test_api_key = "testapikey"

    client = EpcClient(user_email=test_user_email, api_key=test_api_key, accept="application/zip")

    with pytest.raises(InvalidHeader):
        client.domestic.recommendations(lmk_key="test")


def test_search():
    # Currently, application/zip cannot be used with /recommendations
    test_user_email = "test@user.com"
    test_api_key = "testapikey"

    # We do not expect this test to actually pass and hit the epc_api, however we
    # make sure the client has been set up correctly

    client = EpcClient(user_email=test_user_email, api_key=test_api_key)

    with pytest.raises(Unauthorized) as err:
        client.domestic.search()

    # Check the url set up correctly
    assert err.value.args[0] == "401 Unauthorized to https://epc.opendatacommunities.org/api/v1/domestic/search"

    # Test with page size and offset parameters

    with pytest.raises(Unauthorized) as err:
        client.domestic.search(size=1000)

    # Check the url set up correctly
    assert err.value.args[0] == \
        '401 Unauthorized to https://epc.opendatacommunities.org/api/v1/domestic/search?size=1000'

    with pytest.raises(Unauthorized) as err:
        client.domestic.search(offset_from=40)

    # Check the url set up correctly
    assert err.value.args[0] == \
        '401 Unauthorized to https://epc.opendatacommunities.org/api/v1/domestic/search?from=40'

    with pytest.raises(Unauthorized) as err:
        client.domestic.search(offset_from=1337, size=1337)

    # Check the url set up correctly
    assert err.value.args[0] == \
        '401 Unauthorized to https://epc.opendatacommunities.org/api/v1/domestic/search?size=1337&from=1337'


def test_search_params():
    test_user_email = "test@user.com"
    test_api_key = "testapikey"

    client = EpcClient(user_email=test_user_email, api_key=test_api_key, accept="application/zip")

    with pytest.raises(InvalidApiParameter):
        client.domestic.search(params={"bad": "bad"})


def test_certificate():
    test_user_email = "test@user.com"
    test_api_key = "testapikey"

    client = EpcClient(user_email=test_user_email, api_key=test_api_key, accept="application/zip")

    with pytest.raises(Unauthorized) as err:
        client.domestic.certificate(lmk_key="test_lmk_key")

    # Check the url set up correctly
    assert err.value.args[0] == \
        '401 Unauthorized to https://epc.opendatacommunities.org/api/v1/domestic/certificate/test_lmk_key'


def test_recommendations():
    test_user_email = "test@user.com"
    test_api_key = "testapikey"

    client = EpcClient(user_email=test_user_email, api_key=test_api_key)

    with pytest.raises(Unauthorized) as err:
        client.domestic.recommendations(lmk_key="test_lmk_key")

    # Check the url set up correctly
    assert err.value.args[0] == \
        '401 Unauthorized to https://epc.opendatacommunities.org/api/v1/domestic/recommendations/test_lmk_key'
