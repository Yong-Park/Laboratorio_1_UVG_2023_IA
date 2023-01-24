from abc import ABC, abstractmethod

class Framework(ABC):
    @abstractmethod
    def __init__(self, maze):
        pass
    @abstractmethod
    def results(self):
        pass
    @abstractmethod
    def goal(self):
        pass
    @abstractmethod
    def step(self):
        pass
    @abstractmethod
    def stepCost(self,paths):
        pass
    @abstractmethod
    def surrounding(self,position):
        pass
    @abstractmethod
    def actions(self):
        pass
