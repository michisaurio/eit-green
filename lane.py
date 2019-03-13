from light import Light
import numpy as np


class Lane:
    def __init__(self, coordinates, speedLimit, light: Light = None, curveType="line", spawnRate=0.0, queue=0) -> None:
        self.coordinates = coordinates  # Start and end coordinates in a list [x.start, y.start, x.end, y.end]. For mergelanes, these are the coordinates of the straight lane.
        self.cars = []  # List with cars in the lane. Assumed topologically sorted.
        self.speedLimit = speedLimit
        self.light = light
        self.curveType = curveType  # String specifying if the curve is an ellipsis, line, laneswitch or merge
        self.length = 0
        self.spawnRate = spawnRate
        self.__queue = queue #This is underscore to overload the setter. This is done becuase the setter assumes that the queue exists
        xLength = coordinates[2] - coordinates[0]
        yLength = coordinates[3] - coordinates[1]
        if (curveType == "line" or curveType == "merge"):
            if (xLength == 0):
                self.length = yLength
            else:
                self.length = xLength
        elif (curveType == "ellipsis"):
            h = (xLength - yLength) ** 2 / (
                    xLength + yLength) ** 2  # mathematical parameter only used to simplify expression below
            self.length = 0.25 * np.pi * (xLength + yLength) * (1 + (3 * h) / (10 + np.sqrt(
                4 - 3 * h)))  # formula is 1/4 times an approximation of the perimeter of an ellipse, see https://www.mathsisfun.com/geometry/ellipse-perimeter.html

    def update(self, timeStep) -> None:

        #Check if there should spawn a new car in the lane. The spawnRate will need testing to determine how high it should be
        if (self.spawnRate * timeStep > np.random.uniform(0, 1)):
            self.queue += 1
        if self.queue > 0:
            self.spawn()

        for i in range(len(self.cars)):
            # TODO: This is where the car should drive and check for collision etc
            (currentCar, criticalDistance) = self.cars[i]
            if criticalDistance > 100:  # Change this magic number to a "global" variable
                acceleration = currentCar.accelerationConstant * (self.speedLimit - currentCar.speed)
            else:
                acceleration = currentCar.distanceConstant * criticalDistance - currentCar.speedConstant * currentCar.speed
            speed = currentCar.speed + timeStep * acceleration
            currentCar.speed = max(0, min(speed, self.speedLimit))  # Add random number to speedLimit
            [x, y, vs] = self.curve(currentCar.parameter)
            currentCar.parameter = currentCar.parameter + timeStep * currentCar.speed / vs
            [x, y, vs] = self.curve(currentCar.parameter)
            currentCar.position = [x, y]

            if i < len(self.cars) - 1:
                self.cars[i].next_car = self.cars[i + 1][0]
            else:
                self.cars[i].next_car = currentCar.nextLane.cars[0][0]

            # Check if car is in new road/lane. Update topological sorting.

            # Update critical distances

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

    def curve(self,
              parameter):  # Parametric equation function. Takes in parameter s and returns x and y coordinates and derivative of s.
        xLength = self.__coordinates[2] - self.__coordinates[0]
        yLength = self.__coordinates[3] - self.__coordinates[1]
        x = 0
        y = 0
        speed = 0
        if (self.__curveType == "line"):
            if (xLength == 0):
                y = self.__coordinates[1] + parameter
                speed = 1
                x = self.__coordinates[0]
            else:
                x = self.__coordinates[0] + parameter
                speed = 1
                x = self.__coordinates[1]
        elif (self.__curveType == "ellipsis"):
            x = xLength * np.cos(parameter)
            y = yLength * np.sin(parameter)
            xdot = -xLength * np.sin(parameter)
            ydot = yLength * np.cos(parameter)
            speed = np.sqrt(xdot ** 2 + ydot ** 2)
        return x, y, speed

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
            print("You tried to set the queue to less than 0")
        elif (queue == self.queue - 1 or queue == self.queue + 1):
            self.__queue = queue
        else:
            print("You tried to change queue by more than 1")

    # TODO: How should we implement this? What is the type of curve?


def project(mergeLane, car):
    velocityProportionalityConstant = mergeLane.speedLimit / car.lane.speedLimit  # Not the best approximation
    carPosition = mergeLane.length - car.parameter * 2 / (
    np.pi) * car.lane.length * velocityProportionalityConstant  # The length of car.lane is an approximation, and we approximate the distance
    return carPosition  # travelled by the car as the percentage of the total angle(angle goes between 0 and pi/2 travelled multiplied with the length
