import random
from .Encoder import Encoder

class Generator:

    def __init__(self):
        print("hello")


    def generateRandomMap(self, x, y, filename):
        matrix= self.__generateMatrix(x,y)

        # randomly selects indices to be the start
        startX = random.randint(0,x-1)
        startY = random.randint(0,y-1)

        # randomly selects indices to be the goal
        goalX = random.randint(0,x-1)
        goalY = random.randint(0,y-1)

        matrix[startX][startY] = 'S'
        matrix[goalX][goalY] = 'F'

        encoder = Encoder()

        self.__randomizeMap(matrix)
        encoder.encode(matrix, filename)
        self.__printMatrix(matrix)



    # simply returns a matrix of x by y. Also init all of them to be 0
    def __generateMatrix(self, x, y):
        n = x
        m = y
        matrix = [0] * n
        for row in range(n):
            matrix[row] = [0] * m
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
                # this ensures that it skips over the start & goal states 'S','F'
                if matrix[row][col] == 0:
                    # if randomProb > 3 then it is unblocked (this ensures a 70% probability)
                    randomProbability = random.randint(1,10)

                    if randomProbability <= 3: # 30% chance to get <= 3 out of 10.
                        matrix[row][col] = 1 # 1 indicates the path is blocked
        return matrix


