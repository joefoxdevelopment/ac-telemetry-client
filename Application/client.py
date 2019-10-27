import re, socket

# Connects to ACServer instance at host:port defined using the following interface
# https://docs.google.com/document/d/1KfkZiIluXZ6mMhLWfDX1qAGbvhGRC3ZUzjVIt5FQpp4/pub

class Client:

    host = None
    port = None

    connection = None

    # These values
    MODE_HANDSHAKE = 0
    MODE_UPDATE    = 1
    MODE_SPOTTER   = 2
    MODE_DISMISS   = 3

    def __init__(self, host, port):
        if [] == re.findall('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', str(host)):
            raise Exception('Host is not a valid IPv4 address. Received: ' + host)

        if [] == re.findall('^\d{1,5}$', str(port)):
            raise Exception('Host is not a valid port number. Received: ' + port)

        self.host = host
        self.port = port

    def connect(self):
        self.handshake()
        self.disconnect()
        return

        while True:
            print('telem data')

            # this try except block is to break on user input
            try:
                stdin = sys.stdin.read()
                if "\n" in stdin or "\r" in stdin:
                    break
            except IOError:
                pass

    def handshake(self):
        print('performing handshake')

        self.connection = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        self.connection.bind((self.host, self.port))

        # Do the "handshaking" part of the request lifecycle
        # This is not a standard UDP thing, just required to talk to
        # Assetto Corsa
        setMode(self.MODE_HANDSHAKE)

        response = self.connection.recv()
        print(response)

    def update():
        print('do update')

    def disconnect(self):
        print('ending connection')
        self.setMode(self.MODE_DISMISS)

    def setMode(self, mode):
        print('Setting mode: ' + str(mode))

        self.connection.send({
            'identifier': 1,
            'version': 1,
            'operationId': mode
        })
