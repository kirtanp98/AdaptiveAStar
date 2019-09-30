import random
from .Encoder import Encoder
from .State import State

#Global variables
startState = None
goalState = None

class Generator:

    def __init__(self):
        print("hello")


    def generateRandomMap(self, x, y, filename):
        matrix= self.__generateMatrix(x,y)

        # randomly selects indices to be the start
        startX = random.randint(0,x-1)
        startY = random.randint(0,y-1)
        startState = matrix[startX][startY]

        # randomly selects indices to be the goal
        goalX = random.randint(0,x-1)
        goalY = random.randint(0,y-1)
        goalState = matrix[goalX][goalY]

        encoder = Encoder()

        #self.__randomizeMap(matrix)
        #encoder.encode(matrix, filename)
        self.__printMatrix(matrix)
        return matrix



    # simply returns a matrix of x by y. Also init all of them to be 0
    def __generateMatrix(self, x, y):
        n = x
        m = y
        matrix = [State()] * n
        for row in range(n):
            matrix[row] = [State()] * m # each row will have the same object, fixed in bottom code

        # Assign a new state person position & fill out its x,y attribute
        for row in range(n):
            for col in range(m):
                matrix[row][col] = State() # new state person space
                state = matrix[row][col]
                state.xPos = row
                state.yPos = col
        return matrix

    def __printMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            print(matrix[row])

    def __randomizeMap(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                currentState = matrix[row][col]
                if currentState != startState or currentState != goalState: #skip start or goal states
                    # if randomProb > 3 then it is unblocked (this ensures a 70% probability)
                    randomProbability = random.randint(1,10)
                    print(randomProbability)
                    if randomProbability <= 3:  # 30% chance to get <= 3 out of 10. 30% to block a path
                        print("Trigg: " + str(randomProbability))
                        currentState.blocked = True  # 1 indicates the path is blocked
        return matrix


