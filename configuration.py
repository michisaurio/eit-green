from light import Light
import intersectionConfigs as inCon
from color import Color

class Configuration:
    def __init__(self, initList, lights: [Light] = None) -> None:
        self.lights = lights
        self.stateList = inCon.main(mergeList=initList)
        #self.stateList = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
        self.curUpdatingYellowToRed = False
        self.curUpdatingRedToGreen = False
        self.curConfig = 0

    # 3 possible states - transitioning from yellow to red, transitioning from red to green and done with transitioning
    # and ready for new input.
    # Each time update is called, the function checks if there is a new input configuration. If there is, and there is
    # no ongoing transition then a new transition will start. If there is an ongoing transition this new input is just
    # ignored.
    # A transition consists of two phases, one from yellow to red, and one from red to green. In each phase there is a
    # counting variable. Every time step this counting variable adds the time step, and after a certain amount of time
    # has passed the lights change colour.
    def update(self, newConfig) -> None:  # TODO: Check if function calls are correct
        for i in self.stateList[newConfig]:
            self.lights[i].color = Color.GREEN

    def prepare(self):
        for light in self.lights:
            if light.color == Color.GREEN:
                light.color = Color.YELLOW

    def allRed(self):
        for light in self.lights:
            light.color = Color.RED

    @property
    def lights(self) -> [Light]:
        return self.__lights

    @lights.setter
    def lights(self, lights: [Light]) -> None:
        if lights == None:
            self.__lights = []
        else:
            if not all(isinstance(i, Light) for i in lights):
                raise TypeError("Expected list of Configuration")
            self.__lights = lights

