# will convert matrix to a textfile

class Encoder:
    def encode(self, matrix, filename):
        # need to add a way specify a location
        rows = len(matrix)
        cols = len(matrix[0])
        f = open(filename, "w+")

        for row in range(rows):
            for col in range(cols):
                f.write(str(matrix[row][col]))
                f.write(" ")

            f.write("\n") # linebreak for each row
        f.close()