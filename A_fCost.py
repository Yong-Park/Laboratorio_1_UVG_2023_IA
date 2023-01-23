from framework import Framework
from math import *

class Fcost_A(Framework):

    def __init__(self, maze):
        
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])

        self.final = []
        self.inicio = None

        self.line_up = []
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

    def algorithm(self):
        self.inicio = None
        self.final = []
        self.line_up = []
        self.visitados = []
        self.came_from = None

        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 8:
                    self.inicio = (x,y)
                elif self.maze[y][x] == 9:
                    self.final.append((x,y))

        print('Este es el inicio:',self.inicio)
        print('Posibles finales',self.final)

        #Algoritmo F cost A star
        self.line_up.append(self.inicio)
        self.visitados.append(self.inicio)
        self.came_from = {self.inicio: None}

        # Se itera mientras la cola no esté vacía
        while  self.line_up:
            # Se saca el primer nodo de la cola
            self.current =  self.line_up.pop(0)
            print("actual: ",self.current)
            # Se comprueba si el nodo actual es el nodo final
            if self.current in self.final:
                # Se construye el camino y se regresa
                self.camino = []
                while self.current != self.inicio:
                    self.camino.append(self.current)
                    self.current = self.came_from[self.current]
                self.camino.append(self.inicio)
                # print("camino final: ", self.camino[::-1])
                return self.camino[::-1]
            
            
            # Se obtienen los vecinos del nodo actual
            neighbours = self.obtener_vecinos(self.current)
            print("sus nodos vecinos: ", neighbours)
            costos = self.calcular_Fcost(neighbours)
            #realizar una revision solo para ver si ya se visito y si es en este caso cambiar su costo a muy elevado
            for costIndex in range(len(costos)):
                if neighbours[costIndex] in self.visitados:
                    # actualizar el costo para que sea muy elevado
                    costos[costIndex] = 999999
                    
            print("valores de F: ", costos)
            costoMinimo = min(costos)
            print("costo minimo: ",costoMinimo)
            # input()
            #solo visitara los que tengan el menor costo
            for costIndex in range(len(costos)):
                if neighbours[costIndex] not in self.visitados and costos[costIndex] == costoMinimo:
                        # Se agrega el vecino a la cola y se marca como visitado
                        print("el que se visito: ", neighbours[costIndex])
                        self.line_up.append(neighbours[costIndex])
                        self.visitados.append(neighbours[costIndex])
                        # Se actualiza el predecesor del vecino
                        self.came_from[neighbours[costIndex]] = self.current
                
            print("=========================")

    def obtener_vecinos(self, posicion):
        posibles = []
        x,y = posicion
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
    
    def calcular_Fcost(self,vecinos):
        Fcost_values = []
        nodos = vecinos
        
        for nodo in (nodos):
            G = dist(self.inicio,nodo)
            H = []
            for nodo_final in self.final:
                h =  dist(nodo_final,nodo)
                H.append(h)
            F = round(G + min(H))
            Fcost_values.append(F)
        return Fcost_values
        