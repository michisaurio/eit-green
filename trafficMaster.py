from configMaster import ConfigMaster
import math
import pyglet
import numpy as np
from pyglet.gl import *
from lane import Lane
from color import Color

window = pyglet.window.Window(width=1200, height=800)
car_image = pyglet.resource.image("images/car_black.png")
carImages = ["images/car_black.png", "images/car_blue.png", "images/car_green.png", "images/car_grey.png", "images/car_lime.png",
          "images/car_olive.png", "images/car_red.png", "images/car_violet.png", "images/ship.png"]
lightImages = {Color.GREEN: "images/light_green.png", Color.RED: "images/light_red.png", Color.YELLOW: "images/light_yellow.png"}

global_car_batch = pyglet.graphics.Batch()
global_lane_batch = pyglet.graphics.Batch()
global_light_batch = pyglet.graphics.Batch()


class TrafficMaster:
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
        xlength  =  pyglet.resource.image("images/car_red.png").width
        ylength =  pyglet.resource.image("images/car_red.png").height
        (dx,dy)=positionCorrectionForPloting(0, 2*xlength, 2*ylength)
        sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/car_red.png"), 100+dx,100+dy, batch=global_lane_batch)
        sprite.update(rotation=0)
        sprite.update(scale=2)
        self.lane_sprites.append(sprite)
        (dx,dy)=positionCorrectionForPloting(-45, 2*xlength, 2*ylength)
        sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/car_blue.png"), 100+dx,100+dy, batch=global_lane_batch)
        sprite.update(rotation=-45)
        sprite.update(scale=2)
        self.lane_sprites.append(sprite)
        (dx,dy)=positionCorrectionForPloting(-90, 2*xlength, 2*ylength)
        sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/car_green.png"), 100+dx,100+dy, batch=global_lane_batch)
        sprite.update(rotation=-90)
        sprite.update(scale=2)
        self.lane_sprites.append(sprite)
        (dx,dy)=positionCorrectionForPloting(-135, 2*xlength, 2*ylength)
        sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/car_violet.png"), 100+dx,100+dy, batch=global_lane_batch)
        sprite.update(rotation=-135)
        sprite.update(scale=2)
        self.lane_sprites.append(sprite)

        laneImageWidth = pyglet.resource.image("images/road.png").width
