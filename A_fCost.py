from framework import Framework
from math import *

class Fcost_A(Framework):

    def __init__(self, maze):
        # asignacion de valores
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])
        # print(self.height, self.width)

        self.final = []
        self.inicio = None
        self.came_from = None

        self.paths = []
        self.visitados = []
        self.camino = []

    #regresa el camino final 
    def results(self):
        return self.visitados, self.camino

    #solo se movera si no esta visitado y es igual al minimo
    def step(self):
        for costIndex in range(len(self.costos)):
            if self.vecinos[costIndex] not in self.visitados and self.costos[costIndex] == self.costoMinimo:
                    self.paths.append(self.vecinos[costIndex])
                    self.visitados.append(self.vecinos[costIndex])
                    self.came_from[self.vecinos[costIndex]] = self.current
    
    #obtiene los vecinos que se encuentre
    def surrounding(self, position):
        posibles = []
        x,y = position
        #derecha
        if x+1 < self.width:
            if self.maze[y][x+1]!=0: 
                posibles.append((x+1,y))
        #izquierda
        if x-1 >=0:
            if self.maze[y][x-1]!=0:
                posibles.append((x-1,y))
        #abajo
        if y+1 < self.height:
            if self.maze[y+1][x]!=0:
                posibles.append((x,y+1))
        #arriba
        if y-1 >=0:
            if self.maze[y-1][x]!=0:
                posibles.append((x,y-1))
        #izquierda superior
        if x-1 >=0 and y-1>=0:
            if self.maze[y-1][x-1]!=0:
                posibles.append((x-1,y-1))
        #izquierda inferior
        if x-1 >=0 and y+1 < self.height:
            if self.maze[y+1][x-1]!=0:
                posibles.append((x-1,y+1))
        #derecha superior
        if x+1 < self.width and y-1>=0:
            if self.maze[y-1][x+1]!=0:
                posibles.append((x+1,y-1))
        #derecha inferior
        if  x+1 < self.width and y+1 < self.height:
            if self.maze[y+1][x+1]!=0:
                posibles.append((x+1,y+1))
        return posibles
    
    #para calcular el cost de F de todos vecinos
    def stepCost(self, paths):
        Fcost_values = []
        nodos = paths
        
        for nodo in (nodos):
            G = dist(self.inicio,nodo)
            H = []
            for nodo_final in self.final:
                h =  dist(nodo_final,nodo)
                H.append(h)
            F = round(G + min(H))
            Fcost_values.append(F)
        return Fcost_values
    
    #revisa si el nodo en el que esta es la meta
    def goal(self):
        if self.current in self.final:
            self.camino = []
            while self.current != self.inicio:
                self.camino.append(self.current)
                self.current = self.came_from[self.current]
            self.camino.append(self.inicio)
            # Reasignar las posiciones de los nodos
            self.camino = self.camino[::-1]

    
    def actions(self):
        # econtrar su posicion inicial y las finales
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 8:
                    self.inicio = (x,y)
                elif self.maze[y][x] == 9:
                    self.final.append((x,y))

        # print('Este es el inicio:',self.inicio)
        # print('Posibles finales',self.final)

        # Algoritmo F cost A star
        self.paths.append(self.inicio)
        self.visitados.append(self.inicio)
        self.came_from = {self.inicio: None}

        while  self.paths:
            # obtener el primer nodo para analizar sus vecinos
            self.current =  self.paths.pop(0)
            # print("actual: ",self.current)
            # Se comprueba si el nodo es la meta
            self.goal()
            
            # Se obtienen los vecinos del nodo actual
            self.vecinos = self.surrounding(self.current)
            # print("sus nodos vecinos: ", vecinos)
            self.costos = self.stepCost(self.vecinos)
            # Realizar una revision solo para ver si ya se visito y si es en este caso cambiar su costo a muy elevado
            for costIndex in range(len(self.costos)):
                if self.vecinos[costIndex] in self.visitados:
                    # actualizar el costo para que sea muy elevado
                    self.costos[costIndex] = 999999
                    
            # print("valores de F: ", costos)
            self.costoMinimo = min(self.costos)
            # print("costo minimo: ",costoMinimo)
            # input()
            # solo visitara los que tengan el menor costo
            self.step()
                
            # print("=========================")
    
    

        