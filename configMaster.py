from configuration import Configuration
import numpy as np

class ConfigMaster:
    def __init__(self, configurations: [Configuration] = None) -> None:
        self.configurations = configurations

    def update(self, timeStep: float) -> None:
        for configuration in self.configurations:
            if np.random.uniform(0, 1) < 0.01:
                configuration.update(timeStep, newConfig=np.random.randint(len(configuration.stateList)))
            else:
                configuration.update(timeStep, newConfig=-1)

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