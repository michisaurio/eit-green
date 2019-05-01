from configuration import Configuration
import numpy as np

class ConfigMaster:
    def __init__(self, configurations: [Configuration] = None) -> None:
        self.configurations = configurations
        self.nextLight = 0
        self.countDown = 7

    def update(self, timeStep: float) -> None:
        for configuration in self.configurations:
            if self.countDown < 0:
                self.nextLight = (self.nextLight+1)%len(configuration.stateList)
                configuration.update(newConfig=self.nextLight)
                self.countDown = 7
            elif self.countDown < 1:
                configuration.allRed()
            elif self.countDown < 2:
                configuration.prepare()
            self.countDown-= timeStep

    @property
    def configurations(self) -> [Configuration]:
        return self.__configurations

    @configurations.setter
    def configurations(self, configurations: [Configuration]) -> None:
        if configurations == None:
            self.__configurations = []
        else:
            if not all(isinstance(i, Configuration) for i in configurations):
                raise TypeError("Expected list of Configuration")
            self.__configurations = configurations