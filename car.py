

class Car:
    numberOfCars = 1
    # A car needs to have an id, position and speed
    def __init__(self, position: [float,float], speed: float = 0, parameter: float = 0, orientation: float=0, road = None,
                 lane = None, nextLane = None, carInFront: "Car" = None, waitTime: float = 0, timeConstant = 1,
                 comfortabilityConstant = 3, length = 4.5, width = 1.8) -> None:
        self.id = Car.numberOfCars
        self.position = position
        self.speed = speed
        self.parameter = parameter
        self.orientation = orientation
        self.road = road
        self.lane = lane
        self.nextLane = nextLane
        self.carInFront = carInFront
        self.waitTime = waitTime #Time that the car is standing still. Definition of still < 10 ?
        self.accelerationConstant = 1 / timeConstant
        self.distanceConstant = 1 / timeConstant**2
        self.speedConstant = 2 / timeConstant
        self.comfortabilityConstant = comfortabilityConstant #This number should be multiplied with the car speed to find the distance one tries to keep from the next car
        self.length = length
        self.width = width


    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = Car.numberOfCars
        Car.numberOfCars += 1

    @property
    def position(self) -> [float, float]:
        return self.__position

    @position.setter
    def position(self, position: [float, float]) -> None:
        if not (type(position)==list and len(position) == 2 and (type(position[0])==float or type(position[0]) == int) and (type(position[1])==float or type(position[1]) == int)):
            raise TypeError("Expected [float, float]")
        self.__position = position

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, speed: float) -> None:
        if type(speed) == int:
            speed = float(speed)
        if not type(speed)== float:
            raise TypeError("Expected float")
        self.__speed = speed

    @property
    def parameter(self) -> float:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: float) -> None:
        if type(parameter) == int:
            parameter = float(parameter)
        if not type(parameter)== float:
            raise TypeError("Expected float")
        self.__parameter = parameter

    @property
    def orientation(self) -> float:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: float) -> None:
        if type(orientation) == int:
            orientation = float(orientation)
        if not type(orientation) == float:
            raise TypeError("Expected float")
        self.__orientation = orientation

    @property
    def road(self):
        return self.__road

    @road.setter
    def road(self, road) -> None:
        self.__road = road

    @property
    def lane(self):
        return self.__lane

    @lane.setter
    def lane(self, lane) -> None:
        self.__lane = lane

    @property
    def nextLane(self):
        return self.__nextLane

    @nextLane.setter
    def nextLane(self, nextLane):
        self.__nextLane = nextLane

    @property
    def carInFront(self) -> "Car":
        return self.__carInFront

    @carInFront.setter
    def carInFront(self, carInFront: "Car") -> None:
        self.__carInFront = carInFront

    @property
    def waitTime(self) -> float:
        return self.__waitTime

    @waitTime.setter
    def waitTime(self, waitTime: float) -> None:
        if type(waitTime) == int:
            waitTime = float(waitTime)
        if not type(waitTime)== float:
            raise TypeError("Expected float")
        self.__waitTime = waitTime

    @property
    def accelerationConstant(self) -> float:
        return self.__accelerationConstant

    @accelerationConstant.setter
    def accelerationConstant(self, accelerationConstant: float) -> None:
        if type(accelerationConstant) == int:
            accelerationConstant = float(accelerationConstant)
        if not type(accelerationConstant) == float:
            raise TypeError("Expected float")
        self.__accelerationConstant = accelerationConstant

    @property
    def distanceConstant(self) -> float:
        return self.__distanceConstant

    @distanceConstant.setter
    def distanceConstant(self, distanceConstant: float) -> None:
        if type(distanceConstant) == int:
            distanceConstant = float(distanceConstant)
        if not type(distanceConstant) == float:
            raise TypeError("Expected float")
        self.__distanceConstant = distanceConstant

    @property
    def speedConstant(self) -> float:
        return self.__speedConstant

    @speedConstant.setter
    def speedConstant(self, speedConstant: float) -> None:
        if type(speedConstant) == int:
            speedConstant = float(speedConstant)
        if not type(speedConstant) == float:
            raise TypeError("Expected float")
        self.__speedConstant = speedConstant

    @property
    def comfortabilityConstant(self) -> float:
        return self.__comfortabilityConstant

    @comfortabilityConstant.setter
    def comfortabilityConstant(self, comfortabilityConstant: float) -> None:
        if type(comfortabilityConstant) == int:
            comfortabilityConstant = float(comfortabilityConstant)
        if not type(comfortabilityConstant) == float:
            raise TypeError("Expected float")
        self.__comfortabilityConstant = comfortabilityConstant

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float) -> None:
        self.__length = length

    @property
    def width(self) -> float:
        return self.__width

    @length.setter
    def width(self, width: float) -> None:
        self.__width = width

    # TODO: We could add types of cars, and thus have pictures that match them. Size might also be needed
