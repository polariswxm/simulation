import os
import sys
import optparse
import subprocess
import random

if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")


from sumolib import checkBinary
import traci

def get_options():
    opt_parse = optparse.OptionParser()
    opt_parse.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = opt_parse.parse_args()
    return options



def run():

    l = traci.getIDList()
    print(l)



if __name__ == "__main__":
    options = get_options()

    #check binary
    if options.nogui:
        sumoBinary = checkBinary("sumo")
    else:
        sumoBinary = checkBinary("sumo-gui")
        traci.start([sumoBinary, "-c","hello.sumo.cfg", "--tripinfo-output", "tripinfo.xml"])

        run()