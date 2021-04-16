"""
    docstring
"""

import signal
import sys


def receive_signal(signal_number, frame):
    """ docstring """
    msg: str = "Signal: {}\nFrame: {}".format(signal_number, frame)
    print(msg)
    sys.exit()


# register the signals to be caught
signal.signal(signal.SIGHUP, receive_signal)
signal.signal(signal.SIGINT, receive_signal)
signal.signal(signal.SIGQUIT, receive_signal)
signal.signal(signal.SIGILL, receive_signal)
signal.signal(signal.SIGTRAP, receive_signal)
signal.signal(signal.SIGABRT, receive_signal)
signal.signal(signal.SIGBUS, receive_signal)
signal.signal(signal.SIGFPE, receive_signal)
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGSEGV, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)
signal.signal(signal.SIGPIPE, receive_signal)
signal.signal(signal.SIGALRM, receive_signal)
signal.signal(signal.SIGTERM, receive_signal)
