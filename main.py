from trafficMaster import TrafficMaster
from lane import Lane
from car import Car
from light import Light
from configuration import Configuration
import color
#TODO Tune parameters
def main():
    lane1 = Lane(coordinates=[0,370,300,370], speedLimit=120, curveType="line", spawnRate=0.4)
    lane2 = Lane(coordinates = [300,430,0,430], speedLimit = 120, curveType="line")
    lane3 = Lane(coordinates=[370, 800, 370, 500], speedLimit=120, curveType="line", spawnRate=0.4)
    lane4 = Lane(coordinates=[430, 500, 430, 800], speedLimit=120, curveType="line")
    lane5 = Lane(coordinates=[800,430,500,430], speedLimit=120, curveType="line", spawnRate=0.4)
    lane6 = Lane(coordinates=[500,370,800,370], speedLimit=120, curveType="line")
    lane7 = Lane(coordinates=[430, 0, 430, 300], speedLimit=120, curveType="line", spawnRate=0.4)
    lane8 = Lane(coordinates=[370, 300, 370, 0], speedLimit=120, curveType="line")
    mergeLane4 = Lane(coordinates=[430, 300, 430, 500], speedLimit=120, curveType="merge", nextLanes=[(lane4, 1)])
    lane11 = Lane(coordinates=[300, 370, 430, 500], speedLimit=120, curveType="ellipsis", isClockWise=0, nextLanes=[(lane4, 1)], parentLane=mergeLane4)
    lane12 = Lane(coordinates=[300, 370, 500, 370], speedLimit=120, curveType="line", nextLanes=[(lane6, 1)])
    lane13 = Lane(coordinates=[300, 370, 370, 300], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane8, 1)])
    lane31 = Lane(coordinates=[370, 500, 500, 370], speedLimit=120, curveType="ellipsis", isClockWise=0 ,nextLanes=[(lane6, 1)])
    lane32 = Lane(coordinates=[370, 500, 370, 300], speedLimit=120, curveType="line", nextLanes=[(lane8, 1)])
    lane33 = Lane(coordinates=[370, 500, 300, 430], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane2, 1)])
    lane51 = Lane(coordinates=[500, 430, 370, 300], speedLimit=120, curveType="ellipsis", isClockWise=0, nextLanes=[(lane8, 1)])
    lane52 = Lane(coordinates=[500, 430, 300, 430], speedLimit=120, curveType="line", nextLanes=[(lane2, 1)])
    lane53 = Lane(coordinates=[500, 430, 430, 500], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane4, 1)], parentLane=mergeLane4)
    lane71 = Lane(coordinates=[430, 300, 300, 430], speedLimit=120, curveType="ellipsis", isClockWise=0, nextLanes=[(lane2, 1)])
    lane72 = Lane(coordinates=[430, 300, 430, 500], speedLimit=120, curveType="line", nextLanes=[(lane4, 1)], parentLane=mergeLane4)
    lane73 = Lane(coordinates=[430, 300, 500, 370], speedLimit=120, curveType="ellipsis", isClockWise=1, nextLanes=[(lane6, 1)])
    lane1.nextLanes = [(lane11, 1), (lane12, 0), (lane13, 0)]
    lane3.nextLanes = [(lane31, 0.2), (lane32, 0), (lane33, 1)]
    lane5.nextLanes = [(lane51, 0), (lane52, 0), (lane53, 1)]
    lane7.nextLanes = [(lane71, 0), (lane72, 1), (lane73, 0)]
    light1 = Light()
    lane1.light = light1
    light1.color = color.Color.RED
    light2 = Light()
    lane3.light = light2
    light2.color = color.Color.RED
    light3 = Light()
    lane5.light = light3
    light3.color = color.Color.RED
    light4 = Light()
    lane7.light = light4
    light4.color = color.Color.RED
    light5 = Light()
    light5.color = color.Color.RED
    config = Configuration(initList=[[0, 1, 2], [4, 5, 6], [8, 9, 10], [12, 13, 14]], lights=[light1, light1, light1, light5, light2, light2, light2, light5, light3, light3, light3, light5, light4, light4, light4, light5])
    tm = TrafficMaster([config])
    tm.lanes = [lane1,lane2, lane3, lane4, lane5, lane6, lane7, lane8, mergeLane4, lane11, lane12, lane13, lane31, lane32, lane33, lane51, lane52, lane53, lane71, lane72, lane73]
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