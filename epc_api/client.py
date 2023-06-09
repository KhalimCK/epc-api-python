import base64
import os
from functools import partial
from pydantic.error_wrappers import ValidationError

import requests
from urllib.parse import urlencode

import epc_api.exceptions as exceptions
from epc_api.schemas import ParamSchema


class EpcClient:
    auth_token, headers, api_key, user_email = (None,) * 4
    valid_accept = [
        "text/csv",
        "application/json",
        "application/zip",
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ]

    host = "https://epc.opendatacommunities.org/api/{version}/{api_type}"

    valid_versions = ("v1",)

    def __init__(
        self,
        auth_token: [None, str] = None,
        user_email: [None, str] = None,
        api_key: [None, str] = None,
        accept: [None, str] = None,
        version: [None, str] = None
    ):
        """
        To authenticate with this epc_api, an auth token is generated by Base64-encoding the string
        <user_email>:<api_key> and therefore when initialising this client, the user can either pass the
        auth_token or the user_email and the api_key
        :param auth_token:      authorisation token for the epc_api. The authorisation token is generated from a users
                                epc_api key and email address, however the authorisation token can be supplied directly
        :param user_email:      Should be the email address that has been used to sign up to the epc_api with
        :param api_key:         The epc_api key which is emailed to you after signing up to the epc_api
        :param accept:          mime type value. If not applied, defaults to "application/json". Valid values can be
                                found in EpcClient.valid_accept
        :param version:         Api version to be used.
        """

        # Attempt to set auth token
        self.set_auth_token(auth_token)

        if self.auth_token is None:
            # Otherwise, we generate auth_token from user_email and api_key
            self._set_user_email(user_email)
            self._set_api_key(api_key)
            self._create_auth_token()

        # For the moment, the only format we allow is .zip
        if accept is not None:
            # Make sure we're given a valid value
            if accept not in self.valid_accept:
                raise exceptions.InvalidApiParameter(
                    "Invalid value supplied for accept, given %s valid values are %s"
                    % (accept, self.valid_accept)
                )
            self._accept = accept
        else:
            # Defualt to application/json
            self._accept = "application/json"

        self.version = version if version in self.valid_versions else "v1"

        # Set up headers
        self._set_headers()

        # Insert version into host
        self._set_host()

        # Set up domestic and non-domestic apis separately
        self.domestic = EpcResource(
            api_type="domestic", host=self.host, headers=self.headers
        )
        self.non_domestic = EpcResource(
            api_type="non-domestic", host=self.host, headers=self.headers
        )

    def set_auth_token(self, auth_token):
        if not auth_token:
            auth_token = os.getenv("EPC_AUTH_TOKEN")
        self.auth_token = auth_token

    def _create_auth_token(self):
        self.auth_token = base64.b64encode(
            ":".join([self.user_email, self.api_key]).encode("utf-8")
        )

    def _set_user_email(self, user_email):
        """
        Utility function which sets the value of user_email. If not set, lookes for EPC_USER_EMAIL in the environment
        """

        if not user_email:
            user_email = os.getenv("EPC_USER_EMAIL")

        self.user_email = user_email

        if not self.user_email:
            raise exceptions.MissingAuth(
                "user_email not passed and could not be found as EPC_USER_EMAIL in environment"
            )

    def _set_api_key(self, api_key):
        """
        Utility function which sets the value of api_key. If not set, lookes for EPC_API_KEY in the environment
        """

        if not api_key:
            api_key = os.getenv("EPC_API_KEY")

        self.api_key = api_key

        if not self.api_key:
            raise exceptions.MissingAuth(
                "api_key not passed and could not be found as EPC_API_KEY in environment"
            )

    def _set_headers(self):
        self.headers = {
            "Authorization": "Basic {auth_token}".format(auth_token=self.auth_token),
            "Accept": self._accept,
        }

    def _set_host(self):
        self.host = partial(self.host.format, version=self.version)


class EpcResource:

    """
    Both domestic and non-domestic urls seem to have analogous funcitonality so we should be able to have
    a single set of methods which interacts with both in an identical fashion
    """

    def __init__(self, api_type, host, headers):
        self.host = host(api_type=api_type)
        self.headers = headers

    def _parse_response(self, response):
        """
        Given a successful response, this function parses the returned values
        """
        if self.headers["Accept"] == "application/json":
            if not response.text:
                # If we get an empty response, we return an empty object
                return {}
            return response.json()

        # For other headers, we take the simple approach and allow the user to parse as they wish
        return response.content

    def call(self, method, url, params):
        response = getattr(requests, method)(
            url=url, headers=self.headers, params=params
        )

        if response.status_code == 200:
            result = self._parse_response(response)
            return result

        if response.status_code == 404:
            raise exceptions.NotFound("404 Response not found, no data available for this request")

        if response.status_code == 401:
            raise exceptions.Unauthorized("401 Unauthorized to %s" % url)

    @staticmethod
    def _validate_params(params):

        try:
            ParamSchema(**params)
        except ValidationError as _:
            # We handle the error and raise a simple error
            raise exceptions.InvalidApiParameter(
                "Invalid parameter passed, check epc_api documentation for valid parameters"
            )
        pass

    def search(self, params: dict = None, size: int = None, offset_from: int = None):
        """
        Function handles interaction with search endpoint
        :param params:          dictionary of parameters that are passed to the /search url. More information on
                                valid parameter values can be found in the epc_api documentation at
                                https://epc.opendatacommunities.org/docs/api/domestic for the domestic epc_api and
                                https://epc.opendatacommunities.org/docs/api/non-domestic for the non-domestic epc_api
        :param size:            The /search endpoint can be provided with a page size integer parameter which can
                                be between 25 and 10000
        :param offset_from:     offset_from is a typical offset parameter which if specified will fetch results after
                                that positional index. For example, providing the value 1000 will fetch results after
                                the 1000th record

        """
        params = {} if params is None else params
        # Search method can be supplied with parameters, we validate them here
        self._validate_params(params)

        url = os.path.join(self.host, "search")
        if size or offset_from:
            url += "?" + urlencode({k: v for k, v in {"size": size, "from": offset_from}.items() if v})

        result = self.call(method="get", url=url, params=params)
        return result

    def certificate(self, lmk_key: str):
        """
        Function handles interaction with certificate endpoint
        :param lmk_key: lmk-key is the LMK key of a certificate from a search result or download
        """

        url = os.path.join(self.host, "certificate", lmk_key)

        result = self.call(method="get", url=url, params={})
        return result

    def recommendations(self, lmk_key: str):
        """
        Function handles interaction with recommendations endpoint
        :param lmk_key: lmk-key is the LMK key of a certificate from a search result or download
        """

        if self.headers["Accept"] == "application/zip":
            raise exceptions.InvalidHeader(
                "application/zip in an invalid mime value for /recommendations, initialise a new client with a "
                "different header value"
            )

        url = os.path.join(self.host, "recommendations", lmk_key)

        result = self.call(method="get", url=url, params={})
        return result
