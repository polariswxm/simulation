import sys
import time

from pip._vendor.distlib.compat import raw_input
from pynput.keyboard import Key, Listener

# import keyboard as kb
sys.path.append('/usr/local/bin/sumo01/sumo-1.3.1/tools')  # import traci,sumolib
sumoBinary = "/usr/local/bin/sumo-gui"  # sumo or sumo-gui connection

import traci
import math
import sumolib
import traci.constants as tc

traci.start([sumoBinary, "-c", "p5.sumo.cfg", "--tripinfo-output", "tripinfo.xml"])

# position = traci.person.getPosition3D("331")
# x0 = position[0]
# y0 = position[1]

step = 0


def getDistance(vehID):

    vehIDList = (777, 778)
    position = traci.person.getPosition("331")
    x0 = position[0]
    y0 = position[1]
    print("-----------person--------------")
    print(x0, y0)

    # for vehID in vehIDList:
    print("---------------" + str(vehID) + "--------------")
    position1 = traci.vehicle.getPosition(vehID)
    x1 = position1[0]
    y1 = position1[1]
    print(x1, y1)
    print("speed: " + str(traci.vehicle.getSpeed("777")))
    distance = math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    if distance <= 1:
        traci.person.moveToXY(personID="331", x=x0, y=y0 - 0.65, edgeID="2to3", keepRoute=1)
    print(distance)


while step < 2000:
    step += 1
    traci.simulationStep()


    position = traci.person.getPosition("331")
    x0 = position[0]
    y0 = position[1]



    direction = raw_input("Enter your input: ")
    if direction == "a":
        # traci.person.moveToXY("331", x=x0, y=y0 - 5, edgeID="5to3", keepRoute=1)
        traci.person.moveToXY(personID="331", x=x0 - 0.5, y=y0, edgeID="2to3", keepRoute=1)
    elif direction == 'd':
        traci.person.moveToXY(personID="331", x=x0 + 0.5, y=y0, angle=90, edgeID="2to3", keepRoute=1)
    elif direction == 'w':
         traci.person.moveToXY(personID="331", x=x0, y=y0 + 2, edgeID="2to3", keepRoute=1)
    elif direction == 's':
        traci.person.moveToXY("331", x=x0, y=y0 - 2, edgeID="2to3", keepRoute=1)
    elif direction == 'x':
        traci.person.moveToXY("331", x=x0+0.5, y=y0-2, angle=135, edgeID="2to3", keepRoute=1)
    elif direction == '':
        traci.person.moveToXY("331", x=x0, y=y0, edgeID="2to3", keepRoute=1)

    # print("-----------person--------------")
    # print(x0, y0)
    # print("-----------vehicle--------------")
    getDistance("777")
    getDistance("778")
    # position1 = traci.vehicle.getPosition("777")
    # x1 = position1[0]
    # y1 = position1[1]
    # print(x1, y1)
    # print("speed: " + str(traci.vehicle.getSpeed("777")))
    #
    # distance = math.sqrt((x0-x1)**2 + (y0-y1)**2)
    # print("distance: " + str(distance))


    time.sleep(1)

traci.close()
print('Done!')
