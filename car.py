from random import uniform
from lane import Lane
from typing import List
class Car:
    # A car needs to have an id, position and speed

    def __init__(self, id: int, position: [float,float] = [0,0], velocity: float = 0, course: float = 0, lane: Lane = None, reactionTime: float = 1.5) -> None:
        self.id = id
        self.position = position
        self.velocity = velocity
        self.course = course #intermediate angle between car and surroundings
        self.lane = lane
        self.reactionTime = reactionTime

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity

    @property
    def reactionTime(self):
        return self.__reactionTime

    @reactionTime.setter
    def reactionTime(self, reactionTime):
        self.__reactionTime = reactionTime

    @property
    def lane(self):
        return self.__lane

    @lane.setter
    def lane(self, lane):
        self.__lane = lane

    # TODO: We could add types of cars, and thus have pictures that match them. Size might also be needed