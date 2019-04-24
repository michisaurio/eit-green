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
    mergeLane4 = Lane(coordinates=[x_cross+lane_width/2, y_cross-lane_width, x_cross+lane_width/2, y_cross+lane_width], speedLimit=120, curveType="merge", nextLanes=[(lane4, 1)], width = lane_width, crosswalk_width= 0)
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
    tm.lanes = [lane1,lane2, lane3, lane4, lane5, lane6, lane7, lane8, mergeLane4, lane14, lane16, lane18, lane36, lane38, lane31, lane58, lane52, lane54, lane72, lane74, lane76]
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


if __name__ == "__main__":
    main()