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

    def __init__(self, uri: str = "/", status: int = 200, data: str = "") -> None:
        self.uri = uri
        self._status: int = status
        self._data: str = data

    @property
    def uri(self) -> str:
        return self._uri

    @uri.setter
    def uri(self, value: str) -> None:
        """ todo: check for valid data and raise ValueError if not """
        self._uri = value

    @property
    def status(self) -> int:
        return self._status

    @status.setter
    def status(self, value: int) -> None:
        """ todo: check for valid data and raise ValueError if not """
        self._status = value

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value: str) -> None:
        """ todo: check for valid data and raise ValueError if not """
        self._data = value

    def __str__(self) -> str:
        return f"[{self.status}] {self.uri}"

    def __compare__(self, uri: str) -> bool:
        return self.uri == uri

    def __eq__(self, other) -> bool:
        """ todo: fix other datatype """
        return self.uri == other.uri


class Borg:  # pylint: disable=too-few-public-methods
    """
    docstring
    """

    _shared_state: object = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state


class Endpoints(Borg):
    """
    manages a collection of endpoints
    """

    def __init__(self, eps=None) -> None:
        super().__init__()
        if eps:
            self._eps = eps
        else:
            if not hasattr(self, "_eps"):
                self._eps = [
                    Endpoint(uri="/health/liveness", status=200, data="ok"),
                    Endpoint(uri="/health/readiness", status=200, data="ok"),
                ]

    def __contains__(self, uri: str) -> bool:
        return self.__getitem__(uri) is not None

    def __getitem__(self, uri: str):
        """ todo: correct return value (Endpoint vs. None) """
        for endpoint in self._eps:
            if endpoint._uri == uri:
                return endpoint
        return None

    def __add__(self, endpoint: Endpoint) -> None:
        self._eps.append(endpoint)
