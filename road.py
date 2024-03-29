from lane import Lane

class Road:
    def __init__(self, lanes: [Lane] = None, nextRoads: ["Road"] = None) -> None:
        self.lanes = lanes
        self.nextRoads = nextRoads
        pass

    def update(self, timeStep: float) -> None:
        for lane in self.lanes:
            lane.updatePositions(timeStep)

    @property
    def lanes(self) -> [Lane]:
        return self.__lanes

    @lanes.setter
    def lanes(self, lanes: [Lane]) -> None:
        if lanes == None:
            self.__lanes = []
        elif type(lanes) != list:
            raise TypeError("Expected list of Lane")
        elif any(type(i) != Lane for i in lanes):
            raise TypeError("Expected list of Lane")
        else:
            self.__lanes = lanes

    @property
    def nextRoads(self) -> ["Road"]:
        return self.__nextRoads

    @nextRoads.setter
    def nextRoads(self, nextRoads: ["Road"]) -> None:
        if nextRoads == None:
            self.nextRoads = []
        else:
            self.__nextRoads = nextRoads
