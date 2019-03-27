from trafficMaster import TrafficMaster
from lane import Lane
from road import Road
from car import Car
from light import Light
import color

def main():
    lane1 = Lane(coordinates=[0,400,350,400], speedLimit=60, curveType="line", spawnRate=0.1)
    lane2 = Lane(coordinates = [400,450,400,800], speedLimit = 60, curveType="line")
    lane3 = Lane(coordinates=[450, 400, 800, 400], speedLimit=60, curveType="line")
    lane4 = Lane(coordinates=[400, 350, 400, 0], speedLimit=60, curveType="line")
    car1 = Car([350, 400])
    car1.lane = lane1
    car1.nextLane = lane3
    lane1.cars = []
    light = Light()
    lane1.light = light
    lane2.light = light
    lane1.nextLanes = [(lane2, 0.2), (lane3, 0.6), (lane4, 1)]
    light.color = color.Color.GREEN
    road1 = Road(lanes=[lane1,lane2, lane3, lane4])
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