'''
    Universidad del Valle de Guatemala
    Inteligencia Artificial - CC3085
    Laboratorio 1 #7 
'''
import random
from problem import problem

def getCoordinatesS(array):
    countRS = 0
    countCS = 0

    for row in array:
        countCS = 0
        for element in row:
            if element == 8:
                return (countRS, countCS)
            countCS += 1   
        countRS += 1  
            
    return "Sin coincidencias"

def getCoordinatesE(array):
    countRE = 0
    countCE = 0
    Results = []
    
    for row in array:
        countCE = 0
        for element in row:
            if element == 9:
                Results.append((countRE, countCE))
            countCE += 1     
        countRE += 1
    
    if (len(Results) != 0):
        return Results 
    else:
        return "Sin coincidencias"

class BFS(problem):
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])
        self.start = getCoordinatesS(matrix)        
        self.finish = getCoordinatesE(matrix)   
        self.frontier = [self.start] 
        self.visited = []  
        self.path = []
        
        self.search()
    
    def actions(self, state):
        if self.matrix[state[0]][state[1]] == 0:
            return "wall"
        else:
            return "path"
    
    def results(self, action, state=None):
        if action == "add":
            if state not in self.visited:
                self.visited.append(state)
                self.frontier.append(state)

    def goalTest(self, state):
        return state in self.finish
    
    def stepCost(self, state, action, newState):
        pass
    
    def pathCost(self, states):
        pass
    
    def frontier_is_Empty(self):
        return True if (len(self.frontier) == 0) else False
    
    def get_neighbors(self, state):
        actual_x = state[0]
        actual_y = state[1]
        
        # look left
        if actual_x > 0:
            veri = self.actions(((actual_x-1), actual_y))
            if veri != "wall":
                self.results("add", ((actual_x-1), actual_y))
        # look right
        if (actual_x < self.width - 1):
            veri = self.actions(((actual_x+1), actual_y))
            if veri != "wall":
                self.results("add", ((actual_x+1), actual_y))   
        # look up
        if actual_y > 0:
            veri = self.actions((actual_x, (actual_y-1)))
            if veri != "wall":
                self.results("add", (actual_x, (actual_y-1)))
        # look down
        if (actual_y < self.height - 1):
            veri = self.actions((actual_x, (actual_y+1)))
            if veri != "wall":
                self.results("add", (actual_x, (actual_y+1)))    
    
    def search(self):
        
        while self.frontier:
            actual_state = self.frontier.pop(0)
            self.path.append(actual_state)    
            
            if self.goalTest(actual_state):
                return self.path
            
            self.get_neighbors(actual_state)
            
        return "No tiene solucion"
            
        
