from car import Car
from light import Light
import numpy as np

class Lane:
    def __init__(self, coordinates, curve, cars: [Car] = [], light: Light = None, curveType = "line") -> None:
        self.coordinates = coordinates #Start and end coordinates in a list [x.start, y.start, x.end, y.end]
        self.curve = curve #Parametric equation function. Takes in parameter s and returns x and y coordinates and derivative of s.
        self.cars = cars
        self.light = light
        self.curveType = curveType #String specifying if the curve is an ellipsis, line or laneswitch
        self.length = 0
        A = coordinates[2] - coordinates[0]
        B = coordinates[3] - coordinates[1]
        if(curveType == "line"):
            if(A == 0):
                self.length = B
            else:
                self.length = A
        elif(curveType == "ellipsis"):
            h = (A-B)**2/(A+B)**2
            self.length = np.pi*(A+B)*(1+(3*h)/(10+np.sqrt(4-3*h)))

    @property
    def update(self) -> None:
        for car in self.cars:
            #TODO: This is where the car should drive and check for collision etc
            vt = self.desiredSpeed(car, self.cars, self.light, self.curveType)
            [x, y, vs] = self.curve(car.parameter)
            car.parameter = car.parameter + trafficMaster.timeStep*vt/vs
            [x, y, vs] = self.curve(car.parameter)
            car.position = [x,y]

            pass

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates

    @property
    def curve(self, s):
        A = self.__coordinates[2]-self.__coordinates[0]
        B = self.__coordinates[3]-self.__coordinates[1]
        x = 0
        y = 0
        vs = 0
        if(self.__curveType == "line"):
            if(A==0):
                y = self.__coordinates[1] + s
                vs = 1
                x = self.__coordinates[0]
            else:
                x = self.__coordinates[0] + s
                vs = 1
                x = self.__coordinates[1]
        elif(self.__curveType == "ellipsis"):
            x = A*np.cos(s)
            y = B*np.sin(s)
            xdot = -A*np.sin(s)
            ydot = B*np.cos(s)
            vs = np.sqrt(xdot**2+ydot**2)
        return x, y, vs

    @curve.setter
    def curve(self, curve):
        print("YOU CANT DO THAT")

    @property
    def cars(self) -> [Car]:
        return self.__cars

    @cars.setter
    def cars(self, cars: [Car]) -> None:
        self.__cars = cars

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
