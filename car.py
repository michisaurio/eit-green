from random import uniform
from lane import Lane
from math import sin, cos
from typing import List

class Car:
    # A car needs to have an id, position and speed

    def __init__(self, id: int, position: [float,float] = [0,0], velocity: float = 0, course: float = 0, state = None, lane: Lane = None, reactionTime: float = 1.5) -> None:
        self.id = id
        self.position = position
        self.velocity = velocity
        self.course = course #intermediate angle between car and surroundings
        self.state = state
        self.lane = lane
        self.reactionTime = reactionTime

    def updatePosition(self, timeStep):
        Ka = 1 # acceleration constant [1/s]
        if self.state is 'aloneOnLane':
            self.velocity = self.velocity + timeStep*Ka*(self.lane.maxVelocity - self.velocity)
            if self.lane.type is 'straightLane':
                self.position = self.position + timeStep*self.velocity*[cos(self.course), sin(self.course)]
            elif self.lane.type is 'curvedLane':
                self.course = self.course + timeStep*self.velocity/self.lane.radius
                self.position = self.position + timeStep*self.velocity*[cos(self.course), sin(self.course)]
        elif self.state is 'behindACar':
            pass

        elif self.state is 'Stop':
            pass
            

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
    def referance_velocity(self) -> float:
        return self.__referance_velocity

    @referance_velocity.setter
    def referance_velocity(self, referance_velocity):
        self.__referance_velocity = referance_velocity

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
