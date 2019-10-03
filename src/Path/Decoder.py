# will convert textfile to a matrix of the size specified on top


class Decoder:
    def decode(self,filename):
        f = open(filename, "r")

        line = f.readline()
        print(line)
