import random

class Sensor:
    # Sensor base class. All other inherit from this one.
    # All sensors have an id and a global position on the map
    # all sensors have a detection rate

    def __init__(self, id: int, position: [float, float], detectRate: float, count: int):
        self.id = id
        self.position = position
        self.detectRate = detectRate

    def isDetected(self) -> bool:
        r = random.random()
        if r <= self.detectRate:
            return True
        return False

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

class InductionLoopCounter(Sensor):

    def __init__(self, id, position, length = 1.85, width = 1.85, detectRate=0.9, count=0):
        super().__init__(id, position, detectRate, count)

        self.length = length
        self.width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    # check if a car crosses a lane
    # lane knows where loop is located. Triggers this method if car enters loop's inner area
    # then there's a probabiblity that car is detected. If it is, increment count.
    def incrementCount(self):
        # ...
        if (self.isDetected()):
            self.count += 1
        # ...

    def resetCount(self):
        self.count = 0

class InductionLoopPresence(Sensor):
    def __init__(self, id, position, width, length, detectRate=0.9):
        super().__init__(id, position, detectRate)

        self.length = length
        self.width = width

        @property
        def length(self):
            return self.__length

        @length.setter
        def length(self, length):
            self.__length = length

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width

class InductionLoopPassing(Sensor):
    def __init__(self, id, position, width, length, detectRate=0.9, luke_time = 3):
        super().__init__(id, position, detectRate)

        self.length = length
        self.width = width
        self.luke_time = luke_time

        @property
        def length(self):
            return self.__length

        @length.setter
        def length(self, length):
            self.__length = length

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width

        @property
        def luke_time(self):
            return self.__luke_time

        @luke_time.setter
        def luke_time(self, luke_time):
            self.__luke_time = luke_time

# test:
# s = InductionLoop(id = 1, position = [0,0], detectRate = 0.9)
# import json
# print(json.dumps(s,
#                 default=lambda obj: vars(obj),
#                 indent=1))
