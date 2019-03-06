from lane import Lane

class Road:
    def __init__(self, lanes: [Lane] = [], nextRoads: ["Road"] = []) -> None:
        self.lanes = lanes
        self.nextRoads = nextRoads
        pass

    def update(self, timeStep: float) -> None:
        for lane in self.lanes:
            lane.update(timeStep)

    def checkConflict(self, conflictingLanes): #this should be run every time a new car enters a set of conflicting lanes

    @property
    def lanes(self) -> [Lane]:
        return self.__lanes

    @lanes.setter
    def lanes(self, lanes: [Lane]) -> None:
        self.__lanes = lanes

    @property
    def nextRoads(self) -> ["Road"]:
        return self.__nextRoads

    @nextRoads.setter
    def nextRoads(self, nextRoads: ["Road"]) -> None:
        self.__nextRoads = nextRoads
