from configMaster import ConfigMaster
from drawer import Drawer
class TrafficMaster:

    def __init__(self) -> None:
        self.configMaster = ConfigMaster() #TODO: How should the configMaster get its configurations?
        self.roads = []
        self.drawer = Drawer()

    def update(self, timeStep: float) -> None:
        self.configMaster.update(timeStep)
        for road in self.roads:
            road.update(timeStep)

    def draw(self) -> None:
        for road in self.roads:
            for lane in road.lanes:
                for car in lane.cars:
                    self.drawer.drawCar(car.position, self.rotation(car.position, lane))
        self.drawer.draw() #Draw all recent stuff
    #TODO: Be able to draw car and also rotate it. Should probably be a .png file? Make a function that does this. Input lane+car. Should get the rotation
    # for car: drawCar(car.position, rotation(car.position(?), lane))

    def rotation(self, position, lane):
        #TODO: This function should return how the car should be rotated
        return 1