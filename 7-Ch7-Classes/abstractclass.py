
from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("File already opned")
        self.opened = True
    
    def close(self):
        if not self.opened:
            raise InvalidOperationError("File not opened")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("File read from file")

class NtworkStream(Stream):
    def read(self):
        print("File read from network")

class MemoryStream(Stream):
    def read(self):
        print("File read from MemoryStream")

str = MemoryStream()
print(str.read())