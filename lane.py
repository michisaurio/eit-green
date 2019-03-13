from light import Light
from color import Color
import numpy as np

class Lane:
    def __init__(self, coordinates, speedLimit, light: Light = None, curveType="line", spawnRate=0.0, queue=0,
                 isMerge=False) -> None:
        self.coordinates = coordinates  # Start and end coordinates in a list [x.start, y.start, x.end, y.end]. For mergelanes, these are the coordinates of the straight lane.
        self.cars = []  # List with tuples of cars in the lane and their critical distance(car, criticalDistance). Assumed topologically sorted such that the first element is the frontmost car in the lane.
        self.speedLimit = speedLimit
        self.light = light
        self.curveType = curveType #String specifying if the curve is an ellipsis, line, laneswitch or merge
        self.length = 0
        self.spawnRate = spawnRate
        self.__queue = queue #Let the constructor overload the setter method to make sure that the queue exists
        self.isMerge = isMerge  # TODO: implement getters and setters
        xLength = abs(coordinates[2] - coordinates[0])
        yLength = abs(coordinates[3] - coordinates[1])
        if(curveType == "line" or curveType == "merge"):
            if(xLength == 0):
                self.length = yLength
            else:
                self.length = xLength
        elif (curveType == "ellipsis"):
            h = (xLength - yLength) ** 2 / (
                    xLength + yLength) ** 2  # mathematical parameter only used to simplify expression below
            self.length = 0.25 * np.pi * (xLength + yLength) * (1 + (3 * h) / (10 + np.sqrt(
                4 - 3 * h)))  # formula is 1/4 times an approximation of the perimeter of an ellipse, see https://www.mathsisfun.com/geometry/ellipse-perimeter.html

    def updatePositions(self, timeStep) -> None: #TODO: take mergelane updating of position into consideration

        if (self.spawnRate * timeStep > np.random.uniform(0, 1)):
            self.queue += 1
        if self.queue > 0:  # and there is space
            self.spawn()

        for i in range(len(self.cars)):
            # TODO: This is where the car should drive and check for collision etc
            (currentCar, criticalDistance) = self.cars[i]
            if criticalDistance > 2 * currentCar.speed * currentCar.comfortabilityConstant: #TODO: Tune this threshold
                acceleration = currentCar.accelerationConstant*(self.speedLimit - currentCar.speed)
            else:
                acceleration = currentCar.distanceConstant * criticalDistance - currentCar.speedConstant * currentCar.speed
            speed = currentCar.speed + timeStep * acceleration
            currentCar.speed = max(0, min(speed, self.speedLimit))  # Add random number to speedLimit
            [x, y, vs] = curve(currentCar.lane, currentCar.parameter)
            currentCar.parameter = currentCar.parameter + timeStep * currentCar.speed / vs
            [x, y, vs] = curve(currentCar.lane, currentCar.parameter)
            currentCar.position = [x, y]

            # Check if car is in new road/lane. Update topological sorting.
            if (currentCar.curveType == "line" and currentCar.parameter > self.length) or (
                    currentCar.curveType == "ellipsis" and currentCar.parameter > np.pi / 2):
                currentCar.parameter = 0
                currentCar.nextLane.cars.append((currentCar, 0))
                if currentCar.nextLane.isMerge:
                    currentCar.nextLane.updateTopologicalSorting()  # should remove the car from its own lane and put it in merge
                currentCar.lane = currentCar.nextLane
                currentCar.nextLane = None  # TODO: give the car a proper nextLane
                self.cars.pop(0)

    def updateTopologicalSort(self):
        sortedCars = []
        for i in range(len(self.cars)):  # updateTopologicalSorting, should only trigger for mergeLanes
            currentCar = self.cars[i][0]
            sortingParameter = self.length - currentCar.parameter
            if currentCar.lane == "ellipsis":
                sortingParameter = project(self, currentCar)
            sortedCars.append((currentCar, sortingParameter))
        sortedCars.sort(key=lambda tup: tup[1])
        self.cars = sortedCars

    def updateCriticalDistance(self):
        if len(self.cars) == 0:
            return
        if self.light.color == Color.RED:
            self.cars[0][1] = self.length - self.cars[0][0].parameter
        elif len(self.cars[0][0].nextLane.cars) == 0:
            self.cars[0][1] = np.inf
        else:
            currentCar = self.cars[0][0]
            currentLaneCriticalDistance = self.length - self.cars[0][0].parameter
            if currentCar.lane.curveType == "ellipsis":
                currentLaneCriticalDistance = project(self, currentCar)
            if currentLaneCriticalDistance > 2*currentCar.speed*currentCar.comfortabilityConstant:
                self.cars[0][1] = currentLaneCriticalDistance
                pass
            nextCar = currentCar.nextLane.cars[-1][0]
            nextLaneCriticalDistance = nextCar.parameter - currentCar.comfortabilityConstant * currentCar.speed  # how far the next car has travelled from the start of the next lane
            if currentCar.nextLane.curveType == "ellipsis":
                nextLaneCriticalDistance = currentCar.nextLane.length * nextCar.parameter * 2 / (np.pi)  # length of the next car from starting point = length of lane * current angle of car / ending angle of lane
            self.cars[0][1] = (currentLaneCriticalDistance + nextLaneCriticalDistance)

        nextCar = self.cars[0][0]
        nextParameter = nextCar.parameter
        if nextCar.lane.curveType == "ellipsis":
            nextParameter = nextCar.lane.length - project(self, nextCar)
        for i in range(1, len(self.cars)):
            currentCar = self.cars[i][0]
            currentParameter = currentCar.parameter
            if currentCar.lane.curveType == "ellipsis":
                currentParameter = currentCar.lane.length - project(self, currentCar)
            self.cars[i][1] = nextParameter - currentParameter - currentCar.comfortabilityConstant * currentCar.speed
            nextParameter = currentParameter


    def spawn(self):
        # TODO: Spawn a new car at the start of the lane if possible
        # REMEMBER TO DECREASE QUEUE !!!!!
        pass


    def desiredSpeed(self):
        pass

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates

    @property
    def cars(self):
        return self.__cars

    @cars.setter
    def cars(self, cars) -> None:
        self.__cars = cars

    @property
    def speedLimit(self) -> int:
        return self.__speedLimit

    @speedLimit.setter
    def speedLimit(self, speedLimit) -> None:
        self.__speedLimit = speedLimit


    @property
    def light(self) -> Light:
        return self.__light

    @light.setter
    def light(self, light: Light):
        self.__light = light

    @property
    def curveType(self):
        return self.__curveType

    @curveType.setter
    def curveType(self, curveType: str):
        self.__curveType = curveType

    @property
    def spawnRate(self):
        return self.__spawnRate

    @spawnRate.setter
    def spawnRate(self, spawnRate):
        self.__spawnRate = spawnRate

    @property
    def queue(self):
        return self.__queue

    @queue.setter
    def queue(self, queue):
        if queue < 0:
            print("WARNING: You tried to set the queue to less than 0")
        elif (queue == self.queue - 1 or queue == self.queue + 1):
            self.__queue = queue
        else:
            print("WARNING: You tried to change queue by more than 1")

    # TODO: How should we implement this? What is the type of curve?


