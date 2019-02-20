from configMaster import ConfigMaster
class TrafficMaster:

    def __init__(self) -> None:
        self.configMaster = ConfigMaster() #TODO: How should the configMaster get its configurations?
        self.roads = []

    def update(self, timeStep: float) -> None:
        self.configMaster.update(timeStep)