# A* algorithm implementation in python

import heapq
import src.Path.Generator


# might want to make these functions static later because we don't need to make an object
# still need to set the values in the cells, and make the function actual work
class Astar:

    tiebreaker = False

    def heuristic(self, point1, point2):  # this is the heuristic function that calculates the manhattan distance
        return abs(point1.xPos - point2.xPos) + abs(point1.yPos - point2.yPos)

    def search(self, grid, start, goal): # actual a* search method
        frontier = BinaryHeapQueue() # priority queue
        frontier.put(start) # frontier is basically going through the grid and getting the cells in to the queue
        cameFrom = {} # path from start to goal
        costSoFar = {} # cost
        cameFrom[start] = None
        costSoFar[start] = 0

        gen = src.Path.Generator.Generator()


        while not frontier.empty(): # the actual path searching
            current = frontier.get()
            current.explored = True  # so we do not visit the same node again

            if current.isBlocked(): #ignore the blocked states
                continue
            if current == goal:# when it gets to the goal the loop will break
                print("Found goal!")
                return goal

            for neighbor in gen.getNeighbors(grid, current): # getting the neighbors
                newCost = costSoFar[current] + 1 # because its a grid, the cost to go to another cell is just 1

                if neighbor not in costSoFar or newCost < costSoFar[neighbor]:
                    costSoFar[neighbor] = newCost
                    neighbor.gVal = newCost
                    neighbor.hVal = self.heuristic(goal, neighbor)
                    neighbor.fVal = neighbor.gVal + neighbor.hVal
                    # tie breaker code - testing - without a tie breaker a* will be slow
                    # comment out code to disable tie breaker
                    if self.tiebreaker:
                        temp = (2*neighbor.fVal)-neighbor.gVal
                        neighbor.fVal = temp

                    frontier.put(neighbor)
                    neighbor.parent = current
                    #cameFrom [neighbor] = current
        print("Can not reach goal!")
        return None


class BinaryHeapQueue: # priority queue implementation
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item):
        heapq.heappush(self.elements, item)


    def get(self):
        return heapq.heappop(self.elements)
