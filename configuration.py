from light import Light
import intersectionConfigs as inCon
from color import Color

class Configuration:
    def __init__(self, lights: [Light] = []) -> None:
        self.lights = lights
        self.statelist = inCon.main()
        self.curUpdating = False
        self.curUpdating2 = False
        self.curConfig = 0

    def update(self, timeStep: float, newConfig) -> None:  # TODO: Check if function calls are correct
        if newConfig != -1 and self.curUpdating == False and self.curUpdating2 == False:
            self.curUpdating = timeStep
            self.curConfig = self.statelist[newConfig]
            for light in self.lights:
                if light.color() == "GREEN":
                    light.color(Color.YELLOW)
        if self.curUpdating != 0:
            self.curUpdating += timeStep
            if self.curUpdating >= 3:
                self.curUpdating = False
                self.curUpdating2 = timeStep
                for light in self.lights:
                    if light.color() == "YELLOW":
                        light.color(Color.RED)
        if self.curUpdating2 != 0:
            self.curUpdating2 += timeStep
            if self.curUpdating == 4:
                self.curUpdating = False
                for i in self.curConfig:
                    self.lights(i).color(Color.GREEN)


    @property
    def lights(self) -> [Light]:
        return self.__lights

    @property.setter
    def lights(self, lights: [Light]) -> None:
        self.__lights = lights

    #TODO: How should the configurations themselves be implemented? A time control might be needed here