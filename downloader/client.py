import os
import downloader.exceptions as exceptions


class EpcClient:
    def __init__(self, auth_token=None, user_email=None):
        self._set_auth_token(auth_token)

        self._set_user_email(user_email)

    def _set_auth_token(self, auth_token):
        """
        Utility function which sets the value of auth_token. If not set, lookes for EPC_AUTH_TOKEN in the environment
        """

        if not auth_token:
            auth_token = os.getenv("EPC_AUTH_TOKEN")

        self.auth_token = auth_token

        if not self.auth_token:
            raise exceptions.MissingAuth(
                "auth_token not passed and could not be found as EPC_AUTH_TOKEN in environment"
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
