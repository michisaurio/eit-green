import road

class Car:
    # A car needs to have an id, position and speed

    def __init__(self, id: int, position: [float,float] = [0,0], speed: float = 0, road: road.Road = None, nextRoad: road.Road = None, carInFront: "Car" = None, waitTime: float = 0) -> None:
        self.id = id
        self.position = position
        self.speed = speed
        self.road = road
        self.nextRoad = nextRoad
        self.carInFront = carInFront
        self.waitTime = waitTime #Time that the car is standing still. Definition of still < 10 ?


    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def position(self) -> [float, float]:
        return self.__position

    @position.setter
    def position(self, position: [float, float]) -> None:
        self.__position = position

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, speed: float) -> None:
        self.__speed = speed

    @property
    def road(self) -> road.Road:
        return self.__road

    @road.setter
    def road(self, road: road.Road) -> None:
        self.__road = road

    @property
    def nextRoad(self) -> road.Road:
        return self.__nextRoad

    @road.setter
    def nextRoad(self, nextRoad: road.Road):
        self.__nextRoad = nextRoad

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
        self.__waitTime = waitTime

    # TODO: We could add types of cars, and thus have pictures that match them. Size might also be needed