def project(mergeLane, car):
    velocityProportionalityConstant = mergeLane.speedLimit / car.lane.speedLimit  # Not the best approximation
    carPosition = mergeLane.length - car.parameter * 2 / (
        np.pi) * car.lane.length * velocityProportionalityConstant  # The length of car.lane is an approximation, and we approximate the distance
    return carPosition  # travelled by the car as the percentage of the total angle(angle goes between 0 and pi/2 travelled multiplied with the length

def curve(lane, parameter):
        # Parametric equation function. Takes in parameter s and returns x and y coordinates and derivative of s.
        xLength = lane.coordinates[2] - lane.coordinates[0]
        yLength = lane.coordinates[3] - lane.coordinates[1]
        x = 0
        y = 0
        vs = 0
        if lane.curveType == "line":
            if xLength == 0:
                y = lane.coordinates[1] + parameter
                vs = 1
                x = lane.coordinates[0]
            else:
                x = lane.coordinates[0] + parameter
                vs = 1
                y = lane.coordinates[1]
        elif lane.curveType == "ellipsis":
            x = xLength * np.cos(parameter)
            y = yLength * np.sin(parameter)
            xdot = -xLength * np.sin(parameter)
            ydot = yLength * np.cos(parameter)
            vs = np.sqrt(xdot ** 2 + ydot ** 2)
        return x, y, vs
