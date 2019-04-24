from configuration import Configuration
import numpy as np

class ConfigMaster:
    def __init__(self, configurations: [Configuration] = None) -> None:
        self.configurations = configurations
        self.nextLight = 0
        self.countDown = 6

    def update(self, timeStep: float) -> None:
        for configuration in self.configurations:
            #if np.random.uniform(0, 1) < 0.01:
            if self.countDown < 0:
                self.nextLight = (self.nextLight+1)%len(configuration.stateList)
                configuration.update(timeStep, newConfig=self.nextLight)
                self.countDown = 6
            else:
                configuration.update(timeStep, newConfig=-1)
                self.countDown -= timeStep

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