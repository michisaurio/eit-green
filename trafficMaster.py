from configMaster import ConfigMaster
import math
import pyglet
import road
import lane
import car

window = pyglet.window.Window(width=400, height=400)
car_image = pyglet.resource.image("ship.png")
car_batch = pyglet.graphics.Batch()
lane_batch = pyglet.graphics.Batch()
light_batch = pyglet.graphics.Batch()

class TrafficMaster:
    #TODO : How is an initial environment set up? Json? I don't know
    def __init__(self) -> None:
        self.configMaster = ConfigMaster() #TODO: How should the configMaster get its configurations?
        self.roads = []
        self.car_sprites = []
         #### TEST BELOW ####

    def update(self, timeStep: float) -> None:
        self.configMaster.update(timeStep)
        for road in self.roads:
            road.update(timeStep)

    def setLaneSprites(self):
        pass

    def draw(self, dt) -> None:
        self.car_sprites = []
        for road in self.roads:
            for lane in road.lanes:
                #TODO: Might want to add light to lanes here
                for car in lane.cars:
                    sprite = pyglet.sprite.Sprite(car_image, *car.position, batch=car_batch)
                    sprite.update(rotation=math.degrees(car.orientation))
                    self.car_sprites.append(sprite)
    #TODO: Be able to draw car and also rotate it. Should probably be a .png file? Make a function that does this. Input lane+car. Should get the rotation
    # for car: drawCar(car.position, rotation(car.position(?), lane))

trafficM = TrafficMaster()



@window.event
def on_draw() -> None:
    window.clear()
    lane_batch.draw()
    light_batch.draw()
    car_batch.draw()


def runPyglet():
    trafficM.setLaneSprites()
    pyglet.clock.schedule(trafficM.draw)
    pyglet.app.run()