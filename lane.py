from light import Light
import numpy as np

class Lane:
    def __init__(self, coordinates, cars, speedLimit, light: Light = None, curveType = "line") -> None:
        self.coordinates = coordinates #Start and end coordinates in a list [x.start, y.start, x.end, y.end]. For mergelanes, these are the coordinates of the straight lane.
        self.cars = cars
        self.speedLimit = speedLimit
        self.light = light
        self.curveType = curveType #String specifying if the curve is an ellipsis, line, laneswitch or merge
        self.length = 0
        xLength = coordinates[2] - coordinates[0]
        yLength = coordinates[3] - coordinates[1]
        if(curveType == "line" or curveType == "merge"):
            if(xLength == 0):
                self.length = yLength
            else:
                self.length = xLength
        elif(curveType == "ellipsis"):
            h = (xLength-yLength)**2/(xLength+yLength)**2 #mathematical parameter only used to simplify expression below
            self.length = 0.25*np.pi*(xLength+yLength)*(1+(3*h)/(10+np.sqrt(4-3*h))) #formula is 1/4 times an approximation of the perimeter of an ellipse, see https://www.mathsisfun.com/geometry/ellipse-perimeter.html


    def update(self, timeStep) -> None:
        for car in self.cars:
            #TODO: This is where the car should drive and check for collision etc
            vt = self.desiredSpeed(car, self.cars, self.light, self.curveType)
            [x, y, vs] = self.curve(car.parameter)
            car.parameter = car.parameter + timeStep*vt/vs
            [x, y, vs] = self.curve(car.parameter)
            car.position = [x, y]


    def desiredSpeed(self):
        pass

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates


    def curve(self, parameter):  #Parametric equation function. Takes in parameter s and returns x and y coordinates and derivative of s.
        xLength = self.__coordinates[2]-self.__coordinates[0]
        yLength = self.__coordinates[3]-self.__coordinates[1]
        x = 0
        y = 0
        speed = 0
        if(self.__curveType == "line"):
            if(xLength==0):
                y = self.__coordinates[1] + parameter
                speed = 1
                x = self.__coordinates[0]
            else:
                x = self.__coordinates[0] + parameter
                speed = 1
                x = self.__coordinates[1]
        elif(self.__curveType == "ellipsis"):
            x = xLength*np.cos(parameter)
            y = yLength*np.sin(parameter)
            xdot = -xLength*np.sin(parameter)
            ydot = yLength*np.cos(parameter)
            speed = np.sqrt(xdot**2+ydot**2)
        return x, y, speed

    @property
    def cars(self):
        return self.__cars

    @cars.setter
    def cars(self, cars) -> None:
        self.__cars = cars

    @property
    def speedLimit(self):
        return self.__speedLimit

    @speedLimit.setter
    def cars(self, speedLimit) -> None:
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

    #TODO: How should we implement this? What is the type of curve?

    #TODO: Fix this
     def checkConflict(self, conflictingLanes): #this should be run every time a new car enters a set of conflicting #not yet implemented
        straightLane = conflictingLanes[0]     #lanes the first lane in conflicting lanes should be a straight lane.
        orderedCarTuples = []
        for currentLane in conflictingLanes:
            for currentCar in currentLane.cars:
                if currentLane.curveType == "line":
                    position = straightLane.length - currentCar.parameter*(straightLane.speedLimit/currentLane.speedLimit)




def project(mergeLane, car):
    velocityProportionalityConstant = mergeLane.speed/car.speed
    carPosition = mergeLane.length - car.parameter*2/(np.pi) * car.lane.length * velocityProportionalityConstant #The length of car.lane is an approximation, and we approximate the distance
    return carPosition#                                                     travelled by the car as the percentage of the total angle(angle goes between 0 and pi/2 travelled multiplied with the length
