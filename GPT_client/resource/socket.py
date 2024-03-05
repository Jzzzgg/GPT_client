"""
Client socket 
"""
import socket

class ClientRunner(object):
    """
    Run socket funtions
    """
    def send(self, value, host, port):
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((host, port))
            sock.sendall(bytes( value+"\n", "utf-8"))
            # Receive data from the server and shut down
# End ClientRunner class
            

cr = ClientRunner()


if __name__ == "__main__":
    pass