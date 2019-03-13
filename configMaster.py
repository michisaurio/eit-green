from configuration import Configuration

class ConfigMaster:
    def __init__(self, configurations: [Configuration] = None) -> None:
        self.configurations = configurations

    def update(self, timeStep: float) -> None:
        for configuration in self.configurations:
            configuration.update(timeStep, newConfig=-1)

    @property
    def configurations(self) -> [Configuration]:
        return self.__configurations

    @configurations.setter
    def configurations(self, configurations: [Configuration]) -> None:
        if configurations == None:
            self.__configurations = []
        else:
            self.__configurations = configurations