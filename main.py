from trafficMaster import TrafficMaster
from lane import Lane
from car import Car
from light import Light
from configuration import Configuration
import color
#TODO Tune parameters
def main():
    screen_width = 1200;
    screen_height = 800;
    lane_width = 80;
    x_cross = screen_width/2;
    y_cross = screen_height/2;

    lane1 = Lane(coordinates=[0,y_cross-lane_width/2,x_cross-lane_width,y_cross-lane_width/2], speedLimit=120, curveType="line", spawnRate=0.4, width = lane_width)
    lane2 = Lane(coordinates=[x_cross-lane_width,y_cross+lane_width/2,0,y_cross+lane_width/2], speedLimit = 120, curveType="line", width = lane_width)
    lane3 = Lane(coordinates=[x_cross-lane_width/2, screen_height, x_cross-lane_width/2, y_cross+lane_width], speedLimit=120, curveType="line", spawnRate=0.4, width = lane_width)
    lane4 = Lane(coordinates=[x_cross+lane_width/2, y_cross+lane_width, x_cross+lane_width/2, screen_height], speedLimit=120, curveType="line", width = lane_width)
    lane5 = Lane(coordinates=[screen_width,y_cross+lane_width/2,x_cross+lane_width,y_cross+lane_width/2], speedLimit=120, curveType="line", spawnRate=0.4, width = lane_width)
    lane6 = Lane(coordinates=[x_cross+lane_width,y_cross-lane_width/2,screen_width,y_cross-lane_width/2], speedLimit=120, curveType="line", width = lane_width)
    lane7 = Lane(coordinates=[x_cross+lane_width/2, 0, x_cross+lane_width/2, y_cross-lane_width], speedLimit=120, curveType="line", spawnRate=0.4, width = lane_width)
    lane8 = Lane(coordinates=[x_cross-lane_width/2, y_cross-lane_width, x_cross-lane_width/2, 0], speedLimit=120, curveType="line", width = lane_width)
    lane9 = Lane(coordinates=[x_cross+lane_width*3/2, 0, x_cross+lane_width*3/2, y_cross-lane_width], speedLimit=120, curveType="line", spawnRate = 0.4, width = lane_width)
    mergeLane4 = Lane(coordinates=[x_cross+lane_width/2, y_cross-lane_width/2, x_cross+lane_width/2, y_cross+lane_width], speedLimit=120, curveType="merge", nextLanes=[(lane4, 1)], width = lane_width, crosswalk_width= 0)
    lane14 = Lane(coordinates=[x_cross-lane_width, y_cross-lane_width/2, x_cross+lane_width/2, y_cross+lane_width], speedLimit=120, curveType="ellipsis", isClockWise=0, nextLanes=[(lane4, 1)], parentLane=mergeLane4, width = lane_width, crosswalk_width= 0)
    lane16 = Lane(coordinates=[x_cross-lane_width, y_cross-lane_width/2, x_cross+lane_width, y_cross-lane_width/2], speedLimit=120, curveType="line", nextLanes=[(lane6, 1)], width = lane_width, crosswalk_width= 0)
    lane18 = Lane(coordinates=[x_cross-lane_width, y_cross-lane_width/2, x_cross-lane_width/2, y_cross-lane_width], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane8, 1)], width = lane_width, crosswalk_width= 0)
    lane36 = Lane(coordinates=[x_cross-lane_width/2, y_cross+lane_width, x_cross+lane_width, y_cross-lane_width/2], speedLimit=120, curveType="ellipsis", isClockWise=0 ,nextLanes=[(lane6, 1)], width = lane_width, crosswalk_width= 0)
    lane38 = Lane(coordinates=[x_cross-lane_width/2, y_cross+lane_width, x_cross-lane_width/2, y_cross-lane_width], speedLimit=120, curveType="line", nextLanes=[(lane8, 1)], width = lane_width, crosswalk_width= 0)
    lane31 = Lane(coordinates=[x_cross-lane_width/2, y_cross+lane_width, x_cross-lane_width, y_cross+lane_width/2], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane2, 1)], width = lane_width, crosswalk_width= 0)
    lane58 = Lane(coordinates=[x_cross+lane_width, y_cross+lane_width/2, x_cross-lane_width/2, y_cross-lane_width], speedLimit=120, curveType="ellipsis", isClockWise=0, nextLanes=[(lane8, 1)], width = lane_width, crosswalk_width= 0)
    lane52 = Lane(coordinates=[x_cross+lane_width, y_cross+lane_width/2, x_cross-lane_width, y_cross+lane_width/2], speedLimit=120, curveType="line", nextLanes=[(lane2, 1)], width = lane_width, crosswalk_width= 0)
    lane54 = Lane(coordinates=[x_cross+lane_width, y_cross+lane_width/2, x_cross+lane_width/2, y_cross+lane_width], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane4, 1)], parentLane=mergeLane4, width = lane_width, crosswalk_width= 0)
    lane72 = Lane(coordinates=[x_cross+lane_width/2, y_cross-lane_width, x_cross-lane_width, y_cross+lane_width/2], speedLimit=120, curveType="ellipsis", isClockWise=0, nextLanes=[(lane2, 1)], width = lane_width, crosswalk_width= 0)
    lane74 = Lane(coordinates=[x_cross+lane_width/2, y_cross-lane_width, x_cross+lane_width/2, y_cross+lane_width], speedLimit=120, curveType="line", nextLanes=[(lane4, 1)], parentLane=mergeLane4, width = lane_width, crosswalk_width= 0)
    lane76 = Lane(coordinates=[x_cross+lane_width/2, y_cross-lane_width, x_cross+lane_width, y_cross-lane_width/2], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane6, 1)], width = lane_width, crosswalk_width= 0)
    lane1.nextLanes = [(lane14, 1), (lane16, 0), (lane18, 0)]
    lane3.nextLanes = [(lane36, 0.2), (lane38, 0), (lane31, 1)]
    lane5.nextLanes = [(lane58, 0), (lane52, 0), (lane54, 1)]
    lane7.nextLanes = [(lane72, 0), (lane74, 1), (lane76, 0)]
    light1 = Light()
    lane1.light = light1
    light1.color = color.Color.RED
    light3 = Light()
    lane3.light = light3
    light3.color = color.Color.RED
    light5 = Light()
    lane5.light = light5
    light5.color = color.Color.RED
    light7 = Light()
    lane7.light = light7
    light7.color = color.Color.RED
    light_pedestrian1 = Light()
    light_pedestrian1.color = color.Color.RED
    light_pedestrian2 = Light()
    light_pedestrian2.color = color.Color.RED
    light_pedestrian3 = Light()
    light_pedestrian3.color = color.Color.RED
    light_pedestrian4 = Light()
    light_pedestrian4.color = color.Color.RED
    config = Configuration(initList=[[0, 1, 2], [4, 5, 6], [8, 9, 10], [12, 13, 14]], lights=[light1, light1, light1, light_pedestrian1, light3, light3, light3, light_pedestrian2, light5, light5, light5, light_pedestrian3, light7, light7, light7, light_pedestrian4])
    tm = TrafficMaster([config])
    tm.lanes = [lane1,lane2, lane3, lane4, lane5, lane6, lane7, lane8, lane9, mergeLane4, lane14, lane16, lane18, lane36, lane38, lane31, lane58, lane52, lane54, lane72, lane74, lane76]
    """
    print(car1.speed)
    tm.update(0.01)
    print(car1.speed)
    tm.update(0.01)
    print(car1.speed)
    tm.update(0.01)
    print(car1.speed)
    tm.update(0.01)
    """
    tm.startSimulation(0.01)

