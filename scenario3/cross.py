import sys
import time

from pip._vendor.distlib.compat import raw_input
from pynput.keyboard import Key, Listener

# import keyboard as kb
sys.path.append('/usr/local/bin/sumo01/sumo-1.3.1/tools')  # import traci,sumolib
sumoBinary = "/usr/local/bin/sumo-gui"  # sumo or sumo-gui connection

import traci
import sumolib
import traci.constants as tc

traci.start([sumoBinary, "-c", "p4.sumo.cfg", "--tripinfo-output", "tripinfo.xml"])

# position = traci.person.getPosition3D("331")
# x0 = position[0]
# y0 = position[1]

step = 0

while step < 2000:
    step += 1
    traci.simulationStep()
    # traci.person.add("p_1", "2to3", pos=0)

    traci.person.add(personID=str(33 + step), edgeID="5to3", pos=0)
    # traci.person.moveToXY("331", x=36, y=70, edgeID=":node3_c0", keepRoute=1)
    # traci.person.appendWalkingStage("331", "3to4", arrivalPos=60)
    # print(traci.person.getNextEdge("331"))
    # print(traci.person.getStage("331"))
    nextEdge = traci.person.getNextEdge("331")
    print("nextEdge: " + nextEdge)
    roadID = traci.person.getRoadID("331")
    print("roadID: " + roadID)

    position = traci.person.getPosition3D("331")
    x0 = position[0]
    y0 = position[1]
    speed = traci.person.getSpeed("331")
    print(speed)
    print(x0, y0)


    # control people walk on edge of "5to3"

    # if step <= 14:

    direction = raw_input("Enter your input: ")
    if direction == "a":
        # traci.person.moveToXY("331", x=x0, y=y0 - 5, edgeID="5to3", keepRoute=1)
        traci.person.moveToXY(personID="331", x=x0 - 0.5, y=y0, edgeID="5to3", keepRoute=0)
    elif direction == 'd':
        traci.person.moveToXY(personID="331", x=x0 + 0.5, y=y0, angle=90, edgeID="5to3", keepRoute=0)
    elif direction == 'w':
         traci.person.moveToXY(personID="331", x=x0, y=y0 + 2, edgeID="5to3", keepRoute=0)
    elif direction == 's':
        traci.person.moveToXY("331", x=x0, y=y0 - 2, edgeID="5to3", keepRoute=0)
    elif direction == 'x':
        traci.person.moveToXY("331", x=x0+0.5, y=y0-2, angle=135, edgeID="5to3", keepRoute=0)
    elif direction == '':
        traci.person.moveToXY("331", x=x0, y=y0, edgeID="5to3", keepRoute=0)

    #
    # direction = raw_input("Enter your input: ")
    # if direction == "a":
    #     # traci.person.moveToXY("331", x=x0, y=y0 - 5, edgeID="5to3", keepRoute=1)
    #     traci.person.moveToXY(personID="331", x=x0 - 0.5, y=y0, edgeID="5to3", keepRoute=0)
    # elif direction == 'd':
    #     traci.person.moveToXY(personID="331", x=x0 + 0.5, y=y0, angle=90, edgeID="5to3", keepRoute=0)
    # elif direction == 'w':
    #      traci.person.moveToXY(personID="331", x=x0, y=y0 + 2, edgeID="5to3", keepRoute=0)
    # elif direction == 's':
    #     traci.person.moveToXY("331", x=x0, y=y0 - 2, edgeID="5to3", keepRoute=0)
    # elif direction == 'x':
    #     traci.person.moveToXY("331", x=x0, y=y0 - 1, edgeID="5to3", keepRoute=0)
    # elif direction == '':
    #     traci.person.moveToXY("331", x=x0, y=y0, edgeID="5to3", keepRoute=0)




    time.sleep(1)

traci.close()
print('Done!')
