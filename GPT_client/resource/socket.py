"""
Client socket 
"""
import socket
from default_library.constants import (HOST, PORT)
from resource.gui import gui

class ClientRunner(object):
    """
    Run socket funtions
    """
    def send(self):
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((HOST, PORT))
            sock.sendall(bytes(gui.get_message() + "\n", "utf-8"))

            # Receive data from the server and shut down