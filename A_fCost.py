from math import *

class A_FCOST:
    
    def __init__(self,maze):
        self.maze = maze
        self.surrounding = []
        self.moved = []
        self.temporal_moved=[]
        self.visited=[]
        self.goal=[]
        self.start = []
        self.move_copy = []
        self.height = len(self.maze)
        self.width = len(self.maze[0])
        self.maze_path = []
        self.Fcost = []
        self.goalDist=[]
        self.searched=[]
        self.Fmin = 0
       
    def Start(self):
        self.StartEndPoint()
        
    
    #obtener sus posiciones de start y end
    def StartEndPoint(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x] == 9:
                    self.goal.append([x,y])
                elif self.maze[y][x] == 8:
                    self.start.append([[x,y]])
                    
        print("goal: ", self.goal)
        print("start: ", self.start)
        #agregar la posicion inicail como lugar que ya se movio
        self.moved.append(self.start[0])
        #comenzar a analizar su entorno
        self.movement()
        self.fCostAnalize()
        
    def movement(self):
        print("========================================================================")
        for mov in self.moved:
            print("moved: ", mov)  
        for i in range(len(self.moved)):
            
            #actual position
            actual_x=self.moved[i][len(self.moved[i])-1][0]
            actual_y=self.moved[i][len(self.moved[i])-1][1]
            self.visited.append([actual_x,actual_y])
            self.move_copy = self.moved[i].copy()
            print("visited points: ",self.visited)
            print("coy of move: ", self.move_copy)
            print("actual position: ",[actual_x,actual_y])
            for endGoal in self.goal:
                if endGoal in self.moved[i]:
                    print("respuesta final: ", self.moved[i])
                    print("largo: ", len(self.moved[i]))
                    return self.moved[i]
                    
            
            #revisar si arriba no es un cuadro negro
            if actual_y-1 >= 0:
                if self.maze[actual_y-1][actual_x] != 0:
                    if([actual_x,actual_y-1]) not in self.visited and ([actual_x,actual_y-1]) not in self.searched:
                        self.surrounding.append([actual_x,actual_y-1])
                        self.searched.append([actual_x,actual_y-1])
                        
            #revisar si arriba derecha no es un cuadro negro
            if actual_y-1 >= 0 and actual_x+1 < self.width:
                if self.maze[actual_y-1][actual_x+1] != 0:
                    if([actual_x+1,actual_y-1]) not in self.visited and ([actual_x+1,actual_y-1]) not in self.searched:
                        self.surrounding.append([actual_x+1,actual_y-1])
                        self.searched.append([actual_x+1,actual_y-1])
            
            #revisar si derecha no es un cuadro negro
            if actual_x+1 < self.width:
                if self.maze[actual_y][actual_x+1] != 0:
                    if([actual_x+1,actual_y]) not in self.visited and ([actual_x+1,actual_y]) not in self.searched:
                        self.surrounding.append([actual_x+1,actual_y])
                        self.searched.append([actual_x+1,actual_y])
                        
            #revisar si derecha inferior no es un cuadro negro
            if actual_x+1 < self.width and actual_y + 1 < self.height:
                if self.maze[actual_y+1][actual_x+1] != 0:
                    if([actual_x+1,actual_y+1]) not in self.visited and ([actual_x+1,actual_y+1]) not in self.searched:
                        self.surrounding.append([actual_x+1,actual_y+1])
                        self.searched.append([actual_x+1,actual_y+1])
                        
            #revisar si abajo no es un cuadro negro
            if actual_y+1 < self.height:
                if self.maze[actual_y+1][actual_x] != 0:
                    if([actual_x,actual_y+1]) not in self.visited and ([actual_x,actual_y+1]) not in self.searched:
                        self.surrounding.append([actual_x,actual_y+1])
                        self.searched.append([actual_x,actual_y+1])
                        
            #revisar si abajo izquierda no es un cuadro negro
            if actual_y+1 < self.height and actual_x-1 >= 0:
                if self.maze[actual_y+1][actual_x-1] != 0:
                    if([actual_x-1,actual_y+1]) not in self.visited and ([actual_x-1,actual_y+1]) not in self.searched:
                        self.surrounding.append([actual_x-1,actual_y+1])
                        self.searched.append([actual_x-1,actual_y+1])
    
            #revisar si izquierda no es un cuadro negro
            if actual_x-1 >=0:
                if self.maze[actual_y][actual_x-1] != 0:
                    if([actual_x-1,actual_y]) not in self.visited and ([actual_x-1,actual_y]) not in self.searched:
                        self.surrounding.append([actual_x-1,actual_y])
                        self.searched.append([actual_x-1,actual_y])
            
            #revisar si izquierda superior no es un cuadro negro
            if actual_x-1 >=0 and actual_y-1>=0:
                if self.maze[actual_y-1][actual_x-1] != 0:
                    if([actual_x-1,actual_y-1]) not in self.visited and ([actual_x-1,actual_y-1]) not in self.searched:
                        self.surrounding.append([actual_x-1,actual_y-1])
                        self.searched.append([actual_x-1,actual_y-1])
                        
            print("alderedores: ", self.surrounding)
            print("buscados: ", self.searched)
            
            self.fCostAnalize()
            
            if type(self.Fcost[0] != list):
                self.Fmin = min(self.Fcost)
                        
                for find in range(len(self.Fcost)):
                    if self.Fcost[find] == self.Fmin:
                        if self.searched[find] not in self.visited:
                            copy2 = self.move_copy.copy()
                            copy2.append(self.searched[find])
                            self.temporal_moved.insert(0,copy2)
                            self.visited.append(self.searched[find])

            else:
                #esto es solo por el momento
                pass
            # print("moved: ", self.moved)    
            print("minimo es: ",self.Fmin)
            for less in range(len(self.Fcost)):
                if self.Fcost[less] == self.Fmin:
                    if self.searched[less] not in self.visited:
                        print("los puntos minimos: ",self.searched[less])
            print("Fcost: ", self.Fcost)
            # input()
            
            
            self.surrounding=[]
        
        self.moved = self.temporal_moved
        self.temporal_moved = []
        self.movement()
            
    def fCostAnalize(self):
        #se va a calcular el valor G y H para obtener el valor F de cada nodo
        # print()
        for x in self.surrounding:
            # print("node: ", x)
            #calcular G
            G = dist(x,self.start[0][0])
            #calcular H
            if len(self.goal) > 1:
                temporal_list = []
                for end in self.goal:
                    H = dist(x,end)
                    temporal_list.append(H)
                self.goalDist.append(temporal_list)
            else:
                H = dist(x,self.goal[0])
                self.goalDist.append(H)
            #calcular F
            # print("G value: ", G)
            # print("H value: ", self.goalDist)
            if (type(self.goalDist[0]) == list):
                F1 = G + self.goalDist[0][0]
                F2 = G + self.goalDist[0][1]
                temporal_list = []
                temporal_list.append(round(F1))
                temporal_list.append(round(F2))
                self.Fcost.append(temporal_list)
            else:
                F = G + self.goalDist[0]
                self.Fcost.append(round(F))
            self.goalDist.pop(0)
            # print("Fcost: ", self.Fcost)
            
            # print("================================")
            
            
        

        