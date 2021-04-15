"""
    http methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
    https://www.ietf.org/assignments/http-status-codes/http-status-codes.txt
"""

import json
from http.server import BaseHTTPRequestHandler
from api.endpoints import Endpoints


class ServiceHandler(BaseHTTPRequestHandler):
    """
    docstring
    """

    def __init__(self, *args, **kwargs) -> None:
        # super/init returns after request processing ends, so call it last
        self._eps = Endpoints()
        super().__init__(*args, **kwargs)

    def _create_response(self, status: int, data: object):
        """
        docstring
        """
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        """
        docstring
        """
        endpoint = self._eps[self.path]
        if endpoint is not None:
            self._create_response(endpoint._status, endpoint._data)
        else:
            self._create_response(404, {"error": "ressource not found"})

    def do_VIEW(self):
        """
        docstring
        """
        self._create_response(501, {"error": "not implemented"})

    def do_POST(self):
        """
        docstring
        """
        self._create_response(501, {"error": "not implemented"})

    def do_PUT(self):
        """
        docstring
        """
        self._create_response(501, {"error": "not implemented"})

    def do_DELETE(self):
        """
        docstring
        """
        self._create_response(501, {"error": "not implemented"})
