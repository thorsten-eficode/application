"""
    docstring
"""


class Endpoint:
    """
    manages an api endpoint
    _uri: str
    _status: int
    _data: str
    """

    def __init__(self, uri: str = "/", status: int = 200, data: str = ""):
        self._uri: str = uri
        self._status: int = status
        self._data: str = data

    def __str__(self):
        return "[{}] {}".format(self._status, self._uri)

    def __compare__(self, uri: str):
        return self._uri == uri

    def __eq__(self, other):
        return self._uri == other.uri


class Borg:  # pylint: disable=too-few-public-methods
    """
    docstring
    """

    _shared_state: object = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Endpoints(Borg):
    """
    manages a collection of endpoints
    """

    def __init__(self, eps=None):
        super().__init__()
        if eps:
            self._eps = eps
        else:
            if not hasattr(self, "_eps"):
                self._eps = [
                    Endpoint(uri="/health/liveness", status=200, data="ok"),
                    Endpoint(uri="/health/readiness", status=200, data="ok")
                ]

    def __contains__(self, uri: str):
        return self.__getitem__(uri) is not None

    def __getitem__(self, uri: str):
        for endpoint in self._eps:
            if endpoint._uri == uri:
                return endpoint
        return None

    def __add__(self, endpoint: Endpoint):
        self._eps.append(endpoint)
