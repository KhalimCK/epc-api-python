class MissingAuth(Exception):
    """Raise when authentication credentials are missing"""

    pass


class InvalidApiParameter(Exception):
    """Raise when an invalid epc_api parameter is supplied"""

    pass


class NotFound(Exception):
    """Raise when a 404 response is returned by the epc epc_api"""

    pass


class InvalidHeader(Exception):
    """
    Raise when an invalid header is supplied. For example, application/zip cannot be provided the
    mime type for the recommendations route
    """

    pass


class Unauthorized(Exception):

    """
    Raise when 401 is returned by the epc_api
    """

    pass
