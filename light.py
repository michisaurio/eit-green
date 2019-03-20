from color import Color

class Light:

    numberOfLights = 1
    def __init__(self, green_max_time: int, green_countdown: int, color: Color = Color.RED) -> None:
        self.id = Light.numberOfLights
        self.color = color
        self.green_max_time = green_max_time
        self.green_countdown = green_countdown

    def incrementCountdown(self, increment) - > None:
        self.__green_countdown += increment

    def InitiateColorChange(self) -> None:
        self.__color = Color.YELLOW

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = Light.numberOfLights
        Light.numberOfLights += 1

    @property
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, color: Color) -> None:
      if not isinstance(color, Color):
            raise TypeError("Expected Color")
        self.__color = color

    @property
    def green_max_time(self) -> int:
        return self.__green_max_time

    @green_max_time.setter
    def green_max_time(self, green_max_time: int) -> None:
        self.__green_max_time = green_max_time

    @property
    def green_countdown(self) -> int:
        return self.__green_countdown

    @green_countdown.setter
    def green_countdown(self, green_countdown: int) -> None:
        self.__green_countdown = green_countdown