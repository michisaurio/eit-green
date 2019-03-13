from light import Light
import intersectionConfigs as inCon
from color import Color

class Configuration:
    def __init__(self, lights: [Light] = []) -> None:
        self.lights = lights
        self.stateList = inCon.main()
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
    def update(self, timeStep: float, newConfig=-1) -> None:  # TODO: Check if function calls are correct
        if newConfig != -1 and not self.curUpdatingYellowToRed and not self.curUpdatingRedToGreen:
            self.curUpdatingYellowToRed = timeStep
            self.curConfig = self.stateList[newConfig]
            for light in self.lights:
                if light.color() == "GREEN":
                    light.color(Color.YELLOW)
        if self.curUpdatingYellowToRed != 0:
            self.curUpdatingYellowToRed += timeStep
            if self.curUpdatingYellowToRed >= 3:
                self.curUpdatingYellowToRed = False
                self.curUpdatingRedToGreen = timeStep
                for light in self.lights:
                    if light.color() == "YELLOW":
                        light.color(Color.RED)
        if self.curUpdatingRedToGreen != 0:
            self.curUpdatingRedToGreen += timeStep
            if self.curUpdatingYellowToRed == 4:
                self.curUpdatingYellowToRed = False
                for i in self.curConfig:
                    self.lights(i).color(Color.GREEN)

    @property
    def lights(self) -> [Light]:
        return self.__lights

    @lights.setter
    def lights(self, lights: [Light]) -> None:
        self.__lights = lights

