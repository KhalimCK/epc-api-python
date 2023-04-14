class MissingAuth(Exception):
    """Raise when authentication credentials are missing"""

    pass


class InvalidApiParameter(Exception):
    """Raise when an invalid api parameter is supplied"""

    pass


class NotFound(Exception):
    """Raise when a 404 response is returned by the epc api"""

    pass


class InvalidHeader(Exception):
    """
    Raise when an invalid header is supplied. For example, application/zip cannot be provided the
    mime type for the recommendations route
    """

    pass
