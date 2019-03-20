from configMaster import ConfigMaster
import math
import pyglet
from pyglet.gl import *
import road
import lane
import car

window = pyglet.window.Window(width=400, height=400)
car_image = pyglet.resource.image("ship.png")
global_car_batch = pyglet.graphics.Batch()
global_lane_batch = pyglet.graphics.Batch()
global_light_batch = pyglet.graphics.Batch()


class TrafficMaster:
    #TODO : How is an initial environment set up? Json? I don't know
    def __init__(self) -> None:
        self.configMaster = ConfigMaster() #TODO: How should the configMaster get its configurations?
        self.roads = []
        self.car_sprites = []
        self.car_batch = pyglet.graphics.Batch()
        self.lane_batch = pyglet.graphics.Batch()
        self.light_batch = pyglet.graphics.Batch()
         #### TEST BELOW ####

    def update(self, timeStep: float) -> None:
        self.configMaster.update(timeStep)
        for road in self.roads:
            road.update(timeStep)
        self.draw()

    def setLaneSprites(self): #TODO : Add the lanes to the lane_batch
        pass

    def draw(self) -> None:
        self.car_sprites = []
        for road in self.roads:
            for lane in road.lanes:
                #TODO: Might want to add light to lanes here
                for car in lane.cars:
                    global global_car_batch
                    sprite = pyglet.sprite.Sprite(car_image, *car[0].position, batch=global_car_batch)
                    sprite.update(rotation=math.degrees(car[0].orientation)+90)
                    self.car_sprites.append(sprite)
                    print(car[0].position)
    #TODO: Be able to draw car and also rotate it. Should probably be a .png file? Make a function that does this. Input lane+car. Should get the rotation
    # for car: drawCar(car.position, rotation(car.position(?), lane))

    def startSimulation(self, timeStep):
        runPyglet(self, timeStep)


@window.event
def on_draw() -> None:
    #window.clear()
    glClearColor(1, 0.3, 0.5, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    #lane_batch.draw()
    #light_batch.draw()
    global_car_batch.draw()
    import time
    time.sleep(0.1)

def runPyglet(trafficM, timeStep):
    trafficM.setLaneSprites()
    pyglet.clock.schedule_interval(trafficM.update, timeStep)
    pyglet.app.run()