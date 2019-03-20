from trafficMaster import TrafficMaster
from lane import Lane
from road import Road
from car import Car

def main():
    lane1 = Lane(coordinates=[20,20,100,20], speedLimit=20)
    car1 = Car(1, [20, 20])
    car1.lane = lane1
    lane1.cars = [(car1, 20)]
    road1 = Road(lanes=[lane1])
    tm = TrafficMaster()
    tm.roads = [road1]
    print(car1.speed)
    tm.update(0.01)
    print(car1.speed)
    tm.update(0.01)
    print(car1.speed)
    tm.update(0.01)
    print(car1.speed)
    tm.update(0.01)


if __name__ == "__main__":
    main()