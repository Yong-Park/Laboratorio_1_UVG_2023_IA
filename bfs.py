'''
    Universidad del Valle de Guatemala
    Inteligencia Artificial - CC3085
    Laboratorio 1 #7 
'''
from problem import problem

#Método para obtener coordenadas del inicio
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

#Método para obtener coordenadas del final/finales
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

# Clase principal del algoritmo BFS que implementa el framework problem
class BFS(problem):
    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])
        self.start = getCoordinatesS(matrix)        
        self.finish = getCoordinatesE(matrix)   
        # Frontier = Lista de fronteras
        self.frontier = [self.start] 
        # Visited = Puntos visitados
        self.visited = []  
        # Path = Camino final
        self.path = []
        
        # Se llama al algoritmo principal
        self.search()
    
    # Se determina si el estado actual es una pared o una parte "accesible"
    def actions(self, state):
        if self.matrix[state[0]][state[1]] == 0:
            return "wall"
        else:
            return "path"
    
    # Dependiendo de la acción se modifican las listas que almacenan los puntos visitados, fronteras, etc
    def results(self, action, state=None):
        if action == "add":
            if state not in self.visited:
                self.visited.append(state)
                self.frontier.append(state)
        if action == 'upd':
            if state not in self.visited:
                self.visited.append(state)
                self.frontier.append(state)
                self.backtracing[state] = self.actualState
        if action == 'back':
            self.path.append(state)
            self.actualState = self.backtracing[state]

    # Se verifica si se llegó a la meta
    def goalTest(self, state):
        return state in self.finish
    
    # No se utiliza debido a que el costo es uniforme
    def stepCost(self):
        pass
    
    def pathCost(self, states):
        return (len(states) - 1) # No se toma en cuenta el inicio 
    
    # Se verifica si todavía hay elementos en la frontera
    def frontier_is_Empty(self):
        return True if (len(self.frontier) == 0) else False
    
    # Se obtienen los vecinos de un punto específico y se realiza una acción con los mismos
    def get_neighbors(self, state, type):
        actual_x = state[0]
        actual_y = state[1]
        
        if (type == "allPath"):
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
        else:
            # look left
            if actual_x > 0:
                veri = self.actions(((actual_x-1), actual_y))
                if veri != "wall":
                    self.results("upd", ((actual_x-1), actual_y))
            # look right
            if (actual_x < self.width - 1):
                veri = self.actions(((actual_x+1), actual_y))
                if veri != "wall":
                    self.results("upd", ((actual_x+1), actual_y))   
            # look up
            if actual_y > 0:
                veri = self.actions((actual_x, (actual_y-1)))
                if veri != "wall":
                    self.results("upd", (actual_x, (actual_y-1)))
            # look down
            if (actual_y < self.height - 1):
                veri = self.actions((actual_x, (actual_y+1)))
                if veri != "wall":
                    self.results("upd", (actual_x, (actual_y+1)))   
    
    # Algoritmo principal
    def search(self):
        # Mientras haya fronteras evalua cada "nodo" del grafo (arreglo de arreglos)
        while not self.frontier_is_Empty():
            
            # Se agrega el punto actual al camino final
            actual_state = self.frontier.pop(0)
            self.path.append(actual_state)    
            
            # Se evalua si se llegó a la meta
            if self.goalTest(actual_state):
                return self.path
            
            # Se obtienen los vecinos en caso de que no sea la meta
            self.get_neighbors(actual_state, "allPath")
            
        return "No tiene solucion"
    
    # Algoritmo para encontrar el camino más corto
    def search_shortest_path(self):
        # Se definen nuevamente las listas de fronteras y visitados
        # Se agrega un diccionario para ir construyendo el camino más corto
        self.frontier = [self.start]
        self.visited = [self.start]
        self.backtracing = {self.start: None}

        # Mientras haya fronteras evalua cada "nodo" del grafo (arreglo de arreglos)
        while not self.frontier_is_Empty():
            self.actualState = self.frontier.pop(0)

            # Se evalua si se llegó a la meta
            if self.goalTest(self.actualState):
                # Se agregan resultados al camino final y se realizan modificaciones para actualizar el camino más corto
                self.path = [self.start]
                while self.actualState != self.start:
                    self.results("back",self.actualState)
                self.path.reverse()
                return self.path
            
            # Se obtienen los vecinos en caso de que no sea la meta
            self.get_neighbors(self.actualState, "shortPath")
            
        return "No tiene solucion"
            