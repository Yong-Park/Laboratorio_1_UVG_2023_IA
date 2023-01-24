from framework import Framework
import math

class DegreeAstar(Framework):

    def __init__(self, maze):
        self.maze = maze
        self.width, self.height = len(maze), len(maze)
        self.ending = []
        self.start = None
        self.came_from = None
        self.paths = []
        self.visited = []
        self.road = []

    def results(self):
        return self.visited, self.road

    def step(self):
        for cost in range(len(self.costs)):
            if ((self.neighbors[cost] not in self.visited) and (self.costs[cost] == self.minimal_cost)):
                self.paths.append(self.neighbors[cost])
                self.visited.append(self.neighbors[cost])
                self.came_from[self.neighbors[cost]] = self.current

    def surrounding(self, position):

        possible_positions = []
        x, y = position
        left, right, up, down = (x - 1), (x + 1), (y - 1), (y + 1)

        if ((left >= 0) and (self.maze[y][left] != 0)):
            possible_positions.append((left, y))
        if ((right < self.width) and (self.maze[y][right])):
            possible_positions.append((right, y))
        if ((up >= 0) and (self.maze[up][x] != 0)):
            possible_positions.append((x, up))
        if ((down < self.height) and (self.maze[down][x] != 0)):
            possible_positions.append((x, down))

        return possible_positions

    def stepCost(self, paths):

        cost_values = []
        nodes = paths

        for node in nodes:
            G = math.dist(self.start, node)
            H = []
            points = []
            for point in self.ending:
                x, y = abs((point[0] - node[0])), abs((point[1] - node[0]))
                points.append((x, y))
                h = math.atan2(point[1], point[0])
                H.append(h)
            F = round(G + min(H))
            cost_values.append(F)
        return cost_values

    def goal(self):
        if self.current in self.ending:
            self.road = []
            while self.current != self.start:
                self.road.append(self.current)
                self.current = self.came_from[self.current]
            self.road = self.road[::-1]

    def actions(self):
        for y in range(self.height):
            for x in range(self.width):
                if (self.maze[y][x] == 8):
                    self.start = (x, y)
                elif (self.maze[y][x] == 9):
                    self.ending.append((x, y))

        self.paths.append(self.start)
        self.visited.append(self.start)
        self.came_from = { self.start: None }

        while (self.paths):
            self.current =  self.paths.pop(0)
            self.goal()
            self.neighbors = self.surrounding(self.current)
            self.costs = self.stepCost(self.neighbors)

            for costIndex in range(len(self.costs)):
                if (self.neighbors[costIndex] in self.visited):
                    self.costs[costIndex] = 999_999

            self.minimal_cost = min(self.costs)
            self.step()
