from trafficMaster import TrafficMaster
from lane import Lane
from road import Road
from car import Car
from light import Light

def main():
    lane1 = Lane(coordinates=[20,60,100,60], speedLimit=20)
    car1 = Car(1, [20, 60])
    car2 = Car(2, [40, 60])
    car2.parameter = 30
    car2.lane = lane1
    car1.lane = lane1
    lane1.cars = [(car1, 20), (car2, 20)]
    light = Light
    lane1.light = light
    road1 = Road(lanes=[lane1])
    print(car2.position)
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