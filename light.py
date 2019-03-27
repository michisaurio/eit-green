from color import Color


class Light:
    numberOfLights = 1

    def __init__(self, color: Color = Color.RED) -> None:
        self.id = Light.numberOfLights
        self.color = color

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