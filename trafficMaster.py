from configMaster import ConfigMaster
import math
import pyglet
from pyglet.gl import *
from lane import Lane
from color import Color

window = pyglet.window.Window(width=800, height=800)
car_image = pyglet.resource.image("images/car_black.png")
carImages = ["images/car_black.png", "images/car_blue.png", "images/car_green.png", "images/car_grey.png", "images/car_lime.png",
          "images/car_olive.png", "images/car_red.png", "images/car_violet.png", "images/ship.png"]
lightImages = {Color.GREEN: "images/light_green.png", Color.RED: "images/light_red.png", Color.YELLOW: "images/light_yellow.png"}

global_car_batch = pyglet.graphics.Batch()
global_lane_batch = pyglet.graphics.Batch()
global_light_batch = pyglet.graphics.Batch()


class TrafficMaster:
    #TODO : How is an initial environment set up? Json? I don't know
    def __init__(self, configs) -> None:
        self.i = 1
        self.configMaster = ConfigMaster(configs) #TODO: How should the configMaster get its configurations?
        self.lanes = []
        self.car_sprites = []
        self.lane_sprites = []
        self.light_sprites = []
        self.car_batch = pyglet.graphics.Batch()
        self.lane_batch = pyglet.graphics.Batch()
        self.light_batch = pyglet.graphics.Batch()
         #### TEST BELOW ####

    def update(self, timeStep: float) -> None:
        self.configMaster.update(timeStep)
        for lane in self.lanes:
            lane.updatePositions(timeStep)
        self.draw()

    def setLaneSprites(self):
        laneImageWidth = pyglet.resource.image("images/road.png").width
        global global_lane_batch

        #################
        #How to add a new image. Change the image and the coordinates properly
        sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/car.png"), 300, 300, batch = global_lane_batch)
        self.lane_sprites.append(sprite)
        #################

        for lane in self.lanes:
            coordinates = lane.coordinates
            if coordinates[1] == coordinates[3] and lane.curveType == "line" and (lane.nextLanes == None or len(lane.nextLanes)>1):
                if coordinates[0] < coordinates[2]:
                    small, big = coordinates[0], coordinates[2]
                    while small < big:
                        sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), small, coordinates[1]-5, batch = global_lane_batch)
                        self.lane_sprites.append(sprite)
                        small += sprite.width
                else:

                    small, big = coordinates[2], coordinates[0]
                    while small < big:
                        sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), small+laneImageWidth, coordinates[1]+5,
                                                      batch=global_lane_batch)
                        sprite.update(rotation = 180)
                        self.lane_sprites.append(sprite)
                        small += sprite.width
            elif coordinates[0] == coordinates[2] and lane.curveType == "line" and (lane.nextLanes == None or len(lane.nextLanes)>1):
                if coordinates[1] < coordinates [3]:
                    small, big = coordinates[1], coordinates[3]
                    while small < big:
                        sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), coordinates[0]+5, small, batch = global_lane_batch)
                        sprite.update(rotation=270)
                        self.lane_sprites.append(sprite)
                        small += sprite.width
                else:
                    small, big = coordinates[3], coordinates[1]
                    while small < big:
                        sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), coordinates[0] - 5,
                                                      small+laneImageWidth, batch=global_lane_batch)
                        sprite.update(rotation=90)
                        self.lane_sprites.append(sprite)
                        small += sprite.width


    def draw(self) -> None:
        self.car_sprites = []
        self.light_sprites = []
        global global_car_batch
        global global_light_batch
        for lane in self.lanes:
            for car in lane.cars:
                sprite = pyglet.sprite.Sprite(pyglet.resource.image(carImages[car[0].image]), *car[0].position, batch=global_car_batch)
                sprite.update(rotation=math.degrees(car[0].orientation))
                self.car_sprites.append(sprite)
            if lane.light:
                sprite = pyglet.sprite.Sprite(pyglet.resource.image(lightImages[lane.light.color]), lane.coordinates[2], lane.coordinates[3],
                                              batch = global_light_batch)
                self.light_sprites.append(sprite)


    def startSimulation(self, timeStep):
        runPyglet(self, timeStep)


@window.event
def on_draw() -> None:
    glClearColor(0.3, 0.75, 0.3, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    #lane_batch.draw()
    #light_batch.draw()
    global_lane_batch.draw()
    global_car_batch.draw()
    global_light_batch.draw()

def runPyglet(trafficM, timeStep):
    trafficM.setLaneSprites()
    pyglet.clock.schedule_interval(trafficM.update, timeStep)
    pyglet.app.run()

@property
def lanes(self) -> [Lane]:
    return self.__lanes

@lanes.setter
def lanes(self, lanes: [Lane]) -> None:
    if lanes == None:
        self.__lanes = []
    elif type(lanes) != list:
        raise TypeError("Expected list of Lane")
    elif any(type(i) != Lane for i in lanes):
        raise TypeError("Expected list of Lane")
    else:
        self.__lanes = lanes