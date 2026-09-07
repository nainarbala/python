from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("File already Opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("File already Closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("FileStream read successfully")


class NetworkStream(Stream):
    def read(self):
        print("NetworkStream read successfully")


class MemoryStream(Stream):
    def read(self):
        print("MemoryStream read successfully")


file = FileStream()
file.open()
file.read()
file.close()

network = NetworkStream()
network.open()
network.read()
network.close()

memory = MemoryStream()
memory.open()
memory.read()
memory.close()
