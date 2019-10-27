import re

class Client:

    host = None
    port = None

    def __init__(self, host, port):
        if [] == re.findall('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host):
            raise Exception('Host is not a valid IPv4 address. Received: ' + host)

        if [] == re.findall('^\d{1,5}$', port):
            raise Exception('Host is not a valid port number. Received: ' + port)

        self.host = host
        self.port = port
