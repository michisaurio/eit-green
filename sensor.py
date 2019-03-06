import random

class Sensor:
  # Sensor base class. All other inherit from this one.
  # All sensors have an id and a global position on the map
  # all sensors have a detection rate

    def __init__(self, id: int, position: [float, float], detectRate: float):
        self.id = id
        self.position = position
        self.detectRate = detectRate

    def isDetected(detectRate) -> bool:
        r = random.random()
        if r <= detectRate:
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


class InductionLoop(Sensor):

  def __init__(self, id, position, detectRate = 0.9, count = 0):
     self.id = id
     self.position = position
     self.detectRate = detectRate
     self.count = count

  # check if a car crosses a lane
  def incrementCount(command):
      # ...
      isDetected(detectRate)
      # ...

  # assuming that this method gets called by another object after traffic lights change
  def resetCount():
      count = 0

  @property
  def count(self) -> int:
      return self.__count

  @count.setter
  def count(self, count) -> int:
      self.__count = count


# test:
#s = InductionLoop(id = 1, position = [0,0], detectRate = 0.9)
#import json
#print(json.dumps(s,
#                 default=lambda obj: vars(obj),
#                 indent=1))
