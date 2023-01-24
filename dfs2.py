from framework import Framework

class DFS(Framework):
    def __init__(self,maze):
        # asignacion de valores
        self.maze = maze
        self.height = len(self.maze)
        self.width = len(self.maze[0])

        self.final = []
        self.inicio = None
        self.came_from = None
        
        self.paths = []
        self.visitados = []
        self.camino = []

    def actions(self):
        pass

    def results(self):
        pass

    def goalTest(self):
        pass

    def stepTest(self):
        pass

    def pathTest(self):
        pass
        
    #para inicar el proceso
    def StartUp(self):
        # econtrar su posicion inicial y las finales
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 8:
                    self.inicio = (x,y)
                elif self.maze[y][x] == 9:
                    self.final.append((x,y))

        print('Este es el inicio:',self.inicio)
        print('Posibles finales',self.final)

        # Algoritmo DFS
        self.paths.append(self.inicio)
        self.visitados.append(self.inicio)
        self.came_from = {self.inicio: None}

        while self.paths:
            # obtener el primer nodo para analizar sus vecinos
            self.current =  self.paths.pop(0)
            # print("actual: ",self.current)
            # Se comprueba si el nodo es la meta
            if self.current in self.final:
                self.camino = []
                while self.current != self.inicio:
                    self.camino.append(self.current)
                    self.current = self.came_from[self.current]
                self.camino.append(self.inicio)
                # Reasignar las posiciones de los nodos
                self.camino = self.camino[::-1]
            
            # Se obtienen los vecinos del nodo actual
            vecinos = self.obtener_vecinos(self.current)
            # print("sus nodos vecinos: ", vecinos)
                    
            # input()
            # solo visitar siempre primero si es posible desde la izquierda luego abajo, derecha y finalmente arriba
            for costIndex in range(len(vecinos)):
                if vecinos[costIndex] not in self.visitados:
                        # print("el que se visito: ", vecinos[costIndex])
                        self.paths.append(vecinos[costIndex])
                        self.visitados.append(vecinos[costIndex])
                        self.came_from[vecinos[costIndex]] = self.current
                        break
                
            # print("=========================")

    #para realizar la parte del movimiento
    def obtener_vecinos(self, posicion):
        posibles = []
        x,y = posicion
        #izquierda
        if x-1 >=0:
            if self.maze[y][x-1]!=0:
                posibles.append((x-1,y))
        #abajo
        if y+1 < self.height:
            if self.maze[y+1][x]!=0:
                posibles.append((x,y+1))
        #derecha
        if x+1 < self.width:
            if self.maze[y][x+1]!=0: 
                posibles.append((x+1,y))
        #arriba
        if y-1 >=0:
            if self.maze[y-1][x]!=0:
                posibles.append((x,y-1))
        return posibles