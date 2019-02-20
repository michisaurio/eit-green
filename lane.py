from car import Car
from light import Light

class Lane:
    def __init__(self, curve, cars: [Car] = [], light: Light = None) -> None:
        self.curve = curve
        self.cars = cars
        self.light = light

    def update(self):
        for car in self.cars:
            #TODO: This is where the car should drive and check for collision etc
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


    #TODO: How should we implement this? What is the type of curve?