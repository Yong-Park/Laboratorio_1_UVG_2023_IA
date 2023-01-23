from abc import ABC, abstractmethod

class problem(ABC):
    
    @abstractmethod
    def actions(self, state):
        pass

    @abstractmethod
    def results(self, state, action):
        pass
    
    @abstractmethod
    def goalTest(self, state):
        pass
    
    @abstractmethod
    def stepCost(self, state, action, newState):
        pass
    
    @abstractmethod
    def pathCost(self, states):
        pass
    