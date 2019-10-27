class Client:

    host = None
    port = None

    def __init__(self, host, port):
        self.host = host
        self.port = port

        print(self.host)
        print(self.port)
