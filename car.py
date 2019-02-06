from random import uniform
class Car:
    reactionTime = 3
    # A car needs to have an id, position and speed

    def __init__(self, id, position, velocity = (0,0), lane = None):
        self.id = id
        self.position = position
        self.velocity = velocity
        self.reactionTime = uniform(1,self.reactionTime)
        self.lane = lane

    def getVelocity(self):
        return self.velocity

    def setVelocity(self, velocity):
        self.velocity = velocity

    def getPosition(self):
        return self.position

    def setPosition(self, postion):
        self.position = postion

    def getReactionTime(self):
        return self.reactionTime

    def setReactionTime(self, reactionTime):
        self.reactionTime = reactionTime

    def getLane(self):
        return self.lane

    def setLane(self, lane):
        self.lane = lane

    # TODO: We could add types of cars, and thus have pictures that match them. Size might also be needed