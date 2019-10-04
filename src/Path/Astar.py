# A* algorithm implementation in python

import heapq
import src.Path.Generator


# might want to make these functions static later because we don't need to make an object
# still need to set the values in the cells, and make the function actual work
class Astar:

    def heuristic(self, point1, point2):  # this is the heuristic function that calculates the manhattan distance
        return abs(point1.xPos - point2.xPos) + abs(point1.yPos - point2.yPos)

    def search(self, grid, start, goal): # actual a* search method
        frontier = BinaryHeapQueue() # priority queue
        frontier.put(start, 0) # frontier is basically going through the grid and getting the cells in to the queue
        cameFrom = {} # path from start to goal
        costSoFar = {} # cost
        cameFrom[start] = None
        costSoFar[start] = 0

        gen = src.Path.Generator.Generator()


        while not frontier.empty(): # the actual path searching
            current = frontier.get()

            if current == goal: # when it gets to the goal the loop will break
                break

            for next in gen.getNeighbors(grid, current): # getting the neighbors
                newCost = costSoFar[current] + 1 # because its a grid, the cost to go to another cell is just 1

                if next not in costSoFar or newCost < costSoFar[next]:
                    costSoFar[next] = newCost
                    priority = newCost + self.heuristic(goal, next)
                    frontier.put(next, priority)
                    cameFrom[next] = current

            return cameFrom, costSoFar # returns the path and cost


class BinaryHeapQueue: # priority queue implementation
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
