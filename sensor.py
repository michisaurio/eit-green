import random


class Sensor:
    # Sensor base class. All other inherit from this one.
    # All sensors have an id and a global position on the map
    # all sensors have a detection rate

    def __init__(self, id: int, position: [float, float], detectRate: float, count: int):
        self.id = id
        self.position = position
        self.detectRate = detectRate
        self.count = count

    def isDetected(self, detectRate) -> bool:
        r = random.random()
        if r <= detectRate:
            return True
        return False

    def resetCount(self):
        self.count = 0

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def position(self) -> [float, float]:
        return self.__position

    @position.setter
    def position(self, position: [float, float]) -> None:
        self.__position = position

    @property
    def detectRate(self) -> float:
        return self.__detectRate

    @detectRate.setter
    def detectRate(self, detectRate: float) -> None:
        self.__detectRate = detectRate

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count


class InductionLoop(Sensor):

    def __init__(self, id, position, detectRate=0.9, count=0):
        super().__init__(id, position, detectRate, count)

    # check if a car crosses a lane
    def incrementCount(self, command):
        # ...
        if (self.isDetected()):
            self.count += 1
        # ...


    # assuming that this method gets called by another object after traffic lights change

# test:
# s = InductionLoop(id = 1, position = [0,0], detectRate = 0.9)
# import json
# print(json.dumps(s,
#                 default=lambda obj: vars(obj),
#                 indent=1))
