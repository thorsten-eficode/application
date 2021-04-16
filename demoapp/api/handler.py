"""
    http methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
    https://www.ietf.org/assignments/http-status-codes/http-status-codes.txt
"""

from http.server import BaseHTTPRequestHandler

from api.endpoints import Endpoint
from api.endpoints import Endpoints


class ServiceHandler(BaseHTTPRequestHandler):
    """
    Custom request handler
    POST: register data with path
    GET:  return previously registered data (see POST)
    """

    def __init__(self, *args, **kwargs) -> None:
        # super/init returns after request processing ends, so call it last
        self._eps = Endpoints()
        super().__init__(*args, **kwargs)

    def _create_response(self, status: int, data: bytes) -> None:
        """ write response """
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:
        """ Answer call with previously stored data (or answer with 404) """
        endpoint = self._eps[self.path]
        if endpoint is not None:
            self._create_response(endpoint._status, endpoint._data)
        else:
            self._create_response(404, b'{"error": "ressource not found"}')

    def do_POST(self) -> None:
        """ Store data in endpoints """
        content_length: int = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self._eps += Endpoint(self.path, 200, post_data)
        self._create_response(200, b'OK')
