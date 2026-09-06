class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opned = False

    def open(self):
        if self.opned:
            raise InvalidOperationError("File already Opened")
        self.opned = True

    def close(self):
        if not self.opned:
            raise InvalidOperationError("File already Closed")
        self.opned = False


class FileStream(Stream):
    def read(self):
        print("FileStream read successfully")


class NetworkStream(Stream):
    def read(self):
        print("NetworkStream read successfully")


file = FileStream()
file.open()
file.read()
file.close()

network = NetworkStream()
network.open()
network.read()
network.close()
