class MissingAuth(Exception):
    """Raise when authentication credentials are missing"""

    pass


class InvalidApiParameter(Exception):
    """Raise when an invalid api parameter is supplied"""

    pass
