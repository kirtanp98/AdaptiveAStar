class State:
    xPos = None
    yPos = None
    parent = None
    blocked = False
    explored = False # so we don't continuously visit the same node
    gVal = 0
    hVal = 0
    fVal = 0


    def isBlocked(self):
        return self.blocked

    def isExplored(self):
        return self.explored

    def inBound(self, width, height):
        x = self.xPos
        y = self.yPos

        result = 0 <= x < width and 0 <= y < height
        return result


