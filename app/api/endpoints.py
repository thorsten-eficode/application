"""
    docstring
"""


class Endpoint:
    """
        manages an api endpoint
        uri: str
        status: int
        data: str
    """

    def __init__(self, uri: str = '/', status: int = 200, data: str = ''):
        self.uri: str = uri
        self.status: int = status
        self.data: str = data
        #print(self.__str__())

    def __str__(self):
        return "[{}] {}".format(self.status, self.uri)

    def __compare__(self, uri: str):
        return self.uri == uri

    def __eq__(self, other):
        return self.uri == other.uri


class Borg:
    """
        docstring
    """

    _shared_state :object = {}

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
                    Endpoint(
                        uri="/health/liveness",
                        status=200,
                        data="ok"
                    ),
                    Endpoint(
                        uri="/health/readiness",
                        status=200,
                        data="ok"
                    )
                ]

    def __contains__(self, uri: str):
        return self.__getitem__(uri) != None

    def __getitem__(self, uri :str):
        for ep in self._eps:
            if (ep.uri == uri):
                return ep
        return None

    def __add__(self, endpoint: Endpoint):
        self._eps.append(endpoint)

