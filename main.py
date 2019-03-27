from trafficMaster import TrafficMaster
from lane import Lane
from road import Road
from car import Car
from light import Light
import color

def main():
    lane1 = Lane(coordinates=[0,400,300,400], speedLimit=120, curveType="line", spawnRate=0.5)
    lane2 = Lane(coordinates = [400,500,400,800], speedLimit = 120, curveType="line")
    lane3 = Lane(coordinates=[500, 400, 800, 400], speedLimit=120, curveType="line")
    lane4 = Lane(coordinates=[400, 300, 400, 0], speedLimit=120, curveType="line")
    lane5 = Lane(coordinates=[300,400,400,500], speedLimit=120, curveType="ellipsis", isClockWise=0, nextLanes=[(lane2,1)])
    car1 = Car([350, 400])
    car1.lane = lane1
    car1.nextLane = lane3
    lane1.cars = []
    light = Light()
    lane1.light = light
    lane2.light = light
    lane1.nextLanes = [(lane5,1)]
    light.color = color.Color.GREEN
    road1 = Road(lanes=[lane1,lane2, lane3, lane4, lane5])
    print(car1.position)
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