def main2():
    screen_height = 800
    screen_width = 1200
    lane_width = 50
    x_cross = screen_width/2;
    y_cross = screen_height/2;
    cross_size = 100

    laneS1 = Lane(coordinates=[x_cross-lane_width, y_cross-cross_size, x_cross-lane_width, 0], speedLimit=120, curveType="line", width = lane_width)
    laneS2 = Lane(coordinates=[x_cross, 0, x_cross, y_cross-cross_size], speedLimit=120, curveType="line", spawnRate=0.4, width = lane_width)
    laneS3 = Lane(coordinates=[x_cross+lane_width, 0, x_cross+lane_width, y_cross-cross_size], speedLimit=120, curveType="line", spawnRate=0.4, width = lane_width)
    laneN3 = Lane(coordinates=[x_cross-lane_width, screen_height, x_cross-lane_width, y_cross+cross_size], speedLimit=120, curveType="line", spawnRate=0.4, width=lane_width)
    laneN2 = Lane(coordinates=[x_cross, screen_height, x_cross, y_cross+cross_size], speedLimit=120, curveType="line", spawnRate=0.4, width=lane_width)
    laneN1 = Lane(coordinates=[x_cross+lane_width, y_cross+cross_size, x_cross+lane_width, screen_height], speedLimit=120, curveType="line", width=lane_width)
    laneV3 = Lane(coordinates=[0, y_cross-lane_width, x_cross-cross_size, y_cross-lane_width], speedLimit=120, curveType="line", spawnRate=0.4, width = lane_width)
    laneV2 = Lane(coordinates=[0, y_cross, x_cross-cross_size, y_cross], speedLimit=120, curveType="line", spawnRate=0.4, width = lane_width)
    laneV1 = Lane(coordinates=[x_cross-cross_size, y_cross+lane_width, 0, y_cross+lane_width], speedLimit=120, curveType="line", width = lane_width)
    laneO1 = Lane(coordinates=[x_cross+cross_size, y_cross-lane_width, screen_width, y_cross-lane_width], speedLimit=120, curveType="line", width = lane_width)
    laneO2 = Lane(coordinates=[screen_width, y_cross, x_cross+cross_size, y_cross], speedLimit=120, curveType="line", spawnRate=0.4, width = lane_width)
    laneO3 = Lane(coordinates=[screen_width, y_cross+lane_width, x_cross+cross_size, y_cross+lane_width], speedLimit=120, curveType="line", spawnRate=0.4, width = lane_width)

    laneSVN = Lane(coordinates=[x_cross+lane_width, y_cross-cross_size, x_cross+lane_width, y_cross+cross_size],
                    speedLimit=120, curveType="merge", width=lane_width, nextLanes=[(laneN1, 1)])

    laneNOS = Lane(coordinates=[x_cross-lane_width, y_cross+cross_size, x_cross-lane_width, y_cross-cross_size],
                speedLimit=120, curveType="merge", width=lane_width, nextLanes=[(laneS1, 1)])

    laneVNO = Lane( coordinates=[x_cross-cross_size, y_cross-lane_width, x_cross+cross_size, y_cross-lane_width],
                speedLimit=120, curveType="merge", width=lane_width, nextLanes=[(laneO1, 1)])

    laneOSV = Lane(coordinates=[x_cross+cross_size, y_cross+lane_width, x_cross-cross_size, y_cross+lane_width],
                speedLimit=120, curveType="merge", width=lane_width, nextLanes=[(laneV1, 1)])

    laneS2V1 = Lane(coordinates=[x_cross, y_cross-cross_size, x_cross-cross_size, y_cross+lane_width], speedLimit=120,
                    curveType="ellipsis", width=lane_width, isClockWise=0, nextLanes=[(laneV1, 1)], parentLane=laneOSV)
    laneS3N1 = Lane(coordinates=[x_cross+lane_width, y_cross-cross_size, x_cross+lane_width, y_cross+cross_size],
                    speedLimit=120, curveType="line", width=lane_width, nextLanes=[(laneN1, 1)], parentLane=laneSVN)
    laneS3O1 = Lane(coordinates=[x_cross+lane_width, y_cross-cross_size, x_cross+cross_size, y_cross-lane_width],
                    speedLimit=120, curveType="ellipsis", width=lane_width, isClockWise=1, nextLanes=[(laneO1, 1)])

    laneV2N1 = Lane(coordinates=[x_cross-cross_size, y_cross, x_cross+lane_width, y_cross+cross_size],
                    speedLimit=120, curveType="ellipsis", width=lane_width, isClockWise=0, nextLanes=[(laneN1, 1)], parentLane=laneSVN)
    laneV3O1 = Lane( coordinates=[x_cross-cross_size, y_cross-lane_width, x_cross+cross_size, y_cross-lane_width],
                speedLimit=120, curveType="line", width=lane_width, nextLanes=[(laneO1, 1)], parentLane=laneVNO)
    laneV3S1 = Lane(coordinates=[x_cross-cross_size, y_cross-lane_width, x_cross-lane_width, y_cross-cross_size],
                speedLimit=120, curveType="ellipsis", width=lane_width, isClockWise=1, nextLanes=[(laneS1, 1)])

    laneN2O1 = Lane(coordinates=[x_cross, y_cross+cross_size, x_cross+cross_size, y_cross-lane_width], speedLimit=120,
                    curveType="ellipsis", width=lane_width, isClockWise=0, nextLanes=[(laneO1, 1)], parentLane=laneVNO)
    laneN3S1 = Lane(coordinates=[x_cross-lane_width, y_cross+cross_size, x_cross-lane_width, y_cross-cross_size],
                speedLimit=120, curveType="line", width=lane_width, nextLanes=[(laneS1, 1)], parentLane=laneNOS)
    laneN3V1 = Lane(coordinates=[x_cross-lane_width, y_cross+cross_size, x_cross-cross_size, y_cross+lane_width],
                speedLimit=120, curveType="ellipsis", width=lane_width, isClockWise=1, nextLanes=[(laneV1, 1)])

    laneO2S1 = Lane(coordinates=[x_cross+cross_size, y_cross, x_cross-lane_width, y_cross-cross_size], speedLimit=120,
                    curveType="ellipsis", width=lane_width, isClockWise=0, nextLanes=[(laneS1, 1)], parentLane=laneNOS)
    laneO3V1 = Lane(coordinates=[x_cross+cross_size, y_cross+lane_width, x_cross-cross_size, y_cross+lane_width],
                speedLimit=120, curveType="line", width=lane_width, nextLanes=[(laneV1, 1)], parentLane=laneOSV)
    laneO3N1 = Lane(coordinates=[x_cross+cross_size, y_cross+lane_width, x_cross+lane_width, y_cross+cross_size],
                speedLimit=120, curveType="ellipsis", width=lane_width, isClockWise=1, nextLanes=[(laneN1, 1)])

    laneS2.nextLanes = [(laneS2V1, 1)]
    laneS3.nextLanes = [(laneS3N1, 0.5), (laneS3O1, 1)]
    laneV2.nextLanes = [(laneV2N1, 1)]
    laneV3.nextLanes = [(laneV3O1, 0.5), (laneV3S1, 1)]
    laneN2.nextLanes = [(laneN2O1, 1)]
    laneN3.nextLanes = [(laneN3S1, 0.5), (laneN3V1, 1)]
    laneO2.nextLanes = [(laneO2S1, 1)]
    laneO3.nextLanes = [(laneO3N1, 0.5), (laneO3V1, 1)]
    lightN2 = Light()
    laneN2.light = lightN2
    lightN2.color = color.Color.RED
    lightN3 = Light()
    laneN3.light = lightN3
    lightN3.color = color.Color.RED
    lightS2 = Light()
    laneS2.light = lightS2
    lightS2.color = color.Color.RED
    lightS3 = Light()
    laneS3.light = lightS3
    lightS3.color = color.Color.RED
    lightV2 = Light()
    laneV2.light = lightV2
    lightV2.color = color.Color.RED
    lightV3 = Light()
    laneV3.light = lightV3
    lightV3.color = color.Color.RED
    lightO2 = Light()
    laneO2.light = lightO2
    lightO2.color = color.Color.RED
    lightO3 = Light()
    laneO3.light = lightO3
    lightO3.color = color.Color.RED
    light_pedestrian1 = Light()
    light_pedestrian1.color = color.Color.RED
    light_pedestrian2 = Light()
    light_pedestrian2.color = color.Color.RED
    light_pedestrian3 = Light()
    light_pedestrian3.color = color.Color.RED
    light_pedestrian4 = Light()
    light_pedestrian4.color = color.Color.RED
    config = Configuration(initList=[[1, 2], [5, 6], [9, 10], [13, 14]],
                           lights=[lightS2, lightS3, lightS3, light_pedestrian1, lightV2, lightV3, lightV3, light_pedestrian2,
                                   lightN2, lightN3, lightN3, light_pedestrian3, lightO2, lightO3, lightO3,
                                   light_pedestrian4])
    tm = TrafficMaster([config])
    tm.lanes = [laneN1, laneN2, laneN3, laneS1, laneS2, laneS3, laneV1, laneV2, laneV3, laneO1, laneO2, laneO3, laneSVN, laneNOS, laneOSV, laneVNO,
                laneS3O1, laneV3S1, laneN3V1, laneO3N1]
    tm.startSimulation(0.01)
if __name__ == "__main__":
    main2()