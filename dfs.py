class DFS:
    def __init__(self,maze):
        self.maze = maze
        self.moved = []
        self.searched =[]
        self.visited=[]
        self.goal=[]
        self.start = []
        self.move_copy = []
        self.height = len(self.maze)
        self.width = len(self.maze[0])
        self.maze_path = []
        
    #para inicar el proceso
    def Start(self):
        self.StartEndPoint()
        # print(self.maze_path)
        return self.maze_path
        
    #obtener el punto donde comienza y donde termina
    #luego utilizarlos para encontrar el camino
    def StartEndPoint(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x] == 9:
                    self.goal.append([x,y])
                elif self.maze[y][x] == 8:
                    self.start.append([x,y])
                    
        # print("goal: ", self.goal)
        # print("start: ", self.start)
        #agregar la posicion inicail como lugar que ya se movio
        self.moved.append(self.start[0])
        #comenzar a analizar su entorno
        self.movement()

    #para realizar la parte del movimiento
    def movement(self):
        for i in range(len(self.moved)):
            # print("path: ", self.moved[i])
            # input()
            #actual position
            if len(self.moved) == 1:
                actual_x=self.moved[len(self.moved)-1][0]
                actual_y=self.moved[len(self.moved)-1][1]
            else:
                actual_x=self.moved[i][len(self.moved[i])-1][0]
                actual_y=self.moved[i][len(self.moved[i])-1][1]
            # print("x: ",actual_x)
            # print("y: ",actual_y)
            # guardar como lugares ya visitados para que no se vuelva a visitar
            self.visited.append([actual_x,actual_y])
            # print("=============")
            
            #revisar si arriba no es un cuadro negro
            if len(self.moved) == 1:
                self.move_copy = self.moved.copy()
            else:
                self.move_copy = self.moved[i].copy()
            self.moved.pop(0)
            copy2 = self.move_copy.copy()
            if actual_y-1 >= 0:
                if self.maze[actual_y-1][actual_x] != 0:
                    if([actual_x,actual_y-1]) not in self.visited:
                        # self.searched.insert(0,[self.moved[len(self.moved)-1][0],self.moved[len(self.moved)-1][1]-1])
                        copy2.append([actual_x,actual_y-1])
                        self.moved.insert(0,copy2)
            
            #revisar si derecha no es un cuadro negro
            copy2 = self.move_copy.copy()
            if actual_x+1 < self.width:
                if self.maze[actual_y][actual_x+1] != 0:
                    if([actual_x+1,actual_y]) not in self.visited:
                        # self.searched.insert(0,[self.moved[len(self.moved)-1][0]+1,self.moved[len(self.moved)-1][1]])
                        copy2.append([actual_x+1,actual_y])
                        self.moved.insert(0,copy2)

            #revisar si abajo no es un cuadro negro
            copy2 = self.move_copy.copy()
            if actual_y+1 < self.height:
                if self.maze[actual_y+1][actual_x] != 0:
                    if([actual_x,actual_y+1]) not in self.visited:
                        # self.searched.insert(0,[self.moved[len(self.moved)-1][0],self.moved[len(self.moved)-1][1]+1])
                        copy2.append([actual_x,actual_y+1])
                        self.moved.insert(0,copy2)
    
            #revisar si izquierda no es un cuadro negro
            copy2 = self.move_copy.copy()
            if actual_x-1 >=0:
                if self.maze[actual_y][actual_x-1] != 0:
                    if([actual_x-1,actual_y]) not in self.visited:
                        # self.searched.insert(0,[self.moved[len(self.moved)-1][0]-1,self.moved[len(self.moved)-1][1]])
                        copy2.append([actual_x-1,actual_y])
                        self.moved.insert(0,copy2)
            
            # for text in self.moved:
            #     print(text)
            
            #revisar si llego a la meta
            for final_goal in self.goal:
                if final_goal in self.moved[i]:
                    print("width: ", self.width)
                    print("height: ", self.height)
                    # print("movement: ", self.moved[i])
                    print("numer of movement: ", len(self.moved[i]))
                    self.maze_path = self.moved[i]
                    self.moved = []

            self.movement()
            break
        
        