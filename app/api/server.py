"""
    docstring
"""

import sys
import socketserver
from api.handler import ServiceHandler

class Server: # pylint: disable=too-few-public-methods
    """
        docstring
    """

    def __init__(self, port: int = 8080):
        self.server = socketserver.ThreadingTCPServer(('',port), ServiceHandler )
        # ensures that Ctrl-C cleanly kills all spawned threads
        self.server.daemon_threads = True
        # quick rebinding
        self.server.allow_reuse_address = True

    def run(self):
        """ docstring """
        self.server.serve_forever()
        try:
            while True:
                sys.stdout.flush()
                self.server.serve_forever()
        except KeyboardInterrupt:
            pass
        self.server.server_close()
