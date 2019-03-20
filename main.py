from trafficMaster import TrafficMaster
from lane import Lane
from road import Road
from car import Car
from light import Light
import color

def main():
    lane1 = Lane(coordinates=[200,100,400,200], speedLimit=20, curveType="ellipsis")
    nextLane = Lane(coordinates=[100, 60, 200, 60], speedLimit=20)
    car1 = Car([20, 60])
    car1.lane = lane1
    lane1.cars = [[car1, 20]]
    light = Light(1)
    lane1.light = light
    light.color = color.Color.GREEN
    road1 = Road(lanes=[lane1])
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