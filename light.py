from color import Color


class Light:

    def __init__(self, id: int, color: Color = Color.RED) -> None:
        self.id = id
        self.color = color

    @property
    def color(self) -> Color:
        return self.__color

    @color.setter
    def color(self, color: Color) -> None:
        self.__color = color