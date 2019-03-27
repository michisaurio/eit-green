
class Sensor:
    # Sensor base class. All other inherit from this one.
    # All sensors have an id and a global position on the map
    # all sensors have a detection rate
    numberOfSensors = 1
    def __init__(self, startParameter: float, endParameter: float, lane):
        self.id = Sensor.numberOfSensors
        self.startParameter = startParameter
        self.endParameter = endParameter
        self.lane = lane

    def getSensorSignal(self) -> bool:
        return self.lane.getSensorSignal(self.startParameter, self.endParameter)

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id
        Sensor.numberOfSensors += 1

    @property
    def startParameter(self) -> float:
        return self.__startParameter

    @startParameter.setter
    def startParameter(self, startParameter: float) -> None:
        if not isinstance(startParameter, (float, int)):
            raise TypeError("Expected float")
        self.__startParameter = startParameter

    @property
    def endParameter(self) -> float:
        return self.__endParameter

    @endParameter.setter
    def endParameter(self, endParameter: float) -> None:
        if not isinstance(endParameter, (float, int)):
            raise TypeError("Expected float")
        self.__endParameter = endParameter

    @property
    def lane(self):
        return self.__lane

    @lane.setter
    def lane(self, lane):
        self.__lane = lane