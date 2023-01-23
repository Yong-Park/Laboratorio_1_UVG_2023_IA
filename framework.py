from abc import ABC, abstractmethod

class Framework(ABC):
    @abstractmethod
    def __init__(self, maze, w, h):
        pass
    @abstractmethod
    def actions(self):
        pass
    @abstractmethod
    def results(self):
        pass
    @abstractmethod
    def goalTest(self):
        pass
    @abstractmethod
    def stepTest(self):
        pass
    @abstractmethod
    def pathTest(self):
        pass