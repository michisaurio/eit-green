from color import Color


class Light:

    def __init__(self, id, color = Color.RED):
        self.id = id
        self.color = color

    def getColor(self):
        # Returns an enum of type Color
        return self.color

    def setColor(self, color):
        # The color should be an enum of type Color
        self.color = color