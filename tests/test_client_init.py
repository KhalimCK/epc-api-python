import pytest
from downloader.exceptions import MissingAuth
from downloader.client import EpcClient
import base64


def test_failed_init_all_args_null():
    with pytest.raises(MissingAuth) as _:
        EpcClient(None, None)


def test_failed_init_auth_token_null():

    test_auth_token = base64.b64encode(b"test")

    with pytest.raises(MissingAuth) as _:
        EpcClient(test_auth_token, None)


def test_failed_init_user_email_null():

    test_user_email = "test@user.com"

    with pytest.raises(MissingAuth) as _:
        EpcClient(None, test_user_email)


def test_successful_init():

    test_user_email = "test@user.com"
    test_auth_token = base64.b64encode(b"test")

    client = EpcClient(test_auth_token, test_user_email)

    assert client.auth_token is not None
    assert client.user_email is not None
