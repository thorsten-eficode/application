"""
    module docstring
"""

import os

from api.server import Server


def main():
    """ start application """
    port: int = int(os.getenv("PORT", "8080"))
    Server(port).run()


if __name__ == "__main__":
    main()
