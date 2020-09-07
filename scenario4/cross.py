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

traci.start([sumoBinary, "-c", "s2.sumo.cfg", "--tripinfo-output", "tripinfo.xml"])

# position = traci.person.getPosition3D("331")
# x0 = position[0]
# y0 = position[1]

step = 0

traci.vehicle.setStop(vehID="111", edgeID="2to3", pos=100, laneIndex=1)
traci.vehicle.setStop(vehID="112", edgeID="5to3", pos=180, laneIndex=0)


while step < 2000:
    step += 1
    traci.simulationStep()
    # traci.person.add("p_1", "2to3", pos=0)

    traci.person.moveToXY(personID="331", x=-19.47, y=56.6, edgeID="2to3", keepRoute=1)

    # control people walk on edge of "5to3"

    # if step <= 14:






    # time.sleep(1)

traci.close()
print('Done!')
