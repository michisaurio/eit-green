from light import Light

class Configuration:
    def __init__(self, lights: [Light] = []) -> None:
        self.lights = lights

    def update(self, timeStep: float) -> None:
        #TODO: Update the configurations
        pass

    @property
    def lights(self) -> [Light]:
        return self.__lights

    @property.setter
    def lights(self, lights: [Light]) -> None:
        self.__lights = lights

    #TODO: How should the configurations themselves be implemented? A time control might be needed here