class InductionLoop(Sensor):

  def __init__(self, id, position, detectRate = 0.9, count = 0):
     self.id = id
     self.position = position
     self.detectRate = detectRate
     self.count = count

  # should be called when a car crosses the position
  def incrementCount(command):
      isDetected(detectRate)

  # assuming that this method gets called by another object after traffic lights change
  def resetCount():
      count = 0

  @property
  def detectRate(self) -> float:
      return self.__detectRate

  @detectRate.setter
  def detectRate(self, detectRate) -> None:
      self.__detectRate = id

  @property
  def count(self) -> int:
      return self.__count

  @count.setter
  def count(self, count) -> int:
      self.__count = count
