from trafficMaster import TrafficMaster
from lane import Lane
from road import Road
from car import Car
from light import Light
import color
#TODO Tune parameters
def main():
    lane1 = Lane(coordinates=[0,375,300,375], speedLimit=120, curveType="line", spawnRate=0.5)
    lane2 = Lane(coordinates = [300,425,0,425], speedLimit = 120, curveType="line")
    lane3 = Lane(coordinates=[375, 800, 375, 500], speedLimit=120, curveType="line", spawnRate=0)
    lane4 = Lane(coordinates=[425, 500, 425, 800], speedLimit=120, curveType="line")
    lane5 = Lane(coordinates=[800,425,425,500], speedLimit=120, curveType="line", spawnRate=0)
    lane6 = Lane(coordinates=[500,375,800,375], speedLimit=120, curveType="line")
    lane7 = Lane(coordinates=[425, 0, 425, 300], speedLimit=120, curveType="line", spawnRate=0)
    lane8 = Lane(coordinates=[375, 300, 375, 0], speedLimit=120, curveType="line")
    lane11 = Lane(coordinates=[300, 375, 425, 500], speedLimit=120, curveType="ellipsis", isClockWise=0, nextLanes=[(lane4, 1)])
    lane12 = Lane(coordinates=[300, 375, 500, 375], speedLimit=120, curveType="line", nextLanes=[(lane6, 1)])
    lane13 = Lane(coordinates=[300, 375, 375, 300], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane8, 1)])
    lane31 = Lane(coordinates=[375, 500, 500, 375], speedLimit=120, curveType="ellipsis", isClockWise=0 ,nextLanes=[(lane6, 1)])
    lane32 = Lane(coordinates=[375, 500, 375, 300], speedLimit=120, curveType="line", nextLanes=[(lane8, 1)])
    lane33 = Lane(coordinates=[375, 500, 300, 425], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane2, 1)])
    lane51 = Lane(coordinates=[500, 425, 425, 300], speedLimit=120, curveType="ellipsis", isClockWise=0, nextLanes=[(lane8, 1)])
    lane52 = Lane(coordinates=[500, 425, 300, 425], speedLimit=120, curveType="line", nextLanes=[(lane2, 1)])
    lane53 = Lane(coordinates=[500, 425, 425, 500], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane4, 1)])
    lane71 = Lane(coordinates=[425, 300, 300, 425], speedLimit=120, curveType="ellipsis", isClockWise=0, nextLanes=[(lane2, 1)])
    lane72 = Lane(coordinates=[425, 300, 425, 500], speedLimit=120, curveType="line", nextLanes=[(lane4, 1)])
    lane73 = Lane(coordinates=[425, 300, 500, 375], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane6, 1)])
    lane1.nextLanes = [(lane11, 1), (lane12, 0), (lane13, 0)] #TODO: fix this
    lane3.nextLanes = [(lane31, 0.2), (lane32, 0.6), (lane33, 1)]
    lane5.nextLanes = [(lane51, 0.2), (lane52, 0.6), (lane53, 1)]
    lane7.nextLanes = [(lane71, 0.2), (lane72, 0.6), (lane73, 1)]
    light = Light()
    lane1.light = light
    lane2.light = light
    light.color = color.Color.GREEN
    road1 = Road(lanes=[lane1,lane2, lane3, lane4, lane5, lane6, lane7, lane8, lane11, lane12, lane13, lane31, lane32, lane33, lane51, lane52, lane53, lane71, lane72, lane73])
    tm = TrafficMaster()
    tm.roads = [road1]
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