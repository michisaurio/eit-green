class Lane:

    def __init__(self, id, startPos, endPos, nextLane = None):
        # If nextLane is None it should mean that this is an end lane.
        # Should lanes be renamed something else?
        # Type of nextlane should be what?
        self.id = id
        self.nextLane = nextLane
        self.startPos = startPos
        self.endPos = endPos

    def getPosition(self):
        #Returns a tuple
        return self.startPos, self.endPos

    #