<<<<<<< HEAD
        laneNoLineImageWidth = pyglet.resource.image("images/road_no_line.png").width
        crossWalkImageWith = pyglet.resource.image("images/road_crosswalk.png").width
        for lane in self.lanes:
            coordinates = lane.coordinates
            global global_lane_batch
            if lane.curveType == 'ellipsis':
                x0 = min(coordinates[0],coordinates[2])
                x1 = max(coordinates[0], coordinates[2])
                y0 = min(coordinates[1], coordinates[3])
                y1 = max(coordinates[1], coordinates[3])
                y01 = y0
                while y01 + laneNoLineImageWidth < y1:
                    x01 = x0
                    while x01 + laneNoLineImageWidth < x1:
                        sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), x01, y01, batch=global_lane_batch)
                        self.lane_sprites.append(sprite)
                        x01 += laneNoLineImageWidth
                    sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), x1-laneNoLineImageWidth, y01, batch=global_lane_batch)
                    self.lane_sprites.append(sprite)
                    y01 += laneNoLineImageWidth
                x01 = x0
                while x01 + laneNoLineImageWidth < x1:
                    sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), x01, y1- laneNoLineImageWidth,
                                                  batch=global_lane_batch)
                    self.lane_sprites.append(sprite)
                    x01 += laneNoLineImageWidth
                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), x1 - laneNoLineImageWidth, y1- laneNoLineImageWidth,
                                              batch=global_lane_batch)
                self.lane_sprites.append(sprite)

            elif coordinates[1] == coordinates[3] and lane.curveType == "line" and (lane.nextLanes == None or len(lane.nextLanes)>1):
                if coordinates[0] < coordinates[2]:
                    x0, x1 = coordinates[0], coordinates[2]
                    x01 = x0
                    while x01 < x1:
                        if x01 + crossWalkImageWith > x1:
                            x01 = x1 - crossWalkImageWith
                        y0 = coordinates[1]
                        y01 = y0
                        y1 = coordinates[1] + lane.width/2
                        while y01 < y1:
                            if y01 + crossWalkImageWith > y1:
                                y01 = y1 - crossWalkImageWith
                            if x01-x0 < crossWalkImageWith or x1-x01 <= crossWalkImageWith:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road_crosswalk.png"), x01+crossWalkImageWith,
                                                              y01, batch=global_lane_batch)
                            else:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), x01+laneImageWidth,
                                                              y01, batch=global_lane_batch)
                            sprite.update(rotation=180)
                            self.lane_sprites.append(sprite)
                            y01 += sprite.width
                        y01 = y0 - laneImageWidth
                        y1 = coordinates[1] - lane.width / 2
                        while y01 > y1:
                            if y01 - crossWalkImageWith < y1:
                                y01 = y1 + crossWalkImageWith
                            if x01 - x0 < crossWalkImageWith or x1 - x01 <= crossWalkImageWith:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road_crosswalk.png"), x01,
                                                              y01, batch=global_lane_batch)
                            else:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), x01,
                                                              y01, batch=global_lane_batch)
                            self.lane_sprites.append(sprite)
                            y01 -= sprite.width
                        x01 += sprite.width

                else:
                    x0, x1 = coordinates[2], coordinates[0]
                    x01 = x0
                    while x01 < x1:
                        if x01 + crossWalkImageWith > x1:
                            x01 = x1 - crossWalkImageWith
                        y0 = coordinates[1]
                        y01 = y0
                        y1 = coordinates[1] + lane.width / 2
                        while y01 < y1:
                            if y01 + crossWalkImageWith > y1:
                                y01 = y1 - crossWalkImageWith
                            if x01 - x0 < crossWalkImageWith or x1 - x01 <= crossWalkImageWith:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road_crosswalk.png"),
                                                              x01 + crossWalkImageWith,
                                                              y01, batch=global_lane_batch)
                            else:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"),
                                                              x01 + laneImageWidth,
                                                              y01, batch=global_lane_batch)
                            sprite.update(rotation=180)
                            self.lane_sprites.append(sprite)
                            y01 += sprite.width
                        y01 = y0 - laneImageWidth
                        y1 = coordinates[1] - lane.width / 2
                        while y01 > y1:
                            if y01 - crossWalkImageWith < y1:
                                y01 = y1 + crossWalkImageWith
                            if x01 - x0 < crossWalkImageWith or x1 - x01 <= crossWalkImageWith:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road_crosswalk.png"), x01,
                                                              y01, batch=global_lane_batch)
                            else:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"), x01,
                                                              y01, batch=global_lane_batch)
                            self.lane_sprites.append(sprite)
                            y01 -= sprite.width
                        x01 += sprite.width


            elif coordinates[0] == coordinates[2] and lane.curveType == "line" and (lane.nextLanes == None or len(lane.nextLanes)>1):
                if coordinates[1] < coordinates [3]:
                    y0, y1 = coordinates[1], coordinates[3]
                    y01 = y0
                    while y01 < y1:
                        if y01 + crossWalkImageWith > y1:
                            y01 = y1 - crossWalkImageWith
                        x0 = coordinates[0]
                        x01 = x0
                        x1 = coordinates[0] + lane.width / 2
                        while x01 < x1:
                            if x01 + crossWalkImageWith > x1:
                                x01 = x1 - crossWalkImageWith
                            if y01 - y0 < crossWalkImageWith or y1 - y01 <= crossWalkImageWith:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road_crosswalk.png"),
                                                              x01 + crossWalkImageWith,
                                                              y01, batch=global_lane_batch)
                            else:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"),
                                                              x01 + laneImageWidth,
                                                              y01, batch=global_lane_batch)
                            sprite.update(rotation=-90)
                            self.lane_sprites.append(sprite)
                            x01 += sprite.width
                        x01 = x0
                        x1 = coordinates[0] - lane.width / 2
                        while x01 > x1:
                            if x01 - crossWalkImageWith < x1:
                                x01 = x1 + crossWalkImageWith
                            if y01 - y0 < crossWalkImageWith or y1 - y01 <= crossWalkImageWith:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road_crosswalk.png"),
                                                              x01 -crossWalkImageWith,
                                                              y01 + crossWalkImageWith, batch=global_lane_batch)
                            else:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"),
                                                              x01 - laneImageWidth,
                                                              y01 + laneImageWidth, batch=global_lane_batch)
                            sprite.update(rotation=90)
                            self.lane_sprites.append(sprite)
                            x01 -= sprite.width
                        y01 += sprite.width

                else:
                    y0, y1 = coordinates[3], coordinates[1]
                    y01 = y0
                    while y01 < y1:
                        if y01 + crossWalkImageWith > y1:
                            y01 = y1 - crossWalkImageWith
                        x0 = coordinates[0]
                        x01 = x0
                        x1 = coordinates[0] + lane.width / 2
                        while x01 < x1:
                            if x01 + crossWalkImageWith > x1:
                                x01 = x1 - crossWalkImageWith
                            if y01 - y0 < crossWalkImageWith or y1 - y01 <= crossWalkImageWith:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road_crosswalk.png"),
                                                              x01 - crossWalkImageWith,
                                                              y01 + crossWalkImageWith, batch=global_lane_batch)
                            else:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"),
                                                              x01 - laneImageWidth,
                                                              y01 + laneImageWidth, batch=global_lane_batch)
                            sprite.update(rotation=90)
                            self.lane_sprites.append(sprite)
                            x01 += sprite.width
                        x01 = x0
                        x1 = coordinates[0] - lane.width / 2
                        x01 = x01
                        while x01 > x1:
                            if x01 - crossWalkImageWith < x1:
                                x01 = x1 + crossWalkImageWith
                            if y01 - y0 < crossWalkImageWith or y1 - y01 <= crossWalkImageWith:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road_crosswalk.png"),
                                                              x01 + crossWalkImageWith,
                                                              y01, batch=global_lane_batch)
                            else:
                                sprite = pyglet.sprite.Sprite(pyglet.resource.image("images/road.png"),
                                                              x01 + laneImageWidth,
                                                              y01, batch=global_lane_batch)
                            sprite.update(rotation=-90)
                            self.lane_sprites.append(sprite)
                            x01 -= sprite.width
                        y01 += sprite.width


    def draw(self) -> None:
        self.car_sprites = []
        self.light_sprites = []
        global global_car_batch
        global global_light_batch
        for lane in self.lanes:
            for car in lane.cars:
                xlength = pyglet.resource.image(carImages[car[0].image]).width
                ylength = pyglet.resource.image(carImages[car[0].image]).height
                (dx, dy) = positionCorrectionForPloting(math.degrees(car[0].orientation), xlength, ylength)
                sprite = pyglet.sprite.Sprite(pyglet.resource.image(carImages[car[0].image]), car[0].position[0]+dx,car[0].position[1]+dy, batch=global_car_batch)
                sprite.update(rotation=math.degrees(car[0].orientation))
                self.car_sprites.append(sprite)
            if lane.light:
                xlength = pyglet.resource.image(lightImages[lane.light.color]).width
                ylength = pyglet.resource.image(lightImages[lane.light.color]).height
                (dx, dy) = positionCorrectionForPloting(0, xlength, ylength)
                sprite = pyglet.sprite.Sprite(pyglet.resource.image(lightImages[lane.light.color]), lane.coordinates[2]+dx, lane.coordinates[3]+dy,
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

def positionCorrectionForPloting(angle, xlength, ylength):
    angle = -np.pi/180*angle
    dx = -xlength/2*np.cos(angle) +ylength/2*np.sin(angle)
    dy = -xlength/2*np.sin(angle) -ylength/2*np.cos(angle)
    return (dx,dy)