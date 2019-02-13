class Lane:
    def __init__(self, id: int, startPos: int, endPos: int, nextLane = None) -> None:
        # If nextLane is None it should mean that this is an end lane.
        # Should lanes be renamed something else?
        # Type of nextlane should be what?
        self.id = id
        self.nextLane = nextLane
        self.startPos = startPos
        self.endPos = endPos
        #TODO This class is very undone