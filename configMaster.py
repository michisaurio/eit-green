from configuration import Configuration

class ConfigMaster:
    def __init__(self, configurations: [Configuration] = []) -> None:
        self.configurations = configurations

    def update(self, timeStep: float) -> None:
        for configuration in self.configurations:
            configuration.update(timeStep)

    @property
    def configurations(self) -> [Configuration]:
        return self.__configurations

    @configurations.setter
    def configurations(self, configurations: [Configuration]) -> None:
        self.__configurations = configurations