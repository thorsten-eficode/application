"""
    docstring
"""

import sys
import socketserver
from api.handler import ServiceHandler


class Server:  # pylint: disable=too-few-public-methods
    """
    docstring
    """

    def __init__(self, port: int = 8080) -> None:
        self._server = socketserver.ThreadingTCPServer(("", port), ServiceHandler)
        # ensures that Ctrl-C cleanly kills all spawned threads
        self._server.daemon_threads = True
        # quick rebinding
        self._server.allow_reuse_address = True

    def run(self) -> None:
        """ docstring """
        self._server.serve_forever()
        try:
            while True:
                sys.stdout.flush()
                self._server.serve_forever()
        except KeyboardInterrupt:
            pass
        self._server.server_close()
