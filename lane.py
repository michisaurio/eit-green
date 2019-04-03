from light import Light
from color import Color
from car import Car
import numpy as np

class Lane:
    def __init__(self, coordinates, speedLimit, light: Light = None, curveType="line", spawnRate=0.0, queue=0,
                 isMerge=False, width = 3.5, nextLanes = None, isClockWise: int = 0) -> None:
        self.coordinates = coordinates  # Start and end coordinates in a list [x.start, y.start, x.end, y.end]. For mergelanes, these are the coordinates of the straight lane.
        self.cars = []  # List with list of cars in the lane and their critical distance [car, criticalDistance]. Assumed topologically sorted such that the first element is the frontmost car in the lane.
        self.speedLimit = speedLimit
        self.light = light
        self.curveType = curveType #String specifying if the curve is an ellipsis, line, laneswitch or merge
        self.length = 0
        self.spawnRate = spawnRate
        self.__queue = queue #Let the constructor overload the setter method to make sure that the queue exists
        self.isMerge = isMerge
        self.width = width
        self.isClockWise = isClockWise
        self.nextLanes = nextLanes
        xLength = abs(coordinates[2] - coordinates[0])
        yLength = abs(coordinates[3] - coordinates[1])
        if(curveType == "line" or curveType == "merge"):
            if(xLength == 0):
                self.length = abs(yLength)
            else:
                self.length = abs(xLength)
        elif (curveType == "ellipsis"):
            h = (xLength - yLength) ** 2 / (
                    xLength + yLength) ** 2  # mathematical parameter only used to simplify expression below
            self.length = 0.4 * np.pi * (xLength + yLength) * (1 + (3 * h) / (10 + np.sqrt(
                4 - 3 * h)))  # formula is 1/4 times an approximation of the perimeter of an ellipse, see https://www.mathsisfun.com/geometry/ellipse-perimeter.html

    def updatePositions(self, timeStep) -> None: #TODO: take mergelane updating of position into consideration

        # Car objects spawned according to a Poisson process (with predetermined mean val?)
        if (self.spawnRate * timeStep > np.random.uniform(0, 1)):
            self.queue += 1
        if self.queue > 0 and (len(self.cars)== 0 or self.cars[-1][0].parameter > 57):  # TODO : The parameter here defines how far the first car has come
            self.spawn()

        i = 0
        while True:
            if i >= len(self.cars):
                break
            # TODO: This is where the car should drive and check for collision etc
            (currentCar, criticalDistance) = self.cars[i]
            if currentCar.id == 3:
                print("id: ", currentCar.id, "crit dist: ", criticalDistance, "Curve type: ", currentCar.lane.curveType)
            if currentCar.id == 2:
                print("id: ", currentCar.id, "crit dist: ", criticalDistance, "Curve type: ", currentCar.lane.curveType)
            if criticalDistance > 2 * currentCar.speed * currentCar.comfortabilityConstant: #TODO: Tune this threshold
                acceleration = currentCar.accelerationConstant*(self.speedLimit - currentCar.speed)
            else:
                acceleration = currentCar.distanceConstant * criticalDistance - currentCar.speedConstant * currentCar.speed

            speed = currentCar.speed + timeStep * acceleration
            currentCar.speed = max(0, speed)  # Add random number to speedLimit
            [x, y, vs, orientation] = curve(currentCar.lane, currentCar.parameter)
            currentCar.parameter = currentCar.parameter + timeStep * currentCar.speed / vs
            [x, y, vs, orientation] = curve(currentCar.lane, currentCar.parameter)
            currentCar.position = [x, y]
            currentCar.orientation = orientation

            # Check if car is in new road/lane. Update topological sorting.
            if (currentCar.lane.curveType == "line" and currentCar.parameter > self.length) or (
                    currentCar.lane.curveType == "ellipsis" and currentCar.parameter > np.pi / 2):
                currentCar.parameter = 0
                if currentCar.nextLane:
                    currentCar.nextLane.cars.append([currentCar, 0])
                    if currentCar.nextLane.isMerge:
                        currentCar.nextLane.updateTopologicalSorting()  # should remove the car from its own lane and put it in merge
                    currentCar.lane = currentCar.nextLane
                    currentCar.nextLane = currentCar.lane.selectNextLane()  # TODO: give the car a proper nextLane
                self.cars.pop(0)
                i -= 1
            i += 1
        self.updateCriticalDistance()



    def getSensorSignal(self, startParameter: float, endParameter: float) -> bool: # Check if there exists a car within the sensors parameter
        return any(startParameter < car[0].parameter < endParameter for car in self.cars)


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
        if self.light and self.light.color == Color.RED:
            self.cars[0][1] = self.length - self.cars[0][0].parameter
        elif self.cars[0][0].nextLane == None or len(self.cars[0][0].nextLane.cars) == 0:
            self.cars[0][1] = np.inf
        else:
            currentCar = self.cars[0][0]
            currentLaneCriticalDistance = self.length - self.cars[0][0].parameter
            if currentCar.lane.curveType == "ellipsis":
                currentLaneCriticalDistance = project(self, currentCar)
            #if currentLaneCriticalDistance > 2*currentCar.speed*currentCar.comfortabilityConstant:
            #    self.cars[0][1] = currentLaneCriticalDistance
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
                currentParameter = currentCar.lane.length * currentCar.parameter * 2 / (np.pi)
            self.cars[i][1] = nextParameter - currentParameter - currentCar.comfortabilityConstant * currentCar.speed - currentCar.comfortabilityConstant*(self.cars[i-1][0].length+currentCar.length)/2
            nextParameter = currentParameter


    def spawn(self):
        self.cars.append([Car([self.coordinates[0], self.coordinates[1]], lane=self, nextLane=self.selectNextLane()), 0])
        self.queue -= 1


    def desiredSpeed(self):
        pass

    def selectNextLane(self):
        if self.nextLanes:
            print(self.nextLanes)
            rndNum = np.random.uniform(0,1)
            for lane in self.nextLanes:
                if lane[1] > rndNum:
                    return lane[0]

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates: [float, float, float, float]):
        if not(type(coordinates) == list and len(coordinates) == 4 and (isinstance(i, (float, int)) for i in coordinates)):
            raise TypeError("Expected [float, float, float, float]")
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
        if not isinstance(speedLimit, int):
            raise TypeError("Expected integer")
        self.__speedLimit = speedLimit


    @property
    def light(self) -> Light:
        return self.__light

    @light.setter
    def light(self, light: Light):
        if not isinstance(light, Light) and light is not None:
            raise TypeError("Expected Light")
        self.__light = light

    @property
    def curveType(self):
        return self.__curveType

    @curveType.setter
    def curveType(self, curveType: str):
        if not isinstance(curveType, str):
            raise TypeError("Expected str")
        if not curveType in {"line", "ellipsis"}:
            raise ValueError("Type of curve does not exist")
        self.__curveType = curveType

    @property
    def spawnRate(self):
        return self.__spawnRate

    @spawnRate.setter
    def spawnRate(self, spawnRate):
        if not isinstance(spawnRate, (float, int)):
            TypeError("Expected float or integer")
        self.__spawnRate = spawnRate

    @property
    def queue(self):
        return self.__queue

    @queue.setter
    def queue(self, queue):
        if not isinstance(queue, int):
            raise TypeError("Expected int")
        if queue < 0:
            print("WARNING: You tried to set the queue to less than 0")
        elif (queue == self.queue - 1 or queue == self.queue + 1):
            self.__queue = queue
        else:
            print("WARNING: You tried to change queue by more than 1")


    @property
    def isMerge(self):
        return self.__isMerge

    @isMerge.setter
    def isMerge(self, isMerge):
        self.__isMerge = isMerge

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def nextLanes(self):
        return self.__nextLanes

    @nextLanes.setter
    def nextLanes(self, nextLanes):
        self.__nextLanes = nextLanes

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
                y = lane.coordinates[1] + np.sign(yLength) * parameter
                vs = 1
                x = lane.coordinates[0]
                if yLength < 0:
                    orientation = np.pi/2
                else:
                    orientation = 3*np.pi/2
            else:
                x = lane.coordinates[0] + np.sign(xLength) * parameter
                vs = 1
                y = lane.coordinates[1]
                orientation = np.arctan2(yLength, xLength)
        elif lane.curveType == "ellipsis":
            if xLength > 0 and yLength > 0:
                startAngle = (np.pi/2) * (3 - lane.isClockWise)
            elif xLength > 0 and yLength < 0:
                startAngle = (np.pi / 2) * (2 - lane.isClockWise)
            elif xLength < 0 and yLength > 0:
                startAngle = (np.pi / 2) * (0 - lane.isClockWise)
            else:
                startAngle = (np.pi / 2) * (1 - lane.isClockWise)

            if lane.isClockWise == 0:
                x = lane.coordinates[0] + xLength * (np.cos(parameter+startAngle)-np.cos(startAngle))
                y = lane.coordinates[1] + yLength * (np.sin(parameter+startAngle)-np.sin(startAngle))
            else:
                x = lane.coordinates[0] + xLength * (np.cos(-parameter + startAngle) - np.cos(startAngle))
                y = lane.coordinates[1] + yLength * (np.sin(-parameter + startAngle) - np.sin(startAngle))
            xdot = -xLength * np.sin(parameter)
            ydot = yLength * np.cos(parameter)
            vs = np.sqrt(xdot ** 2 + ydot ** 2)
            #orientation = np.arctan2(ydot,-xdot)
            if lane.isClockWise == 0:
                orientation = -(parameter+startAngle+np.pi/2)
            else:
                orientation = parameter+startAngle+np.pi/2

        if not 'orientation' in locals():
            raise ValueError("No orientation was set")
        return x, y, vs, orientation
