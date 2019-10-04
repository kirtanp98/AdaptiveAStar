# A* algorithm implementation in python

import heapq
import src.Path.Generator


class Astar:

    def heuristic(self, point1, point2):
        return abs(point1.xPos - point2.xPos) + abs(point1.yPos - point2.yPos)

    def search(self, grid, start, goal):
        frontier = BinaryHeapQueue()
        frontier.put(start, 0)
        cameFrom = {}
        costSoFar = {}
        cameFrom[start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in src.Generator.getNeighbors(grid, current):
                newCost = costSoFar[current] + 1

                if next not in costSoFar or newCost < costSoFar[next]:
                    costSoFar[next] = newCost
                    priority = newCost + self.heuristic(goal, next)
                    frontier.put(next, priority)
                    cameFrom[next] = current

            return cameFrom, costSoFar


class BinaryHeapQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
