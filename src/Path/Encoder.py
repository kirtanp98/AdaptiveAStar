# will convert matrix to a visual textfile

class Encoder:
    def encode(self, matrix, filename, startX, startY, endX, endY):
        # need to add a way specify a location
        rows = len(matrix)
        cols = len(matrix[0])
        f = open(filename, "w+")

        f.write(str(rows) + " " + str(cols)
                + " start("+str(startX) +","+str(startY) + ") end("+str(endX)+","+str(endY) + ")")
        f.write("\n")
        f.write("\n")

        for row in range(rows):
            for col in range(cols):
                state = matrix[row][col]
                if(state.isBlocked()): # 1 represents blocked, while 0 is unblocked
                    f.write("1 ")
                else:
                    f.write("0 ")
            f.write("\n") # linebreak for each row
        f.close()