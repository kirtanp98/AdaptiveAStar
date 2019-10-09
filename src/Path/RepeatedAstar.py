import heapq
import src.Path.Generator


class RepeatedAstar:

    matrix = None
    openSet = None
    closeSet = []
    counter = 0
    goal = None
    tester = 0

    # Init heap here
    def __init__(self):
        self.openSet = BinaryHeapQueue()


    def heuristic(self, point1, point2):  # this is the heuristic function that calculates the manhattan distance
        return abs(point1.xPos - point2.xPos) + abs(point1.yPos - point2.yPos)

    def computePath(self):
        gen = src.Path.Generator.Generator()

        while len(self.openSet.elements) and self.goal.gVal > self.openSet.peek().fVal:
            tempState = self.openSet.get()
            self.closeSet.append(tempState)

            for neighbors in gen.getNeighbors(self.matrix, tempState):
                #self.tester += 1
                #print(self.tester)
                if neighbors.blocked:  # if blocked, we put it in the open list with a large fVal
                    neighbors.fVal = 9999999
                    self.openSet.put(neighbors)
                else:
                    if neighbors.explored:
                        continue
                    else:
                        neighbors.gVal = tempState.gVal + 1

                        if neighbors in self.openSet.elements:
                            self.openSet.elements.remove(neighbors)
                        neighbors.explored = True
                        neighbors.hVal = self.heuristic(self.goal, neighbors)
                        neighbors.fVal = neighbors.gVal + neighbors.hVal
                        neighbors.parent = tempState
                        self.openSet.put(neighbors)



    def repeatedAstar(self, start, goal):
        counter = 0
        #
        # for x in matrix[][]:
        #     x.search=0
        reachedTarget = True

        while start != goal:
            print("here")
            self.counter += 1
            start.gVal = 0
            start.search = counter
            goal.gVal = 9999998 # this value is going to be one less lower than the blocked units
            goal.search = counter
            self.closeSet = []
            start.hVal = self.heuristic(start, goal)
            start.fVal = start.gVal + start.hVal
            self.openSet.put(start)

            self.computePath()

            if len(self.openSet.elements) == 0:
                print("Did not reach the target")
                reachedTarget = False
                break

            agent = start
            while agent is not None:
                agent = start.parent

            start = agent
            #move the agent to where the start state
            #Set the start state to the current agent
            #if the agent is not at the goal state then that means

        if reachedTarget:
            print("Reached Target")


class BinaryHeapQueue: # priority queue implementation
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item):
        heapq.heappush(self.elements, item)

    def get(self):
        return heapq.heappop(self.elements)

    def peek(self):
        return self.elements[0]


