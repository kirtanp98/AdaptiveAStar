
class Generator:

    def __init__(self):
        print("hello")


    def generateRandomMap(self, x, y, filename):
        #first want to generate a matrix[x][y]
        matrix= self.generateMatrix(x,y)




    # simply returns a matrix of x by y
    def __generateMatrix(self, x, y):
        n = x
        m = y
        matrix = [0] * n
        for row in range(n):
            matrix[row] = [0] * m
        return matrix