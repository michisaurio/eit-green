from color import Color

class Light:

    def __init__(self, id: int, green_max_time: int, green_countdown: int, color: Color = Color.RED) -> None:
        self.id = id
        self.color = color
        self.green_max_time = green_max_time
        self.green_countdown = green_countdown

    def incrementCountdown(self, increment) - > None:
        self.__green_countdown += increment

    def InitiateColorChange(self) -> None:
        self.__color = Color.YELLOW

    @property
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, color: Color) -> None:
        self.__color = color

    @property
    def green_max_time(self) -> int:
        return self.__green_max_time

    @green_max_time.setter
    def green_max_time(self, green_max_time) -> None:
        self.__green_max_time = green_max_time

    @property
    def green_countdown(self) -> int:
        return self.__green_countdown

    @green_countdown.setter
    def green_countdown(self, green_countdown) -> None:
        self.__green_countdown = green_countdown
