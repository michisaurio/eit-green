from light import Light
import intersectionConfigs as inCon
from color import Color

class Configuration:
    def __init__(self, lights: [Light] = []) -> None:
        self.lights = lights
        self.statelist = inCon.main()
        self.curUpdatingYellowtoRed = False
        self.curUpdatingRedtoGreen = False
        self.curConfig = 0

    def update(self, timeStep: float, newConfig=-1) -> None:  # TODO: Check if function calls are correct
        if newConfig != -1 and self.curUpdatingYellowtoRed == False and self.curUpdatingRedtoGreen == False:
            self.curUpdatingYellowtoRed = timeStep
            self.curConfig = self.statelist[newConfig]
            for light in self.lights:
                if light.color() == "GREEN":
                    light.color(Color.YELLOW)
        if self.curUpdatingYellowtoRed != 0:
            self.curUpdatingYellowtoRed += timeStep
            if self.curUpdatingYellowtoRed >= 3:
                self.curUpdatingYellowtoRed = False
                self.curUpdatingRedtoGreen = timeStep
                for light in self.lights:
                    if light.color() == "YELLOW":
                        light.color(Color.RED)
        if self.curUpdatingRedtoGreen != 0:
            self.curUpdatingRedtoGreen += timeStep
            if self.curUpdatingYellowtoRed == 4:
                self.curUpdatingYellowtoRed = False
                for i in self.curConfig:
                    self.lights(i).color(Color.GREEN)


    @property
    def lights(self) -> [Light]:
        return self.__lights

    @lights.setter
    def lights(self, lights: [Light]) -> None:
        self.__lights = lights

    #TODO: How should the configurations themselves be implemented? A time control might be needed here