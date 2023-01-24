from framework import Framework

class DFS(Framework):
    def __init__(self,maze):
        self.maze = maze
        self.moved = []
        self.visited=[]
        self.meta=[]
        self.start = []
        self.move_copy = []
        self.height = len(self.maze)
        self.width = len(self.maze[0])
        self.maze_path = []
        
    #regresa los resultados
    def results(self):
        return self.visited, self.maze_path
    
    #revisar si llego a la meta
    def goal(self):
        for final_goal in self.meta:
            if final_goal in self.moved[self.movePosition]:
                # print("width: ", self.width)
                # print("height: ", self.height)
                # print("movement: ", self.moved[i])
                # print("numer of movement: ", len(self.moved[i]))
                self.maze_path = self.moved[self.movePosition]
                self.moved = []
    
    def step(self):
        pass
    
    def stepCost(self, paths):
        pass

    #revisa su entorno
    def surrounding(self, position):
        #revisar si arriba no es un cuadro negro
        actual_x,actual_y = position
        self.x, self.y = actual_x,actual_y
        copy2 = self.move_copy.copy()
        if actual_y-1 >= 0:
            if self.maze[actual_y-1][actual_x] != 0:
                if([actual_x,actual_y-1]) not in self.visited:
                    copy2.append([actual_x,actual_y-1])
                    self.moved.insert(0,copy2)
        
        #revisar si derecha no es un cuadro negro
        copy2 = self.move_copy.copy()
        if actual_x+1 < self.width:
            if self.maze[actual_y][actual_x+1] != 0:
                if([actual_x+1,actual_y]) not in self.visited:
                    copy2.append([actual_x+1,actual_y])
                    self.moved.insert(0,copy2)

        #revisar si abajo no es un cuadro negro
        copy2 = self.move_copy.copy()
        if actual_y+1 < self.height:
            if self.maze[actual_y+1][actual_x] != 0:
                if([actual_x,actual_y+1]) not in self.visited:
                    copy2.append([actual_x,actual_y+1])
                    self.moved.insert(0,copy2)

        #revisar si izquierda no es un cuadro negro
        copy2 = self.move_copy.copy()
        if actual_x-1 >=0:
            if self.maze[actual_y][actual_x-1] != 0:
                if([actual_x-1,actual_y]) not in self.visited:
                    copy2.append([actual_x-1,actual_y])
                    self.moved.insert(0,copy2)
    
    #inicio del proceso
    def actions(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x] == 9:
                    self.meta.append([x,y])
                elif self.maze[y][x] == 8:
                    self.start.append([x,y])
        #agregar la posicion inicail como lugar que ya se movio
        self.moved.append(self.start[0])
        #comenzar a analizar su entorno
        while self.moved:
            for i in range(len(self.moved)):
                self.movePosition= i
                #actual position
                if len(self.moved) == 1:
                    actual_x=self.moved[len(self.moved)-1][0]
                    actual_y=self.moved[len(self.moved)-1][1]
                else:
                    actual_x=self.moved[i][len(self.moved[i])-1][0]
                    actual_y=self.moved[i][len(self.moved[i])-1][1]
                # guardar como lugares ya visitados para que no se vuelva a visitar
                self.visited.append([actual_x,actual_y])           
                #condicion para realizar copia
                if len(self.moved) == 1:
                    self.move_copy = self.moved.copy()
                else:
                    self.move_copy = self.moved[i].copy()
                self.moved.pop(0)
                
                #analiza su entorno y se agrega de arriba,derecha,abajo,izquierda
                self.surrounding((actual_x,actual_y))
                #revisa si llego a la meta
                self.goal()
                break
