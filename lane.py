from car import Car
from light import Light

class Lane:
    def __init__(self, curve, cars: [Car] = [], light: Light = None, curveType = "line") -> None:
        self.curve = curve #Parametric equation
        self.cars = cars
        self.light = light
        self.curveType = curveType

    def update(self) -> None:
        for car in self.cars:
            #TODO: This is where the car should drive and check for collision etc
            vt = Lane.desiredSpeed(car, self.cars, self.light, self.curveType)
            [x, y, vs] = Lane.curve(car.parameter)
            car.parameter = car.parameter + timeStep*vt/vs
            [x, y, vs] = Lane.curve(car.parameter)
            car.position = [x,y]

            pass

    @property
    def curve(self):
        return self.__curve

    @curve.setter
    def curve(self, curve):
        self.__curve = curve

